import logging

from fastapi import FastAPI
from app.api.routes import runs, quarantine, quarantine_admin, tickets, admin


logging.basicConfig(level=logging.INFO)

PREFIX = "/playwright"
app = FastAPI(
    title="Playwright Quarantine Service",
    openapi_url=f"{PREFIX}/openapi.json",
    docs_url=f"{PREFIX}/docs",
    redoc_url=f"{PREFIX}/redoc",
)

app.include_router(runs.router, prefix=PREFIX)
app.include_router(quarantine.router, prefix=PREFIX)
app.include_router(quarantine_admin.router, prefix=PREFIX)
app.include_router(tickets.router, prefix=PREFIX)

admin.router.mount_to(app=app)
