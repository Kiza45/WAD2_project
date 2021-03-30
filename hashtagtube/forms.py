from django import forms
from hashtagtube.models import Category, Page, UserProfile
from django.contrib.auth.models import User

class CategoryForm(forms.ModelForm):
	title = forms.CharField(max_length=25,
		                    help_text="Please enter the category name.")
	
	class Meta:
		model = Category
		fields = ('title',)

class PageForm(forms.ModelForm):
	title = forms.CharField(max_length=30,
		                    help_text="Please enter the title of the page.")
	video = forms.FileField(help_text="Please upload the video of the page.")
	thumbnail = forms.ImageField()
	date = forms.DateField()
	views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

	class Meta:
		model = Page

		fields = ('title', 'video', 'thumbnail','views',)


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username','email','password',)

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('picture',)