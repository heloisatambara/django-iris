from django.shortcuts import render
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