# GeditRoot - Gedit with admin permission
# Created by Matt Pijanowski (WebStrongTeam)

import os
import sys

if len(sys.argv) == 1:
	os.system('nautilus admin:///')
elif sys.argv[1][0] == "/":
	os.system('nautilus admin:///"'"{}"'"'.format(sys.argv[1]))
else:
	os.system('nautilud admin://"'"{}"'"/"'"{}"'"'.format(os.getcwd(), sys.argv[1]))
