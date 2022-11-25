import maya.cmds as cmds
import os
from functools import partial
#------------------ Directions ----------------------------------------
'''
1. Make sure project is Set
2. Place your image planes in the sourceimages folder of your project.
3. Select the camera you want to create planes for.
4. Use the slider to toggle between images.
'''
#----------------------------------------------------------------------
projectDir = cmds.workspace(q = 1, rd = 1)
print(projectDir)
sourceImgDir = projectDir + 'sourceimages'
imgPlaneDir = projectDir + 'sourceimages' + '\image_planes'
if os.path.isdir(imgPlaneDir) and len(os.listdir(imgPlaneDir)) == 0:
    os.rmdir(imgPlaneDir)
if not os.path.isdir(imgPlaneDir): 
    os.chdir(sourceImgDir)
    os.makedirs('image_planes')
    imgList = os.listdir(sourceImgDir)
    for item in imgList[1:-1]:
        os.rename(sourceImgDir + '/' + item, imgPlaneDir + '/' + item)
def getSliderValue(ctrlName):
    value = cmds.intSliderGrp(ctrlName, q = 1, value = 1)
    return value
selCam = cmds.ls(sl = 1)[0]
planeName = selCam + '_imgPlane'    
def toggleImage(slider, *args):
    value = getSliderValue(slider)
    if cmds.objExists(planeName + '*'):
        cmds.delete(planeName + '*')
    imgList = os.listdir(imgPlaneDir)
    selImg = imgList[value]
    os.chdir(imgPlaneDir)
    cmds.imagePlane(c = selCam + 'Shape', n = planeName, fn = selImg)
    cmds.setAttr(selCam + '_imgPlaneShape2.depth', 100)
window = cmds.window(title = 'Toggle_Image_Planes', widthHeight=(200, 55))
cmds.columnLayout( adjustableColumn = 1 )
selCtrl = cmds.intSliderGrp(min = 0, max = len(os.listdir(imgPlaneDir)) - 1, v = 0, s = 1, dc = 'empty')
cmds.intSliderGrp(selCtrl, e = 1, dc = partial(toggleImage, selCtrl))
cmds.setParent( '..' )
cmds.showWindow( window )
