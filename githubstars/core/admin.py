from django.contrib import admin

from githubstars.core.models import Tag
from githubstars.core.models import Repository


@admin.register(Repository)
class RepositoryAdmin(admin.ModelAdmin):

    list_display = ['user', 'name', 'url_github', '_tags', 'created_at']
    search_fields = ['user']
    list_filter = ['user']

    def url_github(self, obj):
        return '<a href="{0}" target="_blank">{0}</a>'.format(obj.url)

    url_github.allow_tags = True
    url_github.short_description = 'URL Github'

    def _tags(self, obj):
        return obj.get_tags()


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):

    list_display = ['name', 'created_at']
