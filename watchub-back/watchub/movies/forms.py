from django import forms
from .models import Review, Comment


class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = ['rank',]


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content', ]