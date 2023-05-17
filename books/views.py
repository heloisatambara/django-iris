from django.shortcuts import render, redirect
from .models import Book

# Create your views here.
def home(request):
    books = Book.objects.all()
    return render(request, "index.html", {"books": books})

def save(request):
    ttitle = request.POST.get("title")
    tauthor = request.POST.get("author")
    Book.objects.create(title=ttitle, author=tauthor)
    books = Book.objects.all()
    return render(request, "index.html", {"books": books})

def edit(request, id):
    book = Book.objects.get(id=id)
    return render(request, "update.html", {"book": book})

def update(request, id):
    book = Book.objects.get(id=id)
    book.title = request.POST.get("title")
    book.author = request.POST.get("author")
    book.save()
    return redirect(home)