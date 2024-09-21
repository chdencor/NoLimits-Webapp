import psycopg2
from psycopg2 import sql

class SupabaseDAO:
    def __init__(self, db_url):
        self.db_url = db_url
        self.conn = None

    def connect(self):
        """Establecer conexión a la base de datos."""
        self.conn = psycopg2.connect(self.db_url)

    def close(self):
        """Cerrar la conexión a la base de datos."""
        if self.conn:
            self.conn.close()

    def fetchAll(self, table_name):
        """Obtener todas las filas de una tabla específica."""
        with self.conn.cursor() as cur:
            query = sql.SQL("SELECT * FROM {}").format(sql.Identifier(table_name))
            cur.execute(query)
            return cur.fetchall()

    def fetchOne(self, table_name, id_value):
        """Obtener una fila de una tabla específica por ID."""
        with self.conn.cursor() as cur:
            query = sql.SQL("SELECT * FROM {} WHERE id = %s").format(sql.Identifier(table_name))
            cur.execute(query, (id_value,))
            return cur.fetchone()

    def create(self, table_name, columns, values):
        """Insertar un nuevo registro en una tabla específica."""
        with self.conn.cursor() as cur:
            query = sql.SQL("INSERT INTO {} ({}) VALUES ({}) RETURNING id").format(
                sql.Identifier(table_name),
                sql.SQL(', ').join(map(sql.Identifier, columns)),
                sql.SQL(', ').join(sql.Placeholder() * len(values))
            )
            cur.execute(query, values)
            self.conn.commit()
            return cur.fetchone()[0]  # Devuelve el ID del nuevo registro

    def update(self, table_name, columns, values, id_value):
        """Actualizar un registro en una tabla específica."""
        with self.conn.cursor() as cur:
            set_clause = sql.SQL(', ').join(
                sql.SQL("{} = %s").format(sql.Identifier(col)) for col in columns
            )
            query = sql.SQL("UPDATE {} SET {} WHERE id = %s").format(
                sql.Identifier(table_name),
                set_clause
            )
            cur.execute(query, values + (id_value,))
            self.conn.commit()

    def delete(self, table_name, id_value):
        """Eliminar un registro de una tabla específica."""
        with self.conn.cursor() as cur:
            query = sql.SQL("DELETE FROM {} WHERE id = %s").format(sql.Identifier(table_name))
            cur.execute(query, (id_value,))
            self.conn.commit()

