from django.contrib.auth.models import User 
from django.db import models
from django.utils.translation import gettext as _

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    content = models.TextField()
    short_content = models.TextField()
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

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
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

    def increment_review_count(self):
        self.review_count += 1
        self.save()

    def decrement_review_count(self):
        if self.review_count > 0:
            self.review_count -= 1
            self.save()

class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
