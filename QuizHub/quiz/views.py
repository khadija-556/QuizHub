from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializer import *
from .models import *

# Create your views here.

class QuizViewSet(ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
