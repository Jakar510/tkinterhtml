from setuptools import setup

url = "https://bitbucket.org/aivarannamaa/tkinterhtml"

setup(
      name="tkinterhtml",
      version=0.7,
      description="Python wrapper for Tkhtml3 (http://tkhtml.tcl.tk/)",
      long_description="See %s for more info" % url,
      url=url,
      license="MIT",
      classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: Freeware",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development",
      ],
      keywords="tkinter Tkinter tkhtml Tkhtml Tk",
      packages=["tkinterhtml"],
      #include_package_data=True,
      package_data={'tkinterhtml': ['tkhtml/Windows/32-bit/Tkhtml/*.tcl',
                                    'tkhtml/Windows/32-bit/Tkhtml/*.dll',
                                    'tkhtml/Windows/64-bit/Tkhtml/*.tcl',
                                    'tkhtml/Windows/64-bit/Tkhtml/*.dll',
                                    
                                    'tkhtml/MacOSX/64-bit/Tkhtml/*.tcl',
                                    'tkhtml/MacOSX/64-bit/Tkhtml/*.dylib',
                                    
                                    'tkhtml/Linux/32-bit/Tkhtml/*.tcl',
                                    'tkhtml/Linux/32-bit/Tkhtml/*.so',
                                    'tkhtml/Linux/64-bit/Tkhtml/*.tcl',
                                    'tkhtml/Linux/64-bit/Tkhtml/*.so'
                                    ]}
)