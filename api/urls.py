from django.urls import path, re_path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('education', views.EducationView)

urlpatterns=[
path('', include(router.urls))
]
