
from django.urls import path, include
from rest_framework import routers
from .api import QuestionViewSet, AccountViewSet,TokenViewSet
# from .views import QuestionView

router = routers.DefaultRouter()
router.register('question', QuestionViewSet, 'question')
router.register('account', AccountViewSet, 'account')
router.register('token', TokenViewSet, 'token')
# urlpatterns = [
#    path('home', QuestionView.as_view()),
# ]

# urlpatterns = router.urls
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]