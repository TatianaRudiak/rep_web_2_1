from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.core.paginator import Paginator
from django.utils import timezone


class QuestionManager(models.Manager):  
        def __str__(self):
            return self.title

        def get_url (self, slug, kwargs):
            return reverse(slug,kwargs)

        def paginate(request, qs, slug):
            try:
                limit = int(request.get('limit', 10))
            except ValueError:
                limit = 10
            if limit > 100:
                limit = 10
            try:
                page = int(request.get('page', 1))
            except ValueError:
                raise Http404
            paginator = Paginator(qs, limit)
            paginator.baseurl = reverse(slug,kwargs={'page': page})
            try:
                page = paginator.page(page)
            except EmptyPage:
                page = paginator.page(paginator.num_pages)
            return {'questions': page, 'paginator': paginator}

        def new(self):
            return self.objects.order_by('-pk')
        
        def popular(self):
            return self.objects.order_by('-rating')

        def current(self):
            pass

class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=250)
    text = models.TextField(blank = True, default='')
    added_at = models.DateTimeField(blank = True, default=django.utils.timezone.now)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(
        User, null=True, on_delete=models.SET_NULL, related_name='question'
    )
    likes = models.ManyToManyField(User, related_name='question_like_user')  
    
    class Meta:
        ordering = ['-added_at']


class Answer(models.Model):
    text = models.TextField(blank = True, default='')
    added_at = models.DateTimeField(blank = True, default=django.utils.timezone.now)
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        User, null=True, on_delete=models.SET_NULL
    )