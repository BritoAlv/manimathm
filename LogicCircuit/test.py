from ast import For
from manim import*
#global variable.
groups = [[],[],[]] # number of grupos de la animación.
# input dots at group 0
objects = [] # don't change this. 
#global variable.

class circuit_component: # general class with shared properties.
	def __init__(self, group, text):
		self.obj = None
		self.is_cyclic = False
		self.value = None
		self.persist = False
		self.input = None
		self.color = WHITE
		self.show_text = text
		self.text = None
		self.objj = None	
	def get_x(a):
		return a.obj.get_center()[0]
	def get_y(a):
		return a.obj.get_center()[1]
	def set_text(self):
		self.text = MathTex(f"{self.value}").next_to(self.obj.get_center())

class input_dot(circuit_component): # a dot that receives input designed for start of the ciruit.
	def __init__(self, pos, group , input = [0], text= False ): # input has to be a list.
		circuit_component.__init__(self, group, text)
		self.obj = Dot(pos)
		self.input = input
		self.objj = VGroup(self.obj).set_color(WHITE)
		objects.append(self)
		groups[group].append(self)
	def set_value(self, value):
		self.value = value

class dot(circuit_component): # a simple dot, designed and only can be used to join different parts of the circuit.
	def __init__(self, pos, group , component_to_connect, use_arc = False, text= False): #  
		circuit_component.__init__(self, group, text)
		self.obj = Dot(pos)
		self.input = component_to_connect
		if use_arc:
			self.view1 = ArcBetweenPoints(start = component_to_connect.obj.get_center(), end = self.obj.get_center(), arc_center=[component_to_connect.obj.get_center()[0]/2+self.obj.get_center()[0]/2, component_to_connect.obj.get_center()[1]/2+self.obj.get_center()[1]/2, 0], angle=PI)
		else:
			self.view1 = Line(start = component_to_connect.obj.get_center(), end = self.obj.get_center())
		self.view = VGroup(self.view1)
		self.objj = VGroup(self.obj, self.view).set_color(WHITE)
		objects.append(self)
		groups[group].append(self)
	def set_value(self):
		self.value = self.input.value

class cyclic_dot(circuit_component):
	'''
	a dot that allow cycles in the circuit, first it is used with a default value in after that it uses
	the value passed to it in its input, a cyclic dot, need an input before render the scene by definition
	so connect to something it, check example in scene.

	This was designed to be able to implement "Prestamo o Arrastre " in the Add Circuit.

	Notice that the value of the cyclic dot persist, ie, when the input change at input dots the value of
	the cyclic dot is the same, to change this behaviour so that each time change input ar input dots the 
	cyclic dot use its defualt value, set persist option to false when creating the dot.
 

	'''
	def __init__(self, pos, group , input = 0, text= False, persist = True ): # input has to be a list.
		circuit_component.__init__(self, group, text)
		self.obj = Dot(pos)
		self.input = None
		self.is_cyclic = True
		self.persist = persist
		self.default_input = input
		self.used_default_input = False
		self.objj = VGroup(self.obj).set_color(WHITE)
		objects.append(self)
		groups[group].append(self)

	def update_view(self, group, component_to_connect, use_arc = False):
		if use_arc:
			self.view1 = ArcBetweenPoints(start = component_to_connect.obj.get_center(), end = self.obj.get_center(), arc_center=[component_to_connect.obj.get_center()[0]/2+self.obj.get_center()[0]/2, component_to_connect.obj.get_center()[1]/2+self.obj.get_center()[1]/2, 0], angle=PI)
		else:
			self.view1 = Line(start = component_to_connect.obj.get_center(), end = self.obj.get_center())
		self.view = VGroup(self.view1).set_color(WHITE)
		groups[group].append(self)
		component_to_connect.objj.add(self.view)
		self.input = component_to_connect			
	def set_value(self):
		if(self.used_default_input == False):
			self.value = self.default_input
			self.used_default_input = True
		else:
			self.value = self.input.value
			if (self.persist == False):
				 self.used_default_input == False


class comp_or(circuit_component): # or component
	def __init__(self, point1, point2, group, text= False ):
		circuit_component.__init__(self, group, text)
		self.obj = Dot(Line(
            start = midpoint(point1.obj.get_center(), point2.obj.get_center()),
            end = Line(
                start = point1.obj.get_center(), 
                end = point2.obj.get_center()).scale(2.4).get_start()
            ).rotate(
                about_point= midpoint(point1.obj.get_center(), point2.obj.get_center()), angle = PI/2).get_end())
		self.input = [point1, point2]
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
		self.view = VGroup(self.view1, self.view2, self.view3)		 
		self.objj = VGroup(self.obj, self.view).set_color(WHITE)
		objects.append(self)
		groups[group].append(self)

	def set_value(self):
		self.value = self.value = 1 if (self.input[0].value  == 1 or self.input[1].value == 1) else 0	

 
