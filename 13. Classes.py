"""GUARDPASS NOGI"""
class guardpass():
    def __init__(self, grips, angle, distance, height, chest_to_chest_connect):
        self.grips = grips;
        self.angle = angle;
        self.distance = distance;
        self.height = height;
        self.chest_to_chest_connect = chest_to_chest_connect;
    def toreandor(self):
        tgpass = "1st step: take a/an {g}\n2nd step: step to side for a {a} angle " \
                "relative to an opponents vertical body line\n" \
                "3rd step: go around opponents body until you pass a {d}\n" \
                "4th step: get a {h} level of your body\n" \
                "5th step: set a sidecontrol by {c}\n".format(g=self.grips,
                                                              a=self.angle,
                                                              d=self.distance,
                                                              h=self.height,
                                                              c=self.chest_to_chest_connect)
        print(tgpass)

    def overunder(self):
        ogpass = "1st step: take a/an {g} on a free opponents leg and lie down your another" \
                 " shoulder on a belly with gripping another leg\n2nd step:" \
                 " step over another leg with your leg that is between opponents leg and lie down your buttocks for a {a} angle " \
                "relative to an opponents vertical body line\n" \
                "3rd step: with a shoulder presure make your legs go around opponents body until you pass a {d}\n" \
                "4th step: get a {h} level of your body\n" \
                "5th step: set a sidecontrol by {c}\n".format(g=self.grips,
                                                              a=self.angle,
                                                              d=self.distance,
                                                              h=self.height,
                                                              c=self.chest_to_chest_connect)
        print(ogpass)

    def doubleunder(self):
        dgpass = "1st step: take a/an {g} with your two hands and rise opponents legs up\n2nd step: " \
                 "move your buttocks to side for a {a} angle " \
                "relative to an opponents vertical body line\n" \
                "3rd step: last steps made you to to pass a {d}\n" \
                "4th step: keep a {h} level of your body\n" \
                "5th step: set a sidecontrol by {c}\n".format(g=self.grips,
                                                              a=self.angle,
                                                              d=self.distance,
                                                              h=self.height,
                                                              c=self.chest_to_chest_connect)
        print(dgpass)

    def kneecut(self):
        kgpass = "1st step: take a/an {g}\n2nd step: while stepping to side for a {a} angle relative to" \
                 " an opponents vertical body line put a knee on opponents hips " \
                 "and another leg put to side like a wedge\n" \
                 "3rd step: move your knee forward until you pass a {d} with your buttocks\n" \
                 "4th step: your body must be on a {h} level\n" \
                 "5th step: set a sidecontrol by {c}\n".format(g=self.grips,
                                                              a=self.angle,
                                                              d=self.distance,
                                                              h=self.height,
                                                              c=self.chest_to_chest_connect)
        print(kgpass)

    def smashpass(self):
        sgpass = "1st step: take a/an {g}\n2nd step: jump with your legs to side for a {a} angle " \
                "relative to an opponents vertical body line\n" \
                "3rd step: your buttocks must be beyond a {d}\n" \
                "4th step: your buttocks must be very {h} and you must squeeze your opponents legs to his shoulders\n" \
                "5th step: step over opponents legs and set a sidecontrol by {c}\n".format(g=self.grips,
                                                              a=self.angle,
                                                              d=self.distance,
                                                              h=self.height,
                                                              c=self.chest_to_chest_connect)
        print(sgpass)

    def legdrag(self):
        lgpass = "1st step: take a/an {g}\n2nd step: step to side for a {a} angle relative to an opponents vertical" \
                 " body line and push opponents leg to anothe side\n" \
                "3rd step: put your shin on an opponents far tie and you will control his {d}\n" \
                "4th step: keep a {h} level of your body\n" \
                "5th step: control his shoulder line with your hands and go around with your " \
                 "legs and set a sidecontrol by {c}\n".format(g=self.grips,
                                                              a=self.angle,
                                                              d=self.distance,
                                                              h=self.height,
                                                              c=self.chest_to_chest_connect)
        print(lgpass)


grips_list = ['grip over shin', 'grip under shin', 'knee grip', 'knee overhook', 'knee underhook', 'wrist grip', 'underhook']
angle_list = ['45', '90', '120', 'no']
distance_list = ['foot level', 'knee level', 'pelvis level']
height_list = ['straight', 'bent', 'low']
chest_to_chest_connect_list = ['crossface + low pelvis + hand between your & opponents pelvises',
                               'underhook + low pelvis + your elbow on the other side',
                               'hand control of opponents pelvis + low butts pressing opponents elbows up']

opponents_position = ['1) seatup', "2) supine + you're far", "3) supine + you're close + one leg between your legs",
                      "4) supine + you're close + two legs between your legs",
                      "5) supine + you're close + your legs between opponents legs\n"]

print(opponents_position[0] + '\n' + opponents_position[1] + '\n' + opponents_position[2] +
      '\n' + opponents_position[3] + '\n' + opponents_position[4])
opp_pos = input('What position does your opponent have? 1, 2, 3, 4 or 5?\n')

if opp_pos == "1":
    print("\nTOREANDOR!\n")
    gpa1 = guardpass(grips_list[2], angle_list[2], distance_list[2], height_list[2], chest_to_chest_connect_list[0])
    gpa1.toreandor()
elif opp_pos == "2":
    print("\nLEGDRAG!\n")
    gpa2 = guardpass(grips_list[0], angle_list[0], distance_list[1], height_list[1], chest_to_chest_connect_list[1])
    gpa2.legdrag()
elif opp_pos == "3":
    print("\nKNEECUT!\n")
    gpa3 = guardpass(grips_list[2], angle_list[1], distance_list[2], height_list[2], chest_to_chest_connect_list[0])
    gpa3.kneecut()
    print("\nOR!\nOVERUNDER!\n")
    gpa3_1 = guardpass(grips_list[4], angle_list[0], distance_list[1], height_list[2], chest_to_chest_connect_list[1])
    gpa3_1.overunder()
elif opp_pos == "4":
    print("\nSMASHPASS!\n")
    gpa4 = guardpass(grips_list[6], angle_list[1], distance_list[2], height_list[2], chest_to_chest_connect_list[0])
    gpa4.smashpass()
elif opp_pos == "5":
    print("\nDOUBLEUNDER!\n")
    gpa5 = guardpass(grips_list[4], angle_list[2], distance_list[2], height_list[2], chest_to_chest_connect_list[2])
    gpa5.doubleunder()
else:
    print("dinahuy")