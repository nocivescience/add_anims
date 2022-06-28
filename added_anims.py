from this import d
from manim import *
import itertools as it
class TwoCase(Scene):
    def construct(self):
        anims=self.all_anims(self.get_triangles())
        self.play(anims)
        self.wait()
    def get_anims(self):
        dot=Dot()
        return Create(dot)
    def other_animations(self):
        circle=Circle()
        return FadeIn(circle)
    def get_triangles(self):
        triangle=Triangle()
        return [GrowFromCenter(triangle)]
    def all_anims(self,*added_anims):
        anims=it.chain(self.get_anims(),*added_anims)
        return anims