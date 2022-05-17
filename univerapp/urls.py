from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import home, IndexView,ChatsView,ChatView,send_message

urlpatterns = [
    path('', home, name='home'),
    path('home/',IndexView.as_view(),name='index'),
    path('chat/',ChatsView.as_view(),name='chats'),
    path('chat/<int:dialog_id>/',ChatView.as_view(),name='chat_id'),
    path('send_message/',send_message,name='send_message'),
    path('login/', auth_views.LoginView.as_view()),
    path('users/', include('django.contrib.auth.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)