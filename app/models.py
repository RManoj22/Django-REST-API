from django.db import models

class Language(models.Model):
    lang = models.CharField(max_length=50)
    
    def __str__(self):
        return self.lang

class Info(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    lang = models.ForeignKey(Language,on_delete=models.PROTECT,default=None)

    class Meta:
        verbose_name_plural = "Info"

    def __str__(self):
        return self.name