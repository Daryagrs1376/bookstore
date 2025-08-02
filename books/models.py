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


# خط12 :
# یعنی هر کامنت به یک کتاب مرتبط است. این رابطه‌ی ManyToOne (هر کتاب چند کامنت) است
# related_name='comments' باعث می‌شود که از طرف کتاب هم بتوانیم به همه کامنت‌ها دسترسی داشته باشی
# مثل book.comments.all()
# در این مدل، رابطه book با Book از نوع ForeignKey است  یعنی ManyToOne 
# f = f string (line16)