from django.contrib import admin
from django.urls import path
from .views import home, signup, loginpage


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signup, name="signup" ),
    path('home/', home, name="home" ),
    path('login/', loginpage, name="login" ),

]
