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
        self.bodysetup()
        self.legsetup()
        self.armsetup()

    def headsetup(self):
        cmds.scale(1,1,1,self.head[0])
        cmds.move(0,10,0,self.head[0])
        cmds.scale(.5,5,1,self.head[1])
        cmds.rotate(43.0,0,0,self.head[1])
        cmds.move(2,10,0,self.head[1])
        cmds.scale(.5,5,1,self.head[2])
        cmds.move(-2,10,0,self.head[2])
        cmds.rotate(43.0, 0, 0, self.head[2])
        cmds.scale(1,2,1,self.head[3])
        cmds.move(0,8,0,self.head[3])

    def bodysetup(self):
        cmds.scale(5,3,3,self.body[0])
        cmds.move(0,6.1,0,self.body[0])
        cmds.scale(3.5, 2, 3, self.body[1])
        cmds.move(0,3.756,0,self.body[1])
        cmds.scale(2, 1, 2, self.body[2])
        cmds.move(0,2.463,0,self.body[2])
    def legsetup(self):
        cmds.scale(1,3,3,self.legLeft[0])
        cmds.scale(1, 3, 1, self.legLeft[0])
        cmds.scale(1, 3, 1, self.legLeft[0])

    def armsetup(self):





robot = Robot()