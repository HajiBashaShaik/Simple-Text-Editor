import tkinter as tk
from tkinter import filedialog,messagebox

#Main window Code

root=tk.Tk()
root.title("Simple Text Editor")
root.geometry("800x600")

#create text area

text=tk.Text(
    root,
    wrap=tk.WORD,
    font=("Times New Roman",12)
)

text.pack(expand=True,fill=tk.BOTH)

#Main Logic

#Function-1 : To Create New File

def new_file():
    text.delete(1.0, tk.END)

#Function-2 : Open New File

def open_file():
    #open file dialogue
    file_path=filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Files","*.txt")]
    )

    if file_path:
        #open selected file
        with open(file_path,"r") as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())

#Function-3 : Save the File

def save_file():
    file_path=filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files","*.txt")]       
    )

    if file_path:
        with open(file_path,"w") as file:
            file.write(text.get(1.0, tk.END))

    messagebox.showinfo("Info", "File saved Sucessfully")

#Menu Bar

menu=tk.Menu(root)
root.config(menu=menu)
file_menu=tk.Menu(menu,tearoff=0)

# New File, Open File, Save File, Exit

menu.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
#Starts and keep Window Open
root.mainloop() 