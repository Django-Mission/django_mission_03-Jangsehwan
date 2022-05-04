from random import choices
import django
from django import forms

from .models import Post

from django.core.exceptions import ValidationError


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class PostCreateForm(PostBaseForm):
    class Meta(PostBaseForm.Meta):
        fields = ['image', 'content']

    def clean_content(self):
        data = self.cleaned_data['content']
        if "비속어" == data:
            raise ValidationError("비속어는 사용하실수 없습니다")
        return data


class PostUpdateForm(PostBaseForm):
    class Meta(PostBaseForm.Meta):
        fields = ['image', 'content']


class PostDetailForm(PostBaseForm):
    def __init__(self, *args, **kwargs):
        super(PostDetailForm, self).__init__(*args, **kwargs)
        for key in self.fields:
            key.fields[key].widget.attrs['disabled'] = True
