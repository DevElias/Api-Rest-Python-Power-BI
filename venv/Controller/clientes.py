from Model import db_config
from pprint import pprint

def getClientes():
    idEmpresa = str('ID da Empresa')
    # Faz a comunicação com o db_config.py
    db_config.cursor.execute("SELECT SA1_Desc, SA1_email FROM SA1 WHERE SA1_IDEA1 = " + idEmpresa + " AND SA1_email != ''")
    clientes = db_config.cursor.fetchall()
    return clientes
