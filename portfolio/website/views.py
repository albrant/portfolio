from django.shortcuts import render
from website.models import Project


def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects,
        'location': 'website',
    }
    return render(
        request,
        'website/project_index.html',
        context
    )


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project,
        'location': 'website',
    }
    return render(
        request,
        'website/project_detail.html',
        context
    )
