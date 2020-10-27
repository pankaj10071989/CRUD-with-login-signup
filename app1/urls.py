from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path

from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('signup1/',views.signup1,name='signup1'),
    path('getdata/',views.getdata,name='getdata'),
    path('verify/', views.verify, name='verify'),
    path('getdatabyid/',views.getdatabyid,name='getdatabyid'),
    path('deletedata/<str:pk>', views.deletedata, name='deletedata'),
    path('editdata/<str:pk>', views.editdata, name='editdata'),
    path('updatedata/<str:pk>', views.updatedata, name='updatedata'),
    path('dashboard/', views.dashboard, name='dashboard'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)