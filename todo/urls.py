from django.urls import path
from todo.views import TodoListCreateAPIView

urlpatterns = [
    path("", TodoListCreateAPIView.as_view(), name='todo-list-create-api')
]
