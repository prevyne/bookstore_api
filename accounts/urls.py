from django.urls import path, reverse_lazy, include
from .views import UserRegistrationView, UserLoginView, UserLogoutView
from django.views.generic import TemplateView

urlpatterns = [
    path('book_list/', include('books.urls'), name = 'booklist'),
    path('home/', TemplateView.as_view( template_name = 'base.html'), name = 'homepage'),
    path('register/', UserRegistrationView.as_view(), name='registration'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),

]
