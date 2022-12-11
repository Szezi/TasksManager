from django.urls import path
from .views import DashboardView, TaskCreate, TaskUpdate, TaskDelete, TasksBoardDetail, TasksBoardCreate, TasksBoardUpdate, TasksBoardDelete, PinedTaskCreate, PinedTaskDelete
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('dashboard', DashboardView.as_view(), name='dashboard'),

    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),

    path('pined_task-create/', PinedTaskCreate.as_view(), name='pined_task-create'),
    path('pined_task-delete/<int:pk>/', PinedTaskDelete.as_view(), name='pined_task-delete'),

    path('board-create/', TasksBoardCreate.as_view(), name='board-create'),
    path('board-detail/<int:pk>/', TasksBoardDetail.as_view(), name='board-detail'),
    path('board-update/<int:pk>/', TasksBoardUpdate.as_view(), name='board-update'),
    path('board-delete/<int:pk>/', TasksBoardDelete.as_view(), name='board-delete')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)