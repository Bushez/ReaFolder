from services.scanner import Scanner
from pathlib import Path
from repositories.projectRepository import ProjectRepository
from models.project import Project
from datetime import datetime

class ProjectService():
    def __init__(self, sessionF):
        self.sessionF  = sessionF


    def add_files(self, path: Path):
        file_paths = Scanner.scan(path)
        with self.sessionF.begin() as s:
            project_repo = ProjectRepository(s)
            existing_paths = project_repo.get_all_paths()
            for file in file_paths:
                str_file = str(file.resolve())
                if str_file not in existing_paths:
                    project = Project()
                    project.name = file.stem
                    project.path = str_file
                    project.modified_at = datetime.fromtimestamp(file.stat().st_mtime)

                    project_repo.create(project)

    def get_all_files(self):
        with self.sessionF() as s:
            project_repo = ProjectRepository(s)
            return project_repo.get_all()

