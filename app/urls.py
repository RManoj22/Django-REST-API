from django.urls import path,include
# from . views import List_and_Create,Retrieve_and_Delete
from . views import InfoAPI
# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register('info', InfoView)

# urlpatterns = [
#     path("",include(router.urls)),
# ]

# urlpatterns = [
#     path('<int:pk>',Retrieve_and_Delete.as_view()),
#     path('',List_and_Create.as_view()),
# ]


urlpatterns = [
    path('',InfoAPI.as_view()),
    path('<int:id>/',InfoAPI.as_view())
]