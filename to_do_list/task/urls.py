from django.urls import path
from task.views import add_tasks, show_tasks, edit_task, delete_task, complete_tasks, completed_tasks

urlpatterns = [
    path('', add_tasks, name="addtask"),
    path('show_tasks/', show_tasks, name="showtasks"),
    path('edit_task/<int:id>', edit_task, name="edittask"),
    path('delete_task/<int:id>', delete_task, name="deletetask"),
    path('complete_tasks/<int:id>', complete_tasks, name="completetasks"),
    path('completed_tasks/', completed_tasks, name="completedtasks")
   
]