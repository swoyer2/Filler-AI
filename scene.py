from manim import *
import networkx as nx

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

        graph2 = Graph(list(nodes), list(edges), layout="tree", root_vertex="Root",layout_scale=3, labels=True, vertex_config={"1": {"fill_color": RED},
                                                                                                                                           "2": {"fill_color": PURPLE},
                                                                                                                                           "3": {"fill_color": BLUE},
                                                                                                                                     "4": {"fill_color": GREEN}},)
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
        graph3 = Graph(list(nodes), list(edges), layout="tree", root_vertex="Root",layout_scale=7, labels=True, layout_config={"vertex_spacing": (1.25, 2)}, 
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
                                                                                                                                "45": {"fill_color": YELLOW},})
        self.wait(2)
        self.play(self.camera.frame.animate.set(width=30))
        self.play(Transform(graph2, graph3))  
        self.replace(graph2, graph3)

        self.wait(3)