from django import forms
from nh48_app.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["mountain_image", "mountain", "caption"]


