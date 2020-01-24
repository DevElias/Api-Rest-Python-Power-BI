from Model import db_config
from pprint import pprint

def getReceita():
    # ID da Empresa no ERPFlex
    idEmpresa = str('ID da Empresa')
    # Executa Query que busca todas receitas no período solicitado
    db_config.cursor.execute("SELECT SA1_Desc as 'Cliente', SA1_Mun as 'Municipio', SA1_email as 'Email', DATE_FORMAT(SE2_Vencto, '%d/%m/%Y') as 'Vencimento', SE2_Valor as 'Valor', SE2_ValorPago as 'Valor Pago' FROM SE2 INNER JOIN SF2 ON SF2_ID = SE2_IDSF2 INNER JOIN SA1 ON SA1_ID = SF2_IDSA1 WHERE SE2_IDEA1 = " + idEmpresa + " AND SE2_Vencto BETWEEN '2020-01-01 00:00:00' AND '2020-01-31 00:00:00';")
    # Faz o Fet das Receitas
    receitas = db_config.cursor.fetchall()
    # Retorna os dados para rotas.py
    return receitas