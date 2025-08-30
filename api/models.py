from django.db import models
from uuid import uuid4


class Question(models.Model):
    text = models.CharField(max_length=200, verbose_name='Текст вопроса')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания вопроса')


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers', verbose_name='Вопрос')
    user_id = models.UUIDField(default=uuid4, verbose_name='ID пользователя')
    text = models.TextField(verbose_name='Текст ответа')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания ответа')
