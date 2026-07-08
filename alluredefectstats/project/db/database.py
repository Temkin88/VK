from playhouse.apsw_ext import APSWDatabase


db = APSWDatabase(
    "./data.db",
    pragmas={
        "journal_mode": "wal",
        "cache_size": -1024 * 64,
        "synchronous": True,
    },
)
