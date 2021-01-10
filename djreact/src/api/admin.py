from django.contrib import admin,messages 
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import Account, Question, Option, Token, Chapter, Level, Mode,Game
from django import forms

# Register your models here.
class OptionInline(admin.StackedInline):
    model = Option
    extra = 4

class QuestionAdmin(admin.ModelAdmin):
    # exclude = ('title',)
    # fields = ('title', 'level')

    fieldsets = [
        ('Question',  {'fields': ['title', 'topic','level', 'game','photo']}),
        # ('Options', {'fields': ['option1', 'option2','option3', 'option4', 'option5','option6']})
    ]
    list_display = ('title','level','game','creation_time')
    list_filter = ('creation_time','level')
    search_fields = ['title']
    inlines = [OptionInline]

    # def level_increased_by_1(self, request, queryset): 
    #     queryset.update('level' += 1) 
    #     messages.success(request, "Selected questions' level upgraded by 1 ")


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

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'username')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Account
        fields = ('username','email', 'password', 'is_active', 'is_admin')
    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

class AccountAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'username', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        ('Personal info', {'fields': ('email','username', 'password')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        ('Personal info', {
            'classes': ('wide',),
            'fields': ('email', 'username','password1', 'password2','is_admin')}
        ),
    )
    search_fields = ('email','username')
    ordering = ('email',)
    filter_horizontal = ()

admin.site.site_header = "H0ST4GE Admin Dashboard"
admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(Question,QuestionAdmin)
admin.site.register(Token,TokenAdmin)
admin.site.register(Chapter)
admin.site.register(Level, LevelAdmin)
admin.site.register(Mode, ModeAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Account,AccountAdmin)
# admin.site.register()
# admin.site.register()
# admin.site.register()
# admin.site.register()
# admin.site.register()
# admin.site.register()
# admin.site.register()
# admin.site.register()
# admin.site.register()
