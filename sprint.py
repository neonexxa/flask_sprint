#######################################################################################
#
# Sprint Command	
# Version : v1.0
#
#######################################################################################	

import argparse
from time import time

ap = argparse.ArgumentParser()
ap.add_argument("command_type")
ap.add_argument("item_name")
args = vars(ap.parse_args())
print(args)