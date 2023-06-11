import os
import shutil
from glob import glob

allArcFiles = [y for x in os.walk(os.getcwd()) for y in glob(os.path.join(x[0], '*.arc'))]

# Unpack everything
for arcFile in allArcFiles:
    path = "arctool -dd -texRE6 -alwayscomp -pc -txt -v 7  \"" + arcFile + "\""
    os.system(path)

# Delete zht.gmd
allGmdFiles = [y for x in os.walk(os.getcwd()) for y in glob(os.path.join(x[0], '*zht.gmd'))]
for gmdFile in allGmdFiles:
    os.remove(gmdFile)

# Repack everything
for arcFile in allArcFiles:
    arcFolder = os.path.splitext(arcFile)[0]
    path = "arctool -dd -texRE6 -alwayscomp -pc -txt -v 7  \"" + arcFolder + "\""
    os.system(path)
    # Uncomment below line if you want the unpacked folders to be deleted at the end
    # shutil.rmtree(arcFolder)