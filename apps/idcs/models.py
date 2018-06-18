from django.db import models


# Create your models here.
class Idc(models.Model):
    name            = models.CharField("机房名称", max_length=32)
    address         = models.CharField("机房地址", max_length=256)
    phone           = models.CharField("联系人", max_length=11)
    email           = models.EmailField("邮件地址", max_length=32)
    letter          = models.CharField("IDC简称", max_length=5)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'resources_idc'
