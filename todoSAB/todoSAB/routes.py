from rest_framework import routers
from todo.views import  TodoViewSet, BoardViewSet

router = routers.DefaultRouter()
router.register(r'todos', TodoViewSet)
router.register(r'boards', BoardViewSet, base_name='board')