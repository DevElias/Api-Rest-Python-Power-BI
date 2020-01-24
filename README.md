# Api REST em Python + POWER BI
Criação de uma API de Receitas comunicando com o ERPFlex e disponibilizando os dados em JSON para o POWER BI

Histórico de Configuração - Python
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

9.Insira a URL da API que você acabou de criar, perceba que passo a mesma URL local mais **/receitas** que é justamente a rota que criamos no arquivo de rotas para o metodo das receitas:
![](https://i.imgur.com/HwLs65u.jpg)

10. Se tudo estiver correto, irá aparecer essas colunas **Record** que parece bizarro, mas na verdade esses são os dados brutos que vamos lapidalos no POWER BI em breve.

11. Nessa tela clique em Para a Tabela

![](https://i.imgur.com/SYq3SO6.jpg)

12. Clique em Aceita:

![](https://i.imgur.com/RP5tZK8.jpg)

13. Agora clique nas flechas indicadas na imagem e clique em aceitar:

![](https://i.imgur.com/a9Wnn1L.jpg)

14. Agora seus Dados já estão mais amigáveis em tabela para trabalhar com eles.
15. Clique em Aplicar e Fechar:

![](https://i.imgur.com/NlpqQCM.jpg)

16. Seus dados serão levados para dentro do POWER BI onde vc pode começar a brincar da forma que lhe convém:

![](https://i.imgur.com/tfo3ZEs.jpg)

17. Daqui para frente você cria seus informes de acordo com sua necessidade e da sua empresa:

![](https://i.imgur.com/W8dx6ZJ.jpg)


DADOS ADICIONAIS:
=================

1. Caso você possua acesso a uma base de dados distinta a usada no exemplo que foi a base de dados de um ERP chamado ERPFlex,
   Você pode conectar sua base de dados e efetuar as consultas SQL no seu banco de dados mudando as Consultas SQL no projeto.
   
   Essas Querys estão localizadas no diretório: **Controller/receita.py**

Dúvidas em como utilizar esse projeto entre em contato comigo por e-mail
eliasv.lima@yahoo.com.br

Um Abraço!

