from django.urls import path

from fusion.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
