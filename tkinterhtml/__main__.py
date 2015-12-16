try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk

from tkinterhtml import TkinterHtml

root = tk.Tk()

html = TkinterHtml(root, fontscale=0.8)
vsb = ttk.Scrollbar(root, orient=tk.VERTICAL, command=html.yview)
hsb = ttk.Scrollbar(root, orient=tk.HORIZONTAL, command=html.xview)
html.configure(yscrollcommand=vsb.set)
html.configure(xscrollcommand=hsb.set)



#html.tag("configure", "selection", "-background", "black")

html.grid(row=0, column=0, sticky=tk.NSEW)
vsb.grid(row=0, column=1, sticky=tk.NSEW)
hsb.grid(row=1, column=0, sticky=tk.NSEW)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

html.parse("""
<html>
<body>
<h1>Hello world!</h1>
<p>First para</p>
<ul>
    <li>first list item</li>
    <li>second list item</li>
</ul>
</body>
</html>    
""")

root.mainloop()
