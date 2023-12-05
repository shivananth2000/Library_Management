from django.shortcuts import render
import json
from django.http import HttpResponse
from books.models import Book_management, Patron_management, Borrowing

# Create your views here.
def index(request):
    return HttpResponse("Library ")