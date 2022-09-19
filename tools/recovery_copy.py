import sys
import os
from datetime import datetime
from distutils.dir_util import copy_tree
import shutil

def main():
    # get arguments
    args = sys.argv[1:]

    # validate argument size
    la = len(args)
    if la < 1 or la > 2:
        print("Command usage example:\n\n \> " + os.path.basename(sys.argv[0]) + " <folder name> <extensions>\n")
        return
    
    # list ignored arguments by defaul
    ignore_exts_str = "*.dll,*.exe,*.bak,obj,objd,out,.git,.vs,TestResults,.pkgrefgen" 
    if la == 2:
        ignore_exts_str = args[1]

    # convert ignore exts to list
    ignore_exts = ignore_exts_str.split(",")
    
    now = datetime.now()
    fromDirectory = args[0]
    toDirectory = os.path.join(fromDirectory + now.strftime("_%Y-%m-%d_%H%M%S"))
    
    print("\nCopy to folder: " + toDirectory)

    shutil.copytree(fromDirectory, toDirectory, ignore = shutil.ignore_patterns(*ignore_exts))

    print("\n")


if __name__ == "__main__":
    main()
