from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from blog import views

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='post-list', permanent=False)),
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    
    
]