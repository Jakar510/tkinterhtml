Wrapper for Tkhtml (http://tkhtml.tcl.tk/)

About Tkhtml binaries
-----------------------
If you ``pip install tkinterhtml``, then besides Python code you also get pre-built Tkhtml binaries and scripts for all main platforms (see the folder *tkhtml* inside resulting package directory).

If you are not happy with those binaries, then you could try compiling Tkhtml yourself. The scripts in *tkinterhtml/tkhtml* explain how I compiled it. Alternatively, you could try the binaries from Active Tcl (but check their license about redistribution).

If you don't want to keep the binaries inside package directory (maybe because you want to zip your packages), then you should copy the *Tkhtml* folder with *pcgIndex.tcl* and dll/so/dylib in it into your Tcl library directory. In Windows it's *<Python root>\tcl*.
