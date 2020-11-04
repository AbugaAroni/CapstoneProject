from django.urls import path, re_path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('education', views.EducationView)
router.register('jobs', views.JobView)
router.register('pictures', views.PicturesView)
router.register('user', views.usersView)
router.register('contact', views.ContactView)
router.register('project', views.ProjectView)
router.register('blog_post', views.Blog_PostView)

urlpatterns=[
path('', include(router.urls))
]
