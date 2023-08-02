import numpy as np
from manim import *

if __name__ == '__main__':
    import subprocess

    params = 'manim -pqh manim_taylor.py A'.split()
    subprocess.run(params,
                   check=True,
                   capture_output=False,
                   text=True)

'''
Problem To Solve:

dada una función f(x), 
un intervalo [a,b]
un número real x
un entero n

graficar la función original en el intervalo [a,b] , y para i = 1, 2, ..., n graficar
el polinomio de taylor de la función alrededor del punto x, en el intervalo [a,b].

'''

import numdifftools as nd
import math
import numpy as np


class TaylorSeries():
    def __init__(self, function, order, center=0):
        self.center = center
        self.f = function
        self.order = order
        self.coefficients = []

        self.__find_coefficients()

    def __find_coefficients(self):
        for i in range(0, self.order + 1):
            self.coefficients.append(
                round(
                    nd.Derivative(
                        self.f,
                        n=i)(self.center) / math.factorial(i),
                    5)
            )
    def approximate_value(self, x):
        """
            Approximates the value of f(x) using the taylor polynomial.
            x = point to approximate f(x)
        """
        fx = 0
        for i in range(len(self.coefficients)):
            fx += self.coefficients[i] * ((x - self.center) ** i)  # coefficient * nth term
        return fx

    def get_coefficients(self):
        """
            Returns the coefficients of the taylor series
        """
        return self.coefficients


class A(MovingCameraScene):
    def construct(self):
        # data of the problem
        x_0 = 0
        h = 0.7
        a = x_0 - h
        b = x_0 + h
        n = 6
        original_func = lambda x: x**5 + 6*x**3 - 4*x**2 + 5
        taylor_objects = []
        for order in range(1, n + 1):
            taylor_objects.append(TaylorSeries(original_func, order, x_0))
        self.camera.frame.save_state()
        # create the axes and the curve
        ax = Axes(
            x_range=[a, b, h / 7],
            y_range=[original_func(x_0) - 2, original_func(x_0) + 2],
            axis_config={
                'color': WHITE,
                'stroke_width': 2,
                'include_numbers': True,
                'decimal_number_config': {
                    'num_decimal_places': 2,
                    'include_sign': False,
                    'color': BLUE
                }
            },
        )
        first_function = ax.plot(original_func, color=BLUE_E, x_range=[a, b])
        plot_functions = VGroup()
        plot_functions.add(first_function)

        l = 0
        colors = [RED, YELLOW_E, LIGHT_PINK, GOLD_A, LIGHT_BROWN, GREEN_E, ORANGE,  PURPLE]
        for taylor in taylor_objects:
            plot_functions.add(
                ax.plot(
                    lambda x: taylor.approximate_value(x), color=colors[l], x_range=[a, b]
                ))
            l += 1
        # create dots based on the graph
        moving_dots = VGroup()
        l = 0
        for func in plot_functions:
            moving_dots.add(
                VGroup(
                    Dot(ax.i2gp(func.t_min, func), color=WHITE),
                    MathTex(f"{l}", color=func.color).next_to(ax.i2gp(func.t_min, func, ), buff=0)
                )
            )
            l += 1
        self.play(Create(ax))
        self.play(Create(plot_functions, run_time=5))

        principal_dot = moving_dots[0]

        self.play(self.camera.frame.animate.scale(0.5).move_to(principal_dot))
        def update_curve(mob):
            mob.move_to(principal_dot.get_center())

        self.camera.frame.add_updater(update_curve)
        self.play(
            *[MoveAlongPath(moving_dots[i], plot_functions[i], rate_func=linear, run_time=5) for i in
              range(0, len(moving_dots))]
        )
        self.camera.frame.remove_updater(update_curve)
