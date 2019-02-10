=================
How to contribute
=================


Preparing your environment
##########################

Start by creating a folder for the project. Create a python3 virtual environment on that folder. Fork the project on GitHub and clone it to that folder.

Install pelican with
::
   pip install pelican

Install fontawsome
::
   pip install pelican-fontawesome

Note: instead you could also use pip with the requirements file.


Seeing the local version of the site
####################################

Start by reading pelican documentation, it's quick and easy and you will need it. After that you can see the site with:
::
   $ pelican --listen

Of course this wont work if you have nothing on the output directory. To create the output you must first do
::
   $ pelican content


Creating a branch for development
#################################

You must create a branch for development of your feature, otherwise you will be editing your master code. Use a meaningfull name like:
::
   git checkout -b fix_whatyouarefixing

You will now be in your branch and you can modify and test the code.


Making a pull request
#####################

When you finish working on the code you will have to make a pull request on GitHub. Please be patient because the approval process may take some time.

Happy Python hacking!


