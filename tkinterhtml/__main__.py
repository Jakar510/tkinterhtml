import urllib.request
try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

from tkinterhtml import HtmlFrame, TkinterHv3

root = tk.Tk()

# frame = HtmlFrame(root, horizontal_scrollbar="auto")
# frame.grid(sticky=tk.NSEW)
# 
# 
# frame.set_content("""
# <html>
# <body>
# <h1>Hello world!</h1>
# <p>First para</p>
# <ul>
#     <li>first list item</li>
#     <li>second list item</li>
# </ul>
# <img src="http://findicons.com/files/icons/638/magic_people/128/magic_ball.png"/>
# </body>
# </html>    
# """)
# 
# #frame.set_content(urllib.request.urlopen("http://tkhtml.tcl.tk/").read().decode())
# print(frame.html.cget("zoom"))


hv3 = TkinterHv3(root)
hv3.grid()
hv3.tk.call(hv3._w, "goto", "http://thonny.cs.ut.ee")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.mainloop()
