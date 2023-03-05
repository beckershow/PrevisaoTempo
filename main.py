from daoConexaoPostgreSQL import Conexao
from controllerPrevisaoPesquisa import ControllerPrevisaoPesquisa
from serviceConsumirApiPrevisaoTempo import ServiceConsumirApiPrevisaoTempo
from controllerConsumirApiPrevisaoTempo import ControllerConsumirApiPrevisaoTempo

if __name__ == '__main__':
    #con = Conexao()
    # con.conectar()
    # rs = con.consultar("select * from public.previsaotempopesquisa")
    # print(rs.fetchall())
    # for row in rs.fetchall():

    #controllerPes = ControllerPrevisaoPesquisa()
    #controllerPes.gravar_previsao_pesquisa('balneario camboriu', 'brasil', 0, 1)
    #controllerPes.gravar_previsao_resultado();

    #serviceApi = ServiceConsumirApiPrevisaoTempo()
    #serviceApi.consultar_previsaotempo('blumenau', 'br')

    controlerApi = ControllerConsumirApiPrevisaoTempo()
    controlerApi.consultar_previsaotempo('blumenau', 'br')
   # controlerApi.consultar_historico_pesquisa()

