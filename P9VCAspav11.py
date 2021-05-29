from manim import *
from math import *
class P4(MovingCameraScene):
	def construct(self):    #Subclase de Scene que permite mover la posición de la cámara
		'''
		Lo primero que voy a crear es el plano y su configuración, 
		    self.axis_config = {
            "stroke_color": WHITE,
            "stroke_width": 2,
            "include_ticks": False,
            "include_tip": False,
            "line_to_number_buff": SMALL_BUFF,
            "label_direction": DR,
            "number_scale_value": 0.5,
        }
        self.y_axis_config = {"label_direction": DR}
        self.background_line_style = {
            "stroke_color": BLUE_D,
            "stroke_width": 2,
            "stroke_opacity": 1,
        }
		'''
		plane = ComplexPlane(
			y_range = (-30, 30),
			x_range=(-30, 30),
			background_line_style = {"stroke_opacity": 0.3, "stroke_color": BLUE_B}, 
			axis_config = {"stroke_color": BLUE_D, "include_tip": True} )
		'''
		Modifico la posición de la cámara
		'''
		self.camera.frame.save_state()
		self.camera.frame.move_to([2,4,0]),
		self.camera.frame.set(width=16, height=13)
		self.add(plane)
		'''
		Ahora voy a añadir dos flechas para indicar que esos son los ejes, y también una etiqueta que
		diga eje y es i, eje x es R. Notemos que cuando definimos la posición de un objeto, el plano
		en que son definidas estas posiciones no es el "plane" definido por mi, en otras palabras 
		cuando rote el plano, para rotar las flechas tengo que rotarlas a ellas también, los updaters
		no sirven
		'''
		flechaejey = Arrow([0,9.1,0], [0,10.1,0], buff=0, stroke_width=2).set_color(BLUE_D)
		flechaejey.label = MathTex("i").set_color(YELLOW).next_to([0,10,0], RIGHT).scale(1.4)
		
		flechaejex = Arrow([12,0,0], [13,0,0], buff=0, stroke_width=2).set_color(BLUE_D)
		flechaejex.label = MathTex("\\mathbb{R^{+}}").set_color(GOLD_B).next_to([13,0,0], DOWN).scale(1.4)
		self.play(
			Create(flechaejey),
			Create(flechaejey.label),
			Create(flechaejex),
			Create(flechaejex.label))
		'''
		Ahora voy a empezar a escribir el enunciado del ejercicio, primero voy a hacer un tex_template
		para modificar la letra que viene por defecto en latex
		'''
		myTemplate = TexTemplate()
		myTemplate.add_to_preamble(r"\usepackage{helvet}")
		myTemplate.add_to_preamble(r"\renewcommand{\sfdefault}{lmss}")
		myTemplate.add_to_preamble(r"\renewcommand{\familydefault}{\sfdefault}")

		'''
		Ahora voy a escribir el enunciado usando arrays o listas, con el comando de latex "mbox",
		su objetivo es escribir texto normal en modo matemático en un espacio suficientemente ancho
		'''
		enunciado1 = MathTex(
			r"\mbox{Sea }",
			r"L",
			r"\mbox{ una línea en }",
			r"\mathbb{C }",
			r"\mbox{ que}", tex_template=myTemplate)
		enunciado2 = MathTex(
			r"\mbox{forma un ángulo }",
			r"\phi",
			r"\mbox{ con el eje }",
			r"x", tex_template=myTemplate)
		enunciado3 = MathTex(
			r"\mbox{Sea }",
			"d",
			r"\mbox{ la distancia de }",
			r"L",
			r"\mbox{ al}", tex_template=myTemplate)
		enunciado4 = MathTex(
			r"\mbox{origen de coordenadas. Si }",
			"z",
			r"\mbox{ es }", tex_template=myTemplate)
		enunciado5 = MathTex(
			r"\mbox{cualquier }",
			r"\mbox{punto en }",
			"L",
			r"\mbox{,}", tex_template=myTemplate)
		enunciado6 = MathTex(
			r"\mbox{Probar que:}", tex_template=myTemplate)

		enunciado1[1].set_color(GREEN)        #L
		enunciado2[1].set_color(RED)          #phi
		enunciado3[1].set_color(ORANGE)       #d
		enunciado3[3].set_color(GREEN)        
		enunciado4[1].set_color(BLUE)         #z
		enunciado5[2].set_color(GREEN)
		enunciado = VGroup(
			enunciado1, 
			enunciado2, 
			enunciado3, 
			enunciado4, 
			enunciado5, 
			enunciado6).scale(1.4)
		enunciado.arrange(DOWN, aligned_edge = LEFT, buff = MED_SMALL_BUFF)
		enunciado.shift(7.6*UP+4.65*LEFT)
		
		'''
		ya el enunciado esta listo para ponerse en la pantalla, ahora voy a
		crear la fórmula
		'''
		formula = MathTex("d", "=", "\\vert", "Im", "(", "z", "\\cdot", "e^", "{", "-i", "\\phi", "}", ")", "\\vert" )
		formula.scale(1.6)
		formula[0].set_color(ORANGE)
		formula[5].set_color(BLUE)
		formula[10].set_color(RED)
		formula.shift(4.1*UP+5.25*LEFT)
		'''
		ahora empezaré a definir los objetos geométricos que conforman la figura
		'''
		lineaL = Line([-10, -3, 0], [8, 11, 0]).set_color(GREEN)
		angulo = Angle(
			lineaL, Line([-20, 0, 0],[20, 0 , 0]),
			other_angle=True, 
			radius=1.3, 
			color = RED, 
			stroke_width=10)
		angulo.label = MathTex("\\phi").scale(1.4).next_to(angulo.point_from_proportion(0.3)).set_color(RED)
		'''
		la funcion line_intersection() no funciona asi que hallaré las coordenadas a mano.
		'''
		lineaLcapejex = Dot(
			[-43/7,0,0],  
			radius=DEFAULT_DOT_RADIUS*1.5).set_color(PURPLE)
		Origen = Dot(
			[0,0,0],  
			radius=DEFAULT_DOT_RADIUS*1.5).set_color(PURPLE)
		prORIGENlineaD = Dot(
			lineaL.get_projection(ORIGIN),
			 radius=DEFAULT_DOT_RADIUS*1.5).set_color(PURPLE)
		linead = Line(ORIGIN, prORIGENlineaD.get_center()).set_color(ORANGE)
		'''
		Para representar el angulo recto entre d y lineaL
		'''
		lineangrecto1 = Line([-1.96, 2.52, 0] , [-1.51, 2.88, 0])
		lineangrecto2 = Line([-1.86, 3.33, 0] , [-1.51, 2.88, 0])
		lineangrecto = VGroup(lineangrecto1, lineangrecto2).set_color(GOLD_A)
		'''
		Lo de arriba
		'''
		puntoz = Dot(lineaL.point_from_proportion(0.3), radius=DEFAULT_DOT_RADIUS*1.5).set_color(BLUE)
		puntoz.label = MathTex("z").set_color(BLUE).scale(1.4).next_to(puntoz, UP)
		puntoz.label.add_updater(
			lambda x: x.become(MathTex("z").set_color(BLUE).scale(1.4).next_to(puntoz, UP)))
		puntoz.flecha = Arrow([0,0,0], puntoz.get_center(), buff=0).set_color(BLUE_C)
		puntoz.flecha.add_updater(
			lambda x: x.become(Arrow([0,0,0], puntoz.get_center(), buff=0).set_color(BLUE_C)))
		'''
		Hasta ahora están definidos los objetos principales de la figura, faltaría añadirlos a la pantalla
		'''
		

		self.wait()
		for i in range(0,5):
			if i ==1 :
				self.play(Create(enunciado1[i]), Create(lineaL))
			else:
				self.play(Write(enunciado1[i]))

		for i in range(0,4):
			if i ==1 :
				self.play(
					Create(enunciado2[i]), 
					Create(angulo), 
					Create(angulo.label), 
					Create(Origen),
					Create(lineaLcapejex))
			else:
				self.play(Write(enunciado2[i]))

		for i in range(0,5):
			if i == 1 :
			    self.play(
			    	Create(enunciado3[i]),
			    	Create(linead))
			if i == 3 :
			    self.play(
			    	Create(enunciado3[i]),
			    	Create(lineangrecto),
			    	Create(prORIGENlineaD))
			if i in [0,2,4]:
			    self.play(Write(enunciado3[i]))

		for i in range(0,3):
			if i==1:
				self.play(
					Create(enunciado4[i]),
					Create(puntoz),
					Create(puntoz.label),
					Create(puntoz.flecha))
			else:
				self.play(Write(enunciado4[i]))

		for i in range(0,4):
			if i == 2:
				self.play(
					Write(enunciado5[i]),
					puntoz.animate.move_to(lineaL.point_from_proportion(0.9))
					)
				self.play(puntoz.animate.move_to(lineaL.point_from_proportion(0.75)))
			if i == 3:
				self.play(
				Create(enunciado5[i])
				)
			if i in [0,1]:
				self.play(Write(enunciado5[i]))			    				    				
		self.play(Write(enunciado6[0]))
		   
		'''
		A partir de aka el codigo en español es el mismo en ingles, y este es
		el fin de las animaciones introduciendo el enunciado.
		Empieza ahora la fórmula.
		'''
		
		self.play(
			Write(formula[0]), 
			Write(formula[1]))
		self.play(
			Write(formula[2]), 
			Write(formula[-1]))
		self.play(
			Write(formula[3]),
			Write(formula[4]),
			Write(formula[-2]))
		self.play(
			Write(formula[5]),
			Write(formula[6]),
			Write(formula[7]),
			Write(formula[8]),
			Write(formula[9]),
			Write(formula[10]),
			Write(formula[11]),
			)
		self.wait()
		self.wait()
		self.wait()
		
		'''
		Se acaba la introducción de la formula. Ahora empieza la animación
		que demuestra que el modulo de e^-iphi es 1. 
		'''
		
		exp = VGroup(
			formula[7].copy(), 
			formula[8].copy(), 
			formula[9].copy(),
			formula[10].copy(),
			formula[11].copy())
		expf = MathTex(
			"\\vert",
			"e^",
			"{",
			"-i",
			"\\phi",
			"}",
			"\\vert",
			"=",
			"\\vert",
			"\\cos",
			"{(-",
			"\\phi",
			")}",
			"+",
			"i\\sin",
			"{(-",
			"\\phi",
			")}",
			"\\vert",
			"1",
			tex_template = myTemplate)
		euler = VGroup(expf[1], expf[2], expf[3], expf[4], expf[5])
		expf.scale(1.6)
		expf.copy = MathTex("\\vert","e^","{","-i","\\phi","}","\\vert","=","\\vert","\\cos","{(-","\\phi",")}","+","i\\sin","{(-","\\phi",")}","\\vert",tex_template = myTemplate).scale(1.6).next_to([2.5,4,0])
		expf[-4].set_color(RED)
		expf[4].set_color(RED)
		expf[11].set_color(RED)
		expf.next_to([2.5,4,0])
		self.play(
			exp.animate.next_to([2.5,4,0]),
			Transform(exp, euler ))
		self.play(
			Write(expf[7]),
			Write(expf[9]),
			Write(expf[13]),
			Write(expf[14]))
		self.play(
			Write(expf[15]),
			Write(expf[16]),
			Write(expf[17]),
			Write(expf[10]),
			Write(expf[11]),
			Write(expf[12]))
		self.wait()
		expf.rectangulo = BackgroundRectangle(
			mobject=expf.copy, 
			color=RED, 
			stroke_width=2, 
			stroke_opacity=1, 
			fill_opacity=0, 
			buff=0.2)
		self.play(FadeIn(expf.rectangulo))
		self.wait()
		self.play(
			Write(expf[0]),
			Write(expf[6]))
		self.play(
			Write(expf[8]),
			Write(expf[-2]))
		trig = VGroup()
		for i in range(8,19): 
			trig.add(expf[i])
		pitagoras = MathTex(
			"\\cos^2",
			"{(-",
			"\\phi",
			")}",
			"+",
			"\\sin^2",
			"{(-",
			"\\phi",
			")}")
		pitagoras.scale(1.6)
		pitagoras[2].set_color(RED)
		pitagoras[7].set_color(RED)
		pitagoras.next_to([2.5,4,0]).shift(3*RIGHT)
		self.play(FadeOut(expf.rectangulo),Transform(trig, pitagoras))
		self.wait()
		self.remove(trig)
		self.play(Transform(pitagoras, expf[-1].shift(7.8*LEFT)))
		self.wait()
		
		'''
		Aka se acaba la animación que explica que el modulo de e es 1,
		empieza ahora la creacion de un vector unitario y su rotacion
		para hallar el vector e^-i\\phi
		'''
		
		unit = Arrow(ORIGIN, [3.6,0,0], buff=0).set_color(PINK)
		unit.brace = Brace(unit, direction=UP, buff=0.1)
		unit.texto = MathTex("1").next_to(unit.brace, UP)
		self.play(
			Create(unit),
			Create(unit.brace),
			Create(unit.texto))
		unitrot = unit.copy()
		self.add(unitrot)
		self.play(
			unitrot.animate.rotate(
				angle=(angulo.angle)/100,
				about_point=ORIGIN))
		unit.angulop = Angle(unit, unitrot, radius=1.3, color = RED, stroke_width=10, other_angle=True)
		unit.angulop.add_updater(lambda x: x.become(Angle(unit, unitrot, radius=1.3, color = RED, stroke_width=10, other_angle=True)))
		unit.angulog = Angle(unit, unitrot, radius=3.55, color = WHITE, stroke_width=2.5, other_angle=True)
		unit.angulog.add_updater(lambda x: x.become(Angle(unit, unitrot, radius=3.55, other_angle=True, color = WHITE, stroke_width=2.5)))
		self.add(unit.angulop, unit.angulog)
		self.play(unitrot.animate.rotate(angle=99/100*(angulo.angle), about_point=ORIGIN).set_color(RED))
		self.wait()
		unit.angulop.clear_updaters()
		unit.angulog.clear_updaters()
		unit.angulop.label = MathTex("\\phi").set_color(RED).next_to(unit.angulop.point_from_proportion(0.65)).scale(1.2)
		self.play(Write(unit.angulop.label))
		unitrot.brace = Brace(unitrot, buff=0.1, direction=unitrot.copy().rotate(3*PI/2).get_unit_vector()).shift(0.2*UP+0.1*LEFT)
		unitrot.label = MathTex("e^","{-i \\cdot", "\\phi","}").next_to(unitrot.brace, LEFT).scale(1.3).shift(1.4*RIGHT+0.65*DOWN)
		unitrot.label[2].set_color(RED)
		self.play(FadeIn(unitrot.brace), FadeIn(unitrot.label))
		self.wait()
		self.wait()
		expff = VGroup()
		for i in range(0,8):
			expff.add(expf[i])
		self.play(
			FadeOut(unitrot.brace),
			FadeOut(unitrot.label),
			FadeOut(unit.brace),
			FadeOut(unit.texto),
			FadeOut(unit.angulog),
			FadeOut(unit.angulop.label),
			Unwrite(expff),
			Unwrite(exp),
			Unwrite(pitagoras))
		self.wait()
		
		'''
		Aka la animacion anterior acaba y ahora esta lista para rotar
		el plano
		'''
		


		puntoz.flecha.clear_updaters()   
		puntozrotflecha = puntoz.flecha.copy()
		cartelangulo = Angle(unit, unitrot, other_angle=True).scale(2.5).shift(8*UP+10*RIGHT).set_color(RED).add_tip()
		cartelangulo.label = MathTex("- \\phi").set_color(RED).scale(1.7).next_to(cartelangulo, RIGHT)
		self.wait()
		self.play(
			Create(cartelangulo),
			Create(cartelangulo.label), run_time=0.5)
		self.play(
			FadeOut(flechaejey),
			FadeOut(flechaejex),
			FadeOut(flechaejex.label),
			FadeOut(flechaejey.label),
			plane.animate.rotate(angle=(angulo.angle)/1000, about_point=ORIGIN),
			run_time=0.5)
		puntozrotflecha.rotate(angle=(angulo.angle)/1000, about_point=ORIGIN)
		puntoz.anglep = Angle(puntoz.flecha, puntozrotflecha, radius=1.3, color = RED, stroke_width=10, other_angle=True)
		puntoz.anglep.add_updater(lambda x: x.become(Angle(puntoz.flecha, puntozrotflecha, radius=1.3, color = RED, stroke_width=10, other_angle=True)))
		puntoz.angleg = Angle(puntoz.flecha, puntozrotflecha, radius=puntoz.flecha.get_length(), color = WHITE, stroke_width=2.5, other_angle=True)
		puntoz.angleg.add_updater(lambda x: x.become(Angle(puntoz.flecha, puntozrotflecha, radius=puntoz.flecha.get_length(), color = WHITE, stroke_width=2.5, other_angle=True)))
		self.add(puntoz.anglep, puntoz.angleg)
		self.play(
			FadeIn(puntozrotflecha),
			FadeOut(angulo),
			FadeOut(angulo.label))
		self.play(
			plane.animate.rotate(angle=999/1000*(angulo.angle), about_point=ORIGIN),
			puntozrotflecha.animate.rotate(angle=999/1000*(angulo.angle), about_point=ORIGIN), 
			run_time=2.5)
		puntozrotlabel = MathTex("z'").next_to(puntozrotflecha.get_end(), RIGHT).set_color(PURPLE).scale(1.4)
		self.play(
			Create(puntozrotlabel),
			puntozrotflecha.animate.set_color(PURPLE),
			run_time=0.8)
		cartelpuntozrotangleg = Angle(unit, unitrot, other_angle=True).scale(2.5).next_to(cartelangulo, DOWN, buff=DEFAULT_MOBJECT_TO_MOBJECT_BUFFER*1.25).set_color(RED).add_tip(at_start=True)
		cartelpuntozrotangleg.label = MathTex(" \\phi").set_color(RED).scale(1.7).next_to(cartelpuntozrotangleg, RIGHT)
		self.play(FadeIn(cartelpuntozrotangleg), FadeIn(cartelpuntozrotangleg.label))
		self.play(
			plane.animate.rotate(angle= -(angulo.angle), about_point=ORIGIN), run_time=2.5)
		self.play(FadeIn(angulo), FadeIn(angulo.label))
		puntoz.anglep.clear_updaters()
		puntoz.angleg.clear_updaters()
		self.play(
			FadeIn(flechaejey),
			FadeIn(flechaejex),
			FadeIn(flechaejex.label),
			FadeIn(flechaejey.label),
			FadeOut(cartelangulo), 
			FadeOut(cartelangulo.label),
			FadeOut(cartelpuntozrotangleg), 
			FadeOut(cartelpuntozrotangleg.label))
		puntozrot = Dot(puntozrotflecha.get_end(), radius=DEFAULT_DOT_RADIUS*1.5).set_color(PURPLE)
		self.play(FadeOut(unit.angulop))
		self.play(Create(puntozrot), FadeOut(unit), FadeOut(unitrot))
		self.wait()
		'''
		Aka se acaba la animacion anterior, seguimos..
		'''
		defz = puntozrotlabel.copy()
		defzprima = MathTex(
			"=", 
			"z", 
			"\\cdot", 
			"e^",
			"{",
			"-i",
			"\\phi",
			"}",)
		defzprima.scale(1.4*1.4)
		defzprima[1].set_color(BLUE)
		defzprima[-2].set_color(RED)
		self.play(
			Create(defz),
			defz.animate.shift(2*UP+0.5*RIGHT).scale(1.4),
			)
		defzprima.next_to(defz, RIGHT)
		self.play(
			Write(defzprima[0]),
			Write(defzprima[1]),
			Write(defzprima[2]),
			Write(defzprima[3]),
			Write(defzprima[4]),
			Write(defzprima[5]),
			Write(defzprima[6]),
			Write(defzprima[7])
			)
		self.wait()
		self.play(
			Unwrite(defzprima[0]),
			Unwrite(defzprima[1]),
			Unwrite(defzprima[2]),
			Unwrite(defzprima[3]),
			Unwrite(defzprima[5]),
			Unwrite(defzprima[6]),
			FadeOut(defz))


		proyzejey = Dot(Line([0,15,0] , [0,-15,0]).get_projection(puntozrot.get_center()), radius=DEFAULT_DOT_RADIUS*1.5).set_color(PURPLE)
		proyzejex = Dot(Line([15,0,0] , [-15,0,0]).get_projection(puntozrot.get_center()), radius=DEFAULT_DOT_RADIUS*1.5).set_color(PURPLE)
		self.play(Create(proyzejex), Create(proyzejey))
		lineaproy = DashedLine(puntozrot.get_center(), proyzejey.get_center())
		lineaprox = DashedLine(puntozrot.get_center(), proyzejex.get_center())
		self.play(Create(lineaprox), Create(lineaproy))
		self.wait()
		Arrowfinaly = Arrow(puntozrotflecha.get_end(), Line([15,0,0] , [-15,0,0]).get_projection(puntozrot.get_center()), buff=0).set_color(GOLD_A)
		Arrowfinaly1 = Arrow(Line([0,15,0] , [0,-15,0]).get_projection(puntozrot.get_center()), ORIGIN, buff=0 ).set_color(GOLD_A)
		self.play(FadeOut(lineaproy), FadeOut(lineaprox), FadeIn(Arrowfinaly), FadeIn(Arrowfinaly1))
		self.wait()
		puntoproy = Dot( Line([15,0,0] , [-15,0,0]).get_projection(puntozrot.get_center()) , radius=DEFAULT_DOT_RADIUS*1.5).set_color(PURPLE)
		self.play(FadeOut(Arrowfinaly1), FadeOut(proyzejey), Create(puntoproy))
		self.wait()

		triang1 = Dot([7,6,0], radius=DEFAULT_DOT_RADIUS*1.5).set_color(PURPLE)
		triang2 = Dot([12,10,0], radius=DEFAULT_DOT_RADIUS*1.5).set_color(BLUE)
		triang3 = Dot([11,6,0], radius=DEFAULT_DOT_RADIUS*1.5).set_color(PURPLE)
		line1 = Line([7,6,0], [12,10,0])
		line11 = Line([5.65,4.92,0], [13.84,11.47,0])
		line2 = Line([12,10,0], [11,6,0])
		line22 = Line([10.43,3.72,0], [12.46,11.83,0])
		line3 = Line([7,6,0], [12.4,6,0])
		angle1 = Angle(line11, line22, other_angle=False, radius=0.8, quadrant=(-1,-1)).set_color(GREEN_SCREEN)
		angle2 = Angle(line11, line3, other_angle=True, radius=0.8).set_color(RED)
		angle3 = Angle(line22, line3, other_angle=True, radius=0.8).set_color(TEAL_B)
		angle11 = Angle(line11, line22, other_angle=False, radius=1.1, quadrant=(-1,-1)).set_color(GREEN_SCREEN)
		angle22 = Angle(line11, line3, other_angle=True, radius=1.1).set_color(LIGHT_PINK)
		angle33 = Angle(line22, line3, other_angle=True, radius=1.23).set_color(TEAL_B)
		textangle1 = MathTex(" \\lambda").set_color(GREEN_SCREEN).scale(1.2)
		textangle1.move_to(angle11.point_from_proportion(0.5))
		textangle2 = MathTex("\\phi").set_color(RED).scale(1.2)
		textangle2.move_to(angle22.point_from_proportion(0.5)) 
		textangle3 = MathTex("\\beta").set_color(TEAL_B).scale(1.2)
		textangle3.move_to(angle33.point_from_proportion(0.5))
		self.play(Create(triang1), Create(triang2), Create(triang3))
		self.play(Create(line1), Create(line2), Create(line3))
		self.play(Create(angle1), Create(angle2), Create(angle3))
		self.play(Create(textangle1), Create(textangle2), Create(textangle3))
		self.wait()
		texx1 = MathTex(" \\lambda").set_color(GREEN_SCREEN).scale(1.4)
		texx1.next_to(triang1, DOWN)
		texx1.shift(0.7*DOWN+1.5*RIGHT)
		texx2 = MathTex("+ \\phi").set_color(RED).scale(1.4)
		texx2.next_to(texx1, RIGHT, buff=DEFAULT_MOBJECT_TO_MOBJECT_BUFFER*0.7)
		texx3 = MathTex("= \\beta").set_color(TEAL_B).scale(1.4)
		texx3.next_to(texx2, RIGHT)
		self.play(Create(texx1), Create(texx2), Create(texx3))
		self.wait()
		anglefinal = Angle(Line([-10,0,0], [10,0,0]), Line( ORIGIN, puntozrot.get_center()), other_angle=False, radius=1.3, stroke_width=10).set_color(GREEN_SCREEN)
		anglelambda = Angle(lineaL, Line( ORIGIN, puntoz.get_center()), other_angle=False, radius=1.3, quadrant=(-1,-1), stroke_width=10).set_color(GREEN_SCREEN)
		anglebeta = Angle(Line([-10,0,0], [10,0,0]), Line( ORIGIN, puntoz.get_center()), other_angle=False, radius=1.7, stroke_width=10).set_color(TEAL_B)
		self.play(Create(anglebeta), Create(anglefinal), Create(anglelambda))
		self.wait()
		lineangrecto11 = Line([6.73, 0, 0] , [6.73, 0.6, 0] )
		lineangrecto22 = Line([7.35, 0.6, 0] , [6.73, 0.6 ,0])
		lineangrecto12 = VGroup(lineangrecto11, lineangrecto22).set_color(GOLD_A)
		self.play(Create(lineangrecto12), FadeOut(anglebeta))
		self.wait()
		triangle1 = Polygon(ORIGIN, prORIGENlineaD.get_center(), puntoz.get_center(), stroke_opacity=0, fill_opacity=0.4, fill_color = RED_C)
		triangle2 = Polygon(ORIGIN, puntozrot.get_center(), proyzejex.get_center(), stroke_opacity=0, fill_opacity=0.4, fill_color = RED_C)
		tst1 = MathTex("\\triangle S_1").move_to([0.5, 3.5, 0]).scale(1.4)
		tst2 = MathTex("\\triangle S_2").move_to([4.5, 1, 0]).scale(1.4)
		self.play(FadeIn(triangle1), FadeIn(triangle2))
		self.play(Create(tst1), Create(tst2))
		self.wait()
		self.play(tst1.animate.move_to([10.4,2.6,0]))
		signooo = MathTex("=").next_to(tst1).scale(1.4)
		self.play(Create(signooo))
		self.play(tst2.animate.next_to(signooo))
		self.wait()
		brrr = Brace(Arrowfinaly, direction=Arrowfinaly.copy().rotate(PI/2).get_unit_vector()).set_color(ORANGE)
		txtt = MathTex("=d").set_color(ORANGE).next_to(brrr).scale(1.4)
		puntozrotlabel.clear_updaters()
		self.play(puntozrotlabel.animate.shift(0.36*UP))
		self.play(Create(brrr))
		self.play(Create(txtt))
		self.wait()
		self.wait()



		

		










			
				






		

		




			
		


