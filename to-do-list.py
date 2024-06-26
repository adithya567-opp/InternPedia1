import tkinter
from tkinter import*

root=Tk()
root.title("To-Do-List")
root.geometry("400x650+400+100")
root.resizable(False,False)

task_list= []

def addTask():
    task = task_entry.get()
    task_entry.delete(0,END)

    if task:
        with open("tasklist.txt",'a') as taskfile:
            taskfile.write("f\n(task)")
        task_list.append(task)
        listbox.insert(END,task)

def deleteTask():
    global task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt","w") as taskfie:
            for task in task_list:
                taskfie.write(task+"\n")

        listbox.delete(ANCHOR)

def openTaskFile():

    try:
        global task_list
        with open("tasklist.txt","r") as taskfile:
            tasks =taskfile.readlines()

        for task in tasks:
            if task != '\n':
                task_list.append(task)
                listbox.insert(END,task)
    except:
        file=open('tasklist.txt','w')
        file.close()
            
#icon
Image_icon=PhotoImage(file="image/task.png")
root.iconphoto(False,Image_icon)

#top bar
TopImage=PhotoImage(file="image/title.png")
Label(root,image=TopImage).pack()

dockImage = PhotoImage(file="image/document.png")

# Resize the image to 50% of its original size
dockImage = dockImage.subsample(2)  # Higher values will make the image smaller

Label(root, image=dockImage, bg="#ebebeb").place(x=5, y=55)

noteImage = PhotoImage(file="image/task.png")
noteImage = noteImage.subsample(6)

# Get the width and height of the window
window_width = root.winfo_width()
window_height = root.winfo_height()

# Calculate the x and y coordinates to place the image in the top-right corner
x = window_width - noteImage.width() - 5
y = 35

Label(root, image=noteImage, bg="#ebebeb").place(x=x, y=y)

heading=Label(root,text="ALL TASK",font="arial 20 bold",fg="black",bg="#ebebeb")
heading.place(x=110,y=80)

#main
frame = Frame(root,width=400,height=50,bg="white")
frame.place(x=0,y=180)

task = StringVar()
task_entry=Entry(frame,width=18,font="arial 20",bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()

button = Button(frame,text="ADD",font="arial 20 bold",width=6,bg="#ff3939",fg="#fff",bd=0,command=addTask)
button.place(x=300,y=0)

#listbox
center_frame = Frame(root, bd=3, width=700, height=280, bg="#32405b")
center_frame.pack(pady=(60, 0))

listbox = Listbox(center_frame, font=('arial', 12), width=40, height=16, bg="#32405b", fg="white", cursor="hand2", selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill=BOTH, padx=2)

scrollbar = Scrollbar(center_frame)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

bottom_frame = Frame(root, bg="#32405b")
bottom_frame.pack(pady=10)

openTaskFile()

#delete
delete_icon = PhotoImage(file="image\delete.png")
delete_icon = delete_icon.subsample(10)
delete_button = Button(bottom_frame, image=delete_icon, bd=0,command=deleteTask)
delete_button.pack(side=RIGHT, padx=10)

root.mainloop()







    
    
    
