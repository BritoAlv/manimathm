#Python3 Code @BritoAlv

from manim import *

if __name__ == '__main__':
    import subprocess
    params = 'manim -pql manim_template.py A'.split()
    subprocess.run(params,
                   check=True,
                   capture_output=False,
                   text=True)

class A(ZoomedScene):
    def construct(self):
        self.camera.background_color = "#ece6e2"
        
        
