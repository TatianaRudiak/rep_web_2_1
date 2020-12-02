from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse 
from .models import Question, Answer

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def question(request, pk):
    question = get_object_or_404(Question, pk=pk)
    answers = question.answer.all()
    return render(request, 'question.html', {'question': question, 'answers': answers})

def popular(request, page):
    qs = Question.objects.popular
    return render(request, 'popular.html', Question.objects.paginate(qs,'popular'))

def index(request, page):
    qs = Question.objects.new
    return render(request, 'index.html', Question.objects.paginate(qs,''))