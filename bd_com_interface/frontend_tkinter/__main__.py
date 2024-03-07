from tkinter import ttk
from tkinter import *
import tkinter.messagebox
import sys, os
import mysql.connector
from sqlalchemy import create_engine




class DbGUI():
    def __init__(self,root):
        self.root=root
        self.root.title('BD Biblioteca')
        self.root.geometry('400x400')
        self.root.config(bg='#C1D0B5')

        title_label = Label(self.root, text='Biblioteca', font=('times new roman', 20, 'bold'), bg='#C1D0B5', fg='#99A98F')
        title_label.place(x=0, y=0, relwidth=1)

    
        book_id_label = Label(self.root, text='ID do Livro', font=('times new roman', 15, 'bold'),bg='#C1D0B5', fg='#99A98F')
        book_id_label.grid(row=4,column=0, padx=132)


    def conexao():
        conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='senharoot!26',
            # database='banco_p1;'
            auto_commit=True
        )


        cursor = conexao.cursor()
        print("Conexão com o banco de dados realizada com sucesso!")




if __name__=='__main__':
    root=Tk()
    DbGUI(root)
    root.mainloop()