from django.contrib import admin
from django.urls import path
from logvision.accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_page, name='login'),
]
