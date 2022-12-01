from django.urls import path
from .views import CustomLoginView, CustomRegisterView, UserDetail, UserUpdate, UserInfo
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login', CustomLoginView.as_view(), name='login'),
    path('register', CustomRegisterView.as_view(), name='register'),
    path('logout', LogoutView.as_view(next_page='home'), name='logout'),
    path('profile-info/<int:pk>/', UserInfo.as_view(), name='profile-detail'),
    path('profile-detail', UserDetail.as_view(), name='profile-detail'),
    path('profile-update', UserUpdate.as_view(), name='profile-update'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)