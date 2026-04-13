from django.contrib import admin
from django.urls import include, path
from app.views import * # Certifique-se de que seu app se chama 'app'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
]