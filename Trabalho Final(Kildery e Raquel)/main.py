import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import psycopg2
import tkinter.ttk as ttk

def menu():
    conn = conectar_banco()

    window = tk.Tk()
    window.title("AltisTelecom")
    window.geometry("500x500")
    window.resizable(False, False)
   
    window.iconbitmap("icon.ico")

    set_background_image(window, "background.jpg")

    btn_adicionar_cliente = tk.Button(window, text="Adicionar Cliente", command=lambda: adicionar_cliente_window(conn),
                                      width=20, height=2, bg="black", fg="white")
    btn_adicionar_cliente.grid(row=0, column=0, padx=10, pady=10)

    btn_ver_clientes = tk.Button(window, text="Ver Clientes", command=lambda: ver_clientes(conn),
                                 width=20, height=2, bg="black", fg="white")
    btn_ver_clientes.grid(row=0, column=1, padx=10, pady=10)

    btn_remover_cliente = tk.Button(window, text="Remover Cliente", command=lambda: remover_cliente_window(conn),
                                    width=20, height=2, bg="black", fg="white")
    btn_remover_cliente.grid(row=0, column=2, padx=10, pady=10)

    btn_adicionar_plano = tk.Button(window, text="Adicionar Plano", command=lambda: adicionar_plano_window(conn),
                                   width=20, height=2, bg="black", fg="white")
    btn_adicionar_plano.grid(row=1, column=0, padx=10, pady=10)

    btn_ver_planos = tk.Button(window, text="Ver Planos", command=lambda: ver_planos(conn),
                               width=20, height=2, bg="black", fg="white")
    btn_ver_planos.grid(row=1, column=1, padx=10, pady=10)

    btn_remover_plano = tk.Button(window, text="Remover Plano", command=lambda: remover_plano_window(conn),
                                 width=20, height=2, bg="black", fg="white")
    btn_remover_plano.grid(row=1, column=2, padx=10, pady=10)

    btn_realizar_venda = tk.Button(window, text="Realizar Venda", command=lambda: realizar_venda_window(conn),
                                  width=20, height=2, bg="black", fg="white")
    btn_realizar_venda.grid(row=2, column=0, padx=10, pady=10)

    btn_alterar_venda = tk.Button(window, text="Alterar Venda", command=lambda: alterar_venda_window(conn),
                                 width=20, height=2, bg="black", fg="white")
    btn_alterar_venda.grid(row=2, column=1, padx=10, pady=10)

    btn_cancelar_venda = tk.Button(window, text="Cancelar Venda", command=lambda: cancelar_venda_window(conn),
                                  width=20, height=2, bg="black", fg="white")
    btn_cancelar_venda.grid(row=2, column=2, padx=10, pady=10)

    btn_ver_vendas = tk.Button(window, text="Ver Vendas", command=lambda: ver_vendas(conn),
                              width=20, height=2, bg="black", fg="white")
    btn_ver_vendas.grid(row=3, column=0, padx=10, pady=10)

    window.mainloop()


def conectar_banco():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="AltisTelecom",
            user="postgres",
            password="postgre"
        )
        return conn
    except psycopg2.Error as e:
        show_message(f"Erro ao conectar ao banco de dados: {str(e)}")


def adicionar_cliente_window(conn):
    window = tk.Toplevel()
    window.title("Adicionar Cliente")
    window.geometry("400x400")

    label_nome = tk.Label(window, text="Nome do Cliente:", fg="black")
    label_nome.pack()

    entry_nome = tk.Entry(window)
    entry_nome.pack()

    label_cpf = tk.Label(window, text="CPF:", fg="black")
    label_cpf.pack()

    entry_cpf = tk.Entry(window)
    entry_cpf.pack()

    label_rg = tk.Label(window, text="RG:", fg="black")
    label_rg.pack()

    entry_rg = tk.Entry(window)
    entry_rg.pack()

    btn_adicionar = tk.Button(window, text="Adicionar",
                              command=lambda: adicionar_cliente(conn, entry_nome.get(), entry_cpf.get(), entry_rg.get(), window),
                              width=10, height=1, bg="black", fg="white")
    btn_adicionar.pack()

def adicionar_cliente(conn, nome, cpf, rg, window):
    try:
        cursor = conn.cursor()
        query = "INSERT INTO clientes (nome, cpf, rg) VALUES (%s, %s, %s)"
        cursor.execute(query, (nome, cpf, rg))
        conn.commit()
        cursor.close()
        messagebox.showinfo("Sucesso", "Cliente adicionado com sucesso!")
        window.destroy()
    except psycopg2.Error as e:
        show_message(f"Erro ao adicionar cliente: {str(e)}")

