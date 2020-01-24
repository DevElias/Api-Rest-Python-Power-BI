# Api REST em Python + POWER BI
Criação de uma API de Receitas comunicando com o ERPFlex e disponibilizando os dados em JSON para o POWER BI

Tutorial de Configuração Incial - Python
=======================================

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

6. Acesse a URL que esta rodando seu projeto local - http://localhost:5000/receitas para verificar se os dados estão sendo retornados do Banco de Dados e disponibilizados via requisição GET:
![](https://i.imgur.com/SuU2Xr8.jpg)

7.Tendo os Dados de retorno em mãos, agora é hora de começar a brincar com o Power BI

POWER BI
========
8. É fundamental você ter um usuário criado no Power BI, faça seu login na ferramenta e em seguida, vá até a opção de Menu Obter Dados > Web:

![](https://i.imgur.com/szuVMLJ.jpg)

9.Insira a URL da API que você acabou de criar, perceba que passo a mesma URL local mais /receitas que é justamente a rota que criamos no arquivo de rotas para o metodo das receitas:
![](https://i.imgur.com/HwLs65u.jpg)
