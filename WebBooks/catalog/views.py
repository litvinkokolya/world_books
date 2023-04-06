from django.shortcuts import render
from .models import Book, Author, Bookinstance, Genre
from django.views import generic

class ВookListView(generic.ListView):
    model = Book
    paginate_by = 3

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 4

def index(request):
    num_books = Book.objects.all().count()
    num_instances = Bookinstance.objects.all().count()
    num_instances_available = Bookinstance.objects.filter(status_exact=2).count()
    num_authors = Author.objects.count()
    return render(request, 'index.html',
                  context={'num_books': num_books,
                           'num_instances': num_instances,
                           'num_instances_abailable': num_instances_available,
                           'num_authors': num_authors})