from django.shortcuts import render
from rest_framework.response import Response
#from streamapp.camera import VideoCamera #2 IPWebCam #MaskDetect, LiveWebCam
# Create your views here.
import cv2
import os,urllib.request
from django.conf import settings
camera=cv2.VideoCapture(0)
Detection = cv2.CascadeClassifier(os.path.join(
			settings.BASE_DIR,'opencv_haarcascade_data/haarcascade_frontalface_default.xml'))
def index(request):
	return render(request, 'streamapp/home.html')

def frame_create():
    while True:
        ret,frame = camera.read()
        if not ret:
            break
        else:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            detected = Detection.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
            for (x, y, w, h) in detected:
                cv2.rectangle(frame, pt1=(x, y), pt2=(x + w, y + h), color=(0,255, 0), thickness=2)
            frame_flip = cv2.flip(frame,1)
            r,buf=cv2.imencode('.jpg',frame_flip)
            frame=buf.tobytes()
            if cv2.waitKey(1)& 0xFF == ord('q'):
                 break
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        
def video_gen(request):
	return Response(frame_create(),
					content_type='multipart/x-mixed-replace; boundary=frame')


#2def webcam_feed(request):
#2	return StreamingHttpResponse(gen(IPWebCam()),
#2					content_type='multipart/x-mixed-replace; boundary=frame')


#def mask_feed(request):
#	return StreamingHttpResponse(gen(MaskDetect()),
#					content_type='multipart/x-mixed-replace; boundary=frame')
					
#def livecam_feed(request):
#	return StreamingHttpResponse(gen(LiveWebCam()),
#					content_type='multipart/x-mixed-replace; boundary=frame')
