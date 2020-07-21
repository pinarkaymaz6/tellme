from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question
# Create your views here.

def index(request):
    latest_questions = Question.objects.order_by('q_date')[:5]
    context = {'latest_questions':latest_questions}
    return render(request, 'tellme/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    context = {"question":question}
    return  render(request, 'tellme/detail.html', context)