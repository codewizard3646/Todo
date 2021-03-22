from django.shortcuts import render
from .models import *
from .serializers import PlanSerializer 
# Create your views here.
from rest_framework.generics import ListAPIView , CreateAPIView,DestroyAPIView

class PlanList(ListAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer


class PlanCreate(CreateAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer


class PlanDestroy(DestroyAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    lookup_field ="id"

