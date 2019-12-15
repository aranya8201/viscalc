from manimlib.imports import *
import numpy as np

SCALE_FACTOR = 0.5

class Intro(Scene):
    def construct(self):
        innerCircle = Circle(radius = 3*SCALE_FACTOR, color = RED)
        outerCircle = Circle(radius = 5*SCALE_FACTOR, color = WHITE)
        area = Annulus(inner_radius = 3*SCALE_FACTOR, outer_radius = 5*SCALE_FACTOR, color = GOLD, fill_opacity = 0.8)

        chord = Line(color = RED, start = 3*DOWN*SCALE_FACTOR, end = 3*DOWN*SCALE_FACTOR+LEFT*4*SCALE_FACTOR, sheen_factor = 0.5)
        innerRadius = Line(color = GOLD, start = LEFT+RIGHT, end = 3*DOWN*SCALE_FACTOR)
        outerRadius = Line(color = GOLD, start = LEFT+RIGHT, end = 3*DOWN*SCALE_FACTOR+LEFT*4*SCALE_FACTOR)

        chordLabel = TextMobject("4", color = GOLD)
        innerRadiusLabel = TexMobject(r"{r}_{1}", color = GOLD)
        outerRadiusLabel = TexMobject(r"{r}_{2}", color = GOLD)

        title = TextMobject("Find this area with the given information")

        chordLabel.next_to(chord, DOWN)
        innerRadiusLabel.next_to(innerRadius, RIGHT)
        outerRadiusLabel.move_to(LEFT*1.2+DOWN*0.3)
        title.to_edge(UP)

        self.play(Write(outerCircle))
        self.play(Write(innerCircle))
        self.play(Write(chord), Write(chordLabel))
        self.play(Write(title), run_time = 4)

        self.wait()

        self.play(DrawBorderThenFill(area), run_time = 2)


        self.wait()
        self.play(Indicate(area))
        self.play(FadeOut(title))
        self.play(FadeOut(area))

        self.wait()

        self.play(Write(innerRadius), Write(outerRadius))
        self.play(Write(innerRadiusLabel), Write(outerRadiusLabel))

        calculationTitle = TextMobject("Area of ring (annulus):")
        calculationOne = TexMobject(r"=\pi{r}_{2}^{2}", "-", r"\pi{r}_{1}^{2}")

        calculationTwo = TexMobject(r"=\pi", r"\left({r}_{2}^{2} - {r}_{1}^{2}\right)")
        calculationThree = TexMobject(r"=\pi \left( {4}^{2} \right)")
        calculationFour = TexMobject(r"=16\pi")


        calculationTitle.move_to(3*UP+4.5*RIGHT)
        calculationOne.move_to(2*UP+5*RIGHT)
        calculationTwo.next_to(calculationOne, DOWN, buff = 0.5)
        calculationThree.next_to(calculationTwo, DOWN, buff = 0.5)
        calculationThree.shift(0.53*LEFT)
        calculationFour.next_to(calculationThree, DOWN, buff = 0.5)
        calculationFour.shift(LEFT*0.25)

        self.play(Write(calculationTitle))
        self.play(Write(calculationOne))
        self.wait(2)
        self.play(ReplacementTransform(calculationOne.copy(),calculationTwo))
        self.wait(2)
        self.play(ReplacementTransform(calculationTwo.copy(), calculationThree))
        self.wait(2)
        self.play(ReplacementTransform(calculationThree.copy(), calculationFour))
        self.wait()

        self.play(FadeOut(calculationTitle), FadeOut(calculationOne), FadeOut(calculationTwo), FadeOut(calculationThree), FadeOut(calculationFour))
        self.play(FadeOut(innerRadius), FadeOut(outerRadius), FadeOut(innerRadiusLabel), FadeOut(outerRadiusLabel))

        self.wait()

        newInner = Circle(radius = 3*SCALE_FACTOR, color = RED)
        newOuter = Circle(radius = 5*SCALE_FACTOR, color = WHITE)
        newChord = Line(color = RED, start = 3*DOWN*SCALE_FACTOR, end = 3*DOWN*SCALE_FACTOR+LEFT*4*SCALE_FACTOR, sheen_factor = 0.5)
        newChordLabel = TextMobject("4", color = GOLD)
        newAnnulusArea = Annulus(inner_radius = 3*SCALE_FACTOR, outer_radius = 5*SCALE_FACTOR, color = GOLD, fill_opacity = 0.8)

        newInner.shift(LEFT*2)
        newOuter.shift(LEFT*2)
        newChord.shift(LEFT*2)
        newChordLabel.next_to(newChord, DOWN)
        newAnnulusArea.shift(LEFT*2)

        self.play(Transform(innerCircle, newInner), Transform(outerCircle, newOuter), Transform(chord, newChord), Transform(chordLabel, newChordLabel))

        circle = Circle(radius = 4*SCALE_FACTOR, color = GOLD)
        circle.shift(3*RIGHT)
        circleArea = Dot(radius = 4*SCALE_FACTOR, fill_opacity = 0.8, color = GOLD)
        circleArea.shift(3*RIGHT)
        circleRadius =  Line(color = GOLD, start = 3*DOWN*SCALE_FACTOR, end = 3*DOWN*SCALE_FACTOR+LEFT*4*SCALE_FACTOR)
        circleRadius.shift(3*RIGHT+1.5*UP)
        circleRadiusLabel = TextMobject("4", color = GOLD)
        circleRadiusLabel.next_to(circleRadius, DOWN)

        self.play(Write(circle), Write(circleRadius), Write(circleRadiusLabel))
        self.play(DrawBorderThenFill(newAnnulusArea))
        self.play(DrawBorderThenFill(circleArea))
        self.play(Indicate(newAnnulusArea, scale_factor = 1.1), Indicate(circleArea, scale_factor = 1.1))

        title = TextMobject("Why do these shapes have the same area?")
        title.to_edge(UP)
        self.play(Write(title))

        self.wait(2)

