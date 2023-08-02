#Python3 Code @BritoAlv

from manim import *

if __name__ == '__main__':
    import subprocess
    params = 'manim -pqk manim_template.py A'.split()
    subprocess.run(params,
                   check=True,
                   capture_output=False,
                   text=True)

coord_range = (0, 20, 1)
len_range = coord_range[1] - coord_range[0]

a = ValueTracker(2.2)
b = ValueTracker(5.6)
c = ValueTracker(2.6)
d = ValueTracker(-4)
e = ValueTracker(6.5)
ff = ValueTracker(5.2)
g = ValueTracker(2)
hh = ValueTracker(5.1)
i = ValueTracker(4.8)

p1 = [0, (a.get_value() * b.get_value() - d.get_value()) / c.get_value(), 0]
p2 = [0, ff.get_value(), 0]
p3 = [(g.get_value() * hh.get_value() - i.get_value() + np.sqrt(4 * e.get_value() * ff.get_value() * g.get_value() + (g.get_value() * hh.get_value() - i.get_value()) ** 2)) / (2 * g.get_value()), 0, 0]
p4 = [(a.get_value() * b.get_value() - d.get_value()) / a.get_value(), 0, 0]

border_points = []
border_points1 = [[0, i] for i in range(0, 21)]
border_points2 = [[i, 20] for i in range(0, 36)]
border_points3 = [[i, 0] for i in range(0, 36)]
border_points4 = [[35, i] for i in range(0, 21)]

for point in border_points1:
    border_points.append(point)
for point in border_points2:
    border_points.append(point)
for point in border_points3:
    border_points.append(point)
for point in border_points4:
    border_points.append(point)

def ode_system(_y):
    return np.array([_y[0] * (a.get_value() * b.get_value() * (1 - _y[0] / b.get_value()) - c.get_value() * _y[1] - d.get_value()), _y[1] * (e.get_value() * (ff.get_value() - _y[1]) + g.get_value() * _y[0] * (hh.get_value() - _y[0]) - i.get_value() * _y[0])])

def ode_system_x(_y):
    return _y[0] * (a.get_value() * b.get_value() * (1 - _y[0] / b.get_value()) - c.get_value() * _y[1] - d.get_value())


def ode_system_z(_y):
    return _y[1] * (e.get_value() * (ff.get_value() - _y[1]) + g.get_value() * _y[0] * (hh.get_value() - _y[0]) - i.get_value() * _y[0])


def x_nullcline_function(x):
    return (a.get_value() * b.get_value() - a.get_value() * x - d.get_value()) / c.get_value()  # returns the z_value.

def z_nullcline_function(x):
    return (e.get_value()*ff.get_value() + g.get_value()*hh.get_value()*x - g.get_value()*(x*x) - i.get_value()*x)/e.get_value()


