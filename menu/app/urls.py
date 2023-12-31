from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:dish_id>/", views.details, name="detail")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)