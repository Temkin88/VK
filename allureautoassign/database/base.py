import peewee as pw


db = pw.SqliteDatabase(
    ":memory:",
    pragmas={
        "journal_mode": "wal",
        "cache_size": -1024 * 64,
    },
)


class BaseModel(pw.Model):
    class Meta:
        database = db
