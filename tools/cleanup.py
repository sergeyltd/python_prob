import sys
import os
import shutil
import re
import stat
import fnmatch

def onerror(func, path, exc_info):
    """
    Error handler for ``shutil.rmtree``.

    If the error is due to an access error (read only file)
    it attempts to add write permission and then retries.

    If the error is for another reason it re-raises the error.

    Usage : ``shutil.rmtree(path, onerror=onerror)``
    """
    # Is the error an access error?
    if not os.access(path, os.W_OK):
        os.chmod(path, stat.S_IWUSR)
        func(path)
    else:
        raise

def purge(dir, folderPattern, exts):
    folderMatcher = re.compile(r"^"+folderPattern+"$")
    for root, dirs, files in os.walk(dir, topdown=False):
        for name in dirs:
            if not folderMatcher.match(name):
                continue
            path = os.path.join(root, name)
            print("   removing folder: "+path)
            if os.path.exists(path):
                shutil.rmtree(path, onerror=onerror)
        for currentFile in files:
            filtered_files = [currentFile for ext in exts if currentFile.endswith(ext)]
            if not any(filtered_files):
                continue
            path = os.path.join(root, currentFile)
            print("   removing file: "+path)
            if os.path.exists(path):
                os.remove(path)

def main():
    # get arguments
    args = sys.argv[1:]

    # validate argument size
    la = len(args)
    if la < 1 or la > 2:
        print("Command usage example:\n\n \> " + os.path.basename(sys.argv[0]) + " <folder name> <pattern folder name comma separated>\n")
        return

    # list ignored arguments by default
    patterns_str = "obj,objd,.pkgrefgen,TestResults,out,log"
    if la == 2:
        patterns_str = args[1]

    # convert ignore exts to list
    patterns = patterns_str.split(",")

    fromDirectory = args[0]

    # print(fromDirectory)
    print("\nPurge folder: " + fromDirectory)

    exts = ['.projhash', '.projhash.userData', '.projhash.userData.assemblies', '.user', '.userData', '.assemblies']

    for folderPattern in patterns:
        purge(fromDirectory, folderPattern, exts)

    print("\n")


if __name__ == "__main__":
    main()

