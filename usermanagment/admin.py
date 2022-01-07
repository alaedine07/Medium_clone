from django.contrib import admin
from usermanagment.models import Users

class UsersAdmin(admin.ModelAdmin):
    pass

admin.site.register(Users, UsersAdmin)
