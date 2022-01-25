from django.contrib import admin

# Register your models here.

from Post_n_Publication.models import Publication, Project


class alterAdminPublication(admin.ModelAdmin):
    list_display = ("publication_short",)
    list_display_links = ("publication_short",)
    search_fields = ("publication_short",)
    ordering = ["pk"]

    def has_add_permission(self, request):
        return True


class alterAdminProject(admin.ModelAdmin):
    list_display = ("project_name",)
    list_display_links = ("project_name",)
    search_fields = ("project_name",)
    ordering = ["pk"]

    def has_add_permission(self, request) -> bool:
        return True


admin.site.register(Publication, alterAdminPublication)
admin.site.register(Project, alterAdminProject)
