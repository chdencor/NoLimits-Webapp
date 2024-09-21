import psycopg2
from psycopg2 import sql
from psycopg2.extras import RealDictCursor

class SupabaseDAO:
    def __init__(self, db_url):
        self.db_url = db_url
        self.conn = None

    def connect(self):
        """Establecer conexión a la base de datos."""
        try:
            self.conn = psycopg2.connect(self.db_url)
            print("Conexión establecida con éxito")
        except psycopg2.OperationalError as e:
            print(f"Error al conectarse a la base de datos: {e}")
            self.conn = None

    def ensureConnection(self):
        """Asegurar que la conexión esté activa antes de realizar una operación."""
        if self.conn is None or self.conn.closed:
            print("Conexión no disponible, intentando reconectar...")
            self.connect()

    def closeConnection(self):
        """Cerrar la conexión a la base de datos."""
        try:
            if self.conn:
                self.conn.close()
                print("Conexión cerrada con éxito")
        except psycopg2.Error as e:
            print(f"Error al cerrar la conexión: {e}")

    def fetchAll(self, table_name):
        """Obtener todas las filas de una tabla específica."""
        self.ensureConnection()
        try:
            with self.conn.cursor() as cur:
                query = sql.SQL("SELECT * FROM {}").format(sql.Identifier(table_name))
                cur.execute(query)
                return cur.fetchall()
        except psycopg2.Error as e:
            print(f"Error al obtener datos de la tabla {table_name}: {e}")
            self.conn.rollback()  # Revertir la transacción fallida
            return None

    def fetchOne(self, table_name, id_value):
        """Obtener una fila de una tabla específica por ID."""
        self.ensureConnection()
        try:
            with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
                query = sql.SQL("SELECT * FROM {} WHERE id = %s").format(sql.Identifier(table_name))
                cur.execute(query, (id_value,))
                return cur.fetchone()  # Ahora devuelve un dict
        except psycopg2.Error as e:
            print(f"Error al obtener la fila de la tabla {table_name} con ID {id_value}: {e}")
            self.conn.rollback()
            return None

    def cleanNumeric(self, value):
        """Retornar None si el valor está vacío o no es un número válido."""
        try:
            return float(value) if value else None
        except (ValueError, TypeError):
            return None

    def create(self, table_name, columns, values):
        """Insertar un nuevo registro en una tabla específica."""
        self.ensureConnection()
        try:
            with self.conn.cursor() as cur:
                query = sql.SQL("INSERT INTO {} ({}) VALUES ({}) RETURNING id").format(
                    sql.Identifier(table_name),
                    sql.SQL(', ').join(map(sql.Identifier, columns)),
                    sql.SQL(', ').join(sql.Placeholder() * len(values))
                )
                cur.execute(query, values)
                self.conn.commit()  # Confirmar la transacción
                return cur.fetchone()[0]  # Devuelve el ID del nuevo registro
        except psycopg2.Error as e:
            print(f"Error al insertar datos en la tabla {table_name}: {e}")
            self.conn.rollback()  # Revertir la transacción fallida
            return None

    def createCripto(self, table_name, columns, values):
        """Insertar una nueva criptomoneda si no existe."""
        self.ensureConnection()
        try:
            # Verificar si la criptomoneda ya existe por símbolo
            symbol = values[columns.index('symbol')]
            if self.checkSymbolExists(table_name, symbol):
                # Si ya existe, simplemente no hacemos nada
                return None
    
            # Si no existe, insertar la nueva criptomoneda
            return self.create(table_name, columns, values)
        except psycopg2.Error as e:
            print(f"Error al insertar datos en la tabla {table_name}: {e}")
            return None

    def checkSymbolExists(self, table_name, symbol):
        """Verificar si el símbolo ya existe en la tabla."""
        self.ensureConnection()
        try:
            with self.conn.cursor() as cur:
                query = sql.SQL("SELECT * FROM {} WHERE symbol = %s").format(sql.Identifier(table_name))
                cur.execute(query, (symbol,))
                return cur.fetchone() is not None
        except psycopg2.Error as e:
            print(f"Error al verificar el símbolo en la tabla {table_name}: {e}")
            return False

    def createRegistro(self, values):
        """Insertar un nuevo registro en la tabla registros."""
        self.ensureConnection()
        try:
            # Limpiar y validar los valores
            cleaned_values = [self.cleanNumeric(v) for v in values]
    
            # Asegúrate de que todos los valores requeridos estén presentes
            if None in cleaned_values:
                print("Error: uno o más valores no son válidos.")
                return None
    
            return self.create('registros', ['price_usd', 'percent_change_24h', 
                                              'percent_change_1h', 'percent_change_7d',
                                              'price_btc', 'market_cap_usd', 
                                              'volume24', 'volume24a', 
                                              'csupply', 'tsupply', 'msupply'],
                                cleaned_values)
        except psycopg2.Error as e:
            print(f"Error al insertar datos en la tabla registros: {e}")
            return None

    def update(self, table_name, columns, values, id_value):
        """Actualizar un registro en una tabla específica."""
        self.ensureConnection()
        try:
            with self.conn.cursor() as cur:
                set_clause = sql.SQL(', ').join(
                    sql.SQL("{} = %s").format(sql.Identifier(col)) for col in columns
                )
                query = sql.SQL("UPDATE {} SET {} WHERE id = %s").format(
                    sql.Identifier(table_name),
                    set_clause
                )
                cur.execute(query, values + (id_value,))
                self.conn.commit()  # Confirmar la transacción
        except psycopg2.Error as e:
            print(f"Error al actualizar la tabla {table_name} con ID {id_value}: {e}")
            self.conn.rollback()  # Revertir la transacción fallida

    def delete(self, table_name, id_value):
        """Eliminar un registro de una tabla específica."""
        self.ensureConnection()
        try:
            with self.conn.cursor() as cur:
                query = sql.SQL("DELETE FROM {} WHERE id = %s").format(sql.Identifier(table_name))
                cur.execute(query, (id_value,))
                self.conn.commit()  # Confirmar la transacción
        except psycopg2.Error as e:
            print(f"Error al eliminar el registro de la tabla {table_name} con ID {id_value}: {e}")
            self.conn.rollback()  # Revertir la transacción fallida
