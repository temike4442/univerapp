from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import home, IndexView,ChatsView

urlpatterns = [
    path('', home, name='home'),
    path('home/',IndexView.as_view(),name='index'),
    path('chat/',ChatsView.as_view(),name='chats'),
    path('login/', auth_views.LoginView.as_view()),
    path('users/', include('django.contrib.auth.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)