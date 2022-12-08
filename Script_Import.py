import maya.cmds as cmds
import os
import Import_Test as it



pd = cmds.workspace(q =1, rd =1)
print(pd)
os.chdir(pd)
wd = os.getcwd()
print(wd)
print(os.path.abspath(wd))
it.test()
