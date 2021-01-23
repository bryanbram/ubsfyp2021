from django.contrib import admin,messages 
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import Account, Question, Option, Token, Chapter, Level, Mode, Game, UserTestResult, UserGameResult, OrganizationKey
from django import forms

# Register your models here.
class OptionInline(admin.StackedInline):
    model = Option
    extra = 4

class QuestionAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Question',  {'fields': ['title', 'topic','level', 'mode','game','photo']}),
    ]
    list_display = ('title','level','game','creation_time')
    list_filter = ('creation_time','level')
    search_fields = ['title']
    inlines = [OptionInline]

class TokenAdmin(admin.ModelAdmin):
    fields = ['email'] #'__all__'
    list_display = ['email', 'token','has_registered','creation_time']

class ModeAdmin(admin.ModelAdmin):
    list_display = ['game_mode','time_limit_in_seconds']

class GameAdmin(admin.ModelAdmin):
    list_display = ['game_level','game_mode','game_number','creation_time']
    list_filter = ('creation_time','game_level','game_mode')

class LevelAdmin(admin.ModelAdmin):    
    list_display = ['chapter_title','level_number']
    list_filter = ['chapter_title']


class AccountAdmin(BaseUserAdmin):

    list_display = ('email', 'username', 'is_staff','has_taken_test')
    list_filter = ('is_staff','has_taken_test')
    fieldsets = (
        ('Personal info', {'fields': ('email','username', 'password')}),
        ('Permissions', {'fields': ('is_staff',)}),
    )

    add_fieldsets = (
        ('Personal info', {
            'classes': ('wide',),
            'fields': ('email', 'username','password1', 'password2','is_staff')}
        ),
    )
    search_fields = ('email','username')
    ordering = ('email',)
    filter_horizontal = ()

class UserTestResultAdmin(admin.ModelAdmin):
    list_display = ['user', 'chapter', 'score']
    list_filter = ['user']

class UserGameResultAdmin(admin.ModelAdmin):
    list_display =['user','game', 'finished_status','result']
    list_filter = ['user','game']

class OrganizationKeyAdmin(admin.ModelAdmin):
    list_display = ['organizationKey']

admin.site.site_header = "H0ST4GE Admin Dashboard"
admin.site.unregister(Group)
# admin.site.unregister(User)
admin.site.register(Question,QuestionAdmin)
admin.site.register(Token,TokenAdmin)
admin.site.register(Chapter)
admin.site.register(Level, LevelAdmin)
admin.site.register(Mode, ModeAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(UserGameResult, UserGameResultAdmin)
admin.site.register(UserTestResult, UserTestResultAdmin)
admin.site.register(OrganizationKey)
# admin.site.register()
# admin.site.register()
# admin.site.register()
# admin.site.register()
# admin.site.register()
# admin.site.register()
