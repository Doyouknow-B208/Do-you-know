from django.db import models

class Nation(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    language = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    twitter_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nation'

class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category'
        
class Dykclub(models.Model):
    id = models.BigAutoField(primary_key=True)
    img_url = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    category = models.ForeignKey(Category, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dykclub'

class DykclubTwitter(models.Model):
    id = models.BigAutoField(primary_key=True)
    content = models.CharField(max_length=2000, blank=True, null=True)
    dykclub = models.ForeignKey(Dykclub, models.DO_NOTHING, blank=True, null=True, related_name="twitter")

    class Meta:
        managed = False
        db_table = 'dykclub_twitter'



class News(models.Model):
    id = models.BigAutoField(primary_key=True)
    link = models.CharField(max_length=2000, blank=True, null=True)
    image = models.CharField(max_length=2000, blank=True, null=True)
    title = models.CharField(max_length=2000, blank=True, null=True)
    keyword = models.CharField(max_length=255, blank=True, null=True)
    nation=  models.ForeignKey(Nation, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news'