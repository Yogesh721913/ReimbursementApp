from apl.models import Employee
from django.urls import path
from . import views
urlpatterns = [
    path('',views.boot),
    path('login',views.home),
    path('Requestform',views.employee,name='Requestform'),
    path('Show',views.show),
    path('Delete/<int:id>',views.Delete),
    path('adminrequest',views.adminrequest),
    path('empredirect/<str:name1>',views.empredirect,name='empredirect'),
    path('statusupdateapprove/<int:id>',views.statusupdateapprove),
    path('statusupdatedisapprove/<int:id>',views.statusupdatedisapprove),
    path('empredirect/showpastreq/<str:take>',views.showpastreq),

    
]
