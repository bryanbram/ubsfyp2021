
from django.urls import path, include
from rest_framework import routers
from .api import QuestionViewSet, AccountViewSet,TokenViewSet
# from .views import QuestionView
from .views import ProjectList, ProjectBugsList,ProjectView,  ProjectVulnerabilityFacet, ProjectVulnerability

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
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    #path for calling sonarcloud api
    #path('sonarcloud/', ProjectView, name = 'sonarcloud'),
    path('projectlist/<str:org>/', ProjectList, name = 'projectlist'),
    path('projectlist/<str:org>/bug/<str:prokey>/', ProjectBugsList, name = 'buglist'),
    path('projectlist/<str:org>/vulnerability/<str:prokey>/', ProjectVulnerabilityFacet, name = 'vulnerabilitylist'),
    path('projectlist/<str:org>/vulnerability/<str:prokey>/<str:issuekey>', ProjectVulnerability, name = 'vulnerability'),

]