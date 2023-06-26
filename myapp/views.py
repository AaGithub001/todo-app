from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializer import *
from rest_framework.views import APIView

# Create your views here.
class UserModelViews(APIView):
    def get(self, request):
        users = UserModel.objects.all()
        serializer = UserModelSerializer(users, many=True).data
        todo = TodoModel.objects.all()
        todoserializer = TodoModelSerializer(todo, many=True).data
        category = Category.objects.all()
        categoryserializer =  CategorySerializer(category, many=True).data
        comment =  Comment.objects.all()
        commentserializer = CommentSerializer(comment, many=True).data
        tag = TagModel.objects.all()
        tagserializer = TagModelSerializer(tag, many=True).data
        context = {
            'users':serializer,
            'todo':todoserializer,
            'category': categoryserializer,
            'comment': commentserializer,
            'tag': tagserializer,

        }
        return Response(context)
    
    def post(self,request):
        serializer = UserModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserModelDetailView(APIView):
    def get(self, request, pk):
        user = UserModel.objects.get(id=pk)
        serializer = UserModelSerializer(user, many=False)
        return Response(serializer.data)
    
    def put(self, request, pk,*args, **kwargs):
        user = UserModel.objects.get(id=pk)
        serializer = UserModelSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request , pk, *args, **kwargs):
       UserModel.object.get(id=pk).delete()
       return Response(status=status.HTTP_200_OK)
    
class TodoModelViews(APIView):
    def get(self, request):
        users = TodoModel.objects.all()
        serializer = TodoModelSerializer(users, many=True)
        return Response(serializer.data)
    

    def post(self,request):
        serializer = TodoModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TodoModelDetailView(APIView):
    def get(self, request, pk):
        user = TodoModel.objects.get(id=pk)
        serializer = TodoModelSerializer(user, many=False)
        return Response(serializer.data)
    
    def put(self, request, pk,*args, **kwargs):
        user = TodoModel.objects.get(id=pk)
        serializer = TodoModelSerializer(instance=user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request , pk, *args, **kwargs):
       TodoModel.object.get(id=pk).delete()

       return Response(status=status.HTTP_200_OK)


class CategoryViews(APIView):
    def get(self, request):
        users = Category.objects.all()
        serializer = CategorySerializer(users, many=True)
        return Response(serializer.data)
    

    def post(self,request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryDetailView(APIView):
    def get(self, request, pk):
        user = Category.objects.get(id=pk)
        serializer = CategorySerializer(user, many=False)
        return Response(serializer.data)
    
    def put(self, request, pk,*args, **kwargs):
        user = Category.objects.get(id=pk)
        serializer = CategorySerializer(instance=user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request , pk, *args, **kwargs):
       Category.object.get(id=pk).delete()
       return Response(status=status.HTTP_200_OK)
    
class CommentViews(APIView):
    def get(self, request):
        users = Comment.objects.all()
        serializer = CommentSerializer(users, many=True)
        return Response(serializer.data)
    

    def post(self,request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentDetailView(APIView):
    def get(self, request, pk):
        user = Comment.objects.get(id=pk)
        serializer = CommentSerializer(user, many=False)
        return Response(serializer.data)
    
    def put(self, request, pk,*args, **kwargs):
        user = Comment.objects.get(id=pk)
        serializer = CommentSerializer(instance=user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request , pk, *args, **kwargs):
       Comment.object.get(id=pk).delete()
       return Response(status=status.HTTP_200_OK)
    
class TagModelViews(APIView):
    def get(self, request):
        users = TagModel.objects.all()
        serializer = TagModelSerializer(users, many=True)
        return Response(serializer.data)
    

    def post(self,request):
        serializer = TagModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TagModelDetailView(APIView):
    def get(self, request, pk):
        user = TagModel.objects.get(id=pk)
        serializer = TagModelSerializer(user, many=False)
        return Response(serializer.data)
    
    def put(self, request, pk,*args, **kwargs):
        user = TagModel.objects.get(id=pk)
        serializer = TagModelSerializer(instance=user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request , pk, *args, **kwargs):
       TagModel.object.get(id=pk).delete()
       return Response(status=status.HTTP_200_OK)