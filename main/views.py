from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Book, Author, Genre
from django.http import FileResponse
from .forms import BookForm, AuthorForm, GenreForm


class BooksView(ListView):
    model = Book
    template_name = 'main/layout.html'
    context_object_name = 'books'


class BooksDetailView(DetailView):
    model = Book
    template_name = 'main/detail_view.html'
    context_object_name = 'book'


class BooksUpdate(UpdateView):
    model = Book
    template_name = 'main/add.html'
    form_class = BookForm
    success_url = reverse_lazy('main')


class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('main')
    template_name = 'main/del.html'


def read(request, id):
    obj = Book.objects.get(id=id)
    filename = obj.file.path
    response = FileResponse(open(filename, 'rb'))
    return response


def add_view(request):
    form = BookForm()
    form2 = AuthorForm()
    form3 = GenreForm()
    err = ''
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES )
        form2 = AuthorForm(request.POST)
        form3 = GenreForm(request.POST)
        if form2.is_valid() and form3.is_valid() and form.is_valid() :
            auth = form2.save(commit= False)
            if auth not in Author.objects.all():
                auth.save()

            gen = form3.save(commit = False)
            if gen not in Genre.objects.all():
                gen.save()
            bk = form.save(commit=False)

            bk.author = auth
            bk.genre = gen
            bk.save()
            return redirect('main')
        else:
            err = 'Invalid values'
    data = {'form': form, 'form2': form2, "form3":form3 , 'err':err}
    return render(request, 'main/add.html', data)
