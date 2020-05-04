from rest_framework import routers
from tasks.viewsets import TaskViewSet, StatusViewSet

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'statuses', StatusViewSet)