from django.db import models
from django.db import models
import os
from .validators import validate_file_extension


def get_path_file(instance, filename):
    title = instance.title
    return os.path.join('lib', title, filename)


class Author(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Genre(models.Model):
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.genre


class Book(models.Model):
    title = models.CharField(max_length=100)
    annotation = models.TextField()
    file = models.FileField(upload_to=get_path_file, validators=[validate_file_extension])
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    genre = models.ForeignKey(Genre, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'

    def delete(self, *args, **kwargs):
        storage, path = self.file.storage, self.file.path

        super(Book, self).delete(*args, **kwargs)

        storage.delete(path)

    def get_absolute_url(self):
        return ''

    def __str__(self):
        return self.title
# Create your models here.
