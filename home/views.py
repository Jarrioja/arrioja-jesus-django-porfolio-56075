from django.shortcuts import render, redirect
from .models import PersonalData, WorkExperience, Projects
from .forms import PersonalDataForm, CreateWork, EditWork, SearchWork, CreateProjectForm, EditProject, SearcProject
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy


# Create your views here.


def index(request):
    try:
        personal_data = PersonalData.objects.get(pk=1)
        work_experiences = WorkExperience.objects.all()
        projects = Projects.objects.all()

        form = SearchWork(request.GET)
        if form.is_valid():
            search = form.cleaned_data['company_name']
            work_experiences = WorkExperience.objects.filter(
                company_name__icontains=search)

        data = {
            'personal_data': personal_data,
            'work_experiences': work_experiences,
            'projects': projects,
            'form': form,

        }
    except PersonalData.DoesNotExist:
        return redirect('forms/personal-data')

    return render(request, 'home/index.html', {'data': data})
    # return render(request, 'home/index.html')


class WorkListView(ListView):
    model = WorkExperience
    context_object_name = 'work_experiences'
    template_name = 'home/works.html'


def works(request):
    work_experiences = WorkExperience.objects.all()

    form = SearchWork(request.GET)
    if form.is_valid():
        search = form.cleaned_data['company_name']
        work_experiences = WorkExperience.objects.filter(
            company_name__icontains=search)
    data = {
        'work_experiences': work_experiences,
        'form': form,
    }
    return render(request, 'home/works.html', {'data': data})


def create_work(request):
    form = CreateWork()
    if request.method == 'POST':
        form = CreateWork(request.POST)
        if form.is_valid():
            company_name = form.cleaned_data['company_name']
            position = form.cleaned_data['position']
            year = form.cleaned_data['year']
            desciption = form.cleaned_data['description']

            work_experience = WorkExperience(
                company_name=company_name, position=position, year=year, desciption=desciption)
            work_experience.save()

            return redirect('/works')

    return render(request, 'work/create_work.html', {'form': form})


def view_work(request, work_id):
    work = WorkExperience.objects.get(id=work_id)
    return render(request, 'work/view_work.html', {'work': work})


def edit_work(request, work_id):
    work = WorkExperience.objects.get(id=work_id)
    form = EditWork(initial={'company_name': work.company_name,
                    'position': work.position, 'year': work.year, 'description': work.description})

    if request.method == 'POST':
        form = EditWork(request.POST)
        if form.is_valid():
            new_data = form.cleaned_data
            work.company_name = new_data['company_name']
            work.position = new_data['position']
            work.year = new_data['year']
            work.desciption = form.cleaned_data['description']
            work.save()
            return redirect('works')

    return render(request, 'work/edit_work.html', {'work': work, 'form': form})


def delete_work(request, work_id):
    work = WorkExperience.objects.get(id=work_id)
    work.delete()
    return redirect('works')


def personal_data_form(request):
    form = PersonalDataForm()
    if request.method == 'POST':
        form = PersonalDataForm(request.POST)

        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            description = form.cleaned_data['description']

            personal_data, created = PersonalData.objects.update_or_create(
                pk=1,
                defaults={'full_name': full_name, 'description': description}
            )

            # personal_data.save()

            return redirect('/')
    return render(request, 'home/personal_data_form.html', {'form': form})


# def projects(request):
#     projects = Projects.objects.all()

#     form = SearcProject(request.GET)
#     if form.is_valid():
#         search = form.cleaned_data['project_name']
#         projects = Projects.objects.filter(
#             project_name__icontains=search)
#     data = {
#         'projects': projects,
#         'form': form,
#     }
#     return render(request, 'home/projects.html', {'data': data})


def create_project(request):
    form = CreateProject()

    if request.method == 'POST':
        form = CreateProject(request.POST)
        if form.is_valid():

            project_name = form.cleaned_data['project_name']
            project_description = form.cleaned_data['project_description']
            project_link = form.cleaned_data['project_link']
            print(project_name)
            project = Projects(
                project_name=project_name, project_description=project_description, project_link=project_link)
            project.save()

            return redirect('/projects')

    return render(request, 'project/create_project.html', {'form': form})


class ProjectsListView(ListView):
    model = Projects
    context_object_name = 'projects'
    template_name = 'home/projects.html'


# class CreateProject(CreateView):
#     model = Projects
#     template_name = 'project/create_project.html'
#     fields = ['project_name', 'project_description', 'project_link']
#     success_url = reverse_lazy('projects')


def view_project(request, project_id):
    project = Projects.objects.get(id=project_id)
    return render(request, 'project/view_project.html', {'project': project})


def edit_project(request, project_id):
    project = Projects.objects.get(id=project_id)
    form = EditProject(initial={'project_name': project.project_name,
                                'project_description': project.project_description, 'project_link': project.project_link})

    if request.method == 'POST':
        form = EditProject(request.POST)
        if form.is_valid():
            new_data = form.cleaned_data
            project.project_name = new_data['project_name']
            project.project_description = new_data['project_description']
            project.project_link = new_data['project_link']
            project.save()
            return redirect('projects')

    return render(request, 'project/edit_project.html', {'project': project, 'form': form})


def delete_project(request, project_id):
    project = Projects.objects.get(id=project_id)
    project.delete()
    return redirect('projects')
