list = ['egg','protien']

for item in list:
    print(item)

def myCollection(username,password):
    return  print((username)+(password))

myCollection("vishwas","star")

class user:
    name = ""
    age = ""
    sex = ""

    def userDescription(self):
        print(self.name+self.age+self.sex)

vehicle1 = user()
vehicle1.name = "ram"
vehicle1.age =  "23"
vehicle1.sex =  "male"

vehicle1.userDescription()

usernumbers = {"ram":"8947882880","john":"8928972897"}

print(usernumbers)

import urllib

import sys

from django.conf import settings
from django.conf.urls import url
from django.http import HttpResponse
from django.core.management import execute_from_command_line

settings.configure(
    DEBUG=True,
    SECRET_KEY='thisisabadkeybutitwilldo',
    ROOT_URLCONF=sys.modules[__name__],
)

def index(request):
    return HttpResponse('Hello, World')

urlpatterns = path('',
    (r'^hello-world/$', index),
)

if __name__ == "__main__":
    execute_from_command_line(sys.argv)

    urlpatterns = (
        url(r'^hello/$',)
    )