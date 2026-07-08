from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str = "postgresql+asyncpg://root:root@db:5432/db"

    quarantine_window_days: int = 14
    quarantine_min_flaky_events: int = 5  # N
    quarantine_min_branches: int = 3      # M
    quarantine_clean_observe_streak: int = 5  # K
    quarantine_max_auto_activate: int = 8  # <-- порог N из вашего требования
    quarantine_alert_chat_id: str      # куда слать алерт

    bot_token: str  # token для VK Teams Bot API
    api_key: str | None = None  # если хотите X-API-Key
    host_base_url: str
    api_host_base_url: str
    gitlab_url: str = 'https://gitlab.corp.mail.ru'

settings = Settings()
