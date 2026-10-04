from pathlib import Path

from database import Database

from models.project import Project
from models.projectTag import ProjectTag
from models.renderfile import RenderFile
from models.renderTag import RenderTag
from models.tag import Tag

from repositories.projectRepository import ProjectRepository

from services.projectService import ProjectService
from views.projects_view import main as mainview
import flet as ft

if __name__ == "__main__":
    
    
    SessionF = Database.start()
    ps = ProjectService(SessionF)
    #ps.add_files(Path("C:/Users/user/Documents"))

    ft.run(lambda page: mainview(page, ps))

    """with SessionF.begin() as session:
        project_repository = ProjectRepository(session)
        for i in project_repository.get_all():
            print(i.name)"""