from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver  
from .models import Chapter, Level



@receiver(post_save, sender=Chapter)
def create_levels(sender, instance, created, **kwargs):
    if created:
        for i in range(1, instance.number_of_levels+1):
            Level.objects.create(chapter_title = instance, level_number = i)
        
