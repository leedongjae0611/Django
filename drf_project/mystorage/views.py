from django.shortcuts import render
from rest_framework import viewsets
from .models import Essay
from .serializers import EssaySerializer

# Create your views here.


class PostViewSet(viewsets.ModelViewSet): #{
    queryset = Essay.objects.all()
    serializer_class = 
#}