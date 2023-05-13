from django.urls import path

from apps.chat.views import Ajax, chat, ajax_remove_data


urlpatterns = [
    path('', chat, name='chat'),
    path('ajax/', Ajax, name='ajax'),
    path('ajax-remove-content/', ajax_remove_data, name='ajax_remove_content'),
]