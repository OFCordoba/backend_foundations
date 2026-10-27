from src.config import settings

def run() -> None:
    print(f"Iniciando servicio en entorno: {settings.app_env}")
    print(f"Puerto configurado: {settings.app_port}")
    print(f"Conexión a base de datos: {settings.db_url}")

if __name__ == "__main__":
    run()