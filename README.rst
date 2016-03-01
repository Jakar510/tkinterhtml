``tkinterhtml``
===============
This is Python wrapper for `Tkhtml3 <http://tkhtml.tcl.tk/>`_.

It's tested with Python 2.7, 3.2, 3.3, 3.4, 3.5.

Includes Python package ``tkinterhtml`` with class ``TkinterHtml`` and Tkhtml binaries for:

* Windows (32 and 64-bit);
* Mac OS X (64-bit, should work on Lion and later, possibly also on 64-bit Snow Leopard);
* Linux (32 and 64-bit, tested on Ubuntu 12.04).

The binaries should work both with Tk 8.5 and 8.6.

Installation
------------
``pip install tkinterhtml``

Usage
-----
See `tkinterhtml/__main__.py <https://bitbucket.org/aivarannamaa/tkinterhtml/src/master/tkinterhtml/__main__.py>`_.

More about Tkhtml binaries
--------------------------
If you ``pip install tkinterhtml``, then besides Python code you also get pre-built Tkhtml binaries and scripts for all main platforms (see the folder *tkhtml* inside resulting package directory). You may delete unnecessary platform directories after installation.

If you are not happy with those binaries, then you could try compiling Tkhtml yourself. The scripts in *tkinterhtml/tkhtml* explain how I compiled it. 

If you don't want to keep the binaries inside package directory (maybe because you want to zip your packages), then you should copy the *Tkhtml* folder with *pcgIndex.tcl* and dll/so/dylib in it into your Tcl library directory. In Windows it's *<Python root>\tcl*.

If binaries compiled by me, you could try the binaries from Active Tcl (but check their license about redistribution). Install Active Tcl and execute ``teacup install Tkhtml`` and then search for binaries (eg. Tkhtml30.dll in Windows). 
