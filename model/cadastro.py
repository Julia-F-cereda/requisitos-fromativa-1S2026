from database.conexao import conectar

def retornar_dados():
    conexao, cursor = conectar()
    cursor.execute("""SELECT cod_requisito, descricao, nivel, valor, situacao FROM tb_requisitos""")
    dado = cursor.fetchall()
    conexao.close()
    return dado

def enviar_dados(descricao:str, nivel:str, valor: str, situacao:str) ->bool:
    conexao, cursor = conectar()
    cursor.execute("""INSERT INTO tb_requisitos (descricao, nivel, valor, situacao)
                   VALUES (%s, %s, %s, %s)""", [descricao, nivel, valor,situacao])
    
    conexao.commit()
    conexao.close()

def excluir_dados(cod_requisito):
    conexao, cursor = conectar()

    cursor.execute("""DELETE FROM tb_requisitos where cod_requisito= %s""",[cod_requisito,])

    conexao.commit()
    conexao.close()


def alterar_sit(situacao, cod_requisito):
    conexao, cursor = conectar()

    cursor.execute("""UPDATE tb_requisitos SET situacao= %s WHERE cod_requisito= %s""",[situacao, cod_requisito])

    conexao.commit()
    conexao.close()
