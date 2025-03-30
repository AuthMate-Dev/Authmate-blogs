from django.contrib import admin
from blogs.models import Post, BlogComment , Author

admin.site.register((BlogComment,Author))
@admin.register(Post)


class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('blog/js/tinyInject.js',)