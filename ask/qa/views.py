from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Answer
from .forms import AnswerForm, AskForm

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def question(request,pk):
    question = get_object_or_404(Question, pk=pk)
    answers = question.answer_set.all()
    if request.method == "POST":
        form = AnswerForm(request.POST,initial={'question': question.pk})
    elif request.method == "GET":
        form = AnswerForm(request.GET,initial={'question': question.pk})
    if form.is_valid():
        answer = form.save()
        url = f'../{question.pk}'
        return HttpResponseRedirect(url)
    else:
        form = AnswerForm(initial={'question': question.pk})
    return render(request, 'question.html', {'question': question, 'answers': answers, 'form': form})

def popular(request, page):
    qs = Question.objects.order_by('-rating')
    return render(request, 'popular.html', Question.objects.paginate(qs, page, 'popular'))

def index(request, page):
    qs = Question.objects.order_by('-pk')
    return render(request, 'index.html', Question.objects.paginate(qs, page,''))

def question_add(request):
    if request.method == "POST":
        form = AskForm(request.POST)
    elif request.method == "GET":
        form = AskForm(request.GET)
    if form.is_valid():
        question = form.save()
        url = f'../question/{question.pk}'
        return HttpResponseRedirect(url)
    else:
        form = AskForm()
        return render(request, 'question_add.html', {'form': form})