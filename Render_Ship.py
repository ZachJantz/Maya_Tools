import maya.cmds as cmds
import os
import shutil

wdir = cmds.workspace(q = 1, rd = 1)
print(wdir)
shutil.copy('H:\MAYA\projects\Test_2', wdir)