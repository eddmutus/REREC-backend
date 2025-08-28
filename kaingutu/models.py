from django.contrib.gis.db import models

# Create your models here.
class Customers(models.Model):
    fid = models.AutoField(primary_key=True)
    geom = models.MultiPointField(blank=True, null=True)
    no = models.IntegerField(blank=True, null=True)
    eastings = models.FloatField(blank=True, null=True)
    northings = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    customer_s_name = models.CharField(db_column='customer_s name', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    id = models.IntegerField(blank=True, null=True)
    phone_number = models.IntegerField(db_column='phone number', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    parcel_number = models.IntegerField(db_column='parcel number', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    power_rate_supply = models.CharField(db_column='power rate supply', blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'customers'
        verbose_name_plural = 'Customers'

class ExistingHtLine(models.Model):
    fid = models.AutoField(primary_key=True)
    geom = models.MultiLineStringField(dim=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'existing_ht_line'
        verbose_name_plural = 'Customers'

class HtLineConstructed(models.Model):
    fid = models.AutoField(primary_key=True)
    geom = models.MultiLineStringField(dim=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ht_line_constructed'
        verbose_name_plural = 'Customers'

class HtPoles(models.Model):
    fid = models.AutoField(primary_key=True)
    geom = models.MultiPointField(blank=True, null=True)
    no = models.IntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    latitude_1 = models.FloatField(blank=True, null=True)
    eastings = models.FloatField(blank=True, null=True)
    northings = models.FloatField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    type = models.CharField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    fitting = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ht_poles'
        verbose_name_plural = 'HTPoles'


class LvPoles(models.Model):
    fid = models.AutoField(primary_key=True)
    geom = models.MultiPointField(blank=True, null=True)
    no = models.IntegerField(blank=True, null=True)
    latitudes = models.FloatField(blank=True, null=True)
    longitudes = models.FloatField(blank=True, null=True)
    eastings = models.FloatField(blank=True, null=True)
    northings = models.FloatField(blank=True, null=True)
    name_string_field = models.CharField(db_column='name(string)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    type_string_field = models.CharField(db_column='type(string)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    height_m_field = models.IntegerField(db_column='height(m)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'lv_poles'
        verbose_name_plural = 'LVPoles'


class Parcels(models.Model):
    fid = models.AutoField(primary_key=True)
    geom = models.MultiPolygonField(dim=3, blank=True, null=True)
    id = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parcels'
        verbose_name_plural = 'Customers'


class SinglePhase(models.Model):
    fid = models.AutoField(primary_key=True)
    geom = models.MultiLineStringField(dim=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'single_phase'
        verbose_name_plural = 'Customers'