class comp_and(circuit_component): # and component
	def __init__(self, point1, point2, group, text= False ):
		circuit_component.__init__(self, group, text)
		self.obj = Dot(Line(
            start = midpoint(point1.obj.get_center(), point2.obj.get_center()),
            end = Line(
                start = point1.obj.get_center(), 
                end = point2.obj.get_center()).scale(2.4).get_start()
            ).rotate(
                about_point= midpoint(point1.obj.get_center(), point2.obj.get_center()), angle = PI/2).get_end())
		self.input = [point1, point2]
		line12 = Line(start = point1.obj.get_center(), end = point2.obj.get_center()).scale(1.7)
		point3 = Dot(line12.get_start())
		point4 = Dot(line12.get_end())
		self.view1 = Line(start = point1.obj.get_center(), end = point2.obj.get_center()).scale(1.7)
		self.view2 = ArcBetweenPoints(point3.get_center(), self.obj.get_center())
		self.view3 = ArcBetweenPoints(self.obj.get_center(), point4.get_center())
		self.view = VGroup(self.view1, self.view2, self.view3)		
		self.objj = VGroup(self.obj, self.view).set_color(WHITE)
		objects.append(self)
		groups[group].append(self)

	def set_value(self):
		self.value = self.value = 1 if (self.input[0].value  == 1 and self.input[1].value == 1) else 0	


class comp_not(circuit_component): #not component
	def __init__(self, group , component_to_connect, use_arc = False, text= False ): #  
		circuit_component.__init__(self, group, text)
		self.obj = Dot([component_to_connect.get_x()+0.5, component_to_connect.get_y(), 0])
		self.input = component_to_connect
		self.view2 = Line(start = self.obj.get_center(), end = [self.obj.get_center()[0]-0.5,self.obj.get_center()[1]+0.3,0])
		self.view3 = Line(start = self.obj.get_center(), end = [self.obj.get_center()[0]-0.5,self.obj.get_center()[1]-0.3,0])
		self.view4 = Line(start = self.view2.get_end(), end = self.view3.get_end())	
		self.view = VGroup(self.view2, self.view3, self.view4)
		try:
			the_angle = Line(start = component_to_connect.input.obj.get_center() , end = component_to_connect.obj.get_center()).get_angle()
		except:
			the_angle = 0			
		self.objj = VGroup(self.obj, self.view).rotate(about_point=component_to_connect.obj.get_center(), angle = the_angle ).set_color(WHITE)
		objects.append(self)
		groups[group].append(self)
	def set_value(self):
		self.value = 0 if self.input.value == 1 else 1


class A(Scene):
	def construct(self):
		################################################################
		### objects need to be defined in order.
		### the scene will be updated group by group put each object in
		### its group, cyclic and input dots are in the first group always.
		### to add an input to an cyclic dot call the method update_view, 
		### passing as arguments the new group where it will be and the component 
		### uncomment one of the scenes to render it.
		### at top of page is a global variable "groups", modify it with
		### the numbers of groups in your animation.
		### diference of an cyclic dot and an input dot is that cyclic dote have 
		### input, so they work in the following way, first time is used a default value for
		### them and after that is value is determined by the circuit and the input appended to it.
		################################################################
		input_size = 1
		"""
		Scene Example 1
		input_size = 3 # your input dots have input of len 3 		
		a = input_dot([1,1,0],0, [1,1,0], text = True)
		b = dot([2,1,0],1, a)
		c = input_dot([1,2,0],0, [1,0,1], text = True)
		d = dot([2,2,0], 1, c)
		e = comp_and(b,d,1, text = True)
		f = dot([e.get_x()+1,e.get_y(),0], 2, e)
		g = comp_not(2, f, text = True)
		h = dot([g.get_x()+0.4, g.get_y()-0.3, 0], 2, g)
		l = comp_not(2, h, text = True)
		"""

		
		
		input_size = 3 # your input dots have input of len 2
		a = cyclic_dot( [0,0,0], 0, input = 1)
		b = dot([1,0,0], 1, a)
		c = comp_not(1, b)
		d = dot([1,1,0], 2, c )
		e = dot([0,1,0], 2, d)
		a.update_view(2, e)
		

		################################################################
		#### don't change anything below
		################################################################

		# first step is to add all objects to scene
		not_cyclic_objects = []
		cyclic_not_persistent = []
		for ob in objects:
			self.add(ob.objj)
			if (ob.is_cyclic == True and ob.persist == False):
				cyclic_not_persistent.append(ob)
			if (ob.is_cyclic == True and ob.persist == True):
				pass
			else:
				not_cyclic_objects.append(ob)
		
		self.wait()
		# animation steps
		# animate each group with starting values given by the inputs.
		# obtain values
		for i in range(0, input_size): # 2 because the input is of size 3
			for j in range(0, len(groups)):
				if j == 0: # we are dealing with input dots
					for obj in groups[j]:
						if(obj.is_cyclic == True):
							# obj is an cyclic circuit component object
							obj.set_value()
							 # we update only once the value of the cyclic dot.
						else:
							# obj is an circuit component object
							obj.set_value(obj.input[i])
							obj.set_text()								
				else:
					for obj in groups[j]:
							obj.set_value()
							obj.set_text()
				# after all objects in same group have its values updated
				# we have to update its text and its color with an animation and that's all
				# the value was updated so this mean that we have to update its color and text
				self.play(AnimationGroup(*[FadeToColor(obj.objj, (RED if obj.value == 0 else BLUE))  for obj in groups[j]]))
				temp = []
				for obj in groups[j]:
					if obj.show_text:
						temp.append(obj)
				self.play(AnimationGroup(*[(Create(obj.text)) for obj in temp]))
			# now we need to put everything to the original state without text, and without colors
			
			self.play(AnimationGroup(*[FadeToColor(obj.objj, WHITE)  for obj in not_cyclic_objects]))
			self.wait()
			temp = []
			for obj in objects:
				if obj.show_text:
					temp.append(obj)			
			self.play(AnimationGroup(*[(FadeOut(obj.text)) for obj in temp]))
			for ob in cyclic_not_persistent:
				ob.used_default_input = False

					
						
					


			
