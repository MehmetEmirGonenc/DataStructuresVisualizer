import tkinter as tk
from tkinter import ttk
from DSalgorithms import LinkedList 
from DSalgorithms import Stack
from DSalgorithms import Queue

# Create the main window
root = tk.Tk()
root.title("DS Diagrams")
root.geometry("700x600")

def show_linkedlist():
    #clean middle_framee and left_frame
    middle_framee.delete("all")
    for widget in left_frame.winfo_children():
        widget.destroy()
    for widget in middle_framee.winfo_children():
        widget.destroy()
        break
    
    # Linked list object created
    ll_object = LinkedList()
    
    # Validation function to avoid from character that aren't numeric
    def validate_input(input):
        if input == "" or input.isdigit() or input[0] == '-':
            return True
        else:
            return False
        
    vcmd = (root.register(validate_input), '%P')
    
    def visualize_list (ordered_list): ## Organize!!
        top_gap = 25
        left_gap = 25
        box_width = 50
        box_height = 50
        box_gap = 50
        
        middle_framee.delete("all")
        gap_num = 0
        for i in range(len(ordered_list)):
            middle_framee.create_rectangle(left_gap + box_width * i + box_gap * gap_num, top_gap, left_gap + box_width * (i+1) + box_gap * gap_num, top_gap + box_height, outline="black", fill="lightblue")
            middle_framee.create_text(left_gap + box_width * i + box_gap * gap_num + (box_width/2), top_gap + (box_height/2), text=ordered_list[i], font=("Arial", 12))
            
            if i < len(ordered_list)-1:
                arrow_x0 = left_gap + box_width * (i+1) + box_gap * gap_num
                arrow_x1 = left_gap + box_width * (i+1) + box_gap * (gap_num+1)
                arrow_y0 = top_gap + box_height/2
                arrow_y1 = top_gap + box_height/2
            
                middle_framee.create_line(arrow_x0, arrow_y0, arrow_x1, arrow_y1 , arrow=tk.LAST,width=3, arrowshape=(10, 10, 5), fill="black")
                gap_num +=1
    
    # Linked list process function
    def linked_list_process(list, func, button):
        """
        list -> LinkedList object
        func -> LinkedList function (insert_begin, insert_end, remove_node)
        button -> tkinter object (button)
        """
        user_input = button.get()
        if user_input != "":
            func(list, int(user_input))
            visualize_list(list.get_list())
        button.delete(0, tk.END)
    
    #add element to begin
    entry_addBeginL = tk.Entry(left_frame, validate="key", validatecommand=vcmd)
    entry_addBeginL.pack()
    btn_addBeginL = tk.Button(left_frame, text="Add begin", command=lambda: linked_list_process(ll_object, LinkedList.insert_begin, entry_addBeginL))
    btn_addBeginL.pack(pady=(0,20))
    
    #add elemen to end
    entry_addEndL = tk.Entry(left_frame, validate="key", validatecommand=vcmd)
    entry_addEndL.pack()
    btn_addEndL = tk.Button(left_frame, text="Add End", command=lambda: linked_list_process(ll_object, LinkedList.insert_end, entry_addEndL))
    btn_addEndL.pack(pady=(0,20))
    
    #remove element
    entry_removeL = tk.Entry(left_frame, validate="key", validatecommand=vcmd)
    entry_removeL.pack()
    btn_removeL = tk.Button(left_frame, text="Remove", command=lambda: linked_list_process(ll_object, LinkedList.remove_node, entry_removeL))
    btn_removeL.pack()
    
    # middle_framee.delete("all")
    # elements = LinkedList.get_list()
    # x, y = 10, 10
    # box_width, box_height = 50, 30
    # for i, element in enumerate(elements):
    #     middle_framee.create_rectangle(x, y, x + box_width, y + box_height, outline="black")
    #     middle_framee.create_text(x + box_width // 2, y + box_height // 2, text=str(element))
    #     if i < len(elements) - 1:
    #         middle_framee.create_line(x + box_width, y + box_height // 2, x + box_width + 20, y + box_height // 2, arrow=tk.LAST)
    #     x += box_width + 30

