from rest_framework import viewsets
from .models import Comment
from .serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.select_related('book').all()
    serializer_class = CommentSerializer


# خط7:
# چرا از select_related استفاده شده؟
#چون مدل Comment، فیلد book از نوع ForeignKey هست
# یعنی رابطه ManyToOne
#وقتی از select_related('book') استفاده می‌کنیم، در یک کوئری SQL، اطلاعات مربوط به کتاب هم لود میشه
# select_related:
#همه‌ی کامنت‌ها و کتاب‌های مربوطه رو با فقط 1 کوئری ترکیبی میاره
#فقط 1 کوئری
