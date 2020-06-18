from tkinter import Tk, Canvas, Label, Frame,Entry, Button, W, E, Listbox, END
import psycopg2

root = Tk()
root.title("Python & PostgreSQL")

#funciones
#conexion a BD
#create
def save_new_student(name, age, adress):
    conn = psycopg2.connect(
        dbname="postgres",
        user ="postgres",
        password="8912", 
        host="localhost",
        port = "5432"
    )

    #cursor y sentencia SQL
    cursor = conn.cursor()
    query = '''INSERT INTO students(name, address, age) VALUES (%s, %s, %s)'''
    cursor.execute(query, (name, adress, age))
    print("Saved")
    conn.commit()
    conn.close()
    display_students()


#Read
def display_students():
    conn = psycopg2.connect(
        dbname="postgres",
        user ="postgres",
        password="8912", 
        host="localhost",
        port = "5432"
    )
    #cursor y sentencia SQL
    cursor = conn.cursor()
    query = '''SELECT * FROM students'''
    cursor.execute(query)

    row = cursor.fetchall()
    listbox = Listbox(frame,width=20, height=5) 
    listbox.grid(row=10, columnspan=4, sticky=W+E)

    for x in row:
        listbox.insert(END, x)

    conn.commit()
    conn.close()
    #refresh dates
   
#Search
def search(id):
    conn = psycopg2.connect(
        dbname="postgres",
        user ="postgres",
        password="8912", 
        host="localhost",
        port = "5432"
    )
    #cursor y sentencia SQL
    cursor = conn.cursor()
    query = '''SELECT * FROM students WHERE id=%s'''
    cursor.execute(query, (id))

    row = cursor.fetchone()

    
    display_search_result(row)
    conn.commit()
    conn.close()
    
def display_search_result(row):
    listbox = Listbox(frame, width=20, height=1)
    listbox.grid(row=9, columnspan=4, sticky=W+E)
    listbox.insert(END, row)


#canvas, contenedor para elementos
canvas = Canvas(root, height=500, width=500)
canvas.pack()

#crear elementos
frame = Frame()
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

label = Label(frame, text ='Texto Cabecera')
label.grid(row=0, column=1)


#Name Input
label = Label(frame, text="Name:")
label.grid(row=1, column=0)
entry_name = Entry(frame)
entry_name.grid(row=1, column=1)

#Age Input
label = Label(frame, text="Age:")
label.grid(row=2, column=0)
entry_age = Entry(frame)
entry_age.grid(row=2, column=1)

#Adress Input
label = Label(frame, text="Adress:")
label.grid(row=3, column=0)
entry_adress = Entry(frame)
entry_adress.grid(row=3, column=1)

#button -> command para ejecutar funcion
button = Button(frame, text='Add', command=lambda:save_new_student(
    entry_name.get(),
    entry_age.get(),
    entry_adress.get()

))
button.grid(row=4, column=1, sticky=W+E )

#SEARCH
label = Label(frame, text = "Search data")
label.grid(row = 5, column = 1)

label = Label(frame, text="Search By ID")
label.grid(row=6, column=0)

id_search = Entry(frame)
id_search.grid(row=6, column=1)

button = Button(frame, text="Search", command=lambda:search(id_search.get()))
button.grid(row=6, column=2)



#mostrar dato
display_students()

# inicializar
root.mainloop()

