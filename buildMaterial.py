import maya.cmds as cmds

def buildMt():
    selectedObj = cmds.ls(sl = 1, fl = 1)
    print(selectedObj)
    for obj in selectedObj:
        surface = cmds.shadingNode('aiStandardSurface', asShader = 1, n  = obj + '_MT')
        diffuse = cmds.shadingNode('file', asTexture = 1, isColorManaged = 1, n = obj + '_MT_diffuse')
        cmds.connectAttr(diffuse + '.outColor', surface + ',baseColor')
        specular = cmds.shadingNode('file', asTexture = 1, isColorManaged = 1, n = obj + '_MT_roughness')
        
        cmds.shadingNode('file', asTexture = 1, isColorManaged = 1, n = obj + '_MT_metalness')
        cmds.shadingNode('file', asTexture = 1, isColorManaged = 1, n = obj + '_MT_normal')
        cmds
        cmds.select(obj)
        cmds.hyperShade(a = surface)
        
        
buildMt()
    