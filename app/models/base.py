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


class Role(TimeStampMixin):
    user: fields.ManyToManyRelation['User'] = fields.ManyToManyField('base.User', related_name='role', on_delete=fields.CASCADE)
    role_name = fields.CharField(max_length=128, description='角色名称名称')
    access: fields.ManyToManyRelation['Access'] = fields.ManyToManyField('base.Access', related_name='role', on_delete=fields.CASCADE)
    role_status = fields.BooleanField(default=False, description='True:启用, False禁用')
    role_desc = fields.CharField(null=True, max_length=255, description='角色描述')

    class Meta:
        table_description = '角色表'
        table = 'role'


class Access(TimeStampMixin):
    role = fields.ManyToManyRelation[Role]
    access_name = fields.CharField(max_length=128, description='权限名称')
    parent_id = fields.IntField(default=0, description='父id')
    scopes = fields.CharField(unique=True, max_length=255, description='权限范围')
    access_desc = fields.CharField(null=True, max_length=255, description='权限描述')
    is_check = fields.BooleanField(default=False, description='是否验证权限 True 为验证')
    is_menu = fields.BooleanField(default=False, description='是否为菜单 True为菜单 False 不是菜单')

    class Meta:
        table_description = '权限表'
        table = 'access'
