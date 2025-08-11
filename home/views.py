from django.shortcuts import render
from todo.models import Todomodel
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.
def todoView(request):
    todo_objs=Todomodel.objects.all().order_by('-priority')
    context={"todos":todo_objs}
    return render(request, 'home/home.html', context)
@api_view(['GET'])
def todoJson(request=Request):
    todos=list(Todomodel.objects.all().order_by('priority').values('title', 'priority','is_done'))
    return Response({'todo':todos}, status=status.HTTP_200_OK)