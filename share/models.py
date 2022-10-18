from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image



# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(blank=True,upload_to='Files')
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return self.title


class Profile(models.Model):

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    first_name = models.CharField('First Name', max_length=100, null='False')
    last_name = models.CharField('Last Name', max_length=100, null='False')
    gender = models.CharField(max_length=50, choices= GENDER_CHOICES, default='NA', null='False')
    email_address = models.EmailField('Email Address',)
    desc_text = 'Hey there! this is a default text description about you. You can change it to suit you profile'
    desc = models.CharField('Description', default = desc_text, max_length=200, null=True)
    avatar = models.ImageField(default='avatar.png', upload_to='avatars/')

    def __str__(self):
        return str(self.first_name)
    

class Comment(models.Model):
	user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
	post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
	text = models.TextField(max_length=2048, blank=True)
	comment_date = models.DateTimeField(auto_now_add=True)