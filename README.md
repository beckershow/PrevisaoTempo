# PrevisaoTempo

#  Instalação do Banco de Dados;
1) baixar e instalar o  postgresql-9.6.24-1-windows-x64

2) configurações para rodar o banco:  Fixei hardcode, então favor respeitar.
     user="postgres"
     password="bck187787"
     port="5432"

3) Rodar o arquivo SqlCriacaoBanco.txt, encontrado no mesmo repositório para criar o banco de dados.
   Existem 2 tabelas: previsaotempopesquisaresultado e previsaotempopesquisa
   previsaotempopesquisa = tabela mestre que guarda os logs de consulta de uma determinada localidade e sua data.
   previsaotempopesquisaresultado = tabela 1xN da tabela pesquisa, que guardar os resutados dos ultimos 5 dias em 3 em 3 horas.
   As chaves são autoinc, e existe fk da tabela resultado oara presquivaopesquisa
   Arquivo da Entidade relacional = MER.jpg  

# Instalação do Python
1) Versão do Python: python-3.8.7-amd64.exe
2) IDE Utilizada: PyCharm Community Edition 2022.3.2
3) Pacotes utilizados no projeto, favor instalar para não termos problemas: 
  requirements:
    - pip psycopg2
    - pip request
    - pip uvicorn
    - pip fastapi

4)  Abrir o projeto e rodar a aplicação: Ou abrir o console: E:\PrevisaoTempo\venv\Scripts\python.exe E:\PrevisaoTempo\apiPrevisao.py 
   - Porta que vai rodar: 127.0.0.1 -> está hardcode
   - porta: 7777 - > está hardcode

    allow_origins=["http://localhost","http://127.0.0.1:3000", 'http://localhost:8080', "http://localhost:3000"] -> se precisar por mais permissões no fastapi para aceitar conexões. deixei *.* todas

5) Ao rodar irá abrir um navegador padrão para testes.


5) Api para debug-> swagger, vocÊ pode entrar no link e digitar http://127.0.0.1:7777/docs#/

http://127.0.0.1:7777/getprevisaotempo/{cidade, pais}?cidade=blumenau&pais=br  exemplo de comunicação       -> para pegar a previsão do tempo
http://127.0.0.1:7777/gethistoricopesquisa  -> para trazer o historico


- Utilizei FastApi, por ser mais rápido implementação e curva de aprendizado maior
- psycopg2 -> utilizado para conexão com banco de dados
- request-> utilizado para requisições
- uvicorn -> biblioteca para dar run na aplicação


6) Para validar o JSON:
https://jsoncrack.com/editor

Obs: Os programas utilizads como banco e python, estão na pasta Programas.