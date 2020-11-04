from rest_framework import serializers
from .models import user, education, job, pictures,  contact, project, blog_post

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = education
        fields = ('id', 'title','qualification','description','start','finish')

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = job
        fields = ('id', 'title', 'description','start','finish')

class PicturesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = pictures
        fields = ('id', 'title','alt_tag','image')

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ('id','user', 'first_name', 'last_name', 'admin', 'about','picturez', 'educationz', 'career')
