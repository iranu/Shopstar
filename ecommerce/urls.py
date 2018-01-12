from django.conf.urls import url

from ecommerce.Views.views import RegistrationAPIView, LoginAPIView, UserRetrieveUpdateAPIView, GetCategroyView, \
    GetProductView, \
    ProfileRetrieveAPIView

urlpatterns = [
    url(r'^users/?$', RegistrationAPIView.as_view()),
    url(r'^users/login?$', LoginAPIView.as_view()),
    url(r'^changepassword/?$', UserRetrieveUpdateAPIView.as_view()),
    url(r'^get_category/?$',GetCategroyView.as_view()),
    url(r'^get_product/?$',GetProductView.as_view()),
    url(r'^profiles/(?P<username>\w+)/?$', ProfileRetrieveAPIView.as_view()),
]