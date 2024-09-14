from rest_framework import serializers
from .models import Task, Post
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    # djangoのデフォルトのユーザーモデル
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}
        # 「'write_only': True」は、データの書き込み（POSTやPUTリクエスト）には使用できるが、データの読み取り（GETリクエスト）には含まれないことを意味します。
        # 「'required': True」は入力が必須（リクエストするデータにこのフィールが必ず含まれていること）であることを示している。

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class PostSerializer(serializers.ModelSerializer):
    # created_atの形式を変えておく
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'created_at')

class TaskSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'title', 'created_at')