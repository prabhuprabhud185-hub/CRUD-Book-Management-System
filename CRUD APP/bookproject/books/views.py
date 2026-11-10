from django.shortcuts import render, redirect, get_object_or_404
from .models import Book

# READ - Display all books
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html',
                  {'books': books})


# CREATE - Add a new book
def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        price = request.POST['price']

        Book.objects.create(
            title=title,
            author=author,
            price=price
        )

        return redirect('book_list')

    return render(request, 'books/book_form.html')


# UPDATE - Modify book price
def update_book(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        book.price = request.POST['price']
        book.save()
        return redirect('book_list')

    return render(request, 'books/book_update.html',
                  {'book': book})


# DELETE - Remove a book
def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('book_list')
