from django.urls import path

from dj_rest_auth.views import UserDetailsView
from .serializers import UserSerializer

urlpatterns = [
    # user정보
    path('user/', UserDetailsView.as_view(serializer_class=UserSerializer)),
]
