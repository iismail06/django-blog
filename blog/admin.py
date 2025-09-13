from django.contrib import admin
from .models import Post, comment

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_on', 'updated_on', 'status')

# Register the Post model with the PostAdmin
admin.site.register(Post, PostAdmin)
admin.site.register(comment)