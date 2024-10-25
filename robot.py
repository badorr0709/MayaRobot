import maya.cmds as cmds
class Robot:
    def __init__(self):
        self.head = [cmds.sphere(r=2, name="centerOfHead"),
            cmds.polyCube(name="leftEar"),
            cmds.polyCube(name="rightEar"),
            cmds.polyCube(name = "neck")]
        self.body = [cmds.polyCube(name="upperChest"),
            cmds.polyCube(name="midChest"),
            cmds.polyCube(name="lowerChest")]
        self.legLeft = [cmds.polyCube(name="rightThigh"),
            cmds.polyCube(name="rightCalf"),
            cmds.polyCube(name="rightFoot")]
        self.legRight = [cmds.polyCube(name="rightThigh"),
            cmds.polyCube(name="rightCalf"),
            cmds.polyCube(name="rightFoot")]
        self.armLeft = [cmds.polyCube(name="leftBicep"),
            cmds.polyCube(name="leftForarm"),
            cmds.polyCube(name="hand")]
        self.armRight= [cmds.polyCube(name="leftBicep"),
            cmds.polyCube(name="leftForarm"),
            cmds.polyCube(name="hand")]
        self.headsetup()
    def headsetup(self):
        for x in range(len(self.head)-1):
            match x:
                case 0:
                    cmds.scale(1,1,1,self.head[x])
                    break
                case 1:
                    cmds.scale(.5,3,1,self.head[x])
                    break
                case 2:
                    cmds.scale(.5,3,1,self.head[x])
                    break
                case 3:
                    cmds.scale(.5,.5,.5,self.head[x])
                    break




robot = Robot()