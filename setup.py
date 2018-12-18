import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='hound-dog',  
     version='0.1',
     scripts=['hounddog'] ,
     author="Paolo Perego",
     author_email="paolo@codiceinsicuro.it", 
     description="An automated web resources discovery hunter", 
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/thesp0nge/hound-dog",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
