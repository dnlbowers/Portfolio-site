from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Project


# Register your models here.
@admin.register(Project)
class ProjectAdmin(SummernoteModelAdmin):
    """
    Allows admin to edit project via admin panel
    """
    list_display = ('title', 'status', 'hosted_url', 'completion_date', 'project_type')
    list_filter = ('status', 'project_type')
    search_fields = ('title', 'description', 'status', 'project_type')
    summernote_fields = ('description',)
    actions = ['make_public', 'hide_project', 'make_coming_soon']
    prepopulated_fields = {'slug': ('title',)}

    ordering = ('completion_date',)

    def make_public(self, request, queryset):
        """
        Makes selected projects public
        """
        queryset.update(status=1)
    
    def hide_project(self, request, queryset):
        """
        Makes selected projects hidden
        """
        queryset.update(status=0)

    def make_coming_soon(self, request, queryset):
        """
        Makes selected projects coming soon
        """
        queryset.update(status=2)
    