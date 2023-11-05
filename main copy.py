import tkinter as tk
import mysql.connector as sql
from tkinter import ttk, messagebox
import customs as cs
from PIL import Image, ImageTk

# Define constants (replace with actual values)
host = "localhost"
user = "root"
password = "Root@123"
database = "library"
columns_1 = ("book_id", "book_name", "student_roll", "student_name", "course", "subject", "issue_date", "return_date")
connection = sql.connect(host=host, user=user, password=password, database=database)
curs = connection.cursor()

def ClearScreen():
    for widget in frame_lhs.winfo_children():
        widget.destroy()

def hide_title_label():
    title_label.place_forget()

def AllBorrowRecords(): #line 42
    ClearScreen()
    hide_title_label()
 
    # Create and configure the Treeview widget
    tree_x = ttk.Scrollbar(frame_lhs, orient=tk.HORIZONTAL)
    tree_y = ttk.Scrollbar(frame_lhs, orient=tk.VERTICAL)
    tree_1 = ttk.Treeview(frame_lhs, columns=columns_1, height=400, selectmode="extended", yscrollcommand=tree_y.set, xscrollcommand=tree_x.set)
    tree_y.config(command=tree_1.yview)
    tree_x.config(command=tree_1.xview)
    tree_x.pack(side=tk.BOTTOM, fill=tk.X)

    # Table headings
    for col in columns_1:
        tree_1.heading(col, text=col, anchor=tk.W)

    tree_1.pack()

    try:
        curs.execute("SELECT * FROM borrow_record") 
        rows = curs.fetchall()

        if not rows:
            messagebox.showinfo("Database Empty", "There is no data to show")
            connection.close()
        else:
            connection.close()
            # Populate the Treeview with fetched records
            for idx, row in enumerate(rows, start=1):
                tree_1.insert("", tk.END, text=idx, values=row)
    except Exception as e:
        messagebox.showerror("Error!", f"Error due to {str(e)}")

def AddNewBook():
    ClearScreen()
    hide_title_label()
    # Create labels, entry fields, and other widgets here
    book_id_label = tk.Label(frame_lhs, text="Book Id", font=("Arial", 15, "bold"), bg="deep sky blue")
    book_id_label.place(x=220, y=30)

    id_entry = tk.Entry(frame_lhs, bg="gray95", fg="black")
    id_entry.place(x=220, y=60, width=300)

    book_name_label = tk.Label(frame_lhs, text="Book Name", font=("Arial", 15, "bold"), bg="deep sky blue")
    book_name_label.place(x=220, y=100)

    bookname_entry = tk.Entry(frame_lhs, bg="gray95", fg="black")
    bookname_entry.place(x=220, y=130, width=300)

    # Create more widgets as needed

    submit_bt_1 = tk.Button(frame_lhs, text='Submit', font=("Arial", 12), bd=2, command=Submit, cursor="hand2", bg="gray", fg="black")
    submit_bt_1.place(x=310, y=459, width=100)

def ReturnBook(): #add , ShowRecordsforReturn
    hide_title_label()
    ClearScreen()
    return_book_label = tk.Label(frame_lhs, text="Return Book", font=("Arial", 30, "bold"), bg="lightgray")
    return_book_label.place(x=250, y=40)

    roll_no_label = tk.Label(frame_lhs, text="Enter the Book ID.", font=("Arial", 15, "bold"), bg="deep sky blue")
    roll_no_label.place(x=210, y=140)

    roll_no_entry = tk.Entry(frame_lhs, bg="gray", fg="black")
    roll_no_entry.place(x=210, y=175, width=300)

    search_button = tk.Button(frame_lhs, text='Search', font=("Arial", 12), bd=2, cursor="hand2", bg="gray", fg="black") #add , command=ShowRecordsforReturn, 
    search_button.place(x=310, y=215, width=100)

def Submit():
    # Handle the submission logic here
    pass

def Search(): #add , SearchBook
    ClearScreen()
    hide_title_label()
    search_book_label = tk.Label(frame_lhs, text="Search Book", font=("Arial", 30, "bold"), bg="deep sky blue")
    search_book_label.place(x=250, y=40)

    book_name_label = tk.Label(frame_lhs, text="Enter the Book Name", font=("Arial", 15, "bold"), bg="deep sky blue")
    book_name_label.place(x=220, y=140)

    book_entry = tk.Entry(frame_lhs, bg="gray", fg="black")
    book_entry.place(x=220, y=175, width=300)

    search_button = tk.Button(frame_lhs, text='Search', font=("Arial", 12), bd=2,cursor="hand2", bg="gray", fg="black") #add command=lambda: SearchBook(book_entry.get()) 
    search_button.place(x=310, y=215, width=100)

