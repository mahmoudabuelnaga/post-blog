from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.urls import reverse

class PostManager(models.Manager):
    def get_queryset(self):
        queryset = super(PostManager, self).get_queryset().filter(status='published')
        queryset = queryset # TODO
        return queryset

class Post(models.Model):
    STATUS_CHOICES  = (
        ('draft','Draft'),
        ('published','Published'),
    )
    author          = models.ForeignKey(User, on_delete=models.CASCADE)
    title           = models.CharField(max_length=250)
    slug            = models.SlugField(blank=True, null=True)
    img             = models.ImageField(upload_to='post_pic', default='123.png')
    body            = models.TextField()
    publish         = models.DateTimeField(default=timezone.now)
    created         = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)
    status          = models.CharField(max_length=9, choices=STATUS_CHOICES, default='draft')
    objects         = PostManager()
    published       = models.Manager()

    class Meta:
        ordering = ('publish',)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post,self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post_detail', args=[
                                            self.publish.year,
                                            self.publish.month,
                                            self.publish.day,
                                            self.slug
                                        ])