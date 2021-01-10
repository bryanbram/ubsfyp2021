from django.apps import AppConfig
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver  
# from .models import Chapter, Level
# from .signals import create_levels

class ApiConfig(AppConfig):
    name = 'api'

    # def ready(self):
    #     post_save.connect(create_levels, sender=Chapter)
