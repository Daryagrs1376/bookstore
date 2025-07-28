from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer



class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.prefetch_related('comments').all()
    serializer_class = BookSerializer
    