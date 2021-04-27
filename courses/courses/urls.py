from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
import main_page.views


urlpatterns = [
    path('',main_page.views.home,name='home'),
    path('admin/', admin.site.urls),
    path('course/',include('course.urls'),name='course'),
    path('accounts/',include('accounts.urls')),
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)