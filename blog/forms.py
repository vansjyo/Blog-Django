from django import forms
from .models import Post

class PostForm(forms.ModelForm):
#PostForm is the name of the form
	class Meta:
		#Tell django which model should be used to create this form
		model = Post
		#Tell django which fields should be imported in the form
		fields = ('title', 'text',)
