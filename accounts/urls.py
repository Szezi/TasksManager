from django.urls import path
from .views import CustomLoginView, CustomRegisterView
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login', CustomLoginView.as_view(), name='login'),
    path('register', CustomRegisterView.as_view(), name='register'),
    path('logout', LogoutView.as_view(next_page='home'), name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)