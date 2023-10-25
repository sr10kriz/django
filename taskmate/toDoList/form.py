from django import forms
from toDoList.models import TodoList

class ToDoForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ['task', 'status']