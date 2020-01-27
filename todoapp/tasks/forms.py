from django import forms

from .models import TodoItem


class AddTask(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)


class TodoItemForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ('description', 'priority')
        labels = {'description': 'Описание', 'priority': ''}
