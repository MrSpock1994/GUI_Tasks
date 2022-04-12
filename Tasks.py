import sqlite3
from tkinter import *
from tkinter import ttk

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

root = Tk()
root.title("Tasks Control")
root.geometry("320x440")


def insert_task():
    conn = sqlite3.connect("Tasks.db")
    cursor = conn.cursor()
    insert_data = [l1insert_window_name.get(), l2insert_window_date.get(), l3insert_window_colleague.get(),
                   select_status.get()]
    cursor.execute("INSERT INTO tasks VALUES (?, ?, ?, ?) ", insert_data)
    conn.commit()
    conn.close()
    l1insert_window_name.delete(0, END)
    l2insert_window_date.delete(0, END)
    l3insert_window_colleague.delete(0, END)


def update_task():
    conn = sqlite3.connect("Tasks.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET tasks = ?, start_date = ?, colleagues = ?, status = ? WHERE oid = ?",
                   [l1update_window_name.get(), l2update_window_date.get(), l3update_window_colleague.get(),
                    l4update_window_status.get(), update_task_id_get.get()])
    conn.commit()
    conn.close()
    update_window.destroy()


def window_update():
    global update_window
    update_window = Toplevel()
    update_window.title("Update Task")
    conn = sqlite3.connect("Tasks.db")
    cursor = conn.cursor()
    cursor.execute("SELECT *, oid FROM tasks Where oid = " + update_task_id_get.get())
    record = cursor.fetchall()
    global l1update_window_name
    global l2update_window_date
    global l3update_window_colleague
    global l4update_window_status
    l1update_window = Label(update_window, text="Task ->")
    l1update_window.grid(row=1, column=0)
    l1update_window_name = Entry(update_window, width=30)
    l1update_window_name.insert(0, record[0][0])
    l1update_window_name.grid(row=1, column=1, padx=20)
    l2update_window = Label(update_window, text="Date ->")
    l2update_window.grid(row=2, column=0)
    l2update_window_date = Entry(update_window, width=30)
    l2update_window_date.insert(0, record[0][1])
    l2update_window_date.grid(row=2, column=1, padx=20)
    l3update_window = Label(update_window, text="Colleague ->")
    l3update_window.grid(row=3, column=0)
    l3update_window_colleague = Entry(update_window, width=30)
    l3update_window_colleague.insert(0, record[0][2])
    l3update_window_colleague.grid(row=3, column=1, padx=20)
    l4update_window = Label(update_window, text="Status ->")
    l4update_window.grid(row=4, column=0)
    l4update_window_status = Entry(update_window, width=30)
    l4update_window_status.insert(0, record[0][3])
    l4update_window_status.grid(row=4, column=1, padx=20)
    btn_update_info = ttk.Button(update_window, text="Submit", command=update_task)
    btn_update_info.grid(row=5, column=0, columnspan=3, pady=5, sticky="ew")


def window_insert():
    insert_window = Toplevel()
    insert_window.title("Insert Task")
    global l1insert_window_name
    global l2insert_window_date
    global l3insert_window_colleague
    global select_status
    status = ["Ongoing", "Finished", "Stopped"]
    select_status = StringVar()
    l4insert_window = ttk.Label(insert_window, text="Status ->")
    l4insert_window.grid(row=4, column=0)
    drop = ttk.OptionMenu(insert_window, select_status, status[0], *status)
    drop.grid(row=4, column=1)
    l1insert_window = ttk.Label(insert_window, text="Task ->")
    l1insert_window .grid(row=1, column=0)
    l1insert_window_name = ttk.Entry(insert_window, width=30)
    l1insert_window_name.grid(row=1, column=1, padx=20)
    l2insert_window = ttk.Label(insert_window, text="Start Date ->")
    l2insert_window.grid(row=2, column=0)
    l2insert_window_date = ttk.Entry(insert_window, width=30)
    l2insert_window_date.grid(row=2, column=1, padx=20)
    l3insert_window = ttk.Label(insert_window, text="Colleague ->")
    l3insert_window.grid(row=3, column=0)
    l3insert_window_colleague = ttk.Entry(insert_window, width=30)
    l3insert_window_colleague.grid(row=3, column=1, padx=20)
    btn_insert2 = ttk.Button(insert_window, text="Submit", command=insert_task)
    btn_insert2.grid(row=5, column=0, columnspan=2)


