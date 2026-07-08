from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

# пример: DATABASE_URL="postgresql+asyncpg://user:pass@host:5432/db"
def make_engine(database_url: str):
    return create_async_engine(database_url, pool_pre_ping=True)

def make_session_factory(engine):
    return async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
