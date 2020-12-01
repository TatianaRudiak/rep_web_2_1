from __future__ import unicode_literals
from django.contrib.auth import get_user_model
from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()
    added_at = models.DateTimeField(blank = True, auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name='question'
    )
    likes = models.ManyToMany(User, related_name='question_like_user')   # список пользователей, поставивших "лайк"

    class Meta:
        ordering = ['-added_at']

    class QuestionManager(models.Manager): 
        objects = QuestionManager()   
        def new(self,count=1):
            return self.objects.all()[:count]
        
        def popular(self):
            return self.objects.order_by('-rating')

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank = True, auto_now_add=True)
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='answer'
    )
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL
    )