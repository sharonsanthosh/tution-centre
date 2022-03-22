from .import views
from django.urls import re_path

urlpatterns = [
    re_path(r'^$',views.MAN_index, name="MAN_index"),
    re_path(r'^MAN_profile/$',views.MAN_profile, name="MAN_profile"),
    re_path(r'^MAN_registration/$',views.MAN_registration, name="MAN_registration"),
    re_path(r'^MAN_registrationstaff/$',views.MAN_registrationstaff, name="MAN_registrationstaff"),
    re_path(r'^MAN_registrationstudent/$',views.MAN_registrationstudent, name="MAN_registrationstudent"),
    re_path(r'^MAN_currentstaff/$',views.MAN_currentstaff, name="MAN_currentstaff"),
]