def runge_kutta(
    start_x_coordinate, end_x_coordinate, start_y_coordinate, func, number_steps
):
    # return the list of images of the given function in the interval from start to end_coordinate.
    h = float(end_x_coordinate - start_x_coordinate) / float(number_steps)
    result = [start_y_coordinate]
    y0 = start_y_coordinate
    for i in range(0, number_steps + 1):
        x0 = start_x_coordinate + h * i
        k1 = h * func([x0, y0])
        k2 = h * func([x0 + 0.5 * h, y0 + 0.5 * k1])
        k3 = h * func([x0 + 0.5 * h, y0 + 0.5 * k2])
        k4 = h * func([x0 + h, y0 + k3])
        y0 = y0 + (h / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
        result.append(y0)
    return result



def rk4(func, tk, _yk, _dt=0.01, **kwargs):
    """
    single-step fourth-order numerical integration (RK4) method
    func: system of first order ODEs
    tk: current time step
    _yk: current state vector [y1, y2, y3, ...]
    _dt: discrete time step size
    **kwargs: additional parameters for ODE system
    returns: y evaluated at time k+1
    """

    # evaluate derivative at several stages within time interval
    f1 = func(_yk, **kwargs)
    f2 = func(_yk + (f1 * (_dt / 2)), **kwargs)
    f3 = func(_yk + (f2 * (_dt / 2)), **kwargs)
    f4 = func(_yk + (f3 * _dt), **kwargs)

    # return an average of the derivative over tk, tk + dt
    return _yk + (_dt / 6) * (f1 + (2 * f2) + (2 * f3) + f4)

def get_trajectory(y0 = np.array([0,0]), number_steps = 400  ):
    state_history = []
    yk = y0
    t = 0
    for t in range(0, number_steps):
        state_history.append(yk)
        yk = rk4(ode_system, t, yk, 0.001)

    state_history = np.array(state_history)
    state_history = [ (p[0], p[1], 0) for p in state_history if np.isfinite(p[0]) and np.isfinite(p[1])]
    return state_history
    

class Case1(MovingCameraScene):
    def construct(self):
        # CAMERA CONFIG
        self.camera.background_color = "#FFFFFF"
        self.camera.frame.scale(3)
        self.camera.frame.shift(10 * UP + 15 * RIGHT)

        # AXES CONFIG
        x_axis = (
            NumberLine(
                x_range=(0, 35, 1),
                length=35,
                color=BLACK,
                stroke_width=2,
                label_direction=UP,
                include_numbers=True,
                numbers_to_exclude=[0],
            )
            .set_color(BLACK)
            .shift(17.5 * RIGHT)
        )

        z_axis = (
            NumberLine(
                x_range=coord_range,
                length=len_range,
                rotation=PI / 2,
                color=BLACK,
                stroke_width=2,
                label_direction=LEFT,
                include_numbers=True,
                numbers_to_exclude=[0],
            )
            .set_color(BLACK)
            .shift(10 * UP)
        )
        label_x_axis = (
            MathTex("x")
            .next_to(x_axis.n2p(35), direction=DOWN, buff=1)
            .set_color(BLACK)
            .scale(3)
        )
        label_z_axis = (
            MathTex("z").next_to(z_axis.n2p(20), buff=1).set_color(BLACK).scale(3)
        )

        # vector_field1 = ArrowVectorField(ode_system,  min_color_scheme_value=2, max_color_scheme_value=10, x_range = [], y_range = [])


        sp0 = Dot([0, 0, 0], color=YELLOW_E)
        sp1 = Dot(p1, color=YELLOW_E).add_updater(lambda m: m.move_to([0, (a.get_value() * b.get_value() - d.get_value()) / c.get_value(), 0]))
        sp2 = Dot(p2, color=YELLOW_E).add_updater(lambda m: m.move_to([0, ff.get_value(), 0]))
        sp3 = Dot(p3, color=YELLOW_E).add_updater(lambda m: m.move_to([(g.get_value() * hh.get_value() - i.get_value() + np.sqrt(4 * e.get_value() * ff.get_value() * g.get_value() + (g.get_value() * hh.get_value() - i.get_value()) ** 2)) / (2 * g.get_value()), 0, 0]))
        sp4 = Dot(p4, color=YELLOW_E).add_updater(lambda m: m.move_to([(a.get_value() * b.get_value() - d.get_value()) / a.get_value(), 0, 0]))


        text_sp1 = (
            MathTex(r"\frac{ab-d}{c}").move_to(sp1).shift(1.3 * LEFT).set_color(BLACK)
        ).add_updater(lambda m: m.move_to(sp1.get_center()))
        text_sp2 = MathTex(r"f").move_to(sp2).shift(1.3 * LEFT).set_color(BLACK).add_updater(lambda m: m.move_to(sp2.get_center()))
        text_sp3 = (
            MathTex(r"\frac{gh-i+\sigma}{2g}")
            .move_to(sp3)
            .shift(1 * DOWN + 1 * LEFT)
            .set_color(BLACK)
        ).add_updater(lambda m: m.move_to(sp3.get_center()))
        text_sp4 = (
            MathTex(r"\frac{ab-d}{a}")
            .move_to(sp4)
            .shift(1 * DOWN + 1 * RIGHT)
            .set_color(BLACK)
        ).add_updater(lambda m: m.move_to(sp4.get_center()))

        vector_field1 = ArrowVectorField(
            ode_system,
            min_color_scheme_value=2,
            max_color_scheme_value=10,
            x_range=[0, 35, 1],
            y_range=[0, 20, 1],
            colors = [RED, YELLOW, BLUE, DARKER_GREY]
        ).add_updater(lambda m: m.become(ArrowVectorField(
            ode_system,
            min_color_scheme_value=2,
            max_color_scheme_value=10,
            x_range=[0, 35, 1],
            y_range=[0, 20, 1],
            colors = [RED, YELLOW, BLUE, DARKER_GREY])))


        description_text = (
            Tex("Plano Fase para el caso $2$:")
            .move_to([20, 14, 0])
            .set_color(BLACK)
            .scale(3)
        )

        # nullcline x_values
        nullcline_x = VGroup()
        nullcline_x_values = [ [t, x_nullcline_function(t), 0] for t in np.arange(0, p4[0], p4[0]/200 ) if np.isfinite(x_nullcline_function(t)) ]

        for point in nullcline_x_values:
             nullcline_x.add(
                 Dot(point, color = PURPLE_A, radius = DEFAULT_DOT_RADIUS*0.6))

        nullcline_x.add_updater(
            lambda m: m.become(
                VGroup(
            *[ Dot(point, color = PURPLE_A, radius = DEFAULT_DOT_RADIUS*0.6) for point in [ [t, x_nullcline_function(t), 0] for t in np.arange(0, ((a.get_value() * b.get_value() - d.get_value()) / a.get_value()), ((a.get_value() * b.get_value() - d.get_value()) / a.get_value())/200 ) if np.isfinite(x_nullcline_function(t)) ] ]
            )
            )
        )

        nullcline_z = VMobject()
        nullcline_z_values = [ [t, z_nullcline_function(t), 0] for t in np.arange(0, p3[0], p3[0]/200) if np.isfinite(z_nullcline_function(t))]

        for point in nullcline_z_values:
            nullcline_z.add(Dot(point, color = ORANGE, radius = DEFAULT_DOT_RADIUS*0.6))

        nullcline_z.add_updater(
            lambda m: m.become(
                VGroup(
            *[ Dot(point, color = ORANGE, radius = DEFAULT_DOT_RADIUS*0.6) for point in [ [t, z_nullcline_function(t), 0] for t in np.arange(0, ((g.get_value() * hh.get_value() - i.get_value() + np.sqrt(4 * e.get_value() * ff.get_value() * g.get_value() + (g.get_value() * hh.get_value() - i.get_value()) ** 2)) / (2 * g.get_value())), ((g.get_value() * hh.get_value() - i.get_value() + np.sqrt(4 * e.get_value() * ff.get_value() * g.get_value() + (g.get_value() * hh.get_value() - i.get_value()) ** 2)) / (2 * g.get_value()))/200) if np.isfinite(z_nullcline_function(t))] ]
            )
            )
        )

        trajectories = VGroup()
        for point in border_points:
            path2 = VMobject().set_color(BLUE_E)
            path2.set_points_smoothly(get_trajectory(point)).set_stroke(width=1.5)
            trajectories.add(path2)

        trajectories.add_updater(
            lambda m: m.become(
                VGroup( *[ VMobject().set_color(BLUE_E).set_points_smoothly(get_trajectory(point)).set_stroke(width=1.5) for point in border_points])
            )
            )
                
    
        # this is specific to each case 
        separatriz = VGroup()
        separatriz_values = get_trajectory( np.array([0.01, ff.get_value()]), 200 )
        separatriz_values.sort()

        for point in separatriz_values:
            separatriz.add(Dot(point, color = GREEN_E, radius=DEFAULT_DOT_RADIUS*0.6))
        
        separatriz.add_updater(
            lambda m: m.become(
            VGroup(
            *[ Dot(point, color = GREEN_E, radius=DEFAULT_DOT_RADIUS*0.6) for point in get_trajectory( np.array([0.01, ff.get_value()]), 200 )]
            )
            )
            )

        # LEGEND
        self.play(
            Create(sp0),
            Create(sp1),
            Create(sp2),
            Create(sp3),
            Create(sp4),
            Write(text_sp1),
            Write(text_sp2),
            Write(text_sp3),
            Write(text_sp4),
            Create(vector_field1),
            Write(description_text),
            Create(nullcline_x),
            Create(nullcline_z),
            Create(x_axis),
            Create(label_x_axis),
            Create(z_axis),
            Create(label_z_axis),
            Create(trajectories),
            Create(separatriz),
            Write(Tex("Separatriz", color = GREEN).scale(2).move_to([-3.5,10,0])),
            Write(Tex("Ceroclina $z$", color = ORANGE).scale(2).move_to([-3.5,8,0])),
            Write(Tex("Ceroclina $x$", color = PURPLE_A).scale(2).move_to([-3.5, 6, 0]))
        )
        self.play(
            i.animate.increment_value(-1),
            g.animate.increment_value(0.5),
            c.animate.increment_value(-0.3)
            )
        self.wait()
        