def remover_cliente_window(conn):
    window = tk.Toplevel()
    window.title("Remover Cliente")
    window.geometry("400x200")

    label_id = tk.Label(window, text="ID do Cliente:", fg="black")
    label_id.pack()

    entry_id = tk.Entry(window)
    entry_id.pack()

    btn_remover = tk.Button(window, text="Remover",
                            command=lambda: remover_cliente(conn, entry_id.get(), window),
                            width=10, height=1, bg="black", fg="white")
    btn_remover.pack()

def remover_cliente(conn, id_cliente, window):
    try:
        cursor = conn.cursor()
        query = "DELETE FROM clientes WHERE id = %s"
        cursor.execute(query, (id_cliente,))
        conn.commit()
        cursor.close()
        messagebox.showinfo("Sucesso", "Cliente removido com sucesso!")
        window.destroy()
    except psycopg2.Error as e:
        show_message(f"Erro ao remover cliente: {str(e)}")

def adicionar_plano_window(conn):
    window = tk.Toplevel()
    window.title("Adicionar Plano")
    window.geometry("400x300")

    label_nome = tk.Label(window, text="Nome do Plano:", fg="black")
    label_nome.pack()

    entry_nome = tk.Entry(window)
    entry_nome.pack()

    label_preco = tk.Label(window, text="Preço:", fg="black")
    label_preco.pack()

    entry_preco = tk.Entry(window)
    entry_preco.pack()

    btn_adicionar = tk.Button(window, text="Adicionar",
                              command=lambda: adicionar_plano(conn, entry_nome.get(), entry_preco.get(), window),
                              width=10, height=1, bg="black", fg="white")
    btn_adicionar.pack()

def ver_clientes(conn):
    cursor = conn.cursor()
    query = "SELECT * FROM clientes"
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()

    window = tk.Toplevel()
    window.title("Ver Clientes")
    window.geometry("400x300")

    listbox = tk.Listbox(window, width=50)
    for row in rows:
        listbox.insert(tk.END, f"ID: {row[0]}. Nome: {row[1]}. CPF: {row[2]}. RG: {row[3]}.")
    listbox.pack()

def ver_vendas(conn):
    window = tk.Toplevel()
    window.title("Ver Vendas")
    window.geometry("400x300")

    cursor = conn.cursor()
    query = "SELECT * FROM vendas"
    cursor.execute(query)
    rows = cursor.fetchall()

    listbox = tk.Listbox(window, width=50)
    for row in rows:
        listbox.insert(tk.END, f"ID: {row[0]}. Cliente: {row[1]}. Plano: {row[2]}.")
    listbox.pack()

    cursor.close()
    

def adicionar_plano(conn, nome, preco, window):
    try:
        cursor = conn.cursor()
        query = "INSERT INTO planos (nome, preco) VALUES (%s, %s)"
        cursor.execute(query, (nome, preco))
        conn.commit()
        cursor.close()
        messagebox.showinfo("Sucesso", "Plano adicionado com sucesso!")
        window.destroy()
    except psycopg2.Error as e:
        show_message(f"Erro ao adicionar plano: {str(e)}")

def remover_plano_window(conn):
    window = tk.Toplevel()
    window.title("Remover Plano")
    window.geometry("400x200")

    label_id = tk.Label(window, text="ID do Plano:", fg="black")
    label_id.pack()

    entry_id = tk.Entry(window)
    entry_id.pack()

    btn_remover = tk.Button(window, text="Remover",
                            command=lambda: remover_plano(conn, entry_id.get(), window),
                            width=10, height=1, bg="black", fg="white")
    btn_remover.pack()

def remover_plano(conn, id_plano, window):
    try:
        cursor = conn.cursor()
        query = "DELETE FROM planos WHERE id = %s"
        cursor.execute(query, (id_plano,))
        conn.commit()
        cursor.close()
        messagebox.showinfo("Sucesso", "Plano removido com sucesso!")
        window.destroy()
    except psycopg2.Error as e:
        show_message(f"Erro ao remover plano: {str(e)}")

def ver_planos(conn):
    window = tk.Toplevel()
    window.title("Ver Planos")
    window.geometry("400x300")

    cursor = conn.cursor()
    query = "SELECT * FROM planos"
    cursor.execute(query)
    rows = cursor.fetchall()

    listbox = tk.Listbox(window, width=50)
    for row in rows:
        listbox.insert(tk.END, f"ID: {row[0]}. Nome: {row[1]}. Preço: {row[2]}.")
    listbox.pack()

    cursor.close()

