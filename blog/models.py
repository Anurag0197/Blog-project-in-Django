# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete = models.CASCADE)
    title = models.CharField(max_length = 200)
    text = models.TextField()
    create_date = models.DateTimeField(default = timezone.now())
    published_date = models.DateTimeField(blank = True,null = True)
    like = models.PositiveIntegerField(default = 0)

    def __str__(self):
        return self.title

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def comment_count(self):
        return self.comments.all()

    def get_absolute_url(self):
        return reverse('blog:post_detail',kwargs = {'pk':self.pk})

    def likes(self):
        self.like += 1
        self.save()

class Comment(models.Model):
    post = models.ForeignKey('blog.Post',related_name ='comments',on_delete = models.CASCADE)
    author = models.CharField(max_length = 200)
    text = models.TextField()
    create_date = models.DateTimeField(default = timezone.now())

    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.text
