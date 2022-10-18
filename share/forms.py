from django import forms
from .models import Post, Profile, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'file']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name','gender', 'email_address', 'desc', 'avatar')
       
       
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email_address': forms.EmailInput(attrs={'class': 'form-control'}),
            'desc': forms.TextInput(attrs={'class': 'form-control'}),
        }      

class CommentForm(forms.Form):
    class Meta:
        model = Comment
        fields = ('text')

        widgets = {
	        'text': forms.Textarea(attrs={
                'rows': 3}),

        }