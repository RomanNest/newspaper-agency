from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import NewspaperForm, RedactorCreationForm
from .models import Newspaper, Redactor, Topic


@login_required
def index(request: HttpRequest) -> HttpResponse:
    num_newspapers = Newspaper.objects.count()
    num_redactors = Redactor.objects.count()
    num_topics = Topic.objects.count()
    num_visits = request.session.get("nim_visits", 0)
    request.session["num_visits"] = num_visits + 1
    contex = {
        "num_newspapers": num_newspapers,
        "num_redactors": num_redactors,
        "num_topics": num_topics,
        "num_visits": num_visits,
    }
    return render(request, "agency/index.html", context=contex)


class TopicListView(LoginRequiredMixin, generic.ListView):
    model = Topic


class RedactorListView(LoginRequiredMixin, generic.ListView):
    model = Redactor


class RedactorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Redactor
    form_class = RedactorCreationForm



class NewspaperListView(LoginRequiredMixin, generic.ListView):
    model = Newspaper


class NewspaperDetailView(LoginRequiredMixin, generic.DetailView):
    model = Newspaper


class NewspaperCreateView(LoginRequiredMixin, generic.CreateView):
    model = Newspaper
    form_class = NewspaperForm
    success_url = reverse_lazy("agency:newspaper_list")


class NewspaperUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Newspaper
    form_class = NewspaperForm
    success_url = reverse_lazy("agency:newspaper_list")


class NewspaperDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Newspaper
    success_url = reverse_lazy("agency:newspaper_list")
