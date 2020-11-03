import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re

from tkinter import *
import tkinter.messagebox
import sqlite3


class product:
    def __init__(self,root):
        p = DataBase()
        p.conn()
        self.root = root
        
        def validate_input(new_value):
            if new_value.isdigit():
                return True
            else:
                return False

        validation = root.register(validate_input)
        
        self.root.title('InstaCook')
        self.root.geometry('1200x1200')
        self.root.config(bg = 'black')

        bookISBN = StringVar()
        bookAuthor = StringVar()
        bookName = StringVar()

        
        def insert():
            print("product: save method called")
            if (len(bookISBN.get()) != 0):
                p.insert(bookISBN.get(), bookAuthor.get(), bookName.get())
                productList.delete(0,END)
                productList.insert(END, bookISBN.get(), bookAuthor.get(), bookName.get())

            else:
                tkinter.messagebox.askyesno("Do you want to enter the product ID?")
                print('product: save method finished')


        def clear():
            print("product: clear method called")
            self.txtbookISBN.delete(0,END)
            self.txtbookAuthor.delete(0,END)
            self.txtbookName.delete(0,END)
            self.ListBox.delete(0,END)
            productList.delete(0,END)
            print("product: clear method finished")

        def search():
            print("product: search method called")
            productList.delete(0,END)
            '''
            for row in p.search(bookISBN.get()):
                productList.insert(END, row, str(" "))
            print("product: search method finished", row)
            '''
            print (" vege1: ", bookAuthor.get())
            print (" vege2: ", bookISBN.get())
            print (" vege3: ", bookName.get())
            #url1 = "https://www.myrecipes.com/search?q=potato&onion"
            url1 = "https://www.myrecipes.com/search?q="
            url1 = url1  + bookAuthor.get()
            url1 =  url1  + "&"
            url1 = url1  + bookISBN.get()
            url1 =  url1  + "&"
            url1 = url1  + bookISBN.get()
            print (url1)
            req = requests.get(url1)
            
            print  (url1)
            page = requests.get(url1)
            soup = BeautifulSoup(page.content, 'html.parser')
            results = soup.findAll(class_="search-result-title-link")
            for ref in results:
                print(ref.get('href'))
                productList.insert(END, ref.get('href'), str(" "))

        def productRec(event):
            print("product 1: productRec called")
            global pd
            searchPd = productList.curselection()[0]
            pd = productList.get(searchPd)
                    
            self.textbookISBN.delete(0,END) 
            self.textbookISBN.insert(END,bookISBN[0])

            self.textbookAuthor.delete(0,END)
            self.textbookAuthor.insert(END,bookISBN[1])

            self.textbookName.delete(0,END)
            self.textbookName.insert(END,bookISBN[2])

            print("product 2: productRecord method finished")

        #This is the graphical user part of the application(GUI)

        MainFrame = Frame(self.root, bg = 'black')
        MainFrame.grid()

        HeadFrame = Frame(MainFrame, bd = 1, padx = 50, pady = 10, bg = "dark blue", relief = RIDGE)
        HeadFrame.pack(side = TOP)

        self.ITitle = Label(HeadFrame, font = ('Comic Sans', 14, 'bold'), fg = 'white',
                            text = 'InstaCook by Raghav', bg= 'dark blue')
        self.ITitle.grid()

        OperationFrame = Frame(MainFrame, bd = 2, width = 1300, height = 230,
                               padx = 50, pady = 10, bg = 'black', relief = RIDGE)
        OperationFrame.pack(side = BOTTOM)

        
        BodyFrame = Frame(MainFrame, bd = 2, width = 1290, height = 800,
                               padx = 30, pady = 150, bg = 'black', relief = RIDGE)
        BodyFrame.pack(side = BOTTOM)


        LeftBodyFrame = LabelFrame(BodyFrame, bd = 2, width = 300, height = 1000,
                               padx = 100, pady = 92,  bg = 'gray', relief = RIDGE,
                                   font = ('Comic Sans', 14, 'bold'), text = 'Vegetables', foreground = "black")
        LeftBodyFrame.pack(side = LEFT)


        RightBodyFrame = LabelFrame(BodyFrame, bd = 2, width = 400, height = 500,
                               padx = 20, pady = 45, bg = 'gray', relief = RIDGE,
                                    font = ('Comic Sans', 14, 'bold'), text = 'Results', foreground = "black")
        RightBodyFrame.pack(side = RIGHT)



        #Add the widget to the leftBodyFrame
        #First "Book ISBN"
        self.labelbookISBN = Label(LeftBodyFrame, font = ('Comic Sans', 14, 'bold'), text = 'Vegetable 1',
                                   padx = 2, pady = 3, bg = 'blue', fg = 'white')
        self.labelbookISBN.grid(row = 0, column = 0, sticky = W)

        self.txtbookISBN = Entry(LeftBodyFrame, font = ('Comic Sans', 14, 'bold'), textvariable = bookISBN, width = 30)
        self.txtbookISBN.grid(row = 0, column = 1, sticky = W)


        #Second "Book Author"
        self.labelbookAuthor = Label(LeftBodyFrame, font = ('Comic Sans', 14, 'bold'), text = 'Vegetable 2',
                                   padx = 2, pady = 3, bg = 'blue', fg = 'white')
        self.labelbookAuthor.grid(row = 1, column = 0, sticky = W)

        self.txtbookAuthor = Entry(LeftBodyFrame, font = ('Comic Sans', 14, 'bold'), textvariable = bookAuthor, width = 30)
        self.txtbookAuthor.grid(row = 1, column = 1, sticky = W)

        
        #Third "Book Name
        self.labelbookName = Label(LeftBodyFrame, font = ('Comic Sans', 14, 'bold'), text = 'Vegetable 3',
                                   padx = 2, pady = 2, bg = 'blue', fg = 'white')
        self.labelbookName.grid(row = 2, column = 0, sticky = W)

        self.txtbookName = Entry(LeftBodyFrame, font = ('Comic Sans', 14, 'bold'), textvariable = bookName, width = 30)
        self.txtbookName.grid(row = 2, column = 1, sticky = W)
        
        
        '''
        #Label in the leftbodyFrame
        self.labelpC1 = Label(LeftBodyFrame, padx = 2, pady =2 )
        self.labelpC1.grid(row = 6, column = 0, sticky = W)

        self.labelpC2 = Label(LeftBodyFrame, padx = 2, pady =2 )
        self.labelpC2.grid(row = 7, column = 0, sticky = W)

        self.labelpC3 = Label(LeftBodyFrame, padx = 2, pady =2 )
        self.labelpC3.grid(row = 8, column = 0, sticky = W)

        self.labelpC4 = Label(LeftBodyFrame, padx = 2, pady =2 )
        self.labelpC4.grid(row = 9, column = 0, sticky = W)
        '''
        #Add scroll bar on the right body frame

        scroll = Scrollbar(RightBodyFrame)
        scroll.grid(row = 0, column = 1, sticky = 'NS')

        productList = Listbox(RightBodyFrame, width = 45, height = 10,
                              font = ('Comic Sans', 14, 'bold'), yscrollcommand = scroll.set)
        productList.bind('<<ListBox select>>', productRec)
        productList.grid(row = 0, column = 0, padx = 8)

        scroll.config(command = productList.yview)

        #Creating the three buttons
        
        '''
        self.buttonSaveData = Button(OperationFrame, text = 'Save', font = ('Comic Sans', 20, 'bold'),
                                     height = 1, width = 10, bd = 4, command = insert )
        self.buttonSaveData.grid(row=0, column = 1)
        '''

        self.buttonClearData = Button(OperationFrame, text = 'Clear ',
                                 font = ('Comic Sans', 20, 'bold'), height = 1, width = 10, bd = 4, command = clear)
        self.buttonClearData.grid(row = 0, column = 2)

        self.buttonSearchData = Button(OperationFrame, text = 'Search',
                                 font = ('Comic Sans', 20, 'bold'), height = 1, width = 10, bd = 4, command = search)
        self.buttonSearchData.grid(row = 0, column = 3)



