from django.contrib import admin
from .models import Task, Post

# models.pyからクラスPOSTとTaskを登録しておく。
admin.site.register(Post)
admin.site.register(Task)