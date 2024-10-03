from django.db import models

# ブログの投稿の際のモデル
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True) #timestampフィールド。auto_now_add=Trueはデータが作られた段階で時間を自動で入力してくれる。

    def __str__(self):
        return str(self.id) + " - " + self.title
    
class Task(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + " - " + self.title