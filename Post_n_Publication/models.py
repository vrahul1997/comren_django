from django.db import models
from shortuuidfield import ShortUUIDField

# Create your models here.
class Publication(models.Model):
    """Publications Db collections"""

    uid = ShortUUIDField(
        unique=True, max_length=22, help_text="Publication UUID", db_index=True
    )
    publication_short = models.CharField(max_length=100, unique=True)
    publication = models.TextField(max_length=300)

    class Meta:
        db_table = "comren_publications"
        verbose_name = "publication_short"
        verbose_name_plural = "publication_shorts"


class Project(models.Model):
    """Projects Db collection"""

    uid = ShortUUIDField(
        unique=True, max_length=22, help_text="Publication UUID", db_index=True
    )
    project_name = models.TextField(max_length=200)
    project_url = models.TextField(max_length=400)

    class Meta:
        db_table = "comren_projects"
        verbose_name = "comren_project"
        verbose_name_plural = "comren_projects"
