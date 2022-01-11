from django.shortcuts import render
from django.http import HttpResponse
from . import models

def hello_world(request):
    return HttpResponse('hello world')


def book_all(request):
    books = models.Books.objects.all()
    return render(request, 'books_list.html', {'books': books})
