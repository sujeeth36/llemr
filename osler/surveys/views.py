from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponse

from osler.surveys.models import Survey, Question


def create(request):
    '''create a new survey, and redirect to editing it'''
    new_survey = Survey(title="Untitled Survey")
    new_survey.save()
    return redirect('surveys:edit', id=new_survey.id)


class SurveyTemplateListView(generic.ListView):
    model = Survey


def fill(request, id):
    survey = Survey.objects.get(id=id)
    return render(request, 'surveys/fill.html', {'survey': survey, 'QuestionType': Question.QuestionType})
