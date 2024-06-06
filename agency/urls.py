from django.urls import path

from .views import (
    index,
    NewspaperListView,
    NewspaperDetailView,
    NewspaperCreateView,
    NewspaperUpdateView,
    NewspaperDeleteView,
    RedactorListView,
)


urlpatterns = [
    path("", index, name="index"),
    path("newspapers/", NewspaperListView.as_view(), name="newspaper_list"),
    path("newspapers/<int:pk>/", NewspaperDetailView.as_view(), name="newspaper_detail"),
    path("newspapers/create/", NewspaperCreateView.as_view(), name="newspaper_create"),
    path("newspapers/<int:pk>/update/", NewspaperUpdateView.as_view(), name="newspaper_update"),
    path("newspapers/<int:pk>/delete/", NewspaperDeleteView.as_view(), name="newspaper_delete"),
    path("redactor/", RedactorListView.as_view(), name="redactor_list"),

]


app_name = 'agency'
