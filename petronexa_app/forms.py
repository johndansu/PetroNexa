from django import forms
from petronexa_app.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
        
class CommentForm(forms.ModelForm):
    user_name = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}))
    comment_content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Type your comment',
        'id': 'usercomment',
        'rows': '4'
    }))
    class Meta:
        model = Comment
        exclude = ['post', 'content', 'rating','created_date','review_count','author']
        # fields = ('content', )

class GasStationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'address', 'content', 'rating', 'price', 'customer_service', 'featured_image', 'latitude', 'longitude']
        widgets = {
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
            'title': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'address': forms.HiddenInput(),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5, 'required': True}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'customer_service': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'image': forms.FileInput(attrs={'class': 'form-control-file', 'accept': 'image/*', 'required': True}),
        }
        
        
