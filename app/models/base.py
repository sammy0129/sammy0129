from tortoise import fields
from tortoise.models import Model


class TimeStampMixin(Model):
    create_at = fields.DatetimeField(auto_now_add=True, description='创建时间')
    update_at = fields.DatetimeField(auto_now=True, description='更新时间')

    class Meta:
        abstract = True


class User(TimeStampMixin):
    username = fields.CharField(null=True, max_length=64, description='用户名')
    user_type = fields.BooleanField(null=True, default=False, description='用户类型, True超管, False普通管理员')
    password = fields.CharField(null=True, max_length=255)
    nickname = fields.CharField(default='testcase', max_length=255, description='昵称')
    avatar = fields.CharField(null=True, max_length=255, default='/avatar_placeholder.png', description='头像')

    class Meta:
        table_description = '用户表'
        table = 'user'


