from django import forms


class PersonalDataForm(forms.Form):
    full_name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)


class WorkExperienceForm(forms.Form):
    company_name = forms.CharField(max_length=100)
    position = forms.CharField(max_length=100)
    year = forms.IntegerField()


class ProjectsForm(forms.Form):
    project_name = forms.CharField(max_length=200)
    project_description = forms.CharField(widget=forms.Textarea)
    project_link = forms.URLField()
