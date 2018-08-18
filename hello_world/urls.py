from django.conf.urls import url
from hello_world import views

urlpatterns = [
    url(r'',views.HelloView.as_view()),
]
