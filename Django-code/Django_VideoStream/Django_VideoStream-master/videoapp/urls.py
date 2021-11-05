from django.urls import path
from videoapp import views


urlpatterns = [
    path('', views.index, name='index'),
    path('video_return', views.video_gen, name='video_return'),
    #3path('webcam_feed', views.webcam_feed, name='webcam_feed'),
   # path('mask_feed', views.mask_feed, name='mask_feed'),
	#path('livecam_feed', views.livecam_feed, name='livecam_feed'),
    ]