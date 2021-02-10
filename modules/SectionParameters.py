# CONSTANTS:
# F1 - gravel
h1_10 = 0.05
h1_9 = 0.25
h1_8 = 0.65
h1_7 = 1.05
h1_6 = 1.6
h1_5 = 2.175
h1_4 = 2.4
h1_3 = 2.625
h1_2 = 3.15
h1_1 = 3.85

# F2 - XPS
h2_12 = 0.05
h2_11 = 0.25
h2_10 = 0.65
h2_9 = 1.05
h2_8 = 1.2
h2_7 = 1.35
h2_6 = 1.4
h2_5 = 1.5
h2_4 = 1.825
h2_3 = 2.175
h2_2 = 2.4
h2_1 = 2.625

# F3 - 0/180
h3_8 = 0.05
h3_7 = 0.25
h3_6 = 0.65
h3_5 = 1.05
h3_4 = 1.6
h3_3 = 2.175
h3_2 = 2.4
h3_1 = 2.625

#F4 - foam glass
h4_10 = 0.05
h4_9 = 0.25
h4_8 = 0.65
h4_7 = 1.05
h4_6 = 1.20
h4_5 = 1.35
h4_4 = 1.75
h4_3 = 2.175
h4_2 = 2.4
h4_1 = 2.625

# F5 - 0/32
h5_8 = 0.05
h5_7 = 0.25
h5_6 = 0.65
h5_5 = 1.05
h5_4 = 1.6
h5_3 = 2.175
h5_2 = 2.4
h5_1 = 2.625

# F6: expanded clay
h6_10 = 0.05
h6_9 = 0.25
h6_8 = 0.65
h6_7 = 1.05
h6_6 = 1.20
h6_5 = 1.35
h6_4 = 1.75
h6_3 = 2.175
h6_2 = 2.4
h6_1 = 2.625

# F7: crushed rock 22/180
h7_10 = 0.05
h7_9 = 0.25
h7_8 = 0.65
h7_7 = 1.05
h7_6 = 1.60
h7_5 = 2.175
h7_4 = 2.4
h7_3 = 2.625
h7_2 = 3.15
h7_1 = 3.85

#####   layer thicknesses   ######
asphalt = 0.25
subbase = 0.8
t016 = 0.3
s016 = 0.1
xps = 0.05
s0180 = 0.65
m0180 = 0.8
t0180 = 1.1
ssubsoil = 0.85
tsubsoil = 1.85
leca = 0.3
foamglass = 0.3
gravel = 1.1
t032 = 1.1
t22180 = 1.1


class SectionParameters:
    def __init__(self):
        self.section_F1_args = ['F1_front',
                                'F1_front_thaw',
                                [h1_9, h1_7, h1_5],
                                [['asphalt:', '250mm'], ['subbase:', '250mm'], ['unsorted gravel', '1100mm'], ['subsoil']],
                                [asphalt, subbase, gravel, tsubsoil],
                                'F1: gravel',
                                'out/section_F1.png']

        self.section_F2_args = ['F2_front',
                                'F2_front_thaw',
                                [h2_11, h2_9, h2_7, h2_6, h2_5, h2_3],
                                [['asphalt:', '250mm'], ['subbase:', '250mm'],
                                 ['0/16:', '300mm'], ['XPS: 50mm'], ['0/16:100mm'], ['0/180:', '650mm'], ['subsoil']],
                                [asphalt, subbase, t016, xps, s016, s0180, tsubsoil],
                                'F2: XPS',
                                'out/section_F2.png']

        self.section_F3_args = ['F3_front',
                                'F3_front_thaw',
                                [h3_7, h3_5, h3_3],
                                [['asphalt:', '250mm'], ['subbase:', '250mm'],
                                 ['Crushed rock 0/180:', '1100mm'], ['subsoil']],
                                [asphalt, subbase, t0180, tsubsoil],
                                'F3: crushed rock',
                                'out/section_F3.png']

        self.section_F4_args = ['F4_front',
                                'F4_front_thaw',
                                [h4_9, h4_7, h4_5, h4_3],
                                [['asphalt:', '250mm'], ['subbase:', '250mm'],
                                 ['foam glass', '300mm'], ['crushed rock 0/180:', '800mm'], ['subsoil']],
                                [asphalt, subbase, foamglass, m0180, tsubsoil],
                                'F4: foam glass',
                                'out/section_F4.png']

        self.section_F5_args = ['F5_front',
                                'F5_front_thaw',
                                [h5_7, h5_5, h5_3],
                                [['asphalt:', '250mm'], ['subbase:', '250mm'],
                                 ['crushed rock 0/32', '1100mm'], ['subsoil']],
                                [asphalt, subbase, t032, tsubsoil],
                                'F5: crushed rock 0/32',
                                'out/section_F5.png']

        self.section_F6_args = ['F6_front',
                                'F6_front_thaw',
                                [h6_9, h6_7, h6_5, h6_3],
                                [['asphalt:', '250mm'], ['subbase:', '250mm'], ['expanded clay:', '300mm'],
                                ['0/180mm:', '800mm'], ['subsoil']],
                                [asphalt, subbase, leca, t0180, tsubsoil],
                                'F6: Expanded clay',
                                'out/section_F6.png']

        self.section_F7_args = ['F7_front',
                                'F7_front_thaw',
                                [h7_9, h7_7, h7_5],
                                [['asphalt:', '250mm'], ['subbase:', '250mm'], ['crushed rock 22/180:', '1100mm'], ['subsoil']],
                                [asphalt, subbase, t22180, tsubsoil],
                                'F7: crushed rock 22/180',
                                'out/section_F7.png']