from rest_framework import viewsets
from .models import Comment
from .serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.select_related('book').all()
    serializer_class = CommentSerializer
