# the algorithm will be place 1000 random points inside a line.
# take the half that no has a finite number of points (at least should be one) for viewers the one
# with the greatest number of points. repeat nutil there is a nice accumulation point.
import random

import numpy as np
from manim import *

if __name__ == '__main__':
    import subprocess
    params = 'manim -pqh main.py A'.split()
    subprocess.run(params,
                   check=True,
                   capture_output=False,
                   text=True)


class B(MovingCameraScene):
    def construct(self):
        self.camera.background_color = "#ece6e2"
        dotA = Dot([0,0,0], color = RED)
        dotB = Dot([0,0,0], color = BLUE)
        self.add(dotA)
        self.wait()
        self.play(Transform(dotA, dotB))




# construct point in x-axis.
def construct_dot(position, **kwargs):
    return Dot([position, 0, 0], **kwargs)

# generate size  random float numbers between a and b


def random_generator(size, a, b):
    list = []
    from random import random
    for i in range(0, size):
        value = random()
        list.append((b-a)*random() + a)
    return list


class A(MovingCameraScene):
    def construct(self):
        self.camera.background_color = "#ece6e2"
        # first part of the animation
        self.camera.frame.scale(1.3)
        statement = Tex("Teorema: En todo conjunto, ", "acotado ", " y con una cantidad ", "infinita ",
                        "de números " , "reales", " existe un punto que es punto de acumulación. ", color=BLACK, tex_template=TexFontTemplates.gfs_neoHellenic)
        statement.set_color_by_tex("acotado", RED)
        statement.set_color_by_tex("infinita", BLUE)
        statement.set_color_by_tex("reales", GREEN)
        statement.shift(4*UP)
        self.play(Write(statement))
        self.wait(duration=2)
        line1 = Tex("Son necesarias simultaneamente las tres condiciones: ",  "acotado, ", "infinitos puntos, ","y reales",  ", la intuición es la siguiente: ", color=BLACK,
                    tex_template=TexFontTemplates.gfs_neoHellenic)
        line1.set_color_by_tex("acotado, ", RED)
        line1.set_color_by_tex("infinitos puntos, ", BLUE)
        line1.set_color_by_tex("y reales", GREEN)
        text2 = "1 - Si se divide un conjunto con una cantidad infinita de puntos en dos partes, habrá al menos una parte con una cantidad infinita de puntos"
        text3 = "2 - Un punto de acumulación tiene otros puntos a su alrededor tan cercanos a él como se desee, mientras más chiquita la longitud del intervalo que contiene a los puntos más pequeña es la distancia entre ellos"
        text4 = "3- Si esa distancia se hace tender a 0, por ejemplo dividiéndola entre 2, continuamente encontraremos un punto de acumulación."
        text5 = "Visualmente sería esto lo que sucede:"

        line2 = Tex(text2, color=BLACK,
                    tex_template=TexFontTemplates.gfs_neoHellenic)
        line3 = Tex(text3, color=BLACK,
                    tex_template=TexFontTemplates.gfs_neoHellenic)
        line4 = Tex(text4, color=BLACK,
                    tex_template=TexFontTemplates.gfs_neoHellenic)
        line5 = Tex(text5, color=BLACK,
                    tex_template=TexFontTemplates.gfs_neoHellenic)

        line1.next_to(statement, DOWN)
        line2.next_to(line1, DOWN)
        line3.next_to(line2, DOWN)
        line4.next_to(line3, DOWN)
        line5.next_to(line4, DOWN)

        self.play(Create(line1, rate_func=rate_functions.ease_in_back, run_time=4))
        self.play(Create(line2, rate_func=rate_functions.ease_in_quad, run_time=4))
        self.play(Create(line3, rate_func=rate_functions.ease_out_expo, run_time=4))
        self.play(Create(line4, rate_func=rate_functions.ease_out_quart, run_time=4))
        self.play(Create(line5, rate_func=rate_functions.ease_in_out_back, run_time=4))
        self.wait()

        
        self.play(
            FadeOut(line1),
            FadeOut(line2),
            FadeOut(line3),
            FadeOut(line4),
            FadeOut(line5)
        )
        new_text = "Se escoge una mitad con infinitos puntos: "
        description = Tex(new_text, color=BLACK,
                          tex_template=TexFontTemplates.gfs_neoHellenic).move_to(statement).shift(2*DOWN)
        self.play(FadeOut(statement), Write(description))
        self.play(self.camera.frame.animate.scale(0.7))
        # second part of the animation
        upper_bound = 6
        lower_bound = -6
        left_dot = Dot([lower_bound, 0, 0], color=RED_E)
        left_brace = Tex("[", color=YELLOW_E).move_to(
            [lower_bound, 0, 0])
        right_dot = Dot([upper_bound, 0, 0], color=RED_E)
        right_brace = Tex("]", color=YELLOW_E).move_to([
            upper_bound, 0, 0])
        x_axis = Line([lower_bound, 0, 0], [upper_bound, 0, 0],
                      color=BLUE_A, fill_opacity=0.3)
        numbers = random_generator(2500, lower_bound, upper_bound)
        dots = [Dot([x, 0, 0], color=BLACK, radius=DEFAULT_DOT_RADIUS*0.05)
                for x in numbers]
        self.play(Create(x_axis))
        self.play(Create(left_dot), Create(right_dot),
                  Create(left_brace), Create(right_brace))


        for dot in dots:
            self.add(dot)


        self.camera.frame.save_state()
        m = 0
        while m < 7:
            m = m+1
            # add middle point.
            middle = (upper_bound + lower_bound)/2
            middle_dot = Dot([middle, 0, 0], color=RED_E,
                             radius=DEFAULT_DOT_RADIUS*(1/m))
            new_left_dot = Dot([lower_bound, 0, 0], color=RED_E,
                               radius=DEFAULT_DOT_RADIUS*(1/m))
            new_right_dot = Dot([upper_bound, 0, 0],
                                color=RED_E, radius=DEFAULT_DOT_RADIUS*(1/m))
            self.play(
                Create(middle_dot),
                Transform(left_dot, new_left_dot),
                Transform(right_dot, new_right_dot))

            # select best half and update variables.
            first_half = 0
            second_half = 0
            for number in numbers:
                if lower_bound < number < middle:
                    first_half += 1
                if middle < number < upper_bound:
                    second_half += 1
            new_camera_position = 0
            if first_half > second_half:
                # move to left.
                new_camera_position = (lower_bound + middle)/2
                upper_bound = middle
                right_dot = middle_dot
                middle_brace = Tex("]", color=YELLOW_E).move_to([
                    middle, 0, 0])

            else:
                # move to right
                new_camera_position = (upper_bound + middle)/2
                lower_bound = middle
                left_dot = middle_dot
                middle_brace = Tex("[", color=YELLOW_E).move_to(
                    [middle, 0, 0])

            self.play(Create(middle_brace))
            self.play(self.camera.frame.animate.move_to(
                [new_camera_position, 0, 0]))
            self.play(self.camera.frame.animate.scale(0.5))

        # select (dot with the biggest number of neighbors) winner dot.

        self.play(Create(
            Dot([(lower_bound + upper_bound)/2, 0, 0], color=GOLD_E)))
        self.play(Restore(self.camera.frame), run_time=2)

        final_text = Tex("Y así se forma un ", "sistema de intervalos encajados infinitesimal",
                         color=BLACK, tex_template=TexFontTemplates.gfs_neoHellenic)
        final_text.shift(2*DOWN).scale(0.7)
        self.play(Write(final_text))
