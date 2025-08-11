from django.shortcuts import render
from .serializers import TodoSerializer
from .models import Todomodel
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics, mixins
#region function based view
@api_view(['GET','POST'])
def TodoSerialzerView(request:Request):
    if request.method=="GET":
        obj_model=Todomodel.objects.all().order_by('priority')
        todo_serializer=TodoSerializer(obj_model, many=True)
        return Response(todo_serializer.data,status.HTTP_200_OK )
    elif request.method=="POST":
        obj_get=TodoSerializer(data=request.data)
        if obj_get.is_valid():
            obj_get.save()
        return Response(obj_get.data, status.HTTP_201_CREATED)
    return Response(None, status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def TodoSerializerDetail(request:Request, id):
    try:
        todo=Todomodel.objects.get(id=id)
    except Todomodel.DoesNotExist:
        return Response(None, status.HTTP_400_BAD_REQUEST)
    
    if request.method=="GET":
        obj_model=TodoSerializer(todo)
        return Response(obj_model.data, status.HTTP_200_OK)
    
    elif request.method=="PUT":
        obj=TodoSerializer(todo, data=request.data)
        if obj.is_valid():
            obj.save()
            return Response(obj.data, status.HTTP_202_ACCEPTED)
        return Response(None, status.HTTP_400_BAD_REQUEST)
    elif request.method=="DELETE":
        todo.delete()
        return Response(None, status.HTTP_204_NO_CONTENT)
#endregion
#region class based view APIView
class TodoApiView(APIView):
    def get(self, request:Request):
        objects=Todomodel.objects.all().order_by('priority')
        obj_serielizer=TodoSerializer(objects, many=True)
        return Response(obj_serielizer.data, status.HTTP_200_OK)
    def post(self, request:Request):
        post_obj=TodoSerializer(data=request.data)
        if post_obj.is_valid():
            post_obj.save()
            return Response(post_obj.data, status.HTTP_201_CREATED)
        return Response(None, status.HTTP_400_BAD_REQUEST)
    
class TodoDetailApiView(APIView):
    def getObject(self,todo_id=int):
        try: 
            return Todomodel.objects.get(id=todo_id)
        except Todomodel.DoesNotExist:
            return None
    def get(self, request:Request , todo_id=int):
        todo_get=self.getObject(todo_id)
        if todo_get is None:
            return Response(None, status.HTTP_404_NOT_FOUND)
        else:
            todo_seri=TodoSerializer(todo_get)
            return Response(todo_seri.data,status.HTTP_202_ACCEPTED)
    def put(self, request:Request , todo_id=int):
        todo_get=self.getObject(todo_id)
        todo_seri=TodoSerializer(todo_get, data=request.data)
        if todo_seri.is_valid():
            todo_seri.save()
            return Response(todo_seri.data, status.HTTP_200_OK)
    def delete(self, request:Request , todo_id=int):
        todo_get=self.getObject(todo_id)
        todo_get.delete()
        return Response(None, status.HTTP_204_NO_CONTENT)
#endregion
#region mixins
class MixinViewApi(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset=Todomodel.objects.all().order_by('priority')
    serializer_class=TodoSerializer
    def get(self, request:Request):
        return self.list(request)
    def post(self, request:Request):
        return self.create(request)
class MixinDetailViewApi(mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset=Todomodel.objects.all().order_by('priority')
    serializer_class=TodoSerializer
    def get(self, request:Request,pk ):
        return self.retrieve(request, pk)
    def put(self, request:Request, pk):
        return self.update(request, pk)
    def delete(self, request:Request, pk):
        return self.destroy(request,pk)
#endregion
#region genericViews

#endregion


