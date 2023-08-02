#Python3 Code @BritoAlv

from manim import *

if __name__ == '__main__':
    import subprocess
    params = 'manim -pql manim_no_inmune_system.py A'.split()
    subprocess.run(params,
                   check=True,
                   capture_output=False,
                   text=True)
        
coord_range = [-60, 60, 1]
len_range = coord_range[1] - coord_range[0]

class A(MovingCameraScene):
    def construct(self):
        # CAMERA CONFIG
        self.camera.background_color = "#FFFFFF"
        self.camera.frame.scale(5)

        # AXES CONFIG
        x_axis = NumberLine(
            x_range=coord_range,
            length=len_range,
            color=BLACK,
            stroke_width=2,
            label_direction=UP,
            include_numbers=True,
            numbers_to_exclude = [0]
        ).set_color(BLACK)

        y_axis = NumberLine(
            x_range=coord_range,
            length=len_range,
            rotation = PI/2,
            color=BLACK,
            stroke_width=2,
            label_direction=LEFT,
            include_numbers=True,
            numbers_to_exclude = [0],
        ).set_color(BLACK)
        label_x_axis = MathTex("t").next_to(x_axis.n2p(34), direction = UP , buff = 1.6).set_color(BLACK).scale(4)
        label_y_axis = MathTex("x").next_to(y_axis.n2p(19) , buff = 1).set_color(BLACK).scale(4)
        self.add(x_axis, y_axis, label_x_axis, label_y_axis)

        # ADD PARAMETERS.
        parametera = ValueTracker(2)
        parameterb = ValueTracker(2)
        parameterd = ValueTracker(3)

        # VECTOR_FIELD CONFIG
        colors = [RED, YELLOW, BLUE, DARK_GRAY]
        vector_field = ArrowVectorField(
            func = lambda pos: np.array( [ pos[0] , pos[1]*( parametera.get_value()*(parameterb.get_value() - pos[1]) - parameterd.get_value()), 0]), 
            x_range = [0, 40, 1 ], 
            y_range = [0, 40, 1 ],  
            min_color_scheme_value=2, 
            max_color_scheme_value=10,
            color = colors
            )
        vector_field.add_updater( lambda vf: vf.become(ArrowVectorField(
            func = lambda pos: np.array( [ pos[0] , pos[1]*( parametera.get_value()*(parameterb.get_value() - pos[1]) - parameterd.get_value()), 0]), 
            x_range = [0, 40, 1 ], 
            y_range = [0, 40, 1 ],  
            min_color_scheme_value=2, 
            max_color_scheme_value=10,
            color = colors
            )) )
        self.play(Create(vector_field))
        
        
        parametera_tex = MathTex(
            f"a = {parametera.get_value()}").move_to([-18, -5, 0]).set_color(BLACK).scale(3.3).add_updater(lambda m: m.become(MathTex(
            f"a = {round(parametera.get_value(), 3)}").move_to([-18, -5, 0]).set_color(BLACK).scale(2.6)))
        parameterb_tex = MathTex(
            f"b = {parameterb.get_value()}").move_to([-18, -8, 0]).set_color(BLACK).scale(3.3).add_updater(lambda m: m.become(MathTex(
            f"b = {round(parameterb.get_value(), 3)}").move_to([-18, -8, 0]).set_color(BLACK).scale(2.6)))
        parameterd_tex = MathTex(
            f"d = {parameterd.get_value()}").move_to([-18, -11, 0]).set_color(BLACK).scale(3.3).add_updater(lambda m: m.become(MathTex(
            f"d = {round(parameterd.get_value(), 3 )}").move_to([-18, -11, 0]).set_color(BLACK).scale(2.6)))
        equation = MathTex("\\dot{x} = x \\big( a(b-x) -d  \\big)").move_to([-18, -14, 0]).set_color(BLACK).scale(2.6)
        description = Tex("En ausencia del Sistema Inmune:").set_color(BLACK).scale(4).move_to([-18, -2, 0])
        line_K = NumberLine(
            x_range=coord_range,
            length=len_range,
            color=BLACK,
            stroke_width=2,
        ).set_color(BLACK).shift( UP*(parameterb.get_value() - parameterd.get_value()/parametera.get_value())).add_updater(lambda m: m.shift( UP*(parameterb.get_value() - parameterd.get_value()/parametera.get_value()) - m.get_center())) 
        K = MathTex("K").set_color(BLACK).scale(3).move_to(
            [0, parameterb.get_value() - parameterd.get_value()/parametera.get_value(),  0]).add_updater( lambda m: m.next_to([0, parameterb.get_value() - parameterd.get_value()/parametera.get_value(),  0]))
        self.play(Write(K), Create(line_K), Write(parametera_tex), Write(parameterb_tex), Write(parameterd_tex), Write(equation), Write(description))
        self.play(
            parametera.animate.increment_value(4), 
            parameterb.animate.increment_value(3), 
            parameterd.animate.increment_value(1)
            , run_time = 4)