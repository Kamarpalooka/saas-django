from django.urls import path
from user_messages import views


urlpatterns = [
    path('', views.UserMessageList.as_view(), name=views.UserMessageList.name),
    path('<uuid:pk>', views.UserMessageDetail.as_view(), name=views.UserMessageDetail.name),
]