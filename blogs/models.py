from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

from django.utils import timezone

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=100)
    avatar = models.URLField()

    def __str__(self):
        return self.name

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)  # Updated to reference Author model
    slug = models.CharField(max_length=130)
    views = models.IntegerField(default=0)
    timeStamp = models.DateTimeField(blank=True, db_index=True)
    content = models.TextField()
    excerpt = models.TextField(default='No excerpt provided')  # New field for excerpt
    coverImage = models.URLField(default='/placeholder.svg?height=400&width=800')  # New field for cover image URL
    date = models.DateField(default=timezone.now)  # New field for the publication date
    category = models.CharField(max_length=100, default='General')  # New field for category
    tags = models.JSONField(default=list)  # New field for tags as a list

    def __str__(self):
        return self.title + " by " + self.author.name


class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:13] + "..." + "by" + " " + self.user.username