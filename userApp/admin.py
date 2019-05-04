from django.contrib import admin
from userApp.models import UserAuthorizingData, UserPersonalData, UserProgress

@admin.register(UserAuthorizingData)
class UserAuthorizingAdmin(admin.ModelAdmin):
    pass

@admin.register(UserPersonalData)
class UserProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    pass
