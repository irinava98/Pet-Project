from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from EXAM.utils import get_user_obj
from posts.forms import PostCreateForm, PostEditForm, PostDeleteForm
from posts.models import Post


# Create your views here.
class PostCreateView(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'create-post.html'
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = get_user_obj()
        return context

    def form_valid(self, form):
        form.instance.author = get_user_obj()
        return super().form_valid(form)


class PostEditView(UpdateView):
    model = Post
    form_class = PostEditForm
    template_name = 'edit-post.html'
    success_url = reverse_lazy('dashboard')
    pk_url_kwarg = 'post_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = get_user_obj()
        return context


class PostDetailView(DetailView):
    model = Post
    pk_url_kwarg = 'post_id'
    template_name = 'details-post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = get_user_obj()
        return context


class PostDeleteView(DeleteView):
    model = Post
    form_class = PostDeleteForm
    pk_url_kwarg = 'post_id'
    template_name = 'delete-post.html'
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = get_user_obj()
        return context

    def get_initial(self):
        return {
            'title': self.object.title,
            'image_url': self.object.image_url,
            'content': self.object.content,
        }

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.success_url)






