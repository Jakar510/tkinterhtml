"""Wrapper for the Tkhtml widget from http://tkhtml.tcl.tk/tkhtml.html"""

import sys
import os.path
import platform
import traceback
import warnings
from urllib.request import urlopen

try:
    from urllib2 import urlopen # Python 2
except ImportError:
    from urllib.request import urlopen

try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk

_tkhtml_loaded = False

def load_tkhtml(master, location=None):
    global _tkhtml_loaded
    if not _tkhtml_loaded:
        if location:
            master.tk.eval('global auto_path; lappend auto_path {%s}' % location)
        master.tk.eval('package require Tkhtml')
        _tkhtml_loaded = True        

def get_tkhtml_folder():
    return os.path.join (os.path.abspath(os.path.dirname(__file__)),
                         "tkhtml",
                         platform.system().replace("Darwin", "MacOSX"),
                         "64-bit" if sys.maxsize > 2**32 else "32-bit")
    

class TkinterHv3(tk.Widget):
    def __init__(self, master, cfg={}, **kw):
        load_tkhtml(master, get_tkhtml_folder())
        master.tk.eval('package require snit')
        master.tk.eval('package require hv3')
        kw["requestcmd"] = master.register(self._requestcmd)
        tk.Widget.__init__(self, master, '::hv3::hv3', cfg, kw)
    
    def _requestcmd(self, handle):
        uri = self.tk.call(handle, "cget", "-uri")
        # TODO: make it asynchronous
        self.tk.call(handle, "append", urlopen(uri).read())
        self.tk.call(handle, "finish")

class TkinterHtml(tk.Widget):
    def __init__(self, master, cfg={}, **kw):
        """
        See options descriptions from here: http://tkhtml.tcl.tk/tkhtml.html
        """
        #print(get_tkhtml_folder())
        load_tkhtml(master, get_tkhtml_folder())
        
        
        if "imagecmd" not in kw:
            kw["imagecmd"] = master.register(self._fetch_image)
            
        tk.Widget.__init__(self, master, 'html', cfg, kw)

        # make selection and copying possible
        self._selection_start_node = None
        self._selection_start_offset = None
        self._selection_end_node = None
        self._selection_end_offset = None
        self.bind("<1>", self._start_selection, True)
        self.bind("<B1-Motion>", self._extend_selection, True)
        self.bind("<<Copy>>", self.copy_selection_to_clipboard, True)
        
        self._image_name_prefix = str(id(self)) + "_img_"
        self._images = set() # to avoid garbage collecting images
        

    def node(self, *arguments):
        return self.tk.call(self._w, "node", *arguments)

    def parse(self, *args):
        source = args[0]
        if "<title>" in source.lower():
            warnings.warn("64-bit Windows Tkhtml has problems with html source containing <title> element. Consider removing it before sending source to parse.\n")
        self.tk.call(self._w, "parse", *args)

    def reset(self):
        return self.tk.call(self._w, "reset")
    
    def tag(self, subcommand, tag_name, *arguments):
        return self.tk.call(self._w, "tag", subcommand, tag_name, *arguments)
    
    def text(self, *args):
        return self.tk.call(self._w, "text", *args)
    
    def xview(self, *args):
        "Used to control horizontal scrolling."
        if args: return self.tk.call(self._w, "xview", *args)
        coords = map(float, self.tk.call(self._w, "xview").split())
        return tuple(coords)

    def xview_moveto(self, fraction):
        """Adjusts horizontal position of the widget so that fraction
        of the horizontal span of the document is off-screen to the left.
        """
        return self.xview("moveto", fraction)

    def xview_scroll(self, number, what):
        """Shifts the view in the window according to number and what;
        number is an integer, and what is either 'units' or 'pages'.
        """
        return self.xview("scroll", number, what)

    def yview(self, *args):
        "Used to control the vertical position of the document."
        if args: return self.tk.call(self._w, "yview", *args)
        coords = map(float, self.tk.call(self._w, "yview").split())
        return tuple(coords)

    def yview_name(self, name):
        """Adjust the vertical position of the document so that the tag
        <a name=NAME...> is visible and preferably near the top of the window.
        """
        return self.yview(name)

    def yview_moveto(self, fraction):
        """Adjust the vertical position of the document so that fraction of
        the document is off-screen above the visible region.
        """
        return self.yview("moveto", fraction)

    def yview_scroll(self, number, what):
        """Shifts the view in the window up or down, according to number and
        what. 'number' is an integer, and 'what' is either 'units' or 'pages'.
        """
        return self.yview("scroll", number, what)
    
    def _fetch_image(self, *args):
        # TODO: load images in the background
        # TODO: support base url
        
        assert len(args) == 1
        url = args[0]
        name = self._image_name_prefix + str(len(self._images))
        
        with urlopen(url) as handle:
            data = handle.read()
            
        self._images.add(tk.PhotoImage(name=name, data=data))
        
        return name
    
    def _start_selection(self, event):
        self.focus_set()
        self.tag("delete", "selection")
        try:
            self._selection_start_node, self._selection_start_offset = self.node(True, event.x, event.y)
        except:
            self._selection_start_node = None
            traceback.print_exc()
    
    def _extend_selection(self, event):
        if self._selection_start_node is None:
            return
        
        try:
            self._selection_end_node, self._selection_end_offset = self.node(True, event.x, event.y)
        except:
            self._selection_end_node = None
            traceback.print_exc()
        
        # TODO: the selection may actually shrink
        self.tag("add", "selection",
            self._selection_start_node, self._selection_start_offset,
            self._selection_end_node, self._selection_end_offset)
    
    def _ctrl_c(self, event):
        if self.focus_get() == self:
            self.copy_selection_to_clipboard()

    
    def copy_selection_to_clipboard(self, event=None):
        if self._selection_start_node is None or self._selection_end_node is None:
            return
        
        start_index = self.text("offset", self._selection_start_node, self._selection_start_offset)
        end_index = self.text("offset", self._selection_end_node, self._selection_end_offset)
        if start_index > end_index:
            start_index, end_index = end_index, start_index
        whole_text = self.text("text")
        selected_text = whole_text[start_index:end_index]
        self.clipboard_clear()
        self.clipboard_append(selected_text)


