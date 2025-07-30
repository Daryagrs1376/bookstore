from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.prefetch_related('comments').all()
    serializer_class = BookSerializer


# خط 6 : 
# باعث میشه وقتی لیست کتابهارا میگیریم کامنتهای مربوط به هر کتاب هم بصورت جدا 
# واکشی بشن و در حافظه جوین بشن
# این متد برای رابطه های many to many و one to many است و نسبت به تعداد کوئری ها بهینه اس
# مثال بدون این متد برای 10 کتاب 1 کوئری برای کتاب و 10 کوئری برای کامنتها اجرا میشه ولی با این متد
# فقط 2 کوئری اجرا میشه که یکیش همه کتابها دیگریش همه کامنتها


# خط 7:
# مشخص می‌کنه از کدوم سریالایزر برای تبدیل داده‌ها به JSON استفاده بشه