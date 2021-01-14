from django.db import models
from django.utils.crypto import get_random_string
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver    

# Create your models here.

class AccountManager(BaseUserManager):

    def create_user(self, email, username, password=None):
        # if not email:
        #     raise ValueError('Users must have an email address')
        user = self.model(
            email = self.normalize_email(email),
            username = username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(primary_key=True)
    username = models.CharField(max_length=20, unique=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    has_taken_test= models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def is_superuser(self):
        return self.is_admin

    class Meta:
        ordering = ['email']


class EmailFormat(models.Model):
    suffix = models.CharField(max_length=20,  unique = True) 

class Token(models.Model):

    email = models.EmailField(max_length=100, primary_key = True)
    token = models.CharField(max_length=20,  unique = True) 
    has_registered= models.BooleanField(default = False)
    creation_time = models.DateTimeField(auto_now_add = True, null=True, blank=True)

    def generate_unique_str(self, str_length):
        return get_random_string(length=str_length)
        # code = ''.join(random.choices(string.ascii_letters, k = length)) 
   
    def save(self,*args, **kwargs):
        if not self.token:
        # Generate token once, then check the db. If it alr exists, keep trying.
            str_length = 10
            while True:
                self.token = self.generate_unique_str(str_length)
                if not Token.objects.filter(token=self.token).exists():
                    super(Token, self).save()
                    return
        else:
            super(Token, self).save(*args, **kwargs)

    class Meta:
        ordering = ['email']

class Chapter(models.Model):
    level_number_choices = [(i,i) for i in range(1,11)]
    title = models.CharField(max_length=50, primary_key=True, blank=True)
    number_of_levels = models.IntegerField(default = 1, choices = level_number_choices) 
    info = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return self.title

    #  def save(self):
    #     for i in range(1, self.number_of_levels):

    #         Level.objects.bulk_create()

    class Meta:
        ordering = ['title']

class Level(models.Model):

    level_number_choices = [(i,i) for i in range(1,11)]

    chapter_title = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    level_number = models.IntegerField(default = 1, choices = level_number_choices) #, validators=[MaxValueValidator(10), MinValueValidator(1)]

    def __str__(self):
        return f"{self.chapter_title}-Level {self.level_number}"

    class Meta:
        ordering = ['chapter_title','level_number']
        unique_together =  ['chapter_title','level_number']

@receiver(post_save, sender=Chapter)
def auto_create_levels(sender, instance, created, **kwargs): # To auto create levels when a chapter is created and number of levels for that chapter is given
    if created:
        for i in range(1, instance.number_of_levels+1):
            Level.objects.create(chapter_title = instance, level_number = i)

class Mode(models.Model):
    game_mode_choices = [
        ('training', 'Training'),
        ('battle', 'Battle'),
        ('challenge', 'Challenge')
    ]
    game_mode = models.CharField(max_length=20, primary_key=True, choices=game_mode_choices, default='T')
    time_limit_in_seconds= models.PositiveSmallIntegerField(null=True, blank =True)

    def __str__(self):
        return self.game_mode

class Game(models.Model):

    game_number_choices = [(i,i) for i in range(1,11)]
    
    game_level = models.ForeignKey(Level, on_delete=models.SET_NULL, null=True)
    game_mode = models.ForeignKey(Mode, on_delete=models.SET_NULL, null=True)
    game_number = models.IntegerField(default = 1, choices = game_number_choices)
    creation_time = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.game_level}---{self.game_mode}---Game {self.game_number}"

class Question(models.Model):
    # question_id = models.CharField(max_length=8,  unique = True)
    title = models.CharField(max_length=200)
    topic = models.CharField(max_length=200, blank=True)
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    mode = models.ForeignKey(Mode, on_delete=models.SET_NULL, null=True, blank=True)
    level = models.ForeignKey(Level, on_delete=models.SET_NULL, null=True, blank=True)
    game = models.ForeignKey(Game, on_delete=models.SET_NULL, null=True, blank=True)
    creation_time = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option_text = models.CharField(max_length=200)
    explanation = models.CharField(max_length=200, null=True, blank=True)
    is_correct = models.BooleanField(default=False)
    creation_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.option_text

class UserTestResult(models.Model): 
    # to track if a user has taken the level determination test
    user =  models.ForeignKey(Account, on_delete=models.CASCADE)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    score = models.IntegerField(default = 0)
    level_result = models.IntegerField(default = 1)

    class Meta:
        unique_together =  ['user','chapter']

class UserGameResult(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    finished_status = models.BooleanField(default=False)
    result = models.IntegerField(default = 0)









