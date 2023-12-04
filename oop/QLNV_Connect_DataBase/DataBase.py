import pyodbc

class DataBase:
    def __init__(self, **kwargs):
        self.driver = kwargs.get('driver')
        self.server = kwargs.get('server')
        self.database = kwargs.get('database')
        self.username = kwargs.get('username')
        self.password = kwargs.get('password')
        self.conn = None
        self.cursor = None

    def connect(self):
        connectionString = f'DRIVER={self.driver};SERVER={self.server};DATABASE={self.database};UID={self.username};PWD={self.password}'
        self.conn = pyodbc.connect(connectionString)
        self.cursor = self.conn.cursor()

    def execute_query(self, query):
        self.cursor.execute(query)

    def fetch_one(self):
        return self.cursor.fetchone()

    def fetch_all(self):
        return list(self.cursor)

