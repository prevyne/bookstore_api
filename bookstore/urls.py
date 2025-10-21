"""
URL configuration for bookstore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schemaView = get_schema_view(
    openapi.Info(
        title= 'Bookstore API Documentation',
        description= 'This is a Swagger documentation for a Bookstore API',
        default_version= 'v1',
        contact = openapi.Contact(email = 'prevyneoketch6@gmail.com')
        ),
    public = True,
    permission_classes= ( IsAuthenticatedOrReadOnly, )
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('books.urls')),
    path('', include('accounts.urls')),

    #Swagger API routes
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schemaView.without_ui(cache_timeout=0),
            name = 'schema-json'),
    path('swagger/', schemaView.with_ui(cache_timeout= 0), name= 'swagger-doc'),
    path('redoc/', schemaView.with_ui(cache_timeout= 0), name= 'redoc'),
]
