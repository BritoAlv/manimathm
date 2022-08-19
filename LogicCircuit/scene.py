from manim import*



class conector:
	def __init__(self, point1, point2):
		self.obj = Line(start = point1.obj.get_center(), end = point2.obj.get_center())
		self.value = point1.value
		self.color = point1.color
		self.input = point1
		self.output = point2
		self.has_text = False
		self.objj = VGroup(self.obj)
		self.obj.set_color(self.color)
	def set_value(self):
		self.value = self.input.value	

class sec_conector:
	def __init__(self, point1, point2):
		# the math
		# center is [point1.obj.get_center[0]+point2.obj.get_center[0], point1.obj.get_center[1]+point2.obj.get_center[1], 0] 
		self.obj = ArcBetweenPoints(start = point1.obj.get_center(), end = point2.obj.get_center(), arc_center=[point1.obj.get_center()[0]/2+point2.obj.get_center()[0]/2, point1.obj.get_center()[1]/2+point2.obj.get_center()[1]/2, 0], angle=PI)
		self.value = point1.value
		self.color = point1.color
		self.input = point1
		self.output = point2
		self.has_text = False
		self.objj = VGroup(self.obj)
		self.obj.set_color(self.color)
	def set_value(self):
		self.value = self.input.value	
class point:
	def __init__(self, pos, value = 0, g = False, input = None):
		self.obj = Dot(pos)
		self.input = input
		self.output = None
		self.value = value
		self.color = RED if self.value == 0 else BLUE 
		self.text = MathTex(f"{self.value}").next_to(self.obj).shift(0.35*UP+0.6*LEFT).set_color(self.color)
		self.objj = VGroup(self.obj).set_color(self.color)
		self.input_dot = g
		self.has_text = True
	def set_value(self, value = 0):
		if self.input_dot:
			self.value = value
		else:
			self.value = self.value if self.input == None else self.input.value		
	def conect(self, otherpoint, use_arc = False):
		if(use_arc):
			con = sec_conector(self, otherpoint)
		else:
			con = conector(self, otherpoint)
		self.output = con
		otherpoint.input = con
		return con

class component_or:
	def __init__(self, point1, point2):
		self.obj = Dot(Line(
            start = midpoint(point1.obj.get_center(), point2.obj.get_center()),
            end = Line(
                start = point1.obj.get_center(), 
                end = point2.obj.get_center()).scale(2.4).get_start()
            ).rotate(
                about_point= midpoint(point1.obj.get_center(), point2.obj.get_center()), angle = PI/2).get_end())
		arc3 = ArcBetweenPoints(point1.obj.get_center(), point2.obj.get_center())
		point6 = Dot(arc3.get_midpoint())
		circle = Circle.from_three_points(point1.obj.get_center(), point2.obj.get_center(), point6.get_center())
		angle1 = Line(start = circle.get_center(), end = point1.obj.get_center()).get_angle()
		angle2 = Line(start = circle.get_center(), end = point2.obj.get_center()).get_angle()
		point10 = Dot(circle.point_at_angle(angle1-0.37))
		point11 = Dot(circle.point_at_angle(angle2+0.37))
		self.view1 = ArcBetweenPoints(point10.get_center(), self.obj.get_center())
		self.view2 = ArcBetweenPoints(self.obj.get_center(), point11.get_center())        
		self.view3 = Arc(arc_center=circle.get_center(), start_angle=angle1-0.37, angle = angle2+0.37-(angle1-0.37), radius = circle.radius) 
		self.input = [point1, point2]
		self.output = None
		self.value = 1 if (self.input[0].value == 1 or self.input[1].value == 1) else 0
		self.view = VGroup(self.view1, self.view2, self.view3)		
		self.color = RED if self.value == 0 else BLUE
		self.has_text = True 
		self.objj = VGroup(self.obj, self.view).set_color(self.color)
		self.text = MathTex(f"{self.value}").next_to(self.obj).shift(0.35*UP+0.6*LEFT).set_color(self.color)
	def set_value(self):
		self.value = self.value = 1 if (self.input[0].value  == 1 or self.input[1].value == 1) else 0	

	def conect(self, otherpoint, use_arc = False):
		if(use_arc):
			con = sec_conector(self, otherpoint)
		else:
			con = conector(self, otherpoint)
		self.output = con
		otherpoint.input = con
		return con	
