from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token

from .views import RegistrationAPIView, LoginAPIView, UserRetrieveUpdateAPIView, GetCategroyView, GetProductView
from ecommerce import views
urlpatterns = [
    url(r'^users/?$', RegistrationAPIView.as_view()),
    url(r'^users/login?$', LoginAPIView.as_view()),
    url(r'^user/?$', UserRetrieveUpdateAPIView.as_view()),
    url(r'^get_category/?$',GetCategroyView.as_view()),
    url(r'^get_product/?$',GetProductView.as_view()),
]