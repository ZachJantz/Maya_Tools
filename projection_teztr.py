import maya.cmds as cmds



def project():
    
    obj = cmds.ls(sl = 1)[0]
    cmds.select(obj)
    cmds.DeleteUVs()
    projectionCam = 'projection1'
    cmds.lookThru(projectionCam)
    camPos = cmds.camera(projectionCam, q = 1, p = 1)
    objPos = cmds.xform(obj, q = 1, t = 1, ws = 1)
    camCenter = cmds.camera(projectionCam, q = 1, wci = 1)
    camCenter = [round(cord, 3) for cord in camCenter]
    print(camCenter)
    #distance = cmds.distanceDimension(sp = objPos, ep = camPos)
    print(distance)
    projection = cmds.polyProjection(obj + '.f[:]', t = 'planar', md = 'c', ch = 1)[0]
    cmds.setAttr(projection + '.projectionCenterX', camCenter[0])
    cmds.setAttr(projection + '.projectionCenterY', camCenter[1])
    cmds.setAttr(projection + '.projectionCenterZ', camCenter[2])


project()