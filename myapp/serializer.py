from rest_framework import serializers
from .models import *

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'


class TodoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoModel
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class TagModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagModel
        fields = '__all__'
        


