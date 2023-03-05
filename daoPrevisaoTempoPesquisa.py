from daoConexaoPostgreSQL import Conexao
from modelPrevisaoTempoPesquisa import ModelPrevisaoTempoPesquisa
import datetime

class DaoPrevisaoTempoPesquisa:


    def __init__(self):
        self=self

    def InserirPesquisa(self, modelprevisao):
        conn = Conexao()
        conn.conectar()
        if conn != None:
            try:
                postgres_insert_query = """ INSERT INTO previsaotempopesquisa
                                            (CIDADE, PAIS, LONGITUDE, LATITUDADE, DATA_HORAPESQUISA)                 
                                            VALUES (%s,%s,%s,%s, %s) RETURNING id"""
                record_to_insert = (modelprevisao.cidade,
                                    modelprevisao.pais,
                                    modelprevisao.longitude,
                                    modelprevisao.latitude,
                                    modelprevisao.data_horapesquisa)

                inseriu = conn.inserir(postgres_insert_query, record_to_insert, modelprevisao)

                if (inseriu):
                    conn.comitar()
                else:
                    conn.rollback()
            finally:
                conn.fechar()