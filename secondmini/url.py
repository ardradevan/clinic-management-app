from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from .import views

urlpatterns = [
    # path('',views.index,name='index'),
    path('accounts/register/',views.register_view,name="register"),
    path('',views.homeview,name='home'),
     path('about/',views.about,name='about'),
     path('booking/',views.booking,name='booking'),
    path('doctors/',views.doctors,name='doctors'),
     path('contact/',views.contact,name='contact'),
     path('department/',views.department,name='department'),
     

    #  path('account/login/',views.loginn,name='login' ),
#     path('signup_view/',views.signup_view),
   
#     path('/',views.signup,name="signup")
]
urlpatterns += staticfiles_urlpatterns()