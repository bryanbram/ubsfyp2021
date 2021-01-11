from .models import Account, Question, Option, Token, Chapter, Level, Mode,Game
from rest_framework import viewsets, permissions
from .serializers import QuestionSerializer, AccountSerializer, TokenSerializer


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AccountSerializer
    filterset_fields = ['email', 'username']


# Question Viewset
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = QuestionSerializer


# class TokenFilterSet(django_filters.FilterSet):
#    class Meta:
#        model = Token
#        fields = ['email', 'token']

class TokenViewSet(viewsets.ModelViewSet):
    queryset = Token.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TokenSerializer
    # filterset_class = TokenFilterSet
    filterset_fields = ['email', 'token']