#This is where I connect the dataBase using structured query
class DataBase:
    def conn(self):
        print("Database: Connection method called")
        con = sqlite3.connect("cooking.db")
        cur = con.cursor()
        query = ("Create table if not exists product(bookISBN text primary key, bookAuthor text, bookName text)")
        cur.execute(query)
        con.commit()
        con.close()
        print("database: connection method finished")



    def insert (self, bookISBN, bookAuthor, bookName):
        print("database: save method called")
        con = sqlite3.connect("cooking.db")
        cur = con.cursor()
        query = ("Insert into product values(?,?,?)")
        cur.execute(query, (bookISBN, bookAuthor, bookName))
 
        con.commit()
        con.close()
        print("database: save method finished")

        
    def search(self, bookISBN = " "):
        print("database: search method called", bookISBN)
        con = sqlite3.connect("cooking.db")
        cur = con.cursor()
        print("cure")
        #cur.execute("select * from product where bookISBN = ? ",(bookISBN))
        query = ("select * from product where bookISBN =  '" ) + bookISBN  +"'"
        print (query)
        cur.execute(query)
        print (query)
        rows = cur.fetchall()
        con.close()
        print(bookISBN,"database: search method finished")
        return rows

if __name__ == '__main__':
    root = Tk()

    application = product(root)
    root.mainloop()

        
        


            
            
