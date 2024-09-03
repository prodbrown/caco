from django.contrib import admin
from .models import Post, Announcement, About, Contact, Comment

# Register your models here.
admin.site.register(Post)
admin.site.register(Announcement)
admin.site.register(About)
admin.site.register(Contact)
admin.site.register(Comment)
