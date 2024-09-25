from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, Project, Task, Comment, Label

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['bio', 'picture', 'phone_number']

class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(required=False, write_only=True)
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'profile']
    
    def create(self, validated_data):
        profile_data = validated_data.pop('profile', {})
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        # UserProfile.objects.create(user=user)
        UserProfile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', {})
        profile = instance.userprofile

        instance.email = validated_data.get('email', instance.email)
        instance.set_password(validated_data.get('password', instance.password))

        instance.save()

        profile.bio = profile_data.get('bio', profile.bio)
        profile.picture = profile_data.get('picture', profile.picture)
        profile.phone_number = profile_data.get('phone_number', profile.phone_number)
        profile.save()

        return instance

class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ['id', 'name']

class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'owner', 'members']

    def create(self, validated_data):
        members = validated_data.pop('members', [])
        project = Project.objects.create(**validated_data)
        project.members.set(members)
        return project

class TaskSerializer(serializers.ModelSerializer):
    assignee = serializers.ReadOnlyField(source='assignee.username')
    labels = serializers.StringRelatedField(many=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'story_points', 'assignee', 'labels', 'project']

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ['id', 'content', 'author', 'task']