class NewConstructionMethod(Scene):
    def construct(self):
        innerCircle = Circle(radius = 3*SCALE_FACTOR, color = RED)
        outerCircle = Circle(radius = 5*SCALE_FACTOR, color = WHITE)
        outerCircle.rotate(0.9273)
        tangent = Line(color = RED, sheen_factor = 0.5, start = 3*RIGHT*SCALE_FACTOR, end = 4*UP*SCALE_FACTOR+RIGHT*3*SCALE_FACTOR)
        pencil = Dot()
        pencil.move_to(tangent.get_end())

        self.play(Write(innerCircle), Write(tangent))
        self.wait()
        self.play(Write(pencil))
        self.wait()
        self.play(Rotating(tangent, run_time = 2, about_point = ORIGIN), Rotating(pencil, run_time = 2, about_point = ORIGIN), Write(outerCircle, run_time = 4))
        self.wait()



class GetArea(Scene):
    def makeTriangle(self,tangent, time, DELTA_X):
        perp_dir_vec = np.array([-1*DELTA_X*np.sin(tangent.get_angle()),DELTA_X*np.cos(tangent.get_angle()),0])
        perpendicular = Line(color = GOLD, stroke_width = 1, stroke_opacity = 1, start = tangent.get_end(), end = tangent.get_end()+perp_dir_vec)
        hypotenuse = Line(color = GOLD,stroke_width = 1, stroke_opacity = 1, start = tangent.get_start(), end = perpendicular.get_end())
        newTangent = Line(color = GOLD, stroke_width = 1, stroke_opacity = 1, start = tangent.get_start(), end = tangent.get_end())
        self.play(Write(perpendicular), Write(hypotenuse), Write(newTangent.copy()), run_time = time)




    def construct(self):
        innerCircle = Circle(radius = 3*SCALE_FACTOR, color = RED)
        outerCircle = Circle(radius = 5*SCALE_FACTOR, color = WHITE)
        tangent = Line(color = RED, start = 3*RIGHT*SCALE_FACTOR, end = 4*UP*SCALE_FACTOR+RIGHT*3*SCALE_FACTOR)


        self.play(Write(innerCircle), Write(outerCircle), Write(tangent))
        d_x = 0.352653961417 #36 triangles
        d_x_label = TextMobject("$h$", color = GOLD).scale(0.5)


        GetArea.makeTriangle(self,tangent, 2, d_x)
        d_x_label.next_to(tangent, UP+LEFT*0.5)
        self.play(Write(d_x_label))
        self.wait()

        for i in range(int(np.round(TAU/np.arctan(d_x/2)))-2):
            GetArea.makeTriangle(self,tangent, 0.1, d_x)
            tangent.rotate(np.arctan(d_x/2)+0.01, about_point = ORIGIN)

        self.wait(3)

        limit = TextMobject(r"$\lim _{ h\rightarrow 0 }$ approximates the area of the annulus more and more accurately").scale(0.7)
        limit.to_edge(UP)
        self.play(Write(limit))

        cover = AnnularSector(color = BLACK, inner_radius = 3*SCALE_FACTOR, outer_radius = 5*SCALE_FACTOR, angle = TAU)
        self.add(cover)

        d_x = 0.12583 #100 triangles
        tangent = Line(color = RED, start = 3*RIGHT*SCALE_FACTOR, end = 4*UP*SCALE_FACTOR+RIGHT*3*SCALE_FACTOR)
        self.play(Write(tangent))
        GetArea.makeTriangle(self, tangent, 2, d_x)

        for i in range(int(np.round(TAU/np.arctan(d_x/2)))):
            GetArea.makeTriangle(self,tangent, 0.02, d_x) #only works at 60 fps
            tangent.rotate(np.arctan(d_x/2), about_point = ORIGIN)

        self.wait(3)

        d_x = 0.03491013 #360 triangles
        self.add(cover)
        tangent = Line(color = RED, start = 3*RIGHT*SCALE_FACTOR, end = 4*UP*SCALE_FACTOR+RIGHT*3*SCALE_FACTOR)
        self.play(Write(tangent))
        GetArea.makeTriangle(self, tangent, 2, d_x)
        for i in range(int(np.round(TAU/np.arctan(d_x/2)))):
            GetArea.makeTriangle(self,tangent, 0.017, d_x) #only works at 60 fps
            tangent.rotate(np.arctan(d_x/2), about_point = ORIGIN)

        self.wait()


