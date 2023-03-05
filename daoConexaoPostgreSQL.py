import psycopg2


class Conexao:

    def __init__(self):
        self.conn = None

    def conectar(self):
        try:
            self.conn = psycopg2.connect(database="previsaotempo",
                                         host="127.0.0.1",
                                         user="postgres",
                                         password="bck187787",
                                         port="5432")

        except Exception as err:
            print(str(err))
            conn = None

    def inserir(self, sql, valores, modelgenerico):
       try:
           if self.conn != None:
               cursor = self.conn.cursor()
               cursor.execute(sql, valores)
               modelgenerico.id = cursor.fetchone()[0]
               return True
       except Exception as err:
           print(str(err))
           return False
       return True

    def consultar(self, sql):
        rs=None
        try:
            if self.conn != None:
                cursor = self.conn.cursor()
                cursor.execute(sql)
                rs = cursor
        except Exception as err:
            print(str(err))
            return None
        return rs

    def proxima_pk(self, tabela, chave):
        sql='select max('+chave+') from '+tabela
        rs = self.consultar(sql)
        pk = rs.first()
        return pk+1

    def fechar(self):
      self.conn.close()

    def comitar(self):
      self.conn.commit()

    def rollback(self):
      self.conn.rollback()
