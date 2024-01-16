import tkinter as tk                #starts kinter window
import mysql.connector as sql
from tkinter import ttk, messagebox
import customs as cs
from PIL import Image, ImageTk      #pillow for images

#mysqlconnection
host = "localhost" 
user = "root"
password = "Root@123"
database = "library"
connection = sql.connect(host='localhost', user='root', password='Root@123', database='libmansys') 
curs = connection.cursor()


#creation of window
root = tk.Tk() 
root.title("Library Management System")
root.geometry("1070x540")       #frame size   #root-window

#addition of widgets
frame_lhs = tk.Frame(root)      #frame-widget on lhs
frame_lhs.place(x=0, y=0, width=740, relheight=1)
title_label = tk.Label(root, text="Library Management System", font=("Helvetica", 20), wraplength=600)    
title_label.place(x=250, y=150)
title_label.lift()
image = Image.open("/Users/AmitSood/Documents/27315.jpg")  
image = image.resize((1070, 540), Image.ANTIALIAS)
background_photo = ImageTk.PhotoImage(image)
background_label = tk.Label(frame_lhs, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
frame_rhs = tk.Frame(root, bg = "grey95")
frame_rhs.place(x=740, y=0, relwidth=1, relheight=1)

frame_3 = tk.Frame(frame_rhs, bg="gray95") #remove
frame_3.place(x=0, y=300, relwidth=1, relheight=1)

def ClearScreen():      
    for widget in frame_lhs.winfo_children():
        widget.destroy()

def hide_title_label():             
    title_label.place_forget()

def ShowBooksGUI():   #All Books table             
   
    ClearScreen()
    hide_title_label()
    # Defining two scrollbars
    scroll_x = ttk.Scrollbar(frame_lhs, orient=tk.HORIZONTAL)
    scroll_y = ttk.Scrollbar(frame_lhs, orient=tk.VERTICAL)
    tree = ttk.Treeview(frame_lhs, columns=cs.columns, height=400, selectmode="extended", yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
    scroll_y.config(command=tree.yview)
    # vertical scrollbar: left side
    scroll_y.pack(side=tk.LEFT, fill=tk.Y)
    scroll_x.config(command=tree.xview)
    # Horizontal scrollbar: at bottom
    scroll_x.pack(side=tk.BOTTOM, fill=tk.X)

    # Table headings
    tree.heading('book_id', text='Book ID', anchor=tk.W)
    tree.heading('book_name', text='Book Name', anchor=tk.W)
    tree.heading('author', text='Author', anchor=tk.W)
    tree.heading('edition', text='Edition', anchor=tk.W)
    tree.heading('price', text='Price', anchor=tk.W)
    tree.heading('qty', text='Quantity', anchor=tk.W)
    tree.pack()

    try:
        curs.execute("SELECT * FROM books") 
        rows = curs.fetchall()
        if not rows:
            messagebox.showinfo("Database Empty", "There is no data to show")
        else:
            # Populate the Treeview with fetched records
            for row_no, row_values in enumerate(rows, start=1):
                tree.insert("", tk.END, text=row_no, values=row_values)
    except Exception as e:
        messagebox.showerror("Error!", f"Error due to {str(e)}")

def BookHoldersGUI_Func(): #Book Holders table
    ClearScreen()
    hide_title_label()
 
    # Creating and configuring the Treeview widget
    tree_x = ttk.Scrollbar(frame_lhs, orient=tk.HORIZONTAL)
    tree_y = ttk.Scrollbar(frame_lhs, orient=tk.VERTICAL)
    
    columns_1 = ("book_id", "book_name", "student_roll", "student_name", "issue_date", "return_date")
    tree_1 = ttk.Treeview(frame_lhs, columns=columns_1, height=400, selectmode="extended", yscrollcommand=tree_y.set, xscrollcommand=tree_x.set)
    
    tree_y.config(command=tree_1.yview)
    tree_x.config(command=tree_1.xview)
    tree_x.pack(side=tk.BOTTOM, fill=tk.X)

    # Table headings
    for col in columns_1:
        tree_1.heading(col, text=col, anchor=tk.W)

    tree_1.pack()

    try:
        curs.execute("SELECT * FROM records") 
        rows = curs.fetchall()

        if not rows:
            messagebox.showinfo("Database Empty", "There is no data to show")
        else:
            # Populate the Treeview with fetched records
            for row_no, row_values in enumerate(rows, start=1):        #to get records from each row
                tree_1.insert("", tk.END, text=row_no, values=row_values)
    except Exception as e:
        messagebox.showerror("Error!", f"Error due to {str(e)}")

def AddNewBookGUI(): #Add books window
    ClearScreen()
    hide_title_label()
    search_background_label = tk.Label(frame_lhs)
    search_background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Load and resize the new image
    search_image_path = "/Users/AmitSood/Documents/27315.jpg"  # Replace with the actual path
    search_image = Image.open(search_image_path)
    search_image = search_image.resize((1070, 540), Image.ANTIALIAS)
    search_background_photo = ImageTk.PhotoImage(search_image)
    search_background_label.configure(image=search_background_photo)
    search_background_label.image = search_background_photo

    book_id = tk.Label(frame_lhs, text="Book Id", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220, y=30)
    id_entry = tk.Entry(frame_lhs, bg=cs.color_4, fg=cs.color_3)
    id_entry.place(x=220, y=60, width=300)

    book_name = tk.Label(frame_lhs, text="Book Name", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220, y=100)
    bookname_entry = tk.Entry(frame_lhs, bg=cs.color_4, fg=cs.color_3)
    bookname_entry.place(x=220, y=130, width=300)

    author = tk.Label(frame_lhs, text="Author", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220, y=170)
    author_entry = tk.Entry(frame_lhs, bg=cs.color_4, fg=cs.color_3)
    author_entry.place(x=220, y=200, width=300)

    edition = tk.Label(frame_lhs, text="Edition", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220, y=240)
    edition_entry = tk.Entry(frame_lhs, bg=cs.color_4, fg=cs.color_3)
    edition_entry.place(x=220, y=270, width=300)

    price = tk.Label(frame_lhs, text="Price", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220, y=310)
    price_entry = tk.Entry(frame_lhs, bg=cs.color_4, fg=cs.color_3)
    price_entry.place(x=220, y=340, width=300)

    quantity = tk.Label(frame_lhs, text="Quantity", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220, y=380)
    qty_entry = tk.Entry(frame_lhs, bg=cs.color_4, fg=cs.color_3)
    qty_entry.place(x=220, y=410, width=300)

    submit_bt_1 = tk.Button(frame_lhs, text='Submit', font=(cs.font_1, 12), bd=2, command=lambda: Submit(id_entry.get(), bookname_entry.get(), author_entry.get(), edition_entry.get(), price_entry.get(), qty_entry.get()), cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=310, y=459, width=100)

    return id_entry, bookname_entry, author_entry, edition_entry, price_entry, qty_entry
def Submit(id_entry, bookname_entry, author_entry, edition_entry, price_entry, qty_entry): #Add New Book function 
    if id_entry == "" or bookname_entry == "" or author_entry == "" or edition_entry == "" or price_entry == "" or qty_entry == "":
        messagebox.showerror("Error!", "Sorry, all fields are required", parent=root)
    else:
        try:
            curs.execute("select * from books where bookid=%s", (id_entry,))
            row = curs.fetchone()

            if row != None:
                messagebox.showerror("Error!", "This book ID already exists, please try again with another one", parent=root)
            else:
                curs.execute("insert into books (bookid,bookname,author,edition,price,quantity) values(%s,%s,%s,%s,%s,%s)",
                                (
                                    id_entry,
                                    bookname_entry.upper(),
                                    author_entry.upper(),
                                    edition_entry,
                                    price_entry,
                                    qty_entry
                                ))
                connection.commit()
                messagebox.showinfo('Done!', "The data has been submitted")

        except Exception as e:
            messagebox.showerror("Error!", f"Error due to {str(e)}", parent=root)


def SearchGUI(): #Search window
    ClearScreen()
    hide_title_label()

    search_background_label = tk.Label(frame_lhs)
    search_background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Load and resize the new image
    search_image_path = "/Users/AmitSood/Documents/searchbook.jpg"  # Replace with the actual path
    search_image = Image.open(search_image_path)
    search_image = search_image.resize((1070, 540), Image.ANTIALIAS)
    search_background_photo = ImageTk.PhotoImage(search_image)
    search_background_label.configure(image=search_background_photo)
    search_background_label.image = search_background_photo

    search_book_label = tk.Label(frame_lhs, text="Search Book", font=("Arial", 30, "bold"), bg="deep sky blue")
    search_book_label.place(x=250, y=40)

    book_name_label = tk.Label(frame_lhs, text="Enter the Book Name", font=("Arial", 15, "bold"), bg="deep sky blue")
    book_name_label.place(x=220, y=140)

    book_entry = tk.Entry(frame_lhs, bg="gray", fg="black")
    book_entry.place(x=220, y=175, width=300)

    search_button = tk.Button(frame_lhs, text='Search', font=("Arial", 12), bd=2, cursor="hand2", bg="gray", fg="black", command=lambda: SearchFunction(book_entry, frame_lhs, root))
    search_button.place(x=310, y=215, width=100)
def SearchFunction(book_entry, frame_lhs, window):
    if book_entry.get() == "":
        messagebox.showerror("Error!", "Please Enter the Book Name", parent=window)
    else:
        try:
            curs.execute("select * from books where bookname like %s", ("%" + book_entry.get() + "%",))
            rows = curs.fetchall()
            if not rows:
                messagebox.showinfo("Database Empty", "There is no data to show", parent=window)

                # Create and configure the Treeview widget 
            tree_x = ttk.Scrollbar(frame_lhs, orient=tk.HORIZONTAL)
            tree_y = ttk.Scrollbar(frame_lhs, orient=tk.VERTICAL)
            tree = ttk.Treeview(frame_lhs, columns=cs.columns, height=400, selectmode="extended", yscrollcommand=tree_y.set, xscrollcommand=tree_x.set)
            tree_y.config(command=tree.yview)
            tree_y.pack(side=tk.LEFT, fill=tk.Y)
            tree_x.config(command=tree.xview)
            tree_x.pack(side=tk.BOTTOM, fill=tk.X)

                # Table headings
            tree.heading('book_id', text='Book ID', anchor=tk.W)
            tree.heading('book_name', text='Book Name', anchor=tk.W)
            tree.heading('author', text='Author', anchor=tk.W)
            tree.heading('edition', text='Edition', anchor=tk.W)
            tree.heading('price', text='Price', anchor=tk.W)
            tree.heading('qty', text='Quantity', anchor=tk.W)
            tree.pack()

            #another way to enumerate one by one
            for row in rows:
                tree.insert("", 'end', values=(row[0], row[1], row[2], row[3], row[4], row[5]))

        except Exception as e:
            messagebox.showerror("Error!", f"Error due to {str(e)}", parent=window)
 

def IssueBookGUI(): #Issue window
    ClearScreen()
    hide_title_label()

    borrow_background_label = tk.Label(frame_lhs)
    borrow_background_label.place(x=0, y=0, relwidth=1, relheight=1)

    borrow_image_path = "/Users/AmitSood/Documents/borrow.jpeg"  # Replace with the actual path
    borrow_image = Image.open(borrow_image_path)
    borrow_image = borrow_image.resize((1070, 540), Image.ANTIALIAS)
    borrow_background_photo = ImageTk.PhotoImage(borrow_image)
    borrow_background_label.configure(image=borrow_background_photo)
    borrow_background_label.image = borrow_background_photo

    book_id = tk.Label(frame_lhs, text="Book Id", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220, y=30)
    idi_entry = tk.Entry(frame_lhs, bg=cs.color_4, fg=cs.color_3)
    idi_entry.place(x=220, y=60, width=300)

    book_name = tk.Label(frame_lhs, text="Book Name", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220, y=100)
    booknamei_entry = tk.Entry(frame_lhs, bg=cs.color_4, fg=cs.color_3)
    booknamei_entry.place(x=220, y=130, width=300)

    student_roll = tk.Label(frame_lhs, text="Student Roll No.", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220, y=170)
    roll_entry = tk.Entry(frame_lhs, bg=cs.color_4, fg=cs.color_3)
    roll_entry.place(x=220, y=200, width=300)

    student_name = tk.Label(frame_lhs, text="Student Name", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220, y=240)
    name_entry = tk.Entry(frame_lhs, bg=cs.color_4, fg=cs.color_3)
    name_entry.place(x=220, y=270, width=300)

    issue_date = tk.Label(frame_lhs, text="Issue Date", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220, y=310)
    issue_entry = tk.Entry(frame_lhs, bg=cs.color_4, fg=cs.color_3)
    issue_entry.place(x=220, y=340, width=300)

    return_date = tk.Label(frame_lhs, text="Return Date", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220, y=380)
    return_entry = tk.Entry(frame_lhs, bg=cs.color_4, fg=cs.color_3)
    return_entry.place(x=220, y=410, width=300)

    submit_bt_1 = tk.Button(frame_lhs, text='Submit', font=(cs.font_1, 12), bd=2, command=lambda: Submit_Issue(idi_entry.get(), booknamei_entry.get(), name_entry.get(), roll_entry.get(), issue_entry.get(), return_entry.get()), cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=310, y=459, width=100)
    show_books = tk.Button(frame_lhs, text='Display all books', font=(cs.font_1, 12), bd=2, command=ShowBooksGUI, cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=510, y=459, width=100)
    return idi_entry.upper(), booknamei_entry.upper(), name_entry.upper(), roll_entry, issue_entry, return_entry
def Submit_Issue(idi_entry, booknamei_entry, name_entry, roll_entry, issue_entry, return_entry):
    if idi_entry == "" or booknamei_entry == "" or name_entry == "" or roll_entry == "" or issue_entry == "" or return_entry == "":
        messagebox.showerror("Error!", "Sorry, all fields are required", parent=root)
    else:
        try:
            curs.execute("select * from books where bookid=%s", (idi_entry,))
            row = curs.fetchone()
            if row == None:
                messagebox.showerror("Error!", "This book does not exist.", parent=root)
                
            if row[1] != booknamei_entry.upper():
                messagebox.showerror("Error!", "Book name does not match existing book id.", parent=root)

            else: 
                book_quantity = row[5]     
                if issue_entry > return_entry: 
                    messagebox.showerror("Error!", "Return date must be higher than issue date", parent=root)
                else:
                    curs.execute("insert into records (bookid,bookname,studentroll,studentname,issuedt,returndt) values(%s,%s,%s,%s,%s,%s)",
                                    (
                                        idi_entry,
                                        booknamei_entry.upper(),
                                        roll_entry,
                                        name_entry.upper(),
                                        issue_entry,
                                        return_entry
                                    ))
                    book_quantity-=1
                    curs.execute("update books set quantity=%s where bookid=%s", (book_quantity, idi_entry))
                    connection.commit()
                    messagebox.showinfo('Done!', "The data has been submitted")

        except Exception as e:
            messagebox.showerror("Error!", f"Error due to {str(e)}", parent=root)

def ReturnBookGUI(): #Return window
    hide_title_label()
    ClearScreen()
    
    borrow_background_label = tk.Label(frame_lhs)
    borrow_background_label.place(x=0, y=0, relwidth=1, relheight=1)

    borrow_image_path = "/Users/AmitSood/Documents/returnbook.jpeg"  # Replace with the actual path
    borrow_image = Image.open(borrow_image_path)
    borrow_image = borrow_image.resize((1070, 540), Image.ANTIALIAS)
    borrow_background_photo = ImageTk.PhotoImage(borrow_image)
    borrow_background_label.configure(image=borrow_background_photo)
    borrow_background_label.image = borrow_background_photo

    return_book_label = tk.Label(frame_lhs, text="Return Book", font=("Arial", 30, "bold"), bg="lightgray")
    return_book_label.place(x=250, y=40)

    roll_no_label = tk.Label(frame_lhs, text="Enter Student Roll No.", font=("Arial", 15, "bold"), bg="deep sky blue")
    roll_no_label.place(x=210, y=140)

    roll_no_entry = tk.Entry(frame_lhs, bg="gray", fg="black")
    roll_no_entry.place(x=210, y=175, width=300)

    search_button = tk.Button(frame_lhs, text='Search', font=("Arial", 12), bd=2, cursor="hand2", bg="gray", fg="black", command=lambda: ShowRecordsforReturn(roll_no_entry.get(), frame_lhs)) #add , , 
    search_button.place(x=210, y=215, width=100)
    show_books = tk.Button(frame_lhs, text='Display book holders', font=(cs.font_1, 12), bd=2, command=BookHoldersGUI_Func,  cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=410, y=215, width=150)
    
    return roll_no_entry

def ShowRecordsforReturn(roll_no_entry, frame_lhs): #Returnable records
    if roll_no_entry == "":
        messagebox.showerror("Error!", "Please enter a roll no.")
    else:
        try:
            curs.execute("select * from records where studentroll=%s", (roll_no_entry, ))
            rows = curs.fetchall()

            if len(rows) == 0:
                messagebox.showerror("Error!", "This roll no. doesn't exist", parent=root)
            else:
                ClearScreen()

                # Defining two scrollbars
                scroll_x = ttk.Scrollbar(frame_lhs, orient=tk.HORIZONTAL)
                scroll_y = ttk.Scrollbar(frame_lhs, orient=tk.VERTICAL)
                tree_1 = ttk.Treeview(frame_lhs, columns=cs.columns_1, height=400, selectmode="extended", yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
                scroll_y.config(command=tree_1.yview)
                # vertical scrollbar: left side
                scroll_y.pack(side=tk.LEFT, fill=tk.Y)
                scroll_x.config(command=tree_1.xview)
                # Horizontal scrollbar: at bottom
                scroll_x.pack(side=tk.BOTTOM, fill=tk.X)

                # Table headings
                tree_1.heading('book_id', text='Book ID', anchor=tk.W)
                tree_1.heading('book_name', text='Book Name', anchor=tk.W)
                tree_1.heading('student_roll', text='Student Roll', anchor=tk.W)
                tree_1.heading('student_name', text='Student Name', anchor=tk.W)
                tree_1.heading('issue_date', text='Issue Date', anchor=tk.W)
                tree_1.heading('return_date', text='Return Date', anchor=tk.W)

                tree_1.pack()
                tree_1.bind('<Double-Button-1>', OnSelectedforReturn) #function called on double clicking
                for list in rows:
                    tree_1.insert("", 'end', text=(rows.index(list) + 1), values=(list[0], list[1], list[2], list[3], list[4], list[5]))
        except Exception as e:
            messagebox.showerror("Error!", f"Error due to {str(e)}", parent=root)

def OnSelectedforReturn(event): #Selecting required record
    try:
        tree_1 = event.widget  # Get the Treeview widget that triggered the event
        selection = tree_1.selection()   
        
        if selection:
            item = tree_1.item(selection)
            row = item['values']      #creating delete button #return book called after deletion
            delete_button = tk.Button(frame_3, text='Remove record', font=(cs.font_1, 12), bd=2, command=lambda r=row: ReturningBook(tree_1, r, delete_button), cursor="hand2", bg=cs.color_2, fg=cs.color_3)
            delete_button.place(x=50, y=0, width=100)
        else:
            messagebox.showerror("Error!", "No item selected", parent=root)
    except Exception as e:
        messagebox.showerror("Error!", f"Error due to {str(e)}", parent=root)
def ReturningBook(tree_1, row, delete_button): #Deletion of book
    try:
        status = messagebox.askokcancel('Returning Book', 'Are you sure you want to proceed?')
        if status:
            curs.execute("delete from records where bookid=%s", (row[0],))
            curs.execute("select * from books where bookid=%s", (row[0],))
            var = curs.fetchone()

            book_count = var[5]
            book_count += 1

            curs.execute("update books set quantity=%s where bookid=%s", (book_count, row[0]))

            connection.commit()
            messagebox.showinfo("Success!", "Thanks for returning the book!")
            tree_1.delete(*tree_1.selection())  # Remove the selected item from the Treeview
            delete_button.destroy()  # Destroy the delete button
            ClearScreen()
    except Exception as e:
        messagebox.showerror("Error!", f"Error due to {str(e)}", parent=root)




#main buttons #move up to widgets
add_book = tk.Button(frame_rhs, text='Add Book', font=(cs.font_1, 12), bd=2, command=AddNewBookGUI, cursor="hand2", bg=cs.color_2, fg=cs.color_3, width = 15, height = 3)
add_book.place(x=180, y=100, width=100)

BookHolders_button = tk.Button(frame_rhs, text='Book Holders', font=("Arial", 12), bd=2, command=BookHoldersGUI_Func, cursor="hand2", bg="gray", fg="black", width = 15, height = 3)
BookHolders_button.place(x=180, y=40, width=100 )

return_book_button = tk.Button(frame_rhs, text='Return Book', font=("Arial", 12), bd=2, command=ReturnBookGUI, cursor="hand2", bg="gray", fg="black", width = 15, height = 3)
return_book_button.place(x=180, y=160, width=100)

issue_book_button = tk.Button(frame_rhs, text='Issue Book', font=("Arial", 12), bd=2, command=IssueBookGUI, cursor="hand2", bg="gray", fg="black", width = 15, height = 3)
issue_book_button.place(x=50, y=160, width=100)

search_book_button = tk.Button(frame_rhs, text='Search Book', font=("Arial", 12), bd=2, command=SearchGUI, cursor="hand2", bg="gray", fg="black", width = 15, height = 3) 
search_book_button.place(x=50, y=100, width=100)

all_books_button = tk.Button(frame_rhs, text='All Books', font=("Arial", 12), bd=2, command=ShowBooksGUI, cursor="hand2", bg="gray", fg="black", width = 15, height = 3)
all_books_button.place(x=50, y=40, width=100)
#initialising
root.mainloop()