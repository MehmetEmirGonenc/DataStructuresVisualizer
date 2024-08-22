import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("DS Diagrams")
root.geometry("700x600")

def show_stack():
    # Canvas üzerinde stack modelini göster
    canvas.delete("all")
    canvas.create_text(200, 200, text="Stack Model", font=('Helvetica', 16))

def show_queue():
    # Canvas üzerinde queue modelini göster
    canvas.delete("all")
    canvas.create_text(200, 200, text="Queue Model", font=('Helvetica', 16))

def show_linkedlist():
    # Canvas üzerinde tree modelini göster
    canvas.delete("all")
    canvas.create_text(200, 200, text="Linked List Model", font=('Helvetica', 16))

def add_model():
    model = entry_add.get()
    # Model ekleme işlemi burada yapılabilir
    
def remove_model():
    model = entry_remove.get()
    # Model silme işlemi burada yapılabilir
  
# Create a frame for the fixed upper section
top_frame = tk.Frame(root, height=80, bg="lightgray",relief="solid",borderwidth="2")
top_frame.pack(fill="x", side="top")

# Example content for the fixed frame (e.g., a label)
# top_Frame = tk.Label(top_Frame, text="Permanent Upper Section", bg="lightgray")
# top_Frame.pack(pady=20)

btn_stack = tk.Button(top_frame, text="Stack", command=show_stack)
btn_stack.pack(side=tk.LEFT,padx=(0,20))

btn_queue = tk.Button(top_frame, text="Queue", command=show_queue)
btn_queue.pack(side=tk.LEFT,padx=(0,20))

btn_tree = tk.Button(top_frame, text="Linked List", command=show_linkedlist)
btn_tree.pack(side=tk.LEFT,padx=(0,20))

# Create a frame for the left section
leftFrame = tk.Frame(root, width=600, bg="lightgray",relief="solid",borderwidth="2")
leftFrame.pack(fill="y", side="left")

# Example content for the fixed frame (e.g., a label)
left_frame = tk.Label(leftFrame, bg="lightgray")
left_frame.pack(pady=200)

# Sol kısım (Ekleme ve silme işlemlerinin bulunduğu sabit bölüm)

entry_add = tk.Entry(left_frame)
entry_add.pack()

btn_add = tk.Button(left_frame, text="Add", command=add_model)
btn_add.pack(pady=(0,20))

entry_remove = tk.Entry(left_frame)
entry_remove.pack()

btn_remove = tk.Button(left_frame, text="Remove", command=remove_model)
btn_remove.pack()

middle_frame = tk.Frame(root)
middle_frame.pack( fill=tk.BOTH, expand=True)

canvas = tk.Canvas(root)
canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Alt kısım için çerçeve oluştur
verticalScroll = tk.Frame(middle_frame)
verticalScroll.pack(fill="both", expand=True, side="bottom")

# Kaydırma özelliği için bir canvas ekle
verticalCanvas = tk.Canvas(verticalScroll)
verticalCanvas.pack(side="left", fill="both", expand=True)

# Dikey kaydırma çubuğunu ekle
v_scrollbar = ttk.Scrollbar(verticalScroll, orient="vertical", command=verticalCanvas.yview)
v_scrollbar.pack(side="left", fill="y")

# Yatay kaydırma çubuğunu ekle
h_scrollbar = ttk.Scrollbar(middle_frame, orient="horizontal", command=verticalCanvas.xview)
h_scrollbar.pack(side="top", fill="x")

# Canvas'ı kaydırma çubuklarıyla yapılandır
verticalCanvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
verticalCanvas.bind('<Configure>', lambda e: verticalCanvas.configure(scrollregion=verticalCanvas.bbox("all")))

# Canvas içinde kaydırılabilir içerik çerçevesi oluştur
vScroll_content = tk.Frame(verticalCanvas)

# Kaydırılabilir içerik çerçevesini canvas'a ekle
verticalCanvas.create_window((0, 0), window=vScroll_content, anchor="sw")

# # Test amacıyla birkaç örnek widget ekleyelim
for i in range(20):
    middle_frame=tk.Label(vScroll_content, text=f"Label {i+1}").grid(row=i, column=0, padx=10, pady=10)

for j in range(10):
   middle_frame=tk.Label(vScroll_content, text=f"Horizontal {j+1}").grid(row=0, column=j, padx=10, pady=10)


# Run the application
root.mainloop()