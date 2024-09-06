from django.shortcuts import render
from .models import Books


def index(request):
    books = Books.objects.all()
    data = {'books': books}
    return render(request, 'books/index.html', context=data)