class component_and:
	def __init__(self, point1, point2):
		self.obj = Dot(Line(
            start = midpoint(point1.obj.get_center(), point2.obj.get_center()),
            end = Line(
                start = point1.obj.get_center(), 
                end = point2.obj.get_center()).scale(2.4).get_start()
            ).rotate(
                about_point= midpoint(point1.obj.get_center(), point2.obj.get_center()), angle = PI/2).get_end())
		line12 = Line(start = point1.obj.get_center(), end = point2.obj.get_center()).scale(1.7)
		point3 = Dot(line12.get_start())
		point4 = Dot(line12.get_end())
		self.view1 = Line(start = point1.obj.get_center(), end = point2.obj.get_center()).scale(1.7)
		self.view2 = ArcBetweenPoints(point3.get_center(), self.obj.get_center())
		self.view3 = ArcBetweenPoints(self.obj.get_center(), point4.get_center())
		self.input = [point1, point2]
		self.output = None
		self.value = 1 if (self.input[0].value == 1 and self.input[1].value == 1) else 0
		self.view = VGroup(self.view1, self.view2, self.view3)		
		self.color = RED if self.value == 0 else BLUE
		self.has_text = True 
		self.objj = VGroup(self.obj, self.view).set_color(self.color)
		self.text = MathTex(f"{self.value}").next_to(self.obj).shift(0.35*UP+0.6*LEFT).set_color(self.color)
	def set_value(self):
		self.value = self.value = 1 if (self.input[0].value == 1 and self.input[1].value == 1) else 0
	def conect(self, otherpoint, use_arc = False):
		if(use_arc):
			con = sec_conector(self, otherpoint)
		else:
			con = conector(self, otherpoint)
		self.output = con
		otherpoint.input = con
		return con
		
class component_not:
	def __init__(self, spoint1):
		p1 = [spoint1.obj.get_center()[0] + 0.4  , spoint1.obj.get_center()[1],0]
		p2 = [spoint1.obj.get_center()[0], spoint1.obj.get_center()[1]+ 0.3 ,0]
		p3 = [spoint1.obj.get_center()[0], spoint1.obj.get_center()[1] -0.3 ,0]
		self.obj = Dot(p1)
		self.input = spoint1
		self.output = None
		self.value = 0 if self.input.value == 1 else 1
		self.view1 = Line(start = p1 , end = p2)
		self.view2 = Line(start = p2, end = p3)
		self.view3 = Line(start = p3, end = p1)
		self.view = VGroup(self.view1, self.view2, self.view3)
		self.color = RED if self.value == 0 else BLUE
		self.has_text = True
		angle = 0 if self.input.input == None else self.input.input.obj.get_angle() 
		self.objj = VGroup(self.obj, self.view).rotate(angle= angle, about_point = self.input.obj.get_center()).set_color(self.color)
		self.text = MathTex(f"{self.value}").next_to(self.obj).shift(0.35*UP+0.6*LEFT).set_color(self.color)
	def set_value(self):
		self.value = 0 if self.input.value == 1 else 1
	def conect(self, otherpoint, use_arc = False):
		if(use_arc):
			con = sec_conector(self, otherpoint)
		else:
			con = conector(self, otherpoint)
		self.output = con
		otherpoint.input = con
		return con

	

	
							

# idea of circuit first define input dots, this don't have self.input becuase it's values need to be updated, the idea is update every object in some order, but the value of input_dots have to be udated passing the vale instead of going to self.input.values

