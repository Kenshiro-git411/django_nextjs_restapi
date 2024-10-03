from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework import viewsets
from .serializers import TaskSerializer, UserSerializer, PostSerializer
from .models import Task, Post

# ★新規ユーザーの作成
class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    # JWTトークンを採用しているため、登録されているユーザーのみエンドポイントにアクセスできるようにしているが、
    # 新規ユーザーはどこもアクセスできなくなってしまうため、新規ユーザーを作成する段階ではだれでも認証されるように設定しておく
    permission_classes = (AllowAny,)

class PostListView(generics.ListAPIView):
    queryset = Post.objects.all() #Postモデルに入っているすべての内容をquerysetに代入する。
    serializer_class = PostSerializer
    permission_classes = (AllowAny,)

# 特定の1つのタスクのみ取得する
class PostRetrieveView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AllowAny,)

# taskの一覧を取得
class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (AllowAny,)

# idに基づいて特定のtaskを参照する
class TaskRetrieveView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (AllowAny,)


class TaskViewSet(viewsets.ModelViewSet): #ModelViewSetを使用するとcrud機能(create,update,delete)がすべて使える。
    queryset = Task.objects.all()
    serializer_class = TaskSerializer