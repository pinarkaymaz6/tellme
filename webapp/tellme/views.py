from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question
from django.utils import timezone
# Create your views here.

def index(request):
    latest_questions = Question.objects.order_by('q_date')[:5]
    context = {'latest_questions':latest_questions}
    return render(request, 'tellme/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {"question":question}
    return render(request, 'tellme/detail.html', context)

def add_question(request):
    try:
        q_title = request.POST['q_title']
        q_text = request.POST['q_text']
        question = Question(q_title=q_title, q_text=q_text, q_date=timezone.now())
        question.save()
    except:
        return render(request, 'tellme/index.html')

    return HttpResponseRedirect(reverse('tellme:index')) 


def add_answer(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        text = request.POST['answer']
        question.answer_set.create(a_text=text, a_date=timezone.now())
        question.save()
    except:
        return render(request, 'tellme/detail.html', {'question': question, 'error_message': 'Please enter some text'})

    return HttpResponseRedirect(reverse('tellme:detail', args=(question.id,))) 