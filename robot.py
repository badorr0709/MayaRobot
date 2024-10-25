import maya.cmds as cmds
    class Robot:
        def __init__(self):
            head = [cmds.sphere(pivot=[0.0, 10.0, 0.0], r=2, name="centerOfHead"),
                    cmds.polyCube(sx=0.5, sy=4.0, sz=1.0, axis=[12.0, 10.0, 0.0], name="leftEar"),
                    cmds.polyCube(sx=0.5, sy=4.0, sz=1.0, axis=[-12.0, 10, 0.0], name="rightEar"),
                    cmds.polyCube(sx=0.5, sy=0.5, sz=0.5,name = "neck")]
            body = [cmds.polyCube(sx=9, sy=4.0, sz=3.0, axis=[0.0, 6.0, 0], name="upperChest"),
                    cmds.polyCube(sx=.5, sy=4.0, sz=1.0, axis=[0.0, 6.0, 0], name="midChest"),
                    cmds.polyCube(sx=.5, sy=4.0, sz=1.0, axis=[0.0, 6.0, 0], name="lowerChest")]
            leg1 = [cmds.polyCube(sx=.5, sy=4.0, sz=1.0, axis=[0.0, 6.0, 0], name="rightThigh"),
                    cmds.polyCube(sx=.5, sy=4.0, sz=1.0, axis=[0.0, 6.0, 0], name="rightCalf"),
                    cmds.polyCube(sx=.5, sy=4.0, sz=1.0, axis=[0.0, 6.0, 0], name="rightFoot")]
            leg2 = [cmds.polyCube(sx=.5, sy=4.0, sz=1.0, axis=[0.0, 6.0, 0], name="leftThigh"),
                    cmds.polyCube(sx=.5, sy=4.0, sz=1.0, axis=[0.0, 6.0, 0], name="leftCalf"),
                    cmds.polyCube(sx=.5, sy=4.0, sz=1.0, axis=[0.0, 6.0, 0], name="leftFoot")]
            arm1 = [cmds.polyCube(sx=.5, sy=4.0, sz=1.0, axis=[0.0, 6.0, 0], nam="leftBicep"),
                    cmds.polyCube(sx=.5, sy=4.0, sz=1.0, axis=[0.0, 6.0, 0], name="leftForarm"),
                    cmds.polyCube(sx=.5, sy=4.0, sz=1.0, axis=[0.0, 6.0, 0], name="hand")]
            arm2 = [cmds.polyCube(sx=.5, sy=4.0, sz=1.0, axis=[0.0, 6.0, 0], name="rightBicep"),
                    cmds.polyCube(sx=.5, sy=4.0, sz=1.0, axis=[0.0, 6.0, 0], name="rightForarm"),
                    cmds.polyCube(sx=.5, sy=4.0, sz=1.0, axis=[0.0, 6.0, 0], name="hand")]

                self.initHeadShape()
                self.initBodyShape()






    def initHeadShape(self):
        cmds.scale(3.0,3.0,3.0,"centerOfHead")
        cmds.scale(.5, 2, .25,"leftEar")
        cmds.scale(.5, 2, .25,"rightEar")
        cmds.scale(.5,.5,.5,"neck")






    def initBodyShape(self):
        cmds.scale(9.0,3.5,3.0,self.body[0])
        cmds.scale(9.0, 3.5, 3.0, self.body[0])
        cmds.scale(9.0,3.5,3.0,self.body[0])




robot = Robot()

