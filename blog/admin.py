from django.contrib import admin

from blog.models import Post


class Post_views(admin.ModelAdmin):
    list_display = ['author','title','text','created_date','published_date']


admin.site.register([Post])
