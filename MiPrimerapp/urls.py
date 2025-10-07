from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('suma/', views.suma, name='suma'),
    path('<str:nombre>', views.saludo, name='saludo'),
    path('about/', views.about, name='about'),
    path('tasks/', views.tasks_index, name='tasks_index'),
    path('tasks/add/', views.tasks_add, name='tasks_add'),
    path('tasks/admin/', views.tasks_admin_list, name='tasks_admin_list'),
    path("index2/",views.index2,name="index2"),
]