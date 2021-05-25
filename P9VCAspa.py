from manim import *
class P4(MovingCameraScene):
	def construct(self):
		plano = NumberPlane( y_range = (-30, 30), x_range=(-30, 30) ,background_line_style = {"stroke_opacity": 0.4})
		self.camera.frame.save_state()
		self.camera.frame.move_to([2, 4, 0])
		self.camera.frame.set(width=16, height=13)
		self.play(Create(plano))
		myTemplate = TexTemplate()
		myTemplate.add_to_preamble(r"\usepackage{helvet}")
		myTemplate.add_to_preamble(r"\usepackage[]{xcolor}")
		myTemplate.add_to_preamble(r"\renewcommand{\sfdefault}{lmss}")
		myTemplate.add_to_preamble(r"\renewcommand{\familydefault}{\sfdefault}")
		enunciado1 = Tex("Sea", tex_template=myTemplate).shift(8.8*LEFT+9.5*UP).scale(1.4)
		self.play(Write(enunciado1))
		enunciado2 = MathTex("L").set_color(GREEN).scale(1.4).next_to(enunciado1, RIGHT)
		lineaL = Line([-10, -3, 0], [8, 11, 0]).set_color(GREEN)
		self.play(Create(enunciado2), Create(lineaL))
		enunciado3 = Tex("una línea que forma un", tex_template=myTemplate).scale(1.4).next_to(enunciado2, RIGHT)
		enunciado4 = Tex("ángulo", tex_template=myTemplate).scale(1.4).next_to(enunciado1, DOWN).align_to(enunciado1, LEFT)
		enunciado5 = MathTex("\\phi").set_color(RED).scale(1.4).next_to(enunciado4, RIGHT)
		angulo = Angle(lineaL, Line([-20, 0, 0],[20, 0 , 0]), other_angle=True, radius=1.3, color = RED, stroke_width=10)
		textoangulo = MathTex("\\phi").scale(1.4).next_to(angulo.point_from_proportion(0.3)).set_color(RED)
		self.play(Write(enunciado3)) 
		self.play(Write(enunciado4))
		self.play(Create(enunciado5), Create(angulo), Create(textoangulo))
		interseccionlineaLejex = Dot([-6.1428, 0, 0], radius=DEFAULT_DOT_RADIUS*1.5).set_color(PURPLE)
		origen = Dot([0,0,0], radius=DEFAULT_DOT_RADIUS*1.5).set_color(PURPLE)
		enunciado6 = Tex("con el eje $x$", tex_template=myTemplate).scale(1.4).next_to(enunciado5, RIGHT)
		self.play(Write(enunciado6), Create(interseccionlineaLejex), Create(origen))
		self.wait()
		enunciado7 = Tex(". Sea", tex_template=myTemplate).scale(1.4).next_to(enunciado6, RIGHT)
		enunciado8 = MathTex("d").set_color(ORANGE).scale(1.4).next_to(enunciado7, RIGHT)
		enunciado9 = Tex("la distancia de", tex_template=myTemplate).scale(1.4).next_to(enunciado4, DOWN).align_to(enunciado1, LEFT)
		enunciado10 = MathTex("L").set_color(GREEN).scale(1.4).next_to(enunciado9, RIGHT)
		enunciado11 = Tex("al origen de", tex_template=myTemplate).scale(1.4).next_to(enunciado10, RIGHT)
		enunciado12 = Tex("coordenadas. Si ", tex_template=myTemplate).scale(1.4).next_to(enunciado9, DOWN).align_to(enunciado1, LEFT)
		proyeccionD = Dot(lineaL.get_projection(ORIGIN), radius=DEFAULT_DOT_RADIUS*1.5).set_color(PURPLE)
		linead = Line(ORIGIN, proyeccionD.get_center()).set_color(ORANGE)
		lineangrecto1 = Line([-1.96, 2.52, 0] , [-1.51, 2.88, 0])
		lineangrecto2 = Line([-1.86, 3.33, 0] , [-1.51, 2.88, 0])
		lineangrecto = VGroup(lineangrecto1, lineangrecto2).set_color(GOLD_A)
		self.play(Write(enunciado7))
		self.play(Write(enunciado8), Create(linead), Create(proyeccionD))
		self.play(Write(enunciado9), Create(lineangrecto))
		self.play(Write(enunciado10))
		self.play(Write(enunciado11))
		self.play(Write(enunciado12))
		enunciado13 = MathTex("z").set_color(BLUE).scale(1.4).next_to(enunciado12, RIGHT)
		enunciado14 = Tex("es cualquier ", tex_template=myTemplate).scale(1.4).next_to(enunciado13, RIGHT)
		enunciado15 = Tex("punto en", tex_template=myTemplate).scale(1.4).next_to(enunciado12, DOWN).align_to(enunciado1, LEFT)
		enunciado16 = MathTex("L").set_color(GREEN).scale(1.4).next_to(enunciado15, RIGHT)
		enunciado17 = Tex(", Probar que:", tex_template=myTemplate).scale(1.4).next_to(enunciado16, RIGHT)
		self.play(Create(enunciado13))
		pointz = Dot(lineaL.point_from_proportion(0.3), radius=DEFAULT_DOT_RADIUS*1.5).set_color(BLUE)
		etiquetaZ = MathTex("z").set_color(BLUE).scale(1.4).next_to(enunciado12, RIGHT).next_to(pointz, UP)
		self.add(pointz, etiquetaZ)
		etiquetaZ.add_updater(lambda x: x.become(MathTex("z").set_color(BLUE).scale(1.4).next_to(enunciado12, UP).next_to(pointz, UP)))
		self.play(pointz.animate.move_to(lineaL.point_from_proportion(0.9)), Write(enunciado14))
		self.play(pointz.animate.move_to(lineaL.point_from_proportion(0.75)),Write(enunciado15))
		vectorz = Arrow(ORIGIN, pointz.get_center() , buff=0).set_color(BLUE_C)
		self.play(Write(enunciado16))
		self.play(Write(enunciado17), Create(vectorz))
		enunciado18 = MathTex(r"d").scale(1.6).next_to(enunciado16, DOWN, buff=DEFAULT_MOBJECT_TO_MOBJECT_BUFFER*2.2).set_color(ORANGE).shift(1*LEFT)
		enunciado19 = MathTex(r"= \vert Im[").set_color(WHITE).scale(1.4).next_to(enunciado18, RIGHT)
		enunciado20 = MathTex("z \\cdot").set_color(BLUE).scale(1.4).next_to(enunciado19, RIGHT)  
		enunciado21 = MathTex(r"  e^{-i}").set_color(WHITE).scale(1.4).next_to(enunciado20, RIGHT, buff = DEFAULT_MOBJECT_TO_MOBJECT_BUFFER*0.6).shift(0.14*UP)
		enunciado22 = MathTex(r"\phi").set_color(RED).scale(1).shift(2.8*LEFT, 5.55*UP)
		enunciado23 = MathTex(r"] \vert").set_color(WHITE).scale(1.4).next_to(enunciado21, RIGHT, buff = DEFAULT_MOBJECT_TO_MOBJECT_BUFFER*2).shift(0.1*DOWN)
		self.play(Write(enunciado18))
		self.play(Write(enunciado19))
		self.play(Write(enunciado20))
		self.play(Write(enunciado21))
		self.play(Write(enunciado22))
		self.play(Write(enunciado23))
		self.wait()
		self.wait()
		self.wait()
		self.wait()
		MIidentEuler = VGroup(enunciado21.copy(), enunciado22.copy())
		self.add(MIidentEuler)
		self.play(MIidentEuler.animate.scale(1.4).move_to([5, 6.6, 0]))
		MDidentEuler1A = MathTex("=").next_to(MIidentEuler, RIGHT).scale(1.4).shift(0.3*DOWN)
		MDidentEuler1 = MathTex(" \\cos").next_to(MDidentEuler1A, RIGHT).scale(1.4)
		MDidentEuler2 = MathTex(" (- \\phi )").next_to(MDidentEuler1, RIGHT, buff=DEFAULT_MOBJECT_TO_MOBJECT_BUFFER*0.5).set_color(RED)
		MDidentEuler3 = MathTex(" + i \\sin").next_to(MDidentEuler2, RIGHT, buff=DEFAULT_MOBJECT_TO_MOBJECT_BUFFER*1.3).scale(1.4)
		MDidentEuler4 = MathTex(" (- \\phi )").next_to(MDidentEuler3, RIGHT, buff=DEFAULT_MOBJECT_TO_MOBJECT_BUFFER*0.5).set_color(RED)
		self.play(Write(MDidentEuler1A))
		self.play(Write(MDidentEuler1))
		self.play(Write(MDidentEuler2))
		self.play(Write(MDidentEuler3))
		self.play(Write(MDidentEuler4))
		GrupoRect = VGroup(MIidentEuler, MDidentEuler1, MDidentEuler2, MDidentEuler3, MDidentEuler4)
		rect = BackgroundRectangle(mobject=GrupoRect, color=RED, stroke_width=2, stroke_opacity=1, fill_opacity=0, buff=0.35).shift(0.15*DOWN)
		self.play(FadeIn(rect))
		AbsMIidentEuler = MIidentEuler.copy()
		self.add(AbsMIidentEuler)
		self.play(AbsMIidentEuler.animate.shift(2.3*DOWN))
		vert1 = MathTex("\\vert").next_to(AbsMIidentEuler, LEFT).scale(2.5).shift(0.1*DOWN)
		vert2 = MathTex("\\vert").scale(2.5).next_to(AbsMIidentEuler, RIGHT).shift(0.1*DOWN)
		self.play(Write(vert1), Write(vert2))
		signoigual = MathTex("=").scale(2.5).next_to(vert2, RIGHT)
		vert3 = MathTex("\\vert").scale(2.5).next_to(signoigual)
		vert4 = MathTex("\\vert").scale(2.5).next_to(vert3).shift(5.4*RIGHT)
		signoigual2 = MathTex("=").scale(2.5).next_to(signoigual, DOWN, buff=DEFAULT_MOBJECT_TO_MOBJECT_BUFFER*6)
		vert5 = MathTex("\\vert").scale(2.5).next_to(signoigual2)
		vert6 = MathTex("\\vert").scale(2.5).next_to(vert5).shift(5.4*RIGHT)
		AbsMDidentEuler = VGroup(MDidentEuler1.copy(), MDidentEuler2.copy(), MDidentEuler3.copy(), MDidentEuler4.copy())
		self.play(Write(signoigual))
		self.add(AbsMDidentEuler)
		self.play(Write(vert3), Write(vert4))
		self.play(AbsMDidentEuler.animate.next_to(vert3, RIGHT))
		MDidentEuler1abs = MathTex(" \\cos^2").next_to(vert5, RIGHT).scale(1.4)
		MDidentEuler2abs = MathTex(" (- \\phi )").next_to(MDidentEuler1abs, RIGHT, buff=DEFAULT_MOBJECT_TO_MOBJECT_BUFFER*0.7).set_color(RED).shift(0.121*DOWN+0.095*LEFT)
		MDidentEuler3abs = MathTex(" +  \\sin^2").next_to(MDidentEuler2abs, RIGHT, buff=DEFAULT_MOBJECT_TO_MOBJECT_BUFFER*1.3).scale(1.4).shift(0.13*UP)
		MDidentEuler4abs = MathTex(" (- \\phi )").next_to(MDidentEuler3abs, RIGHT, buff=DEFAULT_MOBJECT_TO_MOBJECT_BUFFER*0.7).set_color(RED).shift(0.105*DOWN+0.08*LEFT)
		signoigual3 = MathTex("=").scale(2.5).next_to(signoigual2, DOWN, buff=DEFAULT_MOBJECT_TO_MOBJECT_BUFFER*6)
		otro = MathTex("\\, 1").scale(2.0).next_to(signoigual3, RIGHT)
		MDidentEulerabs = VGroup(MDidentEuler1abs, MDidentEuler2abs, MDidentEuler3abs, MDidentEuler4abs).shift(0.15*RIGHT)
		self.play(Write(signoigual2), Write(vert5), Write(vert6))
		self.play(Create(MDidentEulerabs))
		self.play(Write(signoigual3),Write(otro))
		vectorbase = Arrow(ORIGIN, [3.6,0,0], buff=0).set_color(PINK)
		brvectorbase = Brace(vectorbase, direction=UP, buff=0.1)    
		txtobr = MathTex("1").next_to(brvectorbase, UP)
		self.play(Create(vectorbase), Create(brvectorbase), Create(txtobr))
		vecotrconangulo = vectorbase.copy()
		self.add(vecotrconangulo)
		self.play(vecotrconangulo.animate.rotate(angle=(angulo.angle)/100, about_point=ORIGIN))
		angulo2 = Angle(vectorbase, vecotrconangulo, radius=1.3, color = RED, stroke_width=10, other_angle=True)
		angulo2.add_updater(lambda x: x.become(Angle(vectorbase, vecotrconangulo, radius=1.3, other_angle=True, color = RED, stroke_width=10)))
		angulo3 = Angle(vectorbase, vecotrconangulo, radius=3.55, color = WHITE, stroke_width=2.5, other_angle=True)
		angulo3.add_updater(lambda x: x.become(Angle(vectorbase, vecotrconangulo, radius=3.55, other_angle=True, color = WHITE, stroke_width=2.5)))
		self.add(angulo2, angulo3)
		self.play(vecotrconangulo.animate.rotate(angle=(angulo.angle), about_point=ORIGIN).set_color(RED))
		angulovalor = MathTex("\\phi").set_color(RED).next_to(angulo2.point_from_proportion(0.65)).scale(1.2)
		self.play(Write(angulovalor))
		vecotrconangulotextbrace = Brace(vecotrconangulo, buff=0.1, direction=vecotrconangulo.copy().rotate(3*PI/2).get_unit_vector()).shift(0.2*UP+0.1*LEFT)
		textangulotex = MathTex("e^{-i \\cdot \\phi}").set_color(RED).next_to(vecotrconangulotextbrace, LEFT).scale(1.3).shift(1.4*RIGHT+0.65*DOWN)
		self.play(FadeIn(vecotrconangulotextbrace), FadeIn(textangulotex))
		self.wait()
		self.play(
			FadeOut(vecotrconangulotextbrace),
			FadeOut(textangulotex), 
			FadeOut(angulovalor), 
			FadeOut(txtobr), 
			FadeOut(brvectorbase), 
			FadeOut(signoigual2),
			FadeOut(vert5),
			FadeOut(vert6),
			FadeOut(MDidentEulerabs),
			FadeOut(signoigual3),
			FadeOut(otro),
			FadeOut(signoigual),
			FadeOut(AbsMDidentEuler),
			FadeOut(vert3),
			FadeOut(vert4),
			FadeOut(MIidentEuler),
			FadeOut(MDidentEuler1A),
			FadeOut(MDidentEuler1),
			FadeOut(MDidentEuler2),
			FadeOut(MDidentEuler3),
			FadeOut(MDidentEuler4),
			FadeOut(rect),
			FadeOut(AbsMIidentEuler),
			FadeOut(vert1),
			FadeOut(vert2),
			)
		self.wait()
		vectorzmult = vectorz.copy()
		vectorzmultetiqueta = MathTex(" z'").next_to(vectorzmult.get_end(), RIGHT).set_color(PURPLE)
		vectorzmultetiqueta.add_updater(lambda x: x.become(MathTex(" z'").next_to(vectorzmult.get_end(), RIGHT).set_color(PURPLE).scale(1.4)))
		self.add(vectorzmult)
		angulorotacion = Angle(vectorbase, vecotrconangulo, other_angle=True).scale(2.5).shift(8*UP+10*RIGHT).set_color(RED).add_tip()
		textoangulorot = MathTex("- \\phi").set_color(RED).scale(1.7).next_to(angulorotacion, RIGHT)
		self.wait()
		self.play(
			Create(angulorotacion),
			Create(textoangulorot),)
		self.play(
			plano.animate.rotate(angle=(angulo.angle)/1000, about_point=ORIGIN),
			vectorzmult.animate.rotate(angle=(angulo.angle)/1000, about_point=ORIGIN).set_color(PURPLE)
			)
		self.add(vectorzmultetiqueta)
		anglezvectzmult = Angle(vectorz, vectorzmult, radius=1.3, color = RED, stroke_width=10, other_angle=True)
		anglezvectzmult.add_updater(lambda x: x.become(Angle(vectorz, vectorzmult, radius=1.3, color = RED, stroke_width=10, other_angle=True)))
		anglezvectzmult2 = Angle(vectorz, vectorzmult, radius=vectorz.get_length(), color = WHITE, stroke_width=2.5, other_angle=True)
		anglezvectzmult2.add_updater(lambda x: x.become(Angle(vectorz, vectorzmult, radius=vectorz.get_length(), color = WHITE, stroke_width=2.5, other_angle=True)))
		self.add(anglezvectzmult, anglezvectzmult2)
		self.play(
			FadeOut(angulo),
			FadeOut(textoangulo),
			plano.animate.rotate(angle=(angulo.angle), about_point=ORIGIN),
			vectorzmult.animate.rotate(angle=(angulo.angle), about_point=ORIGIN).set_color(PURPLE) 
			, run_time=4)
		self.play(FadeOut(angulorotacion), FadeOut(textoangulorot))
		angulorotacion3 = Angle(vectorbase, vecotrconangulo, other_angle=True).scale(2.5).next_to(angulorotacion, DOWN, buff=DEFAULT_MOBJECT_TO_MOBJECT_BUFFER*1.25).set_color(RED).add_tip(at_start=True)
		textoangulorot3 = MathTex(" \\phi").set_color(RED).scale(1.7).next_to(angulorotacion3, RIGHT)
		self.play(FadeIn(angulorotacion3), FadeIn(textoangulorot3))
		self.play(plano.animate.rotate(angle= -(angulo.angle), about_point=ORIGIN), run_time=4)
		self.play(FadeIn(angulo), FadeIn(textoangulo))
		self.play(FadeOut(angulorotacion3), FadeOut(textoangulorot3))
		Dotzmult = Dot(vectorzmult.get_end(), radius=DEFAULT_DOT_RADIUS*1.5).set_color(PURPLE)
		formula =  MathTex(" z'").next_to(vectorzmult.get_end(), RIGHT).set_color(PURPLE).scale(1.4)
		angulo2.clear_updaters()
		angulo3.clear_updaters()
		self.play(FadeOut(angulo2) , FadeOut(angulo3))
		self.play(Create(Dotzmult),FadeOut(vectorbase), FadeOut(vecotrconangulo))
		self.add(formula)
		self.play(formula.animate.shift(2*UP+2*RIGHT))
		MDformula = MathTex("=z \\cdot ").scale(1.4)
		MDformula.next_to(formula, RIGHT)
		MDformula.shift(0.15*DOWN)
		MDformulaa = VGroup(enunciado21.copy(), enunciado22.copy()).next_to(MDformula, RIGHT)
		MDformulaa.shift(0.15*UP)
		self.play(Create(MDformula), Create(MDformulaa))
		self.wait()
		self.play(FadeOut(formula), FadeOut(MDformula), FadeOut(MDformulaa))
		proyzejey = Dot(Line([0,15,0] , [0,-15,0]).get_projection(Dotzmult.get_center()), radius=DEFAULT_DOT_RADIUS*1.5).set_color(PURPLE)
		proyzejex = Dot(Line([15,0,0] , [-15,0,0]).get_projection(Dotzmult.get_center()), radius=DEFAULT_DOT_RADIUS*1.5).set_color(PURPLE)
		self.play(Create(proyzejex), Create(proyzejey))
		lineaproy = DashedLine(Dotzmult.get_center(), proyzejey.get_center())
		lineaprox = DashedLine(Dotzmult.get_center(), proyzejex.get_center())
		self.play(Create(lineaprox), Create(lineaproy))
		self.wait()
		Arrowfinaly = Arrow(vectorzmult.get_end(), Line([15,0,0] , [-15,0,0]).get_projection(Dotzmult.get_center()), buff=0).set_color(GOLD_A)
		Arrowfinaly1 = Arrow(Line([0,15,0] , [0,-15,0]).get_projection(Dotzmult.get_center()), ORIGIN, buff=0 ).set_color(GOLD_A)
		self.play(FadeOut(lineaproy), FadeOut(lineaprox), FadeIn(Arrowfinaly), FadeIn(Arrowfinaly1))
		self.wait()
		puntoproy = Dot( Line([15,0,0] , [-15,0,0]).get_projection(Dotzmult.get_center()) , radius=DEFAULT_DOT_RADIUS*1.5).set_color(PURPLE)
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
		anglefinal = Angle(Line([-10,0,0], [10,0,0]), Line( ORIGIN, Dotzmult.get_center()), other_angle=False, radius=1.3, stroke_width=10).set_color(GREEN_SCREEN)
		anglelambda = Angle(lineaL, Line( ORIGIN, pointz.get_center()), other_angle=False, radius=1.3, quadrant=(-1,-1), stroke_width=10).set_color(GREEN_SCREEN)
		anglebeta = Angle(Line([-10,0,0], [10,0,0]), Line( ORIGIN, pointz.get_center()), other_angle=False, radius=1.7, stroke_width=10).set_color(TEAL_B)
		self.play(Create(anglebeta), Create(anglefinal), Create(anglelambda))
		self.wait()
		lineangrecto11 = Line([6.73, 0, 0] , [6.73, 0.6, 0] )
		lineangrecto22 = Line([7.35, 0.6, 0] , [6.73, 0.6 ,0])
		lineangrecto12 = VGroup(lineangrecto11, lineangrecto22).set_color(GOLD_A)
		self.play(Create(lineangrecto12), FadeOut(anglebeta))
		self.wait()
		triangle1 = Polygon(ORIGIN, proyeccionD.get_center(), pointz.get_center(), stroke_opacity=0, fill_opacity=0.4, fill_color = RED_C)
		triangle2 = Polygon(ORIGIN, Dotzmult.get_center(), proyzejex.get_center(), stroke_opacity=0, fill_opacity=0.4, fill_color = RED_C)
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
		vectorzmultetiqueta.clear_updaters()
		self.play(vectorzmultetiqueta.animate.shift(0.36*UP))
		self.play(Create(brrr))
		self.play(Create(txtt))
		self.wait()
		self.wait()














		

 
		






		



		

		





		

		
		

		
		

		






		

		




		


		



 



		

		




		
		


