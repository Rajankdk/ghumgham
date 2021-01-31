from django.db import models

# Create your models here.
class Destination(models.Model): #model ko M capital
    name=models.CharField(max_length=20)
    img=models.ImageField(upload_to='pic_name')
    desc=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)

class DjangoBitmap(models.Model):
    fieldname = models.TextField(db_column='FieldName', blank=True, null=True)  # Field name made lowercase.
    datatypes = models.CharField(db_column='DataTypes', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Django_Bitmap'

class Pdxdataformats(models.Model):
    fieldnum = models.SmallIntegerField(db_column='FieldNum', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    format = models.CharField(db_column='Format', max_length=12, blank=True, null=True)  # Field name made lowercase.
    datatype = models.CharField(db_column='DataType', max_length=1, blank=True, null=True)  # Field name made lowercase.
    datalen = models.SmallIntegerField(db_column='DataLen', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'PDXDataFormats'