def show_finished():
    conn = sqlite3.connect("Tasks.db")
    cursor = conn.cursor()
    show_finished_tasks = Toplevel()
    show_finished_tasks.title("Finished Tasks")
    cursor.execute("SELECT *, oid FROM tasks WHERE status = 'Finished'")
    records = cursor.fetchall()
    print_records = ''
    for record in records:
        print_records += str(record) + "\n"
    query_label = ttk.Label(show_finished_tasks, text=print_records)
    query_label.grid(row=2, column=0, columnspan=2)
    conn.commit()
    conn.close()


def show_currently():
    conn = sqlite3.connect("Tasks.db")
    cursor = conn.cursor()
    show_currently_tasks = Toplevel()
    show_currently_tasks.title("Currently Tasks")
    cursor.execute("SELECT *, oid FROM tasks WHERE status = 'Ongoing'")
    records = cursor.fetchall()
    print_records = ''
    for record in records:
        print_records += str(record) + "\n"
    query_label = ttk.Label(show_currently_tasks, text=print_records)
    query_label.grid(row=1, column=0, columnspan=2)
    conn.commit()
    conn.close()


def show_stopped():
    conn = sqlite3.connect("Tasks.db")
    cursor = conn.cursor()
    show_stopped_tasks = Toplevel()
    show_stopped_tasks.title("Stopped Tasks")
    cursor.execute("SELECT *, oid FROM tasks WHERE status = 'Stopped'")
    records = cursor.fetchall()
    print_records = ''
    for record in records:
        print_records += str(record) + "\n"
    query_label = ttk.Label(show_stopped_tasks, text=print_records)
    query_label.grid(row=2, column=0, columnspan=2)
    conn.commit()
    conn.close()


def show_all():
    conn = sqlite3.connect("Tasks.db")
    cursor = conn.cursor()
    show_all_tasks = Toplevel()
    show_all_tasks.title("All Tasks")
    cursor.execute("SELECT *, oid FROM tasks")
    records = cursor.fetchall()
    print_records = ''
    for record in records:
        print_records += str(record) + "\n"
    query_label = ttk.Label(show_all_tasks, text=print_records)
    query_label.grid(row=2, column=0, columnspan=2)
    conn.commit()
    conn.close()


def delete_task():
    conn = sqlite3.connect("Tasks.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE oid = " + del_task_id_get.get())
    conn.commit()
    conn.close()
    del_task_id_get.delete(0, END)


def delete_all_task():
    conn = sqlite3.connect("Tasks.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks")
    conn.commit()
    conn.close()


btn_insert1 = ttk.Button(root, text="Insert new task", command=window_insert)
btn_insert1.grid(row=0, column=2, columnspan=3, pady=5, sticky="ew")

btn_show_currently = ttk.Button(root, text="Show currently tasks", command=show_currently)
btn_show_currently.grid(row=1, column=2, columnspan=3, pady=5, sticky="ew")

btn_show_stopped = ttk.Button(root, text="Show stopped tasks", command=show_stopped)
btn_show_stopped.grid(row=2, column=2, columnspan=3, pady=5, sticky="ew")

btn_show_finished = ttk.Button(root, text="Show finished tasks", command=show_finished)
btn_show_finished.grid(row=3, column=2, columnspan=3, pady=5, sticky="ew")

del_task_id = ttk.Label(root, text="Insert below the id you want to delete")
del_task_id.grid(row=4, column=2, columnspan=3, pady=5, sticky="ew")
del_task_id_get = ttk.Entry(root, width=10)
del_task_id_get.grid(row=5, column=2, columnspan=3)
btn_delete = ttk.Button(root, text="Delete", command=delete_task)
btn_delete.grid(row=6, column=2, columnspan=3, pady=5, sticky="ew")

update_task_id = ttk.Label(root, text="Insert below the id you want to update")
update_task_id.grid(row=7, column=2, columnspan=3, pady=5, sticky="ew")
update_task_id_get = ttk.Entry(root, width=10)
update_task_id_get.grid(row=8, column=2, columnspan=3)
btn_update = ttk.Button(root, text="Update", command=window_update)
btn_update.grid(row=9, column=2, columnspan=3, pady=5, sticky="ew")

btn_show_all = ttk.Button(root, text="Show all tasks", command=show_all)
btn_show_all.grid(row=10, column=2, columnspan=3, pady=5, sticky="ew")

btn_delete_all = ttk.Button(root, text="Delete all tasks", command=delete_all_task)
btn_delete_all.grid(row=11, column=2, columnspan=3, pady=5, sticky="ew")


root.mainloop()
