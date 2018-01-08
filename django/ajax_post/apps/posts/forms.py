from django import forms
from django.forms import ModelForm, CharField, Textarea
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['content']
        labels = {
            'content': _('Post'),
        }
        widgets = {
            'content': Textarea(attrs={'cols': 50, 'rows': 5}),
        }

    def clean_content(self):
        data = self.cleaned_data.get('content')
        if not data:
            raise forms.ValidationError(
                _("Please enter a post!"),
                code='invalid',
                )
        return data