from django.urls import path
from home.views import index, personal_data, work_experience, projects

urlpatterns = [
    path('', index, name='index'),
    path('forms/personal-data/', personal_data, name='personal_data_edit'),
    path('forms/work-experience/', work_experience, name='work_experience_edit'),
    path('forms/projects/', projects, name='projects_edit')
    # path('show-time/', show_time, name='show_time'),
    # path('saludo/<str:name>/<str:last_name>/', saludo, name='saludo'),
    # path('students/', students, name='alumnos'),
    # path('students/new/', create_student, name='create_student')
]
