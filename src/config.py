import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    def __init__(self) -> None:
        self.app_env: str = os.getenv("APP_ENV", "development")
        port_raw: str | None = os.getenv("APP_PORT")
        if not port_raw:
            raise ValueError("La variable de entorno APP_PORT no está definida.")
        self.app_port: int = int(port_raw)
        self.db_url: str = os.getenv("DATABASE_URL", "sqlite:///./default.db")

settings = Settings()