from itertools import *

for x in product("ABC",repeat=3):
    print ("".join(x))