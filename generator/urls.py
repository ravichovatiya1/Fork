from django.urls import path
from . import views

urlpatterns = [
    # path('', views.meme_generator, name='meme_generator'),
    path('', views.meme_library, name='meme_library'),
    path('generate/', views.meme_generate, name='meme_generate'),
    path('download/<int:meme_id>/', views.meme_download, name='meme_download'),
    path('upload', views.meme_upload, name='meme_upload'),
    path('delete/<int:meme_id>/', views.meme_delete, name='meme_delete'),
    path('update/<int:meme_id>/', views.meme_update, name='meme_update'),
]