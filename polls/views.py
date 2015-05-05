from django.shortcuts import render
from django.http import HttpResponse

from .models import Question
# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date') [:5]
    output = ', '.join([p.question_text for p in latest_question_list])
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("this is question number %s." % question_id)

def results(request, question):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s.") % question_id
