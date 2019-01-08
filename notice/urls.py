from django.conf.urls import url
from .views import NoticeViewSet

notice_list = NoticeViewSet.as_view({"get": "list", "post": "create"})

notice_detail = NoticeViewSet.as_view(
    {"get": "retrieve", "patch": "partial_update", "delete": "destroy"}
)


urlpatterns = [
    url("^notices/$", notice_list, name="notice-list"),
    url("^notices/(?P<pk>[0-9]+)/$", notice_detail, name="notice-detail"),
]