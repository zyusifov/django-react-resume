from django.contrib import admin

from .models.user import User
from .models.resume import Resume

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    pass
admin.site.register(User, UserAdmin)

class ResumeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Resume, ResumeAdmin)