class Combine(Scene):
    def makeTriangle(self,tangent, time, DELTA_X):
        perp_dir_vec = np.array([-1*DELTA_X*np.sin(tangent.get_angle()),DELTA_X*np.cos(tangent.get_angle()),0])
        perpendicular = Line(color = GOLD, stroke_width = 1, stroke_opacity = 0.2, start = tangent.get_end(), end = tangent.get_end()+perp_dir_vec)
        hypotenuse = Line(color = GOLD,stroke_width = 1, stroke_opacity = 0.2, start = tangent.get_start(), end = perpendicular.get_end())
        newTangent = Line(color = GOLD, stroke_width = 1, stroke_opacity = 0.2, start = tangent.get_start(), end = tangent.get_end())
        self.add(perpendicular, hypotenuse, newTangent)

    def moveTriangle(self, tangent, centreTangent, time, DELTA_X):
        perp_dir_vec = np.array([-1*DELTA_X*np.sin(tangent.get_angle()),DELTA_X*np.cos(tangent.get_angle()),0])
        perpendicular = Line(color = GOLD, stroke_width = 1, stroke_opacity = 1, start = tangent.get_end(), end = tangent.get_end()+perp_dir_vec)
        hypotenuse = Line(color = GOLD,stroke_width = 1, stroke_opacity = 1, start = tangent.get_start(), end = perpendicular.get_end())
        newTangent = Line(color = GOLD, stroke_width = 1, stroke_opacity = 1, start = tangent.get_start(), end = tangent.get_end())

        centre_perp_vec = np.array([-1*DELTA_X*np.sin(centreTangent.get_angle()),DELTA_X*np.cos(centreTangent.get_angle()),0])
        centrePerp = Line(color = RED, stroke_width = 1, stroke_opacity = 1, start = centreTangent.get_end(), end = centreTangent.get_end()+centre_perp_vec)
        centreHyp = Line(color = RED,stroke_width = 1, stroke_opacity = 1, start = centreTangent.get_start(), end = centrePerp.get_end())
        self.play(Transform(newTangent, centreTangent), Transform(perpendicular, centrePerp), Transform(hypotenuse, centreHyp), run_time = time)



    def construct(self):
        areaCircle = Circle(radius = 4*SCALE_FACTOR, color = GOLD, fill_opacity = 0.3)
        tangent = Line(color = RED, start = 3*RIGHT*SCALE_FACTOR, end = 4*UP*SCALE_FACTOR+RIGHT*3*SCALE_FACTOR)
        self.wait(2)
        d_x = 0.352653961417 #36 triangles
        radius = Line(color = RED, stroke_width = 1, stroke_opacity = 1, start = ORIGIN, end = 4*RIGHT*SCALE_FACTOR)

        for i in range(int(np.round(TAU/np.arctan(d_x/2)))):
            Combine.makeTriangle(self,tangent, 0.1, d_x)
            tangent.rotate(np.arctan(d_x/2)+0.01, about_point = ORIGIN)

        self.wait()

        for i in range(int(np.round(TAU/np.arctan(d_x/2)))-2):
            Combine.moveTriangle(self, tangent, radius, 0.1, d_x)
            tangent.rotate(np.arctan(d_x/2)+0.01, about_point = ORIGIN)
            radius.rotate(np.arctan(d_x/2)+0.01, about_point = ORIGIN)

        self.wait(2)
        self.remove(radius, tangent)
        cover = Circle(color = BLACK, fill_opacity = 1, radius = 5)

        d_x = 0.12583
        tangent = Line(color = RED, start = 3*RIGHT*SCALE_FACTOR, end = 4*UP*SCALE_FACTOR+RIGHT*3*SCALE_FACTOR)
        radius = Line(color = RED, stroke_width = 1, stroke_opacity = 1, start = ORIGIN, end = 4*RIGHT*SCALE_FACTOR)
        self.play(Write(cover))
        self.wait()

        for i in range(int(np.round(TAU/np.arctan(d_x/2)))):
            Combine.makeTriangle(self,tangent, 0.1, d_x)
            tangent.rotate(np.arctan(d_x/2), about_point = ORIGIN)

        self.wait()

        for i in range(int(np.round(TAU/np.arctan(d_x/2)))):
            Combine.moveTriangle(self, tangent, radius, 0.1, d_x)
            tangent.rotate(np.arctan(d_x/2), about_point = ORIGIN)
            radius.rotate(np.arctan(d_x/2), about_point = ORIGIN)

        self.wait(2)
        self.remove(radius, tangent)
        cover = Circle(color = BLACK, fill_opacity = 1, radius = 5)

        d_x = 0.03491013
        tangent = Line(color = RED, start = 3*RIGHT*SCALE_FACTOR, end = 4*UP*SCALE_FACTOR+RIGHT*3*SCALE_FACTOR)
        radius = Line(color = RED, stroke_width = 1, stroke_opacity = 1, start = ORIGIN, end = 4*RIGHT*SCALE_FACTOR)
        self.play(Write(cover))
        self.wait()

        for i in range(int(np.round(TAU/np.arctan(d_x/2)))):
            Combine.makeTriangle(self,tangent, 0.1, d_x)
            tangent.rotate(np.arctan(d_x/2), about_point = ORIGIN)

        self.wait()

        for i in range(int(np.round(TAU/np.arctan(d_x/2)))):
            Combine.moveTriangle(self, tangent, radius, 0.1, d_x)
            tangent.rotate(np.arctan(d_x/2), about_point = ORIGIN)
            radius.rotate(np.arctan(d_x/2), about_point = ORIGIN)

        self.play(Write(areaCircle))
        self.play(Indicate(areaCircle))

        cover = Circle(color = BLACK, fill_opacity = 1, radius = 5)
        self.play(Write(cover))
