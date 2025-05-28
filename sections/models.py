from django.db import models
from django.utils.translation import gettext_lazy as gtl


class Section(models.Model):
  title = models.CharField(max_length=160, verbose_name=gtl("Title"))
  description = models.TextField(verbose_name=gtl("Description"), blank=True, null=True)

  def __str__(self):
    return self.title
  
  class Meta:
    verbose_name = gtl("Section")
    verbose_name_plural = gtl("Sections")
    ordering = ["id"]


class Content(models.Model):
  section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name=gtl("Section"))
  title = models.CharField(max_length=160, verbose_name=gtl("Title"))
  content = models.TextField(verbose_name=gtl("Content"))

  def __str__(self):
    return self.title
  
  class Meta:
    verbose_name = gtl("Content")
    verbose_name_plural = gtl("Contents")
    ordering = ["id"]