from django.urls import path

from apps.chat.views import Ajax, chat


urlpatterns = [
    path('', chat, name='chat'),
    path('ajax/', Ajax, name='ajax'),
]