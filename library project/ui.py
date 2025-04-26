from logic import add_book, Book, save_library, library
import tkinter as tk
from tkinter import messagebox as msgbx
class Window:
    def __init__(self):

        self.window= tk.Tk()
        self.window.title("Book Wishlist Manager")
        self.window.resizable(width=False, height=False)

        tk.Label(self.window, text="Title: ").grid(row=0,column=0,sticky="e", pady=2)
        self.ent_title = tk.Entry(self.window, bd=2, relief="solid")
        self.ent_title.grid(row=0,column=1,pady=2,padx=5)

        tk.Label(self.window, text="Author: ").grid(row=1,column=0,sticky="e",pady=2)
        self.ent_author = tk.Entry(self.window, bd=2, relief="solid")
        self.ent_author.grid(row=1,column=1,pady=2)

        tk.Label(self.window, text="Genre: ").grid(row=2,column=0,sticky="e",pady=2)
        self.ent_genre = tk.Entry(self.window, bd=2, relief="solid")
        self.ent_genre.grid(row=2,column=1,pady=2)

        tk.Label(self.window, text="Pages: ").grid(row=3,column=0,sticky="e",pady=2)
        self.ent_pages = tk.Entry(self.window, bd=2, relief="solid")
        self.ent_pages.grid(row=3,column=1,pady=2)

        self.btn_add = tk.Button(self.window, text="Add Book", bd=2, relief="raised", command=self.add_book)
        self.btn_add.grid(row=4,column=0,pady=10,sticky="ew")

        self.btn_save = tk.Button(self.window, text="Save Library", bd=2, relief="raised", command=self.saveLibrary)
        self.btn_save.grid(row=4,column=1,pady=10,sticky="ew")

        self.book_listbox = tk.Listbox(self.window,width=50)
        self.book_listbox.grid(row=5,column=0,columnspan=2,pady=10)
        
        self.window.mainloop()
    
    def add_book(self):
        title = self.ent_title.get()
        author = self.ent_author.get()
        genre = self.ent_genre.get()
        pages = self.ent_pages.get()

        if not author or not title:
            msgbx.showinfo("Input error", "Title and Author are required")
            return
        
        book = Book(title,author,genre,pages)
        add_book(book)
        self.update_listbox()
        
        self.ent_title.delete(0, tk.END)
        self.ent_author.delete(0, tk.END)
        self.ent_genre.delete(0, tk.END)
        self.ent_pages.delete(0, tk.END)
    
    def saveLibrary(self):
        save_library()
        msgbx.showinfo("Saved", "Library saved succesfully!")

    def update_listbox(self):
        self.book_listbox.delete(0, tk.END)
        for book in library:
            self.book_listbox.insert(tk.END, str(book))