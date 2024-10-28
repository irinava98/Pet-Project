from django import forms
from authors.models import Author


class AuthorCreateForm(forms.ModelForm):
    class Meta:
        model = Author
        exclude = ['info', 'image_url']
        labels = {
            'first_name': 'First Name:',
            'last_name': 'Last Name:',
            'passcode': 'Passcode:',
            'pets_number': 'Pets Number:'
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter your first name...'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter your last name...'}),
            'passcode': forms.PasswordInput(attrs={'placeholder': 'Enter 6 digits...'}),
            'pets_number': forms.TextInput(attrs={'placeholder': 'Enter the number of your pets...'})
        }
        help_texts = {
            'passcode': 'Your passcode must be a combination of 6 digits'
        }


class AuthorEditForm(forms.ModelForm):
    class Meta:
        model = Author
        exclude = ['passcode']
        labels = {
            'first_name': 'First Name:',
            'last_name': 'Last Name:',
            'pets_number': 'Pets Number:',
            'info': 'Info:',
            'image_url': 'Profile Image URL:'
        }

