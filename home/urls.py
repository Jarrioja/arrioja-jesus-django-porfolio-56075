from django.urls import path
from home.views import index, personal_data_form, create_work, view_work, delete_work, edit_work, works,  delete_project, edit_project, view_project, ProjectsListView, WorkListView  # , CreateProject,

urlpatterns = [
    path('', index, name='index'),

    # path('works/', works, name='works'),
    path('works/', WorkListView.as_view(), name='works'),
    path('works/new/', create_work, name='create_work'),
    path('works/delete/<int:work_id>/', delete_work, name="delete_work"),
    path('works/edit/<int:work_id>/', edit_work, name="edit_work"),
    path('works/<int:work_id>/', view_work, name="view_work"),



    path('forms/personal-data/', personal_data_form, name='personal_data_edit'),

    path('projects/', ProjectsListView.as_view(), name='projects'),
    path('projects/new/', create_work, name='create_project'),
    path('projects/delete/<int:project_id>/',
         delete_project, name="delete_project"),
    path('projects/edit/<int:project_id>/', edit_project, name='edit_project'),
    path('projects/<int:project_id>/', view_project, name="view_project"),
]
