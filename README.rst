Wrapper for Tkhtml (http://tkhtml.tcl.tk/).

Tested with Python 2.7, 3.2, 3.3, 3.4, 3.5.

Includes Python package ``tkinterhtml`` with class ``TkinterHtml`` and Tkhtml binaries for:

* Windows (32 and 64-bit);
* Mac OS X (64-bit, should work on Lion and later, possibly also on 64-bit Snow Leopard);
* Linux (32 and 64-bit, tested on Ubuntu 12.04).

The binaries should work both with Tk 8.5 and 8.6.

Usage
------
See ``tkinterhtml/__main__.py``.

More about Tkhtml binaries
--------------------------
If you ``pip install tkinterhtml``, then besides Python code you also get pre-built Tkhtml binaries and scripts for all main platforms (see the folder *tkhtml* inside resulting package directory). You may delete unnecessary platform directories after installation.

If you are not happy with those binaries, then you could try compiling Tkhtml yourself. The scripts in *tkinterhtml/tkhtml* explain how I compiled it. Alternatively, you could try the binaries from Active Tcl (but check their license about redistribution).

If you don't want to keep the binaries inside package directory (maybe because you want to zip your packages), then you should copy the *Tkhtml* folder with *pcgIndex.tcl* and dll/so/dylib in it into your Tcl library directory. In Windows it's *<Python root>\tcl*.
