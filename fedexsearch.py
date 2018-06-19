import tkinter as tk
import webbrowser

root = tk.Tk()


def my_function():
    current_id = my_entry.get()
    url_member = 'https://www.fedex.com/apps/fedextrack/?tracknumbers=' + str(current_id)
    webbrowser.open(url_member)
    # do stuff with url_member


root.title("Peca Macola")
root.geometry("300x100")

my_label = tk.Label(root, text="Fedex Tracking ID:")
my_label.grid(row=0, column=0)
my_entry = tk.Entry(root)
my_entry.grid(row=0, column=1)

my_button = tk.Button(root, text="Search", command=my_function)
my_button.grid(row=0, column=2)

root.mainloop()
