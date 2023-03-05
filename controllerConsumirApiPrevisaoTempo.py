from serviceConsumirApiPrevisaoTempo import ServiceConsumirApiPrevisaoTempo
from modelPrevisaoTempoPesquisaResultado import ModelPrevisaoTempoPesquisaResultado
from controllerPrevisaoPesquisa import ControllerPrevisaoPesquisa
from modelPrevisaoTempoPesquisa import ModelPrevisaoTempoPesquisa
import json


class ControllerConsumirApiPrevisaoTempo:

    def __init__(self):
        self = self
        last_idpesquisa = -1

    # rotina que busca a previsão do tempo dos ultimos 5 dias em 3 em 3 horas de uma determidade cidade e pais;
    def consultar_previsaotempo(self, cidade, pais):
        serviceApi = ServiceConsumirApiPrevisaoTempo()
        jsonretorno = serviceApi.consultar_previsaotempo(cidade, pais)

        if jsonretorno["cod"] != "404":
            # se deu tudo certo, vamos gravar o histórico de pesquisa
            # ao gravar historico de pesquisa, vamos retornar o id, e repassar pra chave estrangeira
            self.gravar_historico_pesquisa(cidade, pais)

            # Após gravar o histórico de pesquisa, vamos pegar o json de consulta e manipular os dados
            list_resultado = self.obter_info_json(jsonretorno, cidade, pais, self.last_idpesquisa)

            # Após obter todos os resultados, vamos gravar no banco as informações do tempo consultada
            self.gravar_resultado_pesquisa(list_resultado)

            # montar json de devolução
            modelPesjson = ModelPrevisaoTempoPesquisa()
            modelPesjson.id = self.last_idpesquisa
            modelPesjson.cidade = cidade
            modelPesjson.pais = pais
            modelPesjson.longitude = 0
            modelPesjson.latitude = 0

            self.montar_json_retorno_sucesso(modelPesjson, list_resultado)



    def obter_info_json(self, json_consulta, cidade, pais, id_pesquisa):
        list_resultados = []
        for list_dateshours in json_consulta["list"]:
            model_result = ModelPrevisaoTempoPesquisaResultado() #shift f6 , snake case

            # informacos do nodo principal
            model_result.data_horaprevisao = list_dateshours["dt_txt"]

            # informacoes do nodo mais segundo nivel
            main = list_dateshours["main"]

            model_result.temp = main["temp"]
            model_result.feel_like = main["feels_like"]
            model_result.temp_min = main["temp_min"]
            model_result.temp_max = main["temp_max"]
            model_result.pressure = main["pressure"]
            model_result.sea_level = main["sea_level"]
            model_result.grnd_level = main["grnd_level"]
            model_result.humidity = main["humidity"]
            model_result.temp_kf = main["temp_kf"]

            # informacoes weather segundo nivel
            weather = list_dateshours["weather"]
            model_result.weather_desc = weather[0]["description"]

            # informacoes de clouds all
            clouds = list_dateshours["clouds"]
            model_result.clouds_all = clouds["all"]

            # informacoes de wind
            wind = list_dateshours["wind"]
            model_result.wind_speed = wind["speed"]
            model_result.wind_deg = wind["deg"]
            model_result.wind_gust = wind["gust"]

            # informacoes de rain
            if list_dateshours.get("rain"):
                rain = list_dateshours["rain"]
                model_result.rain_3h = rain["3h"]
            else:
                model_result.rain_3h = 0

            # informacoes de sys
            sys = list_dateshours["sys"]
            model_result.sys_pod = sys["pod"]
            model_result.id_pesquisatempoprevisao = id_pesquisa
            list_resultados.append(model_result)

        return list_resultados

    def gravar_historico_pesquisa(self, cidade, pais):
        # gravando o historico de pesquisa no banco
        controllerPrevisa = ControllerPrevisaoPesquisa()
        controllerPrevisa.gravar_previsao_pesquisa(cidade, pais, 0, 0)

        self.last_idpesquisa = controllerPrevisa.gatLastId()

    def gravar_resultado_pesquisa(self, list_resultados):
        # gravando o historico do resultados da pesquisa no banco
        controllerResultado = ControllerPrevisaoPesquisa()
        for resultado in list_resultados:
            controllerResultado.gravar_previsao_resultado_model(resultado)

    def getLastId(self):
        return last_id

    def montar_json_retorno_sucesso(self, modelpesq, lista_resultado):
        dict_model_pes = modelpesq.__dict__

        # adicionar sucesso;
        dict_model_pes["success"] = True

        # adicionar novo nested no json
        dict_model_pes["resultados"] = [res.__dict__ for res in lista_resultado]

        #converter para json
        jsonfinal = json.dumps(dict_model_pes, indent=4)


        print(jsonfinal)
        #print(jsonLoad)
