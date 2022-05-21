from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import home, IndexView,ChatsView,ChatView,send_message,CourseView,MaterialsView,HomeTaskView,HomeTaskDetailView,edithometask

urlpatterns = [
    path('', home, name='home'),
    path('home/',IndexView.as_view(),name='index'),
    path('chat/',ChatsView.as_view(),name='chats'),
    path('chat/<int:dialog_id>/',ChatView.as_view(),name='chat_id'),
    path('course/<int:course_id>/',CourseView.as_view(),name='course_id'),
    path('course/<int:course_id>/materials/',MaterialsView.as_view(),name='materials'),
    path('course/<int:course_id>/hometask/',HomeTaskView.as_view(),name='hometasks'),
    path('course/<int:course_id>/hometask/<int:hometask_id>/',HomeTaskDetailView.as_view(),name='hometask_detail'),
    path('send_message/',send_message,name='send_message'),
    path('edithometask/<int:pk>/',edithometask,name='edithometask'),
    path('login/', auth_views.LoginView.as_view()),
    path('users/', include('django.contrib.auth.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)