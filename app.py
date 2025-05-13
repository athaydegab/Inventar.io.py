import tkinter as tk
from tkinter import messagebox, simpledialog
from db_config import get_connection
from datetime import datetime

def adicionar_item():
    nome = simpledialog.askstring("Adicionar Item", "Nome do item:")
    quantidade = simpledialog.askinteger("Adicionar Item", "Quantidade:")
    if nome and quantidade:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO itens (nome, quantidade) VALUES (%s, %s)", (nome, quantidade))
        conn.commit()
        conn.close()
        messagebox.showinfo("Sucesso", "Item adicionado com sucesso!")

def retirar_item():
    item_id = simpledialog.askinteger("Retirar Item", "ID do item:")
    qtd = simpledialog.askinteger("Retirar Item", "Quantidade a retirar:")
    quem = simpledialog.askstring("Retirar Item", "Quem está retirando?")
    
    if item_id and qtd and quem:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT quantidade FROM itens WHERE id = %s", (item_id,))
        resultado = cursor.fetchone()
        if resultado and resultado[0] >= qtd:
            cursor.execute("UPDATE itens SET quantidade = quantidade - %s WHERE id = %s", (qtd, item_id))
            cursor.execute("""
                INSERT INTO historico (item_id, quem, data_retirada, quantidade_retirada)
                VALUES (%s, %s, %s, %s)
            """, (item_id, quem, datetime.now(), qtd))
            conn.commit()
            messagebox.showinfo("Sucesso", "Item retirado com sucesso!")
        else:
            messagebox.showwarning("Erro", "Quantidade insuficiente ou item não encontrado.")
        conn.close()

def visualizar_inventario():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM itens")
    resultado = cursor.fetchall()
    conn.close()

    janela = tk.Toplevel(root)
    janela.title("Inventário Atual")
    for item in resultado:
        tk.Label(janela, text=f"ID: {item[0]} | Nome: {item[1]} | Quantidade: {item[2]}").pack()

def ver_historico():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT h.id, i.nome, h.quem, h.quantidade_retirada, h.data_retirada
        FROM historico h
        JOIN itens i ON i.id = h.item_id
        ORDER BY h.data_retirada DESC
        LIMIT 10
    """)
    resultado = cursor.fetchall()
    conn.close()

    janela = tk.Toplevel(root)
    janela.title("Histórico de Retiradas")
    for linha in resultado:
        tk.Label(janela, text=f"{linha[0]} | {linha[1]} | {linha[2]} | {linha[3]} | {linha[4]}").pack()

# Interface principal
root = tk.Tk()
root.title("Inventário do Armário")

tk.Button(root, text="Adicionar Item", command=adicionar_item, width=30).pack(pady=5)
tk.Button(root, text="Retirar Item", command=retirar_item, width=30).pack(pady=5)
tk.Button(root, text="Ver Inventário", command=visualizar_inventario, width=30).pack(pady=5)
tk.Button(root, text="Ver Histórico", command=ver_historico, width=30).pack(pady=5)

root.mainloop()
