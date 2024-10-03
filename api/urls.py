from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from api.views import TaskViewSet, CreateUserView, TaskListView, TaskRetrieveView,\
    PostListView, PostRetrieveView

#ModelViewSetで定義したviewの場合、routerを設定できる。
router = routers.DefaultRouter()
router.register('tasks', TaskViewSet, basename='tasks') #urlとviewを関連付ける。第一引数がエンドポイント、第二引数がview名

urlpatterns = [
    path('list-post/', PostListView.as_view(), name='list-post'),
    path('detail-post/<str:pk>/', PostRetrieveView.as_view(), name='detail-post'),
    path('list-task/', TaskListView.as_view(), name='list-task'),
    path('detail-task/<str:pk>/', TaskRetrieveView.as_view(), name='detail-task'),
    path('register/', CreateUserView.as_view(), name='register'),
    path('auth/', include('djoser.urls.jwt')), #JWTトークンを取得するためのエンドポイント。自動的にauth/jwt/createというパスが作られる。ここにusername,passwordをPostメソッドで渡すとjwtトークンを返してくれる？
    path('', include(router.urls)),#ルート（最初のurlにアクセスした時）にアクセスした時、routerに登録してあるurl先（tasks）に飛ぶようになる。
]