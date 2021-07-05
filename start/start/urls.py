
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('apl.urls')),
     path('login',include('apl.urls')),
    path('Requestform',include('apl.urls')),
    path('Show',include('apl.urls')),
    path('Delete/<int:id>',include('apl.urls')),
    path('adminrequest',include('apl.urls')),
    path('empredirect/<str:name1>',include('apl.urls')),
    path('statusupdateapprove/<int:id>',include('apl.urls')),
    path('statusupdatedisapprove/<int:id>',include('apl.urls')),
    path('empredirect/showpastreq/<str:take>',include('apl.urls')),
   

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

