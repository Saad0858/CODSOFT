import tkinter as tk
import string
import random
import tkinter.font as font

def generate_password():
    password_length = int(length_entry.get())
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(password_length))
    password_label.insert(tk.END, password)

def reset_password():
    length_entry.delete(0, tk.END)
    user_entry.delete(0, tk.END)
    password_label.delete(0, tk.END)


root = tk.Tk()
root.title("Password Generator")
root.geometry('900x600+350+100')
frame1 = tk.Frame(root)

label_title = tk.Label(frame1, text="Password Generator", fg='blue')
label_font = font.Font(size=30, family='comic sans ms')
label_title['font'] = label_font
label_title.grid(pady=(10,10), column=1, columnspan=4)

user = tk.Label(frame1, text="Enter User Name", font=("comic sans ms", 16))
user.grid(row=3, pady=(20, 10), column=1, padx=(20, 5))

entry_task_font = font.Font(size=14,family='comic sans ms')
user_entry = tk.Entry(frame1, font=entry_task_font, fg='maroon')
user_entry.grid(row=3, pady=(20, 10), column=2, padx=(20, 5))

length_label = tk.Label(frame1, text="Password Length:", font=("comic sans ms", 16))
length_label.grid(row=4, pady=(20, 10), column=1, padx=(20, 5))

length_entry = tk.Entry(frame1, font=entry_task_font, fg='maroon')
length_entry.grid(row=4, pady=(20, 10), column=2, padx=(20, 5))

btn_font = font.Font(size=14)
generate_button = tk.Button(frame1, text="Generate Password", command=generate_password, fg='red')
generate_button['font'] = btn_font
generate_button.grid(row=5, pady=(20, 10), column=1, padx=(20, 5), columnspan=4)

generate_label= tk.Label(frame1, text="Generated Password", font=("comic sans ms", 16))
generate_label.grid(row=6, pady=(20, 10), column=1, padx=(20, 5))

listbox_tasks_font = font.Font(size=14, family='comic sans ms')
password_label = tk.Entry(frame1, font=entry_task_font, fg='maroon')
password_label.grid(row=6, pady=(20, 10), column=2, padx=(20, 5))

reset_button = tk.Button(frame1, text="Reset", command=reset_password, fg='red')
reset_button['font'] = btn_font
reset_button.grid(row=7, pady=(20, 10), column=1, padx=(20, 5), columnspan=4)

frame1.pack()

root.mainloop()