def show_stack():
    #clean middle_framee and left_frame
    middle_framee.delete("all")
    for widget in left_frame.winfo_children():
     widget.destroy()
    
    #add element to end
    entry_addS = tk.Entry(left_frame)
    entry_addS.pack()
    btn_addS = tk.Button(left_frame, text="Push", command=Stack.push)
    btn_addS.pack(pady=(0,20))
    
    #remove last element 
    entry_removeS = tk.Entry(left_frame)
    entry_removeS.pack()
    btn_removeS = tk.Button(left_frame, text="Pop", command=Stack.pop)
    btn_removeS.pack()   

def show_queue():
    #clean middle_framee and left_frame
    middle_framee.delete("all")
    for widget in left_frame.winfo_children():
     widget.destroy()
    
    #add element to end
    entry_addQ = tk.Entry(left_frame)
    entry_addQ.pack()
    btn_addQ = tk.Button(left_frame, text="Enqueue", command=Queue.enqueue)
    btn_addQ.pack(pady=(0,20))
    
    #remove the first element
    entry_removeQ = tk.Entry(left_frame)
    entry_removeQ.pack()
    btn_removeQ = tk.Button(left_frame, text="Dequeue", command=Queue.dequeue)
    btn_removeQ.pack()
    
# Create a frame for the fixed upper section
top_frame = tk.Frame(root, height=80, bg="lightgray",relief="solid",borderwidth="2")
top_frame.pack(fill="x", side="top")

# Create a frame for the left section
left_Frame = tk.Canvas(root, width=600, bg="lightgray",relief="solid",borderwidth="2")
left_Frame.pack(fill="y", side="left")

# Example content for the fixed frame (e.g., a label)
left_frame = tk.Label(left_Frame, bg="lightgray")
left_frame.pack(pady=200)

middle_framee = tk.Canvas(root, width=600, height=600)
middle_framee.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

#adding buttons to top_frame
btn_tree = tk.Button(top_frame, text="Linked List", command=show_linkedlist)
btn_tree.pack(side=tk.LEFT,padx=(0,20))
btn_stack = tk.Button(top_frame, text="Stack", command=show_stack)
btn_stack.pack(side=tk.LEFT,padx=(0,20))
btn_queue = tk.Button(top_frame, text="Queue", command=show_queue)
btn_queue.pack(side=tk.LEFT,padx=(0,20))

# Create frame for bottom
verticalScroll = tk.Frame(middle_framee)
verticalScroll.pack(fill="both", expand=True, side="bottom")

#Add a canvas for the scroll feature
verticalCanvas = tk.Canvas(verticalScroll)
verticalCanvas.pack(side="left", fill="both", expand=True)

# Add vertical scroll bar
v_scrollbar = ttk.Scrollbar(verticalScroll, orient="vertical", command=verticalCanvas.yview)
v_scrollbar.pack(side="left", fill="y")

# Add horizontal scroll bar
h_scrollbar = ttk.Scrollbar(middle_framee, orient="horizontal", command=verticalCanvas.xview)
h_scrollbar.pack(side="top", fill="x")

# Configure Canvas with scrollbars
verticalCanvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
verticalCanvas.bind('<Configure>', lambda e: verticalCanvas.configure(scrollregion=verticalCanvas.bbox("all")))

# Create scrollable content frame in Canvas
vScroll_content = tk.Frame(verticalCanvas)

# Add scrollable content frame to canvas
verticalCanvas.create_window((0, 0), window=vScroll_content, anchor="sw")

# # Test amacıyla birkaç örnek widget ekleyelim
# for i in range(20):
#     middle_frame=tk.Label(vScroll_content, text=f"Label {i+1}").grid(row=i, column=0, padx=10, pady=10)

# for j in range(10):
#    middle_frame=tk.Label(vScroll_content, text=f"Horizontal {j+1}").grid(row=0, column=j, padx=10, pady=10)


# Run the application
root.mainloop()