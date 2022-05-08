from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404

from .models import Survey, Question
# Create your views here.

def index(request):
    survey_id = 1
    surveyQuestions = Question.objects.filter(survey_id=1)[:3]
    # context = {('survey ' + str(survey_id) + ' questions') : questions}
    context = {'surveyQuestions' : surveyQuestions, 'survey_id' : survey_id}
    return render(request, 'feedbacks/index.html', context)

def surveyAnswer(request, survey_id):
    try:
        survey = Survey.objects.get(id = survey_id)
    except Survey.DoesNotExist:
        raise Http404("Survey not found")
    return render(request, 'feedbacks/details.html', {'surveyAnswered' : survey})

def answerDetail(request, question_id):
    print("qution :" + str(question_id))
    survey_id = request.GET.get('survey_id')
    path = request.GET.get('path')
    print("survey :" + str(survey_id))
    print("path :" + str(path))
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'feedbacks/details.html', {'question' : question, "refererPath" : path})