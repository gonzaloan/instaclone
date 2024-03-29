"""Posts Views"""

from django.contrib.auth.mixins import LoginRequiredMixin
# Django
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

# Forms
from posts.forms import PostForm
# Model
from posts.models import Post


class PostsFeedView(LoginRequiredMixin, ListView):
    """Return all published posts."""
    template_name = 'posts/feed.html'
    model = Post
    ordering = '-created'
    paginate_by = 5
    context_object_name = 'posts'


class CreatePostView(LoginRequiredMixin, CreateView):
    """Create new Post"""
    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed.html')

    def get_context_data(self, **kwargs):
        """Add user and profile to context"""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context


class PostDetailView(LoginRequiredMixin, DetailView):
    """Return post detail"""
    template_name = 'posts/detail.html'
    queryset = Post.objects.all()
    context_object_name = 'post'
