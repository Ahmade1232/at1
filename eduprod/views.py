from django.core import serializers
from django.shortcuts import render
from .models import Question
import random

def index(request):
    questions = Question.objects.all()
    questions_list = list(questions)  # Convert queryset to list
    random.shuffle(questions_list)  # Shuffle the list
    questions_json = serializers.serialize('json', questions_list[:2])
    #questions_json = serializers.serialize('json', questions_list)
    return render(request, 'eduprod/index.html', {'questions_json': questions_json})
