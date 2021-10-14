import tkinter as tk
import PyPDF2
from PIL import Image,ImageTk
from tkinter.filedialog import askopenfile

root = tk.Tk() 

canvas =tk.Canvas(root,width=600,height=300,bg='#DEEEEA')
canvas.grid(columnspan=3,rowspan=3)

logo = Image.open('pdf.png')
logo =ImageTk.PhotoImage(logo)
logo_label = tk.Label(image = logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)


instruction = tk.Label(root,text='Select a PDF file to extract its text',font="Raleway")
instruction.grid(columnspan=3,column=0,row=1)


browse_text = tk.StringVar()
browse_btn = tk.Button(root,textvariable=browse_text,command=lambda:open_file(),font='Raleway',bg='#F54748',fg='white',height=2,width=15)
browse_text.set("Browse")
browse_btn.grid(column=1,row=2)

canvas =tk.Canvas(root,width=600,height=250,bg='#DEEEEA')
canvas.grid(columnspan=3)

def open_file():
    browse_text.set("Loading...")
    file = askopenfile(parent=root,mode='rb',title='Choose a file',filetype=[("Pdf file","*.pdf")])
    if file:
        read_pdf = PyPDF2.PdfFileReader(file)
        page = read_pdf.getPage(0)
        page_content = page.extractText()

        textbox = tk.Text(root, height=10,width=50,padx=15,pady=15)
        textbox.insert(1.0,page_content)
        textbox.tag_configure("center",justify="center")
        textbox.tag_add("center",1.0,"end")
        textbox.grid(column=1,row=3)
        browse_text.set("Browse")


root.mainloop()
