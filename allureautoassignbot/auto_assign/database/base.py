import peewee as pw


db = pw.SqliteDatabase(
    "./base.db",
    pragmas={
        "journal_mode": "wal",
        "cache_size": -1024 * 64,
    },
)


class BaseModel(pw.Model):
    class Meta:
        database = db
