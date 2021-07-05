import tkinter as tk

root = tk.Tk()

main_frame = tk.Frame(root, bg='yellow')
main_frame.pack(side='top', fill='both', expand=True)

inner_left = tk.Frame(main_frame, bg='green')
inner_left.pack(side='left', expand=True)
text_left = tk.Label(inner_left, text='jgjhgjg')
text_left.pack(side='top')

inner_right = tk.Frame(main_frame, bg='red')
inner_right.pack(side='left', fill='both', expand=True)
text_left = tk.Label(inner_right, text='jgjhgjg')
text_left.pack(side='top')

root.mainloop()