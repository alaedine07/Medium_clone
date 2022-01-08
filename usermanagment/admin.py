from django.contrib import admin
from usermanagment.models import BlogUsers

class BlogUsersAdmin(admin.ModelAdmin):
    pass


admin.site.register(BlogUsers, BlogUsersAdmin)