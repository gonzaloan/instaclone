""" User views"""

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Models
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, FormView, UpdateView

from posts.models import Post
# Forms
from users.forms import SignUpForm
from users.models import Profile


class UserDetailView(LoginRequiredMixin, DetailView):
    """User DetaiL View"""
    template_name = "users/detail.html"
    # Nombre del slug
    slug_field = 'username'
    # El argumento que colocamos en urls.py
    slug_url_kwarg = 'username'

    queryset = User.objects.all()
    # Define name we are sending to template
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        """Add users's post to context"""
        context = super().get_context_data(**kwargs)

        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context


class SignUpView(FormView):
    """Users sign up View."""
    template_name = 'users/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """Save form data"""
        form.save()
        return super().form_valid(form)


def login_view(request):
    """Login view"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            # Redirección
            return redirect('posts:feed')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid Username and password'})

    return render(request, 'users/login.html')


@login_required
def logout_view(request):
    """Logout a user"""
    logout(request)
    return redirect('users:login')


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """Update Profile View"""
    template_name = "users/update_profile.html"
    model = Profile
    fields = ['website', 'biography', 'phone_number', 'picture']

    def get_object(self):
        """Return users profile"""
        return self.request.user.profile

    def get_success_url(self):
        """Return to users profile"""
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username': username})
