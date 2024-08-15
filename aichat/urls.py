from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('', views.main, name='main'),
    path('chat/<int:chat_id>/', views.chat_view, name='chat_view'),
    path('chat/<int:chat_id>/send/', views.send_message, name='send_message'),
    path('create_chat/', views.create_chat, name='create_chat'),
    path('delete_chat/<int:chat_id>/', views.delete_chat, name='delete_chat'),
    path('admin/', admin.site.urls),
]
