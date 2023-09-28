from gzip import FCOMMENT
from token import COMMENT
from django.db import models
from django.contrib.auth.models import *
# from django.contrib.auth import *
from django.conf import settings
# from django.contrib.gis.db import models

# Create your models here.
class UserProfile(AbstractUser):
    
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username
    
class CustomUser(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    address = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=15)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

# Model for Blog Categories
class Category(models.Model):
    name = models.CharField(max_length=100)
    # slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

# class Place(models.Model):
#     name = models.CharField(max_length=255)
#     location = models.PointField()
    
#     def __str__(self):
#         return self.name

# Model for Blog Posts
class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    content = models.TextField()
    short_content = models.TextField()
    categories = models.ManyToManyField(Category)
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    featured_image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    map = models.URLField()
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    customer_service = models.CharField(
        choices=[
            ('poor', 'Poor'),
            ('average', 'Average'),
            ('good', 'Good'),
            ('excellent', 'Excellent'),
        ],
        max_length=10
    )
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

    def __str__(self):
        return self.title
        

# Model for Comments on Blog Posts
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.IntegerField(default=0, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    review_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"

    def increment_review_count(self):
        self.review_count += 1
        self.save()

    def decrement_review_count(self):
        if self.review_count > 0:
            self.review_count -= 1
            self.save()
   
class UserEditHistory(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    # edited_by = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    # Add fields to track changes, e.g., edited_field_name, previous_value, new_value, etc.

    def __str__(self):
        return f"{self.user.username} - {self.timestamp}"
    
