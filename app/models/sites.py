from .base import TimeStampMixin
from tortoise import fields
from tortoise.models import Model

class Site(TimeStampMixin):
    country = fields.CharField(null=False, max_length=64, description='国家')
    domain = fields.CharField(null=False, max_length=128, description='域名')
    currency = fields.CharField(null=False, max_length=32, description='货币')
    category = fields.CharField(null=False, max_length=32, description='类别')
    ecomdept = fields.CharField(null=False, max_length=32, description='电商类型')

