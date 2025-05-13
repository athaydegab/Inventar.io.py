from datetime import datetime

def retirar_item(item_id, quem, qtd):
    cursor.execute("SELECT quantidade FROM itens WHERE id = %s", (item_id,))
    atual = cursor.fetchone()[0]
    if atual >= qtd:
        cursor.execute("UPDATE itens SET quantidade = quantidade - %s WHERE id = %s", (qtd, item_id))
        cursor.execute("INSERT INTO historico (item_id, quem, data_retirada, quantidade_retirada) VALUES (%s, %s, %s, %s)", 
                       (item_id, quem, datetime.now(), qtd))
        conn.commit()
    else:
        print("Quantidade insuficiente.")


def adicionar_item(nome, quantidade):
    cursor.execute("INSERT INTO itens (nome, quantidade) VALUES (%s, %s)", (nome, quantidade))
    conn.commit()
