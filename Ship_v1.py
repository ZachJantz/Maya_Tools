#import maya.cmds as cmds
import os


def ship(store):
    #pDir = cmds.workspace(q =1, rd = 1)
    farmTemp = store
    farmDir = r"I:\Savannah\SDM Render Farm"
    os.mkdir(farmDir + farmTemp)
    
ship('Temp')
    