class A(MovingCameraScene):
	def construct(self):
		self.camera.frame.move_to([3,3,0])
		tex = Tex("AAA")
		inputs = []
		objects = []
		pointB = point([0,0,0], input = [1,0,1,0], g = True )
		pointA = point([0,3,0],input = [0,0,1,0], g = True )
		inputs.append(pointB)
		inputs.append(pointA)
		objects.append(pointB)
		objects.append(pointA)
		point1 = point([0,0.6,0])
		lineB1 = pointB.conect(point1)
		objects.append(lineB1)
		objects.append(point1)
		point2 = point([2,0.6,0])
		line12 = point1.conect(point2)
		objects.append(line12)
		objects.append(point2)
		point3 = point([0,2.4,0])
		line13 = point1.conect(point3)
		objects.append(line13)
		objects.append(point3)
		point4 = point([2,2.4,0])
		line34 = point3.conect(point4)
		objects.append(line34)
		objects.append(point4)
		point5 = point([1,3,0])
		lineA5 = pointA.conect(point5)
		objects.append(lineA5)
		objects.append(point5)
		point6 = point([2,3,0])
		line56 = point5.conect(point6)
		objects.append(line56)
		objects.append(point6)
		point7 = point([1,2.6,0])
		line57 = point5.conect(point7)
		objects.append(line57)
		objects.append(point7)
		point8 = point([1,2.2,0])
		line78 = point7.conect(point8, use_arc = True)
		objects.append(line78)
		objects.append(point8)
		point9 = point([1,1.2,0])
		line89 = point8.conect(point9)
		objects.append(line89)
		objects.append(point9)
		point10 = point([2,1.2,0])
		line910 = point9.conect(point10)
		objects.append(line910)
		objects.append(point10)
		point11 = component_or(point2, point10)
		objects.append(point11)
		point12 = component_or(point4, point6)
		objects.append(point12)
		point13 = point([point11.obj.get_center()[0]+2,point11.obj.get_center()[1],0])
		line1113 = point11.conect(point13)
		objects.append(line1113)
		objects.append(point13)
		point14 = point([point13.obj.get_center()[0]+2,point13.obj.get_center()[1],0])
		line1314 = point13.conect(point14)
		objects.append(line1314)
		objects.append(point14)
		point15 = point([point12.obj.get_center()[0]+1,point12.obj.get_center()[1],0])
		line1215 = point12.conect(point15)
		objects.append(line1215)
		objects.append(point15)
		point151 = point([point15.obj.get_center()[0]+1,point15.obj.get_center()[1],0])
		line15151 = point15.conect(point151)
		objects.append(line15151)
		objects.append(point151)
		point16 = component_not(point151)
		objects.append(point16)
		point17 = point([point13.obj.get_center()[0],point13.obj.get_center()[1]+0.6,0])
		line1617 = point16.conect(point17)
		objects.append(line1617)
		objects.append(point17)
		point18 = point([point17.obj.get_center()[0]+2,point17.obj.get_center()[1],0])
		line1718 = point17.conect(point18)
		objects.append(line1718)
		objects.append(point18)
		point19 = component_or(point14, point18)
		objects.append(point19)
		for object in objects:
			self.play(Create(object.objj))
			if object.has_text:
				self.play(Create(object.text))
		self.wait()
		textt = Tex("Comienza")
		self.play(FadeIn(textt))
		self.play(FadeOut(textt))
		for i in range(0, 2): 
			textt = Tex("Comienza")
			self.play(FadeIn(textt))
			self.play(FadeOut(textt))
			for ob in objects:
				temp = ob.value
				if ob in inputs:
					ob.set_value(ob.input[i])
				else:
					ob.set_value()	
				if (temp != ob.value):
					# if the value of the object changed we need to update its text and its color.
					# there are objects that do not have text
					ob.color = RED if ob.value == 0 else BLUE
					if ob.has_text:
						self.play(FadeOut(ob.text))
						ob.text = MathTex(f"{ob.value}").next_to(ob.obj).shift(0.35*UP+0.6*LEFT).set_color(ob.color)
						self.play(FadeToColor(ob.objj, ob.color), FadeIn(ob.text))
					else:
						self.play(FadeToColor(ob.objj, ob.color))
			self.play(FadeIn(tex))
			self.wait()
			self.play(FadeOut(tex))						
	