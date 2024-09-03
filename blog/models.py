from django.db import models
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=200)
#    content = models.TextField()  # Use TextField for rich text content
    content = RichTextField(blank=True, null=True)  # Use TextField for rich text content
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    file = models.FileField(upload_to='files/', blank=True, null=True)
    audio = models.FileField(upload_to='audio/', blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Announcement(models.Model):
    title = models.CharField(max_length=200)
#    content = models.TextField()  # Use TextField for rich text content
    content = RichTextField(blank=True, null=True)  # Use TextField for rich text content
    image = models.ImageField(upload_to='announcements/images/', blank=True, null=True)
    audio = models.FileField(upload_to='announcements/audio/', blank=True, null=True)
    video = models.FileField(upload_to='announcements/videos/', blank=True, null=True)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class About(models.Model):
#    content = models.TextField()  # Use TextField for rich text content
    content = RichTextField()  # Use TextField for rich text content

    def __str__(self):
        return "About Us"

class Contact(models.Model):
#    content = models.TextField()  # Use TextField for rich text content
    content = RichTextField()  # Use TextField for rich text content

    def __str__(self):
        return "Contact Us"

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    content = models.TextField()  # Use TextField for rich text content
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'
