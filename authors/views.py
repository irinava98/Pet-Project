from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView
from EXAM.utils import get_user_obj
from authors.forms import AuthorCreateForm, AuthorEditForm
from authors.models import Author


# Create your views here.
class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorCreateForm
    template_name = 'create-author.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class AuthorEditView(UpdateView):
    model = Author
    form_class = AuthorEditForm
    template_name = 'edit-author.html'
    success_url = reverse_lazy('author-details')

    def get_object(self, queryset=None):
        return get_user_obj()


class AuthorDetailView(DetailView):
    template_name = 'details-author.html'

    def get_object(self, queryset=None):
        return get_user_obj()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = self.get_object()
        context['author'] = author
        latest_post = author.posts.order_by('-updated_at').first()
        context['latest_post'] = latest_post
        return context


class AuthorDeleteView(DeleteView):
    template_name = 'delete-author.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return get_user_obj()
