from django.views.generic import TemplateView, ListView
from EXAM.utils import get_user_obj
from posts.models import Post


# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['author'] = get_user_obj()
        return context


class DashboardView(ListView):
    model = Post
    template_name = 'dashboard.html'
    context_object_name = 'post_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['author'] = get_user_obj()
        return context
