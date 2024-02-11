from django.shortcuts import render, redirect
from .models import PersonalData, WorkExperience, Projects
from .forms import PersonalDataForm, WorkExperienceForm, ProjectsForm

# Create your views here.


def index(request):
    try:
        personal_data = PersonalData.objects.get(pk=1)
        work_experiences = WorkExperience.objects.all()
        projects = Projects.objects.all()

        data = {
            'personal_data': personal_data,
            'work_experiences': work_experiences,
            'projects': projects
        }
    except PersonalData.DoesNotExist:
        return redirect('forms/personal-data')

    return render(request, 'index.html', {'data': data})


def personal_data(request):
    form = PersonalDataForm()
    if request.method == 'POST':
        form = PersonalDataForm(request.POST)

        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            description = form.cleaned_data['description']

            personal_data, created = PersonalData.objects.get_or_create(
                pk=1,
                full_name=full_name, description=description)

            personal_data.save()

            return redirect('/')
    return render(request, 'personal_data_form.html', {'form': form})


def work_experience(request):
    form = WorkExperienceForm()
    if request.method == 'POST':
        form = WorkExperienceForm(request.POST)
        if form.is_valid():
            company_name = form.cleaned_data['company_name']
            position = form.cleaned_data['position']
            year = form.cleaned_data['year']

            work_experience = WorkExperience(
                company_name=company_name, position=position, year=year)
            work_experience.save()

            return redirect('/')

    return render(request, 'work_experience_form.html', {'form': form})


def projects(request):
    form = ProjectsForm()
    if request.method == 'POST':
        form = ProjectsForm(request.POST)
        if form.is_valid():
            project_name = form.cleaned_data['project_name']
            project_description = form.cleaned_data['project_description']
            project_link = form.cleaned_data['project_link']

            projects = Projects(
                project_name=project_name, project_description=project_description, project_link=project_link)
            projects.save()

            return redirect('/')

    return render(request, 'projects_form.html', {'form': form})
