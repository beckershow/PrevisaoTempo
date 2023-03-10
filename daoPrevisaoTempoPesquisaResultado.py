import json

from daoConexaoPostgreSQL import Conexao
from modelPrevisaoTempoPesquisaResultado import ModelPrevisaoTempoPesquisaResultado
import functools
import logging
class DaoPrevisaoTempoResultado:


    def __init__(self):
        self=self

    def retornar_consulta_pesquisa(self):
        conn = Conexao()
        conn.conectar()
        if conn != None:
            #prs.data_horaprevisao,
            sql = """select 
                	   to_char(p.data_horapesquisa, 'dd/mm/yyyy HH:MM:SS') data_horapesquisa,   
                	   p.cidade, p.pais, to_char(prs.data_horaprevisao, 'dd/mm/yyyy HH:MM:SS') data_horaprevisao,  
                	   prs.temp, prs.weather_desc
                	  from previsaotempopesquisa p
                	  inner join previsaotempopesquisaresultado prs ON prs.id_pesquisatempoprevisao = p.id
                	  order by data_horapesquisa desc
                	  limit 50 """
            try:
                cursor = conn.consultar(sql)

                items = [dict(zip([key[0] for key in cursor.description], row)) for row in cursor]

                # adicionar novo nested no json
                json_resultstr = json.dumps({'items': items})
                return json.loads(json_resultstr)


            finally:
                conn.fechar()


    def InserirConsulta(self, modelprevconsulta):
        conn = Conexao()
        conn.conectar()
        if conn != None:
            try:
                postgres_insert_query =""" INSERT INTO previsaotempopesquisaresultado
                                           (
                                             temp, feels_like, temp_min, temp_max, pressure, sea_level, grn_level,
                                             humidity, temp_kf, weather_desc, clouds_all, wind_speed, wind_deg, 
                                             wind_gust, rain_3h, sys_pod, id_pesquisatempoprevisao, data_horaprevisao                                                                                            
                                           ) 
                                           VALUES 
                                          (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s, %s) RETURNING id"""
                record_to_insert = (modelprevconsulta.temp,
                                    modelprevconsulta.feel_like,
                                    modelprevconsulta.temp_min,
                                    modelprevconsulta.temp_max,
                                    modelprevconsulta.pressure,
                                    modelprevconsulta.sea_level,
                                    modelprevconsulta.grnd_level,
                                    modelprevconsulta.humidity,
                                    modelprevconsulta.temp_kf,
                                    modelprevconsulta.weather_desc,
                                    modelprevconsulta.clouds_all,
                                    modelprevconsulta.wind_speed,
                                    modelprevconsulta.wind_deg,
                                    modelprevconsulta.wind_gust,
                                    modelprevconsulta.rain_3h,
                                    modelprevconsulta.sys_pod,
                                    modelprevconsulta.id_pesquisatempoprevisao,
                                    modelprevconsulta.data_horaprevisao)

                inseriu = conn.inserir(postgres_insert_query, record_to_insert, modelprevconsulta)
                if (inseriu):
                    conn.comitar()
                else:
                    conn.rollback()
            finally:
                conn.fechar()