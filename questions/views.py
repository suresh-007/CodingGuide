from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

from .models import Question,Answer


def questions_list(request):
    questions = Question.objects.all()
    return render(request,
                  'questions/list.html',
                  context = {'questions':questions}
                 )
def display_question(request,id):
    question = Question.objects.get(id=id)
    answers = Answer.objects.filter(question__id=id)
    return render(request,
                  'questions/question.html',
                  context={'question':question,'answers':answers})