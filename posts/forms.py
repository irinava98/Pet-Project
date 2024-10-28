from django import forms
from EXAM.mixins import ReadOnlyMixin
from posts.models import Post


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['updated_at', 'author']

        labels = {
            'title': 'Title:',
            'image_url': 'Post Image URL:',
            'content': 'Content:'
        }


class PostCreateForm(PostBaseForm):
    class Meta(PostBaseForm.Meta):
        help_texts = {
            'image_url': 'Share your funniest furry photo URL!'
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Put an attractive and unique title...'}),
            'content': forms.Textarea(attrs={'placeholder': 'Share some interesting facts about your adorable pets...'})
        }
        error_messages = {
            'title': {
                'unique': 'Oops! That title is already taken. How about something fresh and fun?'
            }
        }


class PostEditForm(PostBaseForm):
    pass


class PostDeleteForm(ReadOnlyMixin, PostBaseForm):
    read_only_fields = ['title', 'image_url', 'content']

