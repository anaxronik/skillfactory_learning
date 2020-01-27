from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import TodoItem


@login_required()
def list(request):
    user = request.user
    user_tasks = TodoItem.objects.filter(owner=user)
    return render(request, 'tasks/tasks_list.html', context={'tasks': user_tasks})


@login_required()
def create_task(request, *args, **kwargs):
    if request.method == 'POST':
        task = TodoItem()
        title = request.POST['title']
        description = request.POST['description']
        if title == '':
            if len(description) >= 100:
                title = description[:100]
            else:
                title = description
        task.title = title
        task.description = description
        task.owner = request.user
        task.save()
        messages.success(request, 'Задача создана')
        return redirect('/tasks/')
    else:
        return render(request, 'tasks/create_task.html')


@login_required()
def delete(request, uid):
    task = TodoItem.objects.get(id=uid)
    if task.owner == request.user:
        task.delete()
    messages.success(request, 'Задача удалена')
    return redirect('/tasks/')


@login_required()
def modify(request, uid):
    if request.method == 'GET':
        task = TodoItem.objects.filter(id=uid)[0]
        return render(request, 'tasks/modify.html', context={'task': task})
    if request.method == 'POST':
        task = TodoItem.objects.filter(id=uid)[0]
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.is_completed = request.POST['status']
        task.save()
        return redirect('/tasks/')


def test(request):
    # return HttpResponse('Test page ok')
    return redirect('tasks:list')


@login_required()
class TaskDetail(DetailView):
    model = TodoItem
    template_name = 'tasks/details.html'


class TaskListView(ListView):
    model = TodoItem
    context_object_name = "tasks"
    template_name = "tasks/list.html"

    def get_queryset(self):
        qs = super().get_queryset()
        u = self.request.user
        if u.is_anonymous:
            return []
        return qs.filter(owner=u)
