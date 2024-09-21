# models/__init__.py

from app.models.supabaseDAO import SupabaseDAO
from app.config import Config

# Crear una instancia del DAO
dao_instance = SupabaseDAO(Config.DATABASE_URL)

def initialize():
    """Función para inicializar el DAO."""
    dao_instance.connect()

# Llama a initialize() al cargar el módulo
initialize()
