from models.project import Project
from sqlalchemy import select
from sqlalchemy.orm import Session

class ProjectRepository():
    def __init__(self, session: Session):
        self.s = session

    def get_all(self):
        return list(self.s.scalars(select(Project)).all())
        
    def create(self, project: Project):
        self.s.add(project)
        self.s.flush()
        return project

    def get_by_id(self, project_id):
        return self.s.get(Project, project_id)

    def get_by_path(self, path):
        return self.s.get(Project, path)

    def get_all_paths(self):
        return set(self.s.scalars(select(Project.path)).all())

    def edit(self, project_id, **params): 
        project = self.get_by_id(project_id)

        if project is None:
            return None

        for field, value in params.items():
            setattr(project, field, value)

        self.s.flush()
        return project

    def delete(self, project_id):
        project = self.get_by_id(project_id)
        if project is None: return False 
        self.s.delete(project)
        return True
        

        