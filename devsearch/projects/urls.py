from django.urls  import path
from . import views
urlpatterns = [

    path("", views.projects, name="projects"),
    path("about-single-project-obj/<str:project_id>", views.project, name="project")

]