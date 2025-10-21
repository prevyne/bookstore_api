from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

# Create your views here.
class UserRegistrationView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration.html'
    success_url = reverse_lazy('login')
    
class UserLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('homepage')
    
class UserLogoutView(LogoutView):
    template_name = 'header.html'
    next_page = reverse_lazy('login')