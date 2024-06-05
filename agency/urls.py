from django.urls import path

from .views import (
    index,
    NewspaperListView,
    NewspaperDetailView,
)


urlpatterns = [
    path("", index, name="index"),
    path("newspapers/", NewspaperListView.as_view(), name="newspaper_list"),
    path("newspapers/<int:pk>", NewspaperDetailView.as_view(), name="newspaper_detail"),
]


app_name = 'agency'
