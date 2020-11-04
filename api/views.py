from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import user, education, job, pictures, contact, project, blog_post
from django.contrib.auth.models import User
from .serializer import userSerializer, EducationSerializer, JobSerializer, PicturesSerializer, ProjectSerializer, Blog_PostSerializer, ContactSerializer

class EducationView(viewsets.ModelViewSet):
    queryset = education.objects.all()
    serializer_class = EducationSerializer

class JobView(viewsets.ModelViewSet):
    queryset = job.objects.all()
    serializer_class = JobSerializer

class PicturesView(viewsets.ModelViewSet):
    queryset = pictures.objects.all()
    serializer_class = PicturesSerializer

class usersView(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = userSerializer

class ProjectView(viewsets.ModelViewSet):
    queryset = project.objects.all()
    serializer_class = ProjectSerializer

class Blog_PostView(viewsets.ModelViewSet):
    queryset = blog_post.objects.all()
    serializer_class = Blog_PostSerializer

class ContactView(viewsets.ModelViewSet):
    queryset = contact.objects.all()
    serializer_class = ContactSerializer
