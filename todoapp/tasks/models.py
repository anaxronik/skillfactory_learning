from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class TodoItem(models.Model):
    PRIORITY_HIGH = 1
    PRIORITY_MEDIUM = 2
    PRIORITY_LOW = 3

    PRIORITY_CHOICES = [
        (PRIORITY_HIGH, 'Высокий приоритет'),
        (PRIORITY_MEDIUM, 'Средний приоритет'),
        (PRIORITY_LOW, 'Низкий приоритет'),
    ]
    title = models.CharField(max_length=128)
    description = models.TextField()
    is_completed = models.BooleanField('выполнено', default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    priority = models.IntegerField('Приоритет', choices=PRIORITY_CHOICES, default=PRIORITY_MEDIUM)

    def __str__(self):
        # отображение класса в строковом виде
        return self.title

    class Meta:
        # подкласс для сортировки
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('tasks:details', args=[self.pk])
