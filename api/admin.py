from django.contrib import admin
from .models import education, job, pictures, user, contact, project, blog_post

# Register your models here.
admin.site.register(education)
admin.site.register(job)
admin.site.register(pictures)
admin.site.register(user)
admin.site.register(contact)
admin.site.register(blog_post)
admin.site.register(project)
