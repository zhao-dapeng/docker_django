from django.db import models


# Create your models here.
class School(models.Model):
    id = models.AutoField(primary_key=True)
    school_name = models.CharField(max_length=255, blank=False, null=False)

    class Meta:
        db_table = 'school'

