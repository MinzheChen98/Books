import pymysql

class DbClient:
    
    def __init__(self):
        print('Connecting database...')
        self.db = pymysql.connect(host='172.104.122.77',
                                  user='ece656',
                                  password='Ece656!@#',
                                  charset='utf8')
        print('Connected!')
        self.cursor = self.db.cursor()
        self.cursor.execute("use books;")
        
        
    def select(self, query: str):
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        return data
        
    def insert(self, table: str, fields: str, values: str) -> None:
        query = "INSERT INTO {}({}) VALUES ({});".format(table, fields, values)
        self.cursor.execute(query)
        self.db.commit()
        print('created')
        
    def update(self, table: str, query: str, fields: str, values: str) -> None:
        query = "UPDATE {} set {} = {} where {};".format(table, fields, values, query)
        self.cursor.execute(query)
        self.db.commit()
        print('updated')
