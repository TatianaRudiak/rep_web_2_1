from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db import models
from django.urls import reverse


class QuestionManager(models.Manager):  
        def __str__(self):
            return self.title

        def paginate(self, qs, page, slug=''):
            limit = 10
            paginator = Paginator(qs, limit)
            paginator.baseurl = str(slug)+'/'+str(page)
            page = paginator.page(page)   
            #try:
            #    page = paginator.page(page)
            #except EmptyPage:
            #    page = paginator.page(paginator.num_pages)
            return {'questions': page, 'paginator': paginator}

        def get_url (self, slug, kwargs):
            return reverse(slug,kwargs)

        def new(self):
            return self.order_by('-pk')
        
        def popular(self):
            return self.order_by('-rating')

        def current(self):
            pass

class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=250)
    text = models.TextField(blank = True, default='')
    added_at = models.DateTimeField(blank = True, auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(
        User, null=True, on_delete=models.SET_NULL, related_name='question'
    )
    likes = models.ManyToManyField(User, blank = True, related_name='question_like_user')  
    
    class Meta:
        ordering = ['-added_at']


class Answer(models.Model):
    text = models.TextField(blank = True, default='')
    added_at = models.DateTimeField(blank = True, auto_now_add=True)
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        User, null=True, on_delete=models.SET_NULL
    )