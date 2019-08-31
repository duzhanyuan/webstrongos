# GEditRoot - GEdit with admin permission 
# Created by Matt Pijanowski (WebStrongTeam)

import os
import sys

if sys.argv[1][0] == "/":
	os.system('gedit admin:///"'"{}"'"'.format(sys.argv[1]))
else:
	os.system('gedit admin://"'"{}"'"/"'"{}"'"'.format(os.getcwd(), sys.argv[1]))
