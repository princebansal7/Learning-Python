# importing from inbuilt 'keyword' module (just a python file), and this module has a variable called 'kwlist'
# 'Package' is collection of module or sub-packages (like sub-folder)
# 'Library' is collection of packages

# Importing module (python file)
import keyword
print(keyword.kwlist) # moduleName.moduleElement
print()

# import variable directly from module
from keyword import kwlist
print(kwlist) # using directly without module name
print()

#    OR

# alias for inbuilt module (to avoid name conflicts with this python file's variable names)
import keyword as kw
print(kw.kwlist)
print()
#    OR

# alias of improted variable
from keyword import kwlist as kwl
print(kwl)
