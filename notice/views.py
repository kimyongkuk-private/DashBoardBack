from rest_framework import viewsets
from .serializers import NoticeSerializer
from .models import Notice


class NoticeViewSet(viewsets.ModelViewSet):
    serializer_class = NoticeSerializer

    def get_queryset(self):
        return Notice.objects.all().order_by("-created_at")

    def perform_create(self, serializer):
        serializer.save()