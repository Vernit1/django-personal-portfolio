from django.urls import path
from . import views

app_name='todowoo'

urlpatterns = [
    #Auth
    path('signup/', views.signupuser, name='signupuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('login/', views.loginuser, name='loginuser'),

    #Todos
    path('', views.todowoohome, name='todowoohome'),
    # path('home', views.todowoohome, name='todowoohome'),
    path('current/', views.currenttodos, name='currenttodos'),
    path('completed/', views.completedtodos, name='completedtodos'),
    path('create/', views.createtodo, name='createtodo'),
    path('todowoo/<int:todo_pk>', views.viewtodo, name='viewtodo'),
    path('todowoo/<int:todo_pk>/complete', views.completetodo, name='completetodo'),
    path('todowoo/<int:todo_pk>/delete', views.deletetodo, name='deletetodo'),
]
