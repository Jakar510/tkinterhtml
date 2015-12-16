from setuptools import setup

setup(
      name="tkinterhtml",
      version=0.2,
      description="Python wrapper for Tkhtml (http://tkhtml.tcl.tk/)",
      url="https://bitbucket.org/aivarannamaa/tkinterhtml",
      license="MIT",
      classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: Freeware",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python",
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
                                    ]}
)