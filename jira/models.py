from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.user.username

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(User, related_name='owner', on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='members', blank=True)

    def __str__(self):
        return self.title

class Label(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    story_points = models.IntegerField()
    assignee = models.ForeignKey(User, related_name='assignee', on_delete=models.SET_NULL, null=True)
    project = models.ForeignKey(Project, related_name='project', on_delete=models.CASCADE)
    labels = models.ManyToManyField(Label, blank=True)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    task = models.ForeignKey(Task, related_name='task', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='author', on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f'Comment by {self.author.username} on {self.task.title}'