class HtmlFrame(ttk.Frame):
    # TODO: if Tkhtml doesn't work out then check out tkgecko
    def __init__(self, master, fontscale=0.8, vertical_scrollbar=True,
                 horizontal_scrollbar=True, **kw):
        """All keyword arguments not listed here are sent to contained TkinterHtml.
        See descriptions of the options here: http://tkhtml.tcl.tk/tkhtml.html
        """ 
        
        ttk.Frame.__init__(self, master, **kw)
    
        html = self.html = TkinterHtml(self, fontscale=fontscale)
        html.grid(row=0, column=0, sticky=tk.NSEW)
        
        if vertical_scrollbar:
            if vertical_scrollbar == "auto":
                vsb = _AutoScrollbar(self, orient=tk.VERTICAL, command=html.yview)
            else:
                vsb = ttk.Scrollbar(self, orient=tk.VERTICAL, command=html.yview)
                
            html.configure(yscrollcommand=vsb.set)
            vsb.grid(row=0, column=1, sticky=tk.NSEW)
        
        if horizontal_scrollbar:
            if horizontal_scrollbar == "auto":
                hsb = _AutoScrollbar(self, orient=tk.HORIZONTAL, command=html.xview)
            else:
                hsb = ttk.Scrollbar(self, orient=tk.HORIZONTAL, command=html.xview)
                
            html.configure(xscrollcommand=hsb.set)
            hsb.grid(row=1, column=0, sticky=tk.NSEW)
        
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
        self.set_content("<html><body></body></html>")
    
    def set_content(self, html_source):
        self.html.reset()
        self.html.parse(html_source)

class _AutoScrollbar(ttk.Scrollbar):
    # http://effbot.org/zone/tkinter-autoscrollbar.htm
    # a vert_scrollbar that hides itself if it's not needed.  only
    # works if you use the grid geometry manager.
    def set(self, lo, hi):
        # TODO: this can make GUI hang or max out CPU when scrollbar wobbles back and forth
        if float(lo) <= 0.0 and float(hi) >= 1.0:
            self.grid_remove()
        else:
            self.grid()
        ttk.Scrollbar.set(self, lo, hi)
        
    def pack(self, **kw):
        raise tk.TclError("cannot use pack with this widget")
    
    def place(self, **kw):
        raise tk.TclError("cannot use place with this widget")

