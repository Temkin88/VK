from peewee import SqliteDatabase, Model, \
    TextField, \
    ForeignKeyField, \
    BooleanField


class BaseModel(Model):

    class Meta:

        database = SqliteDatabase('data.db')


class Chat(BaseModel):

    chat_id = TextField(unique=True)
    is_group = BooleanField()
    title = TextField()
    invite_link = TextField(null=True)
    join_moderation = BooleanField()
    public = BooleanField()


Chat.create_table()


class User(BaseModel):

    first_name = TextField()
    last_name = TextField()
    # about = TextField()
    uin = TextField()
    is_admin = BooleanField(default=False)
    chat = ForeignKeyField(Chat, lazy_load=False, backref='user')


User.create_table()


class UserPhoto(BaseModel):

    user = ForeignKeyField(User, lazy_load=False, backref='user_photo')
    url = TextField()

    class Meta:

        db_table = 'user_photo'


UserPhoto.create_table()


class CustomGroup(BaseModel):

    name = TextField()
    chat = ForeignKeyField(Chat, lazy_load=False, backref='custom_group')

    class Meta:

        db_table = 'custom_group'


CustomGroup.create_table()


class CustomGroupMember(BaseModel):

    custom_group = ForeignKeyField(CustomGroup, backref='custom_group_member')
    user = ForeignKeyField(User, lazy_load=False, backref='custom_group_member')

    class Meta:

        db_table = 'custom_group_member'


CustomGroupMember.create_table()
