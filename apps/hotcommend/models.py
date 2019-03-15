# @Time    : ${3/10/2019} ${TIME}
# @Author  : $Sutrue
# @Remark  :
from django.db import models

# Create your models here.

# class Commendation(models.Model):
#     assin = models.CharField(max_length=100, blank=False, null=False)
#     title = models.CharField(max_length=200, blank=True, null=True)
#     type = models.CharField(max_length=20, blank=True, null=True)
#
#     class Meta:
#         db_table = 'commendation'


class hot_list(models.Model):
    assin = models.CharField(max_length=200, blank=False, null=False)
    title = models.CharField(max_length=200, blank=True, null=True)
    categories = models.CharField(max_length=20, blank=True, null=True)
    sales_count = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'hot_list'

class transaction_record(models.Model):
    user_id = models.CharField(max_length=255, blank=False, null=False)
    item_id = models.CharField(max_length=255, blank=False, null=False)
    rating = models.CharField(max_length=100, blank=True, null=True)
    date = models.CharField(max_length=255, blank=False, null=False)

    class Meta:
        db_table = 'transaction_record'
