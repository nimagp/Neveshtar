from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

from accounts.forms import User

USER = get_user_model()

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    text = models.TextField()
    link = models.CharField(max_length=300, default='', unique = True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    meta_description = models.CharField(default="توضیحات پست", max_length=150)
    


    def publish(self):
        self.published_date = timezone.now()
        self.save()
    @property
    def likes_amount(self):
        return self.like_set.all().count()
    @property
    def comments_amount(self):
        return self.comment_set.all().count()
    @property
    def liked_users(self):
        likes = self.like_set.all()
        return [like.user for like in likes]
        

    def __str__(self):
        return self.title
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    
    def __str__(self):
        return self.text
 
class Like(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)


