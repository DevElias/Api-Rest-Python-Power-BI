# Api REST em Python + POWER BI
Criação de uma API de Receitas comunicando com o ERPFlex e disponibilizando os dados em JSON para o POWER BI

Tutorial de Configuração Incial - Python
++++++++++++++++++++++++++++++++++++++++

1. Acesse o diretório Model/db_config.py

2. Informe os parâmetros de comunicação com o Banco de Dados (Host, User,Password e database):
![](https://i.imgur.com/LoXTZyT.jpg)

3. Acesse o diretório Controller/receita.py para modificar o ID da Empresa:
![](https://i.imgur.com/igsZ46t.jpg)

4. Agora no **Terminal** acesse o diretório /Template/rotas.py é neste arquivo que estão configuradas todas as rotas da API:

**Arquivo de Rotas**
![](https://i.imgur.com/9onevNs.jpg)

5. Execute o comando de run server no diretório das rotas >> python rotas.py
![](https://i.imgur.com/MR2Bte9.jpg)
