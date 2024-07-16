from manim import *

class Something(Scene):
    def construct(self):
        circle = Circle()
        self.play(Create(circle))
        self.wait(2)
        square = Square()
        self.play(Transform(circle, square), run_time=2)
        self.play(ApplyMethod(circle.shift,UP))
        self.play(ApplyMethod(circle.rotate,0.3))
        self.play(ApplyMethod(circle.scale,2))

class Counting(Scene):
    def construct(self):
        number = Text("0")
        self.play(Write(number))
        for i in range(10):
            self.play(Transform(number, Text(str(i))))

import networkx as nx

class Tree(MovingCameraScene):
    def construct(self):
        
        square = Square()
        self.play(Create(square))
        self.wait(2)
        edges = [("Root", "1"), ("Root", "2"), ("Root", "3"), ("Root", "4")]
        nodes = ["Root", "1", "2", "3", "4"]
        graph1 = Graph(["Root"], list(),layout_scale=3, labels=True,)
        self.play(Uncreate(square))
        self.play(DrawBorderThenFill(graph1))

        graph2 = Graph(list(nodes), list(edges), layout="tree", root_vertex="Root",layout_scale=3, labels=False, vertex_config={"1": {"fill_color": RED},
                                                                                                                                           "2": {"fill_color": PURPLE},
                                                                                                                                           "3": {"fill_color": BLUE},
                                                                                                                                     "4": {"fill_color": GREEN},
                                                                                                                                     },
                                                                                                                                     )
        self.play(Transform(graph1, graph2))  
        self.replace(graph1, graph2)
        edges = [("Root", "1"), ("Root", "2"), ("Root", "3"), ("Root", "4")
                 ,("1", "12"), ("1", "13"), ("1", "14"), ("1", "15")
                 ,("2", "21"), ("2", "23"), ("2", "24"), ("2", "25")
                 ,("3", "32"), ("3", "31"), ("3", "34"), ("3", "35")
                 ,("4", "42"), ("4", "43"), ("4", "41"), ("4", "45")]
        nodes = ["Root", "1", "2", "3", "4", "12", "13", "14", "15"
                 ,"21", "23", "24", "25", "32", "31", "34", "35", "42"
                 ,"43", "41", "45"]
        graph3 = Graph(list(nodes), list(edges), layout="tree", root_vertex="Root",layout_scale=7, labels=False, layout_config={"vertex_spacing": (1.25, 2)}, 
                                                                                                                    vertex_config={"1": {"fill_color": RED},
                                                                                                                                "2": {"fill_color": PURPLE},
                                                                                                                                "3": {"fill_color": BLUE},
                                                                                                                                "4": {"fill_color": GREEN},
                                                                                                                                "12": {"fill_color": PURPLE},
                                                                                                                                "13": {"fill_color": BLUE},
                                                                                                                                "14": {"fill_color": GREEN},
                                                                                                                                "15": {"fill_color": YELLOW},
                                                                                                                                "21": {"fill_color": RED},
                                                                                                                                "23": {"fill_color": BLUE},
                                                                                                                                "24": {"fill_color": GREEN},
                                                                                                                                "25": {"fill_color": YELLOW},
                                                                                                                                "31": {"fill_color": RED},
                                                                                                                                "32": {"fill_color": PURPLE},
                                                                                                                                "34": {"fill_color": GREEN},
                                                                                                                                "35": {"fill_color": YELLOW},
                                                                                                                                "41": {"fill_color": RED},
                                                                                                                                "42": {"fill_color": PURPLE},
                                                                                                                                "43": {"fill_color": BLUE},
                                                                                                                                "45": {"fill_color": YELLOW},
                                                                                                                                })
        self.wait(2)
        self.play(self.camera.frame.animate.set(width=20))
        self.play(Transform(graph2, graph3))  
        self.replace(graph2, graph3)
        self.wait(3)

        depth = Integer(number=2).set_color(YELLOW).scale(3).set_x(0).set_y(4)
        self.play(Write(depth))
        self.play(ShowPassingFlash(graph3.copy().set_color(YELLOW), run_time=2, time_width=2))
        self.wait(3)
        scores = [1, 0, 2, -1, 0, 0, 1, 2, -2, 1, 0, 1, 0, 3, 1, 0]
        toWrite = []
        for i, score in enumerate(scores):
            toWrite.append(Integer(number=score).set_color(WHITE).scale(.7).set_x(-9.5+1.27*i).set_y(-3))
        for number in toWrite:
            self.play(Write(number), run_time=.3)
        self.wait(3)

        self.play(self.camera.frame.animate.set(width=25))
        max2 = Text('Minimizer').scale(.5).set_x(-11).set_y(-2)
        min1 = Text('Maximizer').scale(.5).set_x(-11).set_y(0)
        self.play(Write(min1))
        self.play(Write(max2))
        self.wait(3)
        self.play(Indicate(max2))
        self.wait(3)

        self.play(self.camera.frame.animate.set(width=15).move_to(toWrite[3]))
        self.wait(3)
        self.play(Indicate(toWrite[3].set_color(YELLOW)))
        self.wait(1)
        toWrite[3].generate_target()
        toWrite[3].target.shift(UP*3.3, LEFT*1.9)
        self.play(MoveToTarget(toWrite[3]))
        self.wait(3)

        self.play(self.camera.frame.animate.move_to(toWrite[7]))
        self.wait(3)
        self.play(Indicate(toWrite[4].set_color(YELLOW)))
        self.wait(1)
        toWrite[4].generate_target()
        toWrite[4].target.shift(UP*3.3, RIGHT*1.9)
        self.play(MoveToTarget(toWrite[4]))
        self.wait(3)

        self.play(self.camera.frame.animate.move_to(toWrite[11]))
        self.wait(3)
        self.play(Indicate(toWrite[8].set_color(YELLOW)))
        self.wait(1)
        toWrite[8].generate_target()
        toWrite[8].target.shift(UP*3.3, RIGHT*1.9)
        self.play(MoveToTarget(toWrite[8]))
        self.wait(3)

        self.play(self.camera.frame.animate.move_to(toWrite[15]))
        self.wait(3)
        self.play(Indicate(toWrite[12].set_color(YELLOW)))
        self.wait(1)
        toWrite[12].generate_target()
        toWrite[12].target.shift(UP*3.3, RIGHT*1.9)
        self.play(MoveToTarget(toWrite[12]))
        self.wait(3)

        toWrite[3].set_color(WHITE)
        toWrite[4].set_color(WHITE)
        toWrite[8].set_color(WHITE)
        toWrite[12].set_color(WHITE)
        self.play(Indicate(max2))
        

        self.play(self.camera.frame.animate.set(width=25).move_to(toWrite[4]))
        self.wait(3)
        self.play(Indicate(toWrite[4].set_color(YELLOW)))
        self.wait(1)
        toWrite[4].generate_target()
        toWrite[4].target.shift(UP*2.5, RIGHT*2.5)
        self.play(MoveToTarget(toWrite[4]))
        self.play(self.camera.frame.animate.move_to(toWrite[4]))
        self.wait(3)

        arrow1 = Arrow(start=UP*1.5, end=LEFT*1.9).set_color(BLUE)
        arrow2 = Arrow(start= UP*1.8, end=LEFT*2).shift(DOWN*1.4, LEFT*2.5).set_color(YELLOW)
        self.play(GrowArrow(arrow1))
        self.play(GrowArrow(arrow2))
        
        self.wait(3)




