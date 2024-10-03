# serializersをimport
from rest_framework import serializers
# models.pyで定義したDBのモデルをimport
from .models import Task, Post
# djangoのデフォルトのユーザーモデルをimport
from django.contrib.auth.models import User

#djangoデフォルトのユーザーモデルに対応するserializer（ユーザー作成用）
class UserSerializer(serializers.ModelSerializer):

    # djangoのデフォルトのユーザーモデルとの関連付け
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}
        # 「'write_only': True」は、データの書き込み（POSTやPUTリクエスト）には使用できるが、データの読み取り（GETリクエスト）には含まれないことを意味している。
        # 「'required': True」は入力が必須（リクエストするデータにこのフィールが必ず含まれていること）であることを示している。

    #ユーザー作成用のメソッド
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

#Postモデルに対応するserializer
class PostSerializer(serializers.ModelSerializer):
    # created_atの形式を変えておく
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    #importしているPostモデルと関連付け
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'created_at')

class TaskSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    #importしているTaskモデルと関連付け
    class Meta:
        model = Task
        fields = ('id', 'title', 'created_at')