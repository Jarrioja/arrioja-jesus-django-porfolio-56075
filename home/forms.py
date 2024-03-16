from django import forms
from ckeditor.fields import RichTextFormField


class PersonalDataForm(forms.Form):
    full_name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)


class WorkBaseForm(forms.Form):
    company_name = forms.CharField(max_length=100)
    position = forms.CharField(max_length=100)
    year = forms.IntegerField()
    description = RichTextFormField()


class CreateWork(WorkBaseForm):
    company_name = forms.CharField(max_length=100)
    position = forms.CharField(max_length=100)
    year = forms.IntegerField()
    description = RichTextFormField()


class EditWork(WorkBaseForm):
    company_name = forms.CharField(max_length=100)
    position = forms.CharField(max_length=100)
    year = forms.IntegerField()
    description = RichTextFormField()


class ProjectBaseForm(forms.Form):
    project_name = forms.CharField(max_length=200)
    project_description = forms.CharField(widget=forms.Textarea)
    project_link = forms.URLField()


class CreateProjectForm(ProjectBaseForm):
    ...


class EditProject(ProjectBaseForm):
    ...


class SearchWork(forms.Form):
    company_name = forms.CharField(max_length=100, required=False)


class SearcProject(forms.Form):
    project_name = forms.CharField(max_length=200, required=False)
