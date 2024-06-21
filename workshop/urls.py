from django.contrib import admin
from django.urls import path
#from django.conf.urls import url, include
# from LOGIN import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from LOGIN.views import UserReg, sharing, discussion, view, workshop, booking, member
from .import views
#from django.conf.urls import url
# from .import index

# from .api import UserList, UserDetail, UserAuthentication

app_name = 'workshop'
urlpatterns = [
    
    path('MainWorkshop',views.workshop, name="MainWorkshop"),
    path('Booking',views.booking, name="Booking"),
    path('Booking/<str:pk>',views.booking, name="Booking"),
    path('CreateWorkshop',views.createWorkshop, name="CreateWorkshop"),
    path('UpdateWorkshop/<str:pk>',views.updateWorkshop, name="UpdateWorkshop"),
    path('DeleteWorkshop/<str:pk>',views.deleteWorkshop, name="DeleteWorkshop"),
    path('ViewWorkshop/<str:pk>',views.viewWorkshop, name="ViewWorkshop"),
    path('MyWorkshop',views.myWorkshop, name="MyWorkshop"),
    path('MyBooking',views.viewBooking, name="MyBooking"),
    path('ViewInbox', views.viewInbox, name="ViewInbox"),
    path('CancelBooking/<str:pk>',views.deleteBooking, name="DeleteBooking"),
    path('WorkshopParticipant/<str:id>',views.WorkshopParticipant, name="WorkshopParticipant"),
    path('AddWorkshopSharing/<str:pk>',views.AddWorkshopSharing, name="AddWorkshopSharing"),
    path('Filter_SoilTag',views.Workshop_SoilTag, name="Workshop_SoilTag"),
    path('Filter_PlantTag',views.Workshop_PlantTag, name="Workshop_PlantTag"),
    # path('Workshop_LocationTag',views.Workshop_LocationTag, name="Workshop_LocationTag"),
    # path('Workshop_DemographicTag',views.Workshop_DemographicTag, name="Workshop_DemographicTag"),
    #path('Location',views.Location, name="Location"),


] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()







