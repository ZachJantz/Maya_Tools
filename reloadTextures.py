import maya.cmds as cmds

def reloadTextures():
    cmds.waitCursor(st = True)
    textureFiles = cmds.ls(type = "file")
    for texture in textureFiles:
        textureFilePath = cmds.getAttr(texture + ".fileTextureName")
        print(textureFilePath)
        cmds.setAttr(texture + ".fileTextureName", textureFilePath, type = "string")
    cmds.waitCursor(st= False)
    
reloadTextures()