def IssueBook(BorrowBookAgain, row):
    ClearScreen()
    hide_title_label()
    tree_x = ttk.Scrollbar(frame_lhs, orient=tk.HORIZONTAL)
    tree_y = ttk.Scrollbar(frame_lhs, orient=tk.VERTICAL)
    tree_1 = ttk.Treeview(frame_lhs, columns=columns_1, height=400, selectmode="extended", yscrollcommand=tree_y.set, xscrollcommand=tree_x.set)
    tree_y.config(command=tree_1.yview)
    tree_x.config(command=tree_1.xview)
    tree_x.pack(side=tk.BOTTOM, fill=tk.X)
    selected_item = tree_1.selection()
    if selected_item:
        row = tree_1.item(selected_item[0])['values']
        # Use 'row' as needed
    else:
        messagebox.showinfo("No Selection", "Please select an item in the Treeview.")

    book_id_label = tk.Label(frame_lhs, text="Book Id", font=("Arial", 15, "bold"), bg="lightblue")
    book_id_label.place(x=130, y=30)

    id_label = tk.Label(frame_lhs, text=row[0], font=("Arial", 10))
    id_label.place(x=130, y=60, width=200)

    book_name_label = tk.Label(frame_lhs, text="Book Name", font=("Arial", 15, "bold"), bg="lightblue")
    book_name_label.place(x=400, y=30)

    book_name = tk.Label(frame_lhs, text=row[1], font=("Arial", 10))
    book_name.place(x=400, y=60, width=200)

    student_roll_label = tk.Label(frame_lhs, text="Student Roll", font=("Arial", 15, "bold"), bg="lightblue")
    student_roll_label.place(x=130, y=100)

    student_roll = tk.Label(frame_lhs, text=row[2], font=("Arial", 10))
    student_roll.place(x=130, y=130, width=200)

    student_name_label = tk.Label(frame_lhs, text="Student Name", font=("Arial", 15, "bold"), bg="lightblue")
    student_name_label.place(x=400, y=100)

    student_name = tk.Label(frame_lhs, text=row[3], font=("Arial", 10))
    student_name.place(x=400, y=130, width=200)

    course_label = tk.Label(frame_lhs, text="Course", font=("Arial", 15, "bold"), bg="lightblue")
    course_label.place(x=130, y=170)

    course = tk.Label(frame_lhs, text=row[4], font=("Arial", 10))
    course.place(x=130, y=200, width=200)

    subject_label = tk.Label(frame_lhs, text="Subject", font=("Arial", 15, "bold"), bg="lightblue")
    subject_label.place(x=400, y=170)

    subject = tk.Label(frame_lhs, text=row[5], font=("Arial", 10))
    subject.place(x=400, y=200, width=200)

    issue_date_label = tk.Label(frame_lhs, text="Issue Date", font=("Arial", 15, "bold"), bg="lightblue")
    issue_date_label.place(x=130, y=240)

    issue_date = tk.Label(frame_lhs, text=row[6], font=("Arial", 10))
    issue_date.place(x=130, y=270, width=200)

    return_date_label = tk.Label(frame_lhs, text="Return Date", font=("Arial", 15, "bold"), bg="lightblue")
    return_date_label.place(x=400, y=240)

    return_date_entry = tk.Entry(frame_lhs, bg="gray", fg="black")
    return_date_entry.insert(0, row[7])
    return_date_entry.place(x=400, y=270, width=200)

    submit_button = tk.Button(frame_lhs, text='Submit', font=("Arial", 12), bd=2, command=lambda: BorrowBookAgain(row), cursor="hand2", bg="gray", fg="black")
    submit_button.place(x=300, y=320, width=100)

def ShowBooks():
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

def BorrowBookAgain(return_date_entry, ClearScreen, row): #whole thing
    try:
        curs.execute("UPDATE borrow_record SET return_date=%s WHERE stu_roll=%s AND book_id=%s",
                     (
                         return_date_entry.get(),
                         row[2],
                         row[0]
                     ))
        messagebox.showinfo("Success!", "The book is issued again")
        connection.commit()
        connection.close()
        ClearScreen()
    except Exception as e:
        messagebox.showerror("Error!", f"Error due to {str(e)}")

root = tk.Tk()
root.title("Library Management System")
root.geometry("1070x540")

frame_lhs = tk.Frame(root, bg = "deep sky blue")
frame_lhs.place(x=0, y=0, width=740, relheight=1)
title_label = tk.Label(root, text="Library Management System", font=("Helvetica", 20), wraplength=600)
title_label.place(x=250, y=150)
title_label.lift()
image = Image.open("/Users/AmitSood/Documents/27315.jpg")  # Replace with your image file path
image = image.resize((1070, 540), Image.ANTIALIAS)
background_photo = ImageTk.PhotoImage(image)
background_label = tk.Label(frame_lhs, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


frame_rhs = tk.Frame(root, bg = "grey95")
frame_rhs.place(x=740, y=0, relwidth=1, relheight=1)

frame_3 = tk.Frame(frame_rhs, bg="gray95")
frame_3.place(x=0, y=300, relwidth=1, relheight=1)


add_book = tk.Button(frame_rhs, text='Add Book', font=(cs.font_1, 12), bd=2, command=AddNewBook, cursor="hand2", bg=cs.color_2, fg=cs.color_3)
add_book.place(x=180, y=100, width=100)

all_borrow_records_button = tk.Button(frame_rhs, text='Book Holders', font=("Arial", 12), bd=2, command=AllBorrowRecords, cursor="hand2", bg="gray", fg="black")
all_borrow_records_button.place(x=180, y=40, width=100 )

return_book_button = tk.Button(frame_rhs, text='Return Book', font=("Arial", 12), bd=2, command=ReturnBook, cursor="hand2", bg="gray", fg="black")
return_book_button.place(x=180, y=160, width=100)

issue_book_button = tk.Button(frame_rhs, text='Issue Book', font=("Arial", 12), bd=2, command=lambda: IssueBook(BorrowBookAgain, None), cursor="hand2", bg="gray", fg="black")
issue_book_button.place(x=50, y=160, width=100)

search_book_button = tk.Button(frame_rhs, text='Search Book', font=("Arial", 12), bd=2, command=Search, cursor="hand2", bg="gray", fg="black") # add  command=lambda: SearchBook(frame_lhs, ClearScreen, GetBookNametoSearch), 
search_book_button.place(x=50, y=100, width=100)

all_books_button = tk.Button(frame_rhs, text='All Books', font=("Arial", 12), bd=2, command=ShowBooks(), cursor="hand2", bg="gray", fg="black")
all_books_button.place(x=50, y=40, width=100)

root.mainloop()