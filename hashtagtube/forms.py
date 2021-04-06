from django import forms
from hashtagtube.models import Category, Page, UserProfile
from django.contrib.auth.models import User


class CategoryForm(forms.ModelForm):
    title = forms.CharField(max_length=25,
                            help_text="Please enter the category name.")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    
    class Meta:
        model = Category
        fields = ('title',)

class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=30,
                            help_text="Please enter the title of the page.")
    video = forms.FileField(required=False, help_text="Please upload the video of the page.")
    
    
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    like_react = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    dislike_react = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    haha_react = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    love_react = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Page

        exclude = ('category','author','thumbnail','date',)
       

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','email','password',)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)