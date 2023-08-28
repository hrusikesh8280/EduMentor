
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InstructorViewSet

router = DefaultRouter()
router.register(r'instructors', InstructorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
