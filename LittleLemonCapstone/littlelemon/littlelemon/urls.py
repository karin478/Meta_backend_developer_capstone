from django.contrib import admin
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from reastaurant import views
from django.urls import path, include




router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('api/booking/', include(router.urls)),
    path('api/menu-items/', include('reastaurant.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api-token-auth/', obtain_auth_token),

]