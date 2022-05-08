from django.urls import path
from django.shortcuts import redirect
from django.utils.http import urlencode

from . import views

app_name = 'feedbacks'
urlpatterns = [
    path('redirect', lambda referer : redirect(urlencode(referer) + '/'), name="redirectBack"),
    path('', views.index, name="index"),
    path('<int:survey_id>/', views.surveyAnswer, name="surveyAnswer"),
    path('question/<int:question_id>/', views.answerDetail, name="answerDetail"),
]