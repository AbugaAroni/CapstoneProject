from rest_framework import serializers
from .models import user, education, job, pictures,  contact, project, blog_post

class EducationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = education
        fields = ('id','url', 'title','qualification','description','start','finish')

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = job
        fields = ('id','url', 'title', 'description','start','finish')

class PicturesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = pictures
        fields = ('id', 'url', 'title','alt_tag','image')

class userSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = user
        fields = ('id','url','user', 'first_name', 'last_name', 'admin', 'about','picturez', 'educationz', 'career')
