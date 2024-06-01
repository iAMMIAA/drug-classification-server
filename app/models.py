from django.db import models

def nameFile(instance, filename):
    return '/'.join(['images', str(instance.namedrug), filename])

class Informationdrug(models.Model):
    namedrug = models.CharField(db_column='nameDrug', primary_key=True, max_length=255)  # Field name made lowercase.
    cites = models.CharField(max_length=255, blank=True)
    detail = models.TextField(blank=True)
    tagDrug = models.CharField(db_column='tagDrug', max_length=255, blank=True)  # Field name made lowercase.
    imgdrug = models.CharField(db_column='imgDrug', max_length=255, blank=True)  # Field name made lowercase.
    colordrug = models.CharField(db_column='colorDrug', max_length=255, blank=True)  # Field name made lowercase.
    shapedrug = models.CharField(db_column='shapeDrug', max_length=255, blank=True)  # Field name made lowercase.
    imprintdrug = models.CharField(db_column='imprintDrug', max_length=255, blank=True)  # Field name made lowercase.
    describedrug = models.TextField(db_column='describeDrug', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'informationdrug'


class UrlImgUser(models.Model):
    id = models.AutoField(primary_key=True)
    imgUser = models.TextField(null=True)

    class Meta:
        db_table = 'urlImgUser'