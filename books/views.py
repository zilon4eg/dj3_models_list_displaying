from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from books.models import Book





def books_view(request):
    template = 'books/books_list.html'

    book_objects = Book.objects.all()
    books = list({'name': b.name, 'author': b.author, 'pub_date': b.pub_date} for b in book_objects)

    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(books, 6)
    page = paginator.get_page(page_number)

    context = {
        'books': page.object_list,
        'page': page
    }
    return render(request, template, context)


def home(request):
    return redirect('books')


def date_of_publication(request, pub_date):
    template = 'books/books_list.html'
    book_objects = Book.objects.filter(pub_date=pub_date)
    books = list({'name': b.name, 'author': b.author, 'pub_date': b.pub_date} for b in book_objects)

    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(books, 6)
    page = paginator.get_page(page_number)

    context = {
        'books': page.object_list,
        'page': page
    }
    return render(request, template, context)
