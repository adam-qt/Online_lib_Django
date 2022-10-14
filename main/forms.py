from .models import Book, Author, Genre
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, FileInput, TypedMultipleChoiceField, \
    TypedChoiceField
from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'annotation', 'file']

        widgets = {
            'title': TextInput(attrs={
                'class': "form-control",
                'placeholder': "Title of book"
            }),

            'annotation' :  Textarea(attrs={
                'class': "form-control",
                'placeholder': "Title of book"
            }),


            'file': FileInput (attrs={
                'class': 'form-control',
                'placeholder': 'add file in PDF format',
                'type': 'file'
            }),
        }


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

        widgets = {
            'name' : TextInput(attrs={

                'placeholder': 'add author'

            })
        }


class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'
        widgets = {
            'genre' : TextInput(attrs={

                'placeholder': 'add genre'

            })
        }
