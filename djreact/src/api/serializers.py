### help to turn the content of a model into json format
from rest_framework import serializers
from .models import Account, Question, Option, Token, Chapter, Level, Mode,Game

class QuestionSerializer(serializers.ModelSerializer):
    serializers.ImageField(use_url=True, required=False, allow_null=True)
    class Meta:
        model = Question
        # fields = ('id', 'question_id', 'name', 'level','creation_time')
        fields = '__all__'

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ("username", "email", "password")#exclude = ('is_admin', 'is_active', 'last_login')

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields =  '__all__' #( "email", "has_registered")