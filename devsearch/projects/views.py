from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

projectslist = [
    {
        "project_id": '1',
        "project_title": "Web Development Project",
        "project_desc": "A project involving development of a web application."
    },
    {
        "project_id": '2',
        "project_title": "Data Analysis Project",
        "project_desc": "A project focused on analyzing large datasets."
    },
    {
        "project_id": '3',
        "project_title": "Mobile App Development Project",
        "project_desc": "Development of a mobile application for iOS and Android platforms."
    },
    {
        "project_id": '4',
        "project_title": "Machine Learning Project",
        "project_desc": "A project involving implementation of machine learning algorithms."
    },
    {
        "project_id": '5',
        "project_title": "Game Development Project",
        "project_desc": "Development of a 2D game using Unity engine."
    }
]



def projects(request):
    context = { 'pagetitle': "ProjectsInfoPage", 'projects': projectslist}
    return render(request, 'projects/projectsinfo.html', context)
def project(request, project_id):
    selectedproject = None
    for project in projectslist:
        if project['project_id'] == project_id:
            selectedproject = project
    context = { 'pagetitle': "ProjectInfoPage"  ,'choosedproject': selectedproject}
    return render(request, 'projects/projectinfo.html', context)