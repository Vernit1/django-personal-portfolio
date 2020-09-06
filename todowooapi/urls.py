from django.urls import path
from . import views

urlpatterns = [
    path('todos/completed/', views.TodoCompletedList.as_view()),
    path('todos/', views.TodoListCreate.as_view()),
    path('todos/<int:pk>', views.TodoRetrieveUpdateDestroyList.as_view()),
    path('todos/<int:pk>/complete', views.TodoComplete.as_view()),

    #Auth
    path('signup', views.signup),
    path('login', views.login),
]
