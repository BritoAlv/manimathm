# given two points draw an add logic gate through them
from manim import*

class B(Scene):
    def construct(self):
        point1 = Dot([0,0,0])
        point2 = Dot([-0.2,0,0])
        point5 = Dot(Line(
            start = midpoint(point1.get_center(), point2.get_center()),
            end = Line(
                start = point1, 
                end = point2).scale(2.4).get_start()
            ).rotate(
                about_point= midpoint(point1.get_center(), point2.get_center()), angle = PI/2).get_end())
        self.add(point1)
        self.add(point2)
        line12 = Line(start = point1, end = point2).scale(1.7)
        self.add(line12)
        point3 = Dot(line12.get_start())
        point4 = Dot(line12.get_end())
        self.add(point3, point4, point5)
        arc1 = ArcBetweenPoints(point3.get_center(), point5.get_center())
        arc2 = ArcBetweenPoints(point5.get_center(), point4.get_center())
        self.add(arc1, arc2)
        self.wait()        

class A(Scene):
    def construct(self):
        point1 = Dot([0,1,0])
        point2 = Dot([0,-2,0])
        point5 = Dot(Line(
            start = midpoint(point1.get_center(), point2.get_center()),
            end = Line(
                start = point1, 
                end = point2).scale(2.4).get_start()
            ).rotate(
                about_point= midpoint(point1.get_center(), point2.get_center()), angle = PI/2).get_end())
        self.add(point1)
        self.add(point2)
        line12 = Line(start = point1, end = point2).scale(1.7)
        line34 = Line(start = point1, end = point2).scale(1.6)
        point = Dot(line12.get_start())
        point7 = Dot(line12.get_end())
        self.add(line12)
        point3 = Dot(line12.get_start())
        point4 = Dot(line12.get_end())
        self.add(point3, point4, point5)
        
        arc1 = ArcBetweenPoints(point3.get_center(), point5.get_center())
        arc2 = ArcBetweenPoints(point5.get_center(), point4.get_center())
        arc3 = ArcBetweenPoints(point1.get_center(), point2.get_center())
        point6 = Dot(arc3.get_midpoint())
        circle = Circle.from_three_points(point1.get_center(), point2.get_center(), point6.get_center())
        angle1 = Line(start = circle.get_center(), end = point1.get_center()).get_angle()
        angle2 = Line(start = circle.get_center(), end = point2.get_center()).get_angle()
        point10 = Dot(circle.point_at_angle(angle1-0.37))
        point11 = Dot(circle.point_at_angle(angle2+0.37))
        arc11 = ArcBetweenPoints(point10.get_center(), point5.get_center())
        arc12 = ArcBetweenPoints(point5.get_center(), point11.get_center())        
        self.add(arc1, arc2, arc3, circle, point10, point11, arc11, arc12)
        self.wait()