from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Comment(models.Model):
    book = models.ForeignKey(Book, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f"Comment on {self.book.title}"
