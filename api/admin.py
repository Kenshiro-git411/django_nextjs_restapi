from django.contrib import admin
from .models import Task, Post

# 管理者画面から確認できるように、models.pyからクラスPOSTモデルとTaskモデルを登録しておく。
admin.site.register(Post)
admin.site.register(Task)