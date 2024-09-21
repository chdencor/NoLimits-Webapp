# models/__init__.py

from models.supabaseDAO import SupabaseDAO
from config import Config

# Crear una instancia del DAO
dao_instance = SupabaseDAO(Config.SUPABASE_DB_URL)

def initialize():
    """Función para inicializar el DAO."""
    dao_instance.connect()

# Llama a initialize() al cargar el módulo
initialize()
