"""
Given the process of solving an integral using Latex, make an animation of the process, use the example.txt to undersand
how generate an animation
"""

from manim import *

# first step is save in an array of strings each step in the process of solving the integral given the format.
steps = []
with open("example.txt", "r") as file:
    steps = file.readlines()


class integral(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        manim_steps = []
        for line in steps:
            manim_steps.append(MathTex(line, color=BLACK).scale(2).shift(1*UP))
        old_object = manim_steps[0].shift(1*UP)
        old_substitution = manim_steps[2]
        self.play(Create(old_object))
        for i in range(1, len(manim_steps)):
            if (i == 2):  # i = 2 is the first substitution
                old_substitution = manim_steps[i].shift(2*DOWN)
                self.play(Create(old_substitution))
            elif (i == 5):  # other substitutions
                new_substitution = manim_steps[i].shift(2.5*DOWN)
                self.play(ReplacementTransform(
                    old_substitution, new_substitution), run_time=1)
                old_substitution = new_substitution
            else:
                new_object = manim_steps[i].shift(1*UP)
                self.play(ReplacementTransform(old_object, new_object),
                          run_time=1)
                old_object = new_object
            self.wait()
