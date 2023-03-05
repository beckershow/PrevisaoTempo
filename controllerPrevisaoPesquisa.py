from modelPrevisaoTempoPesquisa import ModelPrevisaoTempoPesquisa
from modelPrevisaoTempoPesquisaResultado import ModelPrevisaoTempoPesquisaResultado
from daoPrevisaoTempoPesquisa import DaoPrevisaoTempoPesquisa
from daoPrevisaoTempoPesquisaResultado import DaoPrevisaoTempoResultado
from datetime import datetime

class ControllerPrevisaoPesquisa:

    def __init__(self):
        self = self
        self.last_id = -1

    def gravar_previsao_pesquisa(self, cidade, pais, longitude, latitude):
        modelPrev = ModelPrevisaoTempoPesquisa()
        modelPrev.cidade = cidade
        modelPrev.pais = pais
        modelPrev.logintudade = longitude
        modelPrev.latitude = latitude
        modelPrev.data_horapesquisa = datetime.now()

        daoPreviPesq = DaoPrevisaoTempoPesquisa();
        daoPreviPesq.InserirPesquisa(modelPrev)

        self.last_id = modelPrev.id;

    def gravar_previsao_resultado(self, temp, feel_like, temp_min, temp_max,
                                  pressure, sea_level, grnd_level, humidity,
                                  temp_kf, weather_desc, clouds_all, wind_speed,
                                  wind_deg, wind_gust, rain_3h, sys_pod, id_pesquisatempoprevisao,
                                  ):
        modelResult = ModelPrevisaoTempoPesquisaResultado()
        modelResult.temp = temp
        modelResult.feel_like = feel_like
        modelResult.temp_min = temp_min
        modelResult.temp_max = temp_max
        modelResult.pressure = pressure
        modelResult.sea_level = sea_level
        modelResult.grnd_level = grnd_level
        modelResult.humidity = humidity
        modelResult.temp_kf = temp_kf
        modelResult.weather_desc = weather_desc
        modelResult.clouds_all = clouds_all
        modelResult.wind_speed = wind_speed
        modelResult.wind_deg = wind_deg
        modelResult.wind_gust = wind_gust
        modelResult.rain_3h = rain_3h
        modelResult.sys_pod = sys_pod
        modelResult.id_pesquisatempoprevisao = id_pesquisatempoprevisao
        modelResult.data_horaprevisao = datetime.datetime()

        daoPreviResult = DaoPrevisaoTempoResultado()
        daoPreviResult.InserirConsulta(modelResult)

    def gravar_previsao_resultado_model(self, modelResult):
        daoPreviResult = DaoPrevisaoTempoResultado()
        daoPreviResult.InserirConsulta(modelResult)

    def gatLastId(self):
        return self.last_id