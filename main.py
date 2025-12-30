from ORE import *

print ("Loading parameters...")
params = Parameters()
print ("   params is of type", type(params))
params.fromFile(r"C:\Users\josep\Desktop\ORE-SWIG-master\ORE-SWIG-master\OREAnalytics-SWIG\Python\Examples\Input\ore.xml")
print ("   setup/asofdate = " + params.get("setup","asofDate"))

# Main Run 
# main.py - run model examples
# folders with .py files with jupyter
# for research file