def realizar_venda_window(conn):
    window = tk.Toplevel()
    window.title("Realizar Venda")
    window.geometry("400x300")

    cursor = conn.cursor()
    query_clientes = "SELECT * FROM clientes"
    cursor.execute(query_clientes)
    rows_clientes = cursor.fetchall()

    label_cliente = tk.Label(window, text="Selecione o Cliente:", fg="black")
    label_cliente.pack()

    combo_cliente = ttk.Combobox(window, values=[f"{row[0]} - {row[1]}" for row in rows_clientes])
    combo_cliente.pack()

    query_planos = "SELECT * FROM planos"
    cursor.execute(query_planos)
    rows_planos = cursor.fetchall()

    label_plano = tk.Label(window, text="Selecione o Plano:", fg="black")
    label_plano.pack()

    combo_plano = tk.ttk.Combobox(window, values=[f"{row[0]} - {row[1]}" for row in rows_planos])
    combo_plano.pack()

    btn_vender = tk.Button(window, text="Vender",
                           command=lambda: realizar_venda(conn, combo_cliente.get(), combo_plano.get(), window),
                           width=10, height=1, bg="black", fg="white")
    btn_vender.pack()

def realizar_venda(conn, cliente, plano, window):
    try:
        cursor = conn.cursor()
        id_cliente = cliente.split(" - ")[0]
        id_plano = plano.split(" - ")[0]
        query = "INSERT INTO vendas (id_cliente, id_plano) VALUES (%s, %s)"
        cursor.execute(query, (id_cliente, id_plano))
        conn.commit()
        cursor.close()
        messagebox.showinfo("Sucesso", "Venda realizada com sucesso!")
        window.destroy()
    except psycopg2.Error as e:
        show_message(f"Erro ao realizar venda: {str(e)}")

def alterar_venda_window(conn):
    window = tk.Toplevel()
    window.title("Alterar Venda")
    window.geometry("400x300")

    cursor = conn.cursor()
    query_vendas = "SELECT * FROM vendas"
    cursor.execute(query_vendas)
    rows_vendas = cursor.fetchall()

    label_venda = tk.Label(window, text="Selecione a Venda:", fg="black")
    label_venda.pack()

    combo_venda = tk.ttk.Combobox(window, values=[f"{row[0]} - Cliente: {row[1]}. Plano: {row[2]}." for row in rows_vendas])
    combo_venda.pack()

    query_planos = "SELECT * FROM planos"
    cursor.execute(query_planos)
    rows_planos = cursor.fetchall()

    label_plano = tk.Label(window, text="Selecione o Novo Plano:", fg="black")
    label_plano.pack()

    combo_plano = tk.ttk.Combobox(window, values=[f"{row[0]} - {row[1]}" for row in rows_planos])
    combo_plano.pack()

    btn_alterar = tk.Button(window, text="Alterar",
                            command=lambda: alterar_venda(conn, combo_venda.get(), combo_plano.get(), window),
                            width=10, height=1, bg="black", fg="white")
    btn_alterar.pack()

def alterar_venda(conn, venda, novo_plano, window):
    try:
        cursor = conn.cursor()
        id_venda = venda.split(" - ")[0]
        id_plano = novo_plano.split(" - ")[0]
        query = "UPDATE vendas SET id_plano = %s WHERE id = %s"
        cursor.execute(query, (id_plano, id_venda))
        conn.commit()
        cursor.close()
        messagebox.showinfo("Sucesso", "Venda alterada com sucesso!")
        window.destroy()
    except psycopg2.Error as e:
        show_message(f"Erro ao alterar venda: {str(e)}")

def cancelar_venda_window(conn):
    window = tk.Toplevel()
    window.title("Cancelar Venda")
    window.geometry("400x200")

    label_id = tk.Label(window, text="ID da Venda:", fg="black")
    label_id.pack()

    entry_id = tk.Entry(window)
    entry_id.pack()

    btn_cancelar = tk.Button(window, text="Cancelar",
                             command=lambda: cancelar_venda(conn, entry_id.get(), window),
                             width=10, height=1, bg="black", fg="white")
    btn_cancelar.pack()

def cancelar_venda(conn, id_venda, window):
    try:
        cursor = conn.cursor()
        query = "DELETE FROM vendas WHERE id = %s"
        cursor.execute(query, (id_venda,))
        conn.commit()
        cursor.close()
        messagebox.showinfo("Sucesso", "Venda cancelada com sucesso!")
        window.destroy()
    except psycopg2.Error as e:
        show_message(f"Erro ao cancelar venda: {str(e)}")

def set_background_image(window, image_path):
    background_image = ImageTk.PhotoImage(Image.open(image_path))
    background_label = tk.Label(window, image=background_image)
    background_label.image = background_image
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

def show_message(message):
    messagebox.showinfo("Message", message)

menu()


