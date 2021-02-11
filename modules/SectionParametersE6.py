# Sensor locations:
# Section F1 - gravel
F1_10 = 0.05    # below first asphalt layer
F1_9 = 0.25     # asphalt/subbase interface
F1_8 = 0.65     # mid subbase
F1_7 = 1.05     # subbase/frost protection interface
F1_6 = 1.6      # mid frost protection
F1_5 = 2.175    # frost protection/subgrade interface
F1_4 = 2.4      # 22.5cm into subgrade
F1_3 = 2.625    # 45.0cm into subgrade
F1_2 = 3.15     # 97.5cm into subgrade
F1_1 = 3.85     # 167.5cm into subgrade
F1_sensor_loc = [F1_10, F1_9, F1_8, F1_7, F1_6, F1_5, F1_4, F1_3, F1_2, F1_1]

# Section F2 - XPS
F2_12 = 0.05    # below first asphalt layer
F2_11 = 0.25    # asphalt/subbase interface
F2_10 = 0.65    # mid subbase
F2_9 = 1.05     # subbase/upper 0/16mm interface
F2_8 = 1.2      # mid upper 0/16mm
F2_7 = 1.35     # upper 0/16mm/xps interface
F2_6 = 1.4      # xps& lower 0/16mm interface
F2_5 = 1.5      # lower 0/16mm/frost protection interface
F2_4 = 1.825    # mid frost protection interface
F2_3 = 2.175    # frost protection/subgrade interface
F2_2 = 2.4      # 22.5cm into subgrade
F2_1 = 2.625    # 45.0cm into subgrade
F2_sensor_loc = [F2_12, F2_11, F2_10, F2_9, F2_8, F2_7, F2_6, F2_5, F2_4, F2_3, F2_2, F2_1]

# Section F3 - 0/180
F3_8 = 0.05     # below first asphalt layer
F3_7 = 0.25     # asphalt/subbase interface
F3_6 = 0.65     # mid subbase
F3_5 = 1.05     # subbase/frost protection interface
F3_4 = 1.6      # mid frost protection
F3_3 = 2.175    # frost protection/subgrade interface
F3_2 = 2.4      # 22.5cm into subgrade
F3_1 = 2.625    # 45.0cm into subgrade
F3_sensor_loc = [F3_8, F3_7, F3_6, F3_5, F3_4, F3_3, F3_2, F3_1]

# Section F4 - foam glass
F4_10 = 0.05    # below first asphalt layer
F4_9 = 0.25     # asphalt subbase interface
F4_8 = 0.65     # mid subbase
F4_7 = 1.05     # subbase/foam glass interface
F4_6 = 1.20     # mid foam glass
F4_5 = 1.35     # foam glass/frost protection interface
F4_4 = 1.75     # mid frost protection
F4_3 = 2.175    # frost protection/subgrade interface
F4_2 = 2.4      # 22.5cm into subgrade
F4_1 = 2.625    # 45.0cm into subgrade
F4_sensor_loc = [F4_10, F4_9, F4_8, F4_7, F4_6, F4_5, F4_4, F4_3, F4_2, F4_1]

# Section F5 - 0/32
F5_8 = 0.05     # below first asphalt layer
F5_7 = 0.25     # asphalt/subbase interface
F5_6 = 0.65     # mid subbase
F5_5 = 1.05     # subbase/0/32mm interface
F5_4 = 1.6      # mid 0/32mm
F5_3 = 2.175    # frost protection/subgrade interface
F5_2 = 2.4      # 22.5cm into subgrade
F5_1 = 2.625    # 45.0cm into subgrade
F5_sensor_loc = [F5_8, F5_7, F5_6, F5_5, F5_4, F5_3, F5_2, F5_1]

# Section F6 - expanded clay
F6_10 = 0.05    # below first asphalt layer
F6_9 = 0.25     # asphalt/subbase interface
F6_8 = 0.65     # mid subbase
F6_7 = 1.05     # subbase/foam glass interface
F6_6 = 1.20     # mid foam glass
F6_5 = 1.35     # foam glass/frost protection interface
F6_4 = 1.75     # mid frost protection
F6_3 = 2.175    # frost protection/subgrade interface
F6_2 = 2.4      # 22.5cm into subgrade
F6_1 = 2.625    # 45.0cm into subgrade
F6_sensor_loc = [F6_10, F6_9, F6_8, F6_7, F6_6, F6_5, F6_4, F6_3, F6_2, F6_1]

# F7: crushed rock 22/180
F7_10 = 0.05    # below first asphalt layer
F7_9 = 0.25     # asphalt/subbase interface
F7_8 = 0.65     # mid subbase
F7_7 = 1.05     # subbase/frost protection interface
F7_6 = 1.60     # mid frost protection
F7_5 = 2.175    # frost protection/subgrade interface
F7_4 = 2.4      # 22.5cm into subgrade
F7_3 = 2.625    # 45.0cm into subgrade
F7_2 = 3.15     # 97.5cm into subgrade
F7_1 = 3.85     # 167.5cm into subgrade
F7_sensor_loc = [F7_10, F7_9, F7_8, F7_7, F7_6, F7_5, F7_4, F7_3, F7_2, F7_1]

# Interface location:
F1_int1 = 0.00  # top of asphalt
F1_int2 = 0.25  # asphalt/subbase interface
F1_int3 = 1.05  # subbase/frost protection interface
F1_int4 = 2.05  # frost protection/subgrade interface
F1_interface = []

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


class SectionParameters2:
    def __inti__(self):
        self.section_F1 =


class SectionParameters:
    def __init__(self):
        self.section_F1_args = ['F1_front',
                                'F1_front_thaw',
                                [F1_9, F1_7, F1_5],
                                [['asphalt:', '250mm'], ['subbase:', '250mm'], ['unsorted gravel', '1100mm'], ['subsoil']],
                                [asphalt, subbase, gravel, tsubsoil],
                                'F1: gravel',
                                'out/section_F1.png']

        self.section_F2_args = ['F2_front',
                                'F2_front_thaw',
                                [F2_11, F2_9, F2_7, F2_6, F2_5, F2_3],
                                [['asphalt:', '250mm'], ['subbase:', '250mm'],
                                 ['0/16:', '300mm'], ['XPS: 50mm'], ['0/16:100mm'], ['0/180:', '650mm'], ['subsoil']],
                                [asphalt, subbase, t016, xps, s016, s0180, tsubsoil],
                                'F2: XPS',
                                'out/section_F2.png']

        self.section_F3_args = ['F3_front',
                                'F3_front_thaw',
                                [F3_7, F3_5, F3_3],
                                [['asphalt:', '250mm'], ['subbase:', '250mm'],
                                 ['Crushed rock 0/180:', '1100mm'], ['subsoil']],
                                [asphalt, subbase, t0180, tsubsoil],
                                'F3: crushed rock',
                                'out/section_F3.png']

        self.section_F4_args = ['F4_front',
                                'F4_front_thaw',
                                [F4_9, F4_7, F4_5, F4_3],
                                [['asphalt:', '250mm'], ['subbase:', '250mm'],
                                 ['foam glass', '300mm'], ['crushed rock 0/180:', '800mm'], ['subsoil']],
                                [asphalt, subbase, foamglass, m0180, tsubsoil],
                                'F4: foam glass',
                                'out/section_F4.png']

        self.section_F5_args = ['F5_front',
                                'F5_front_thaw',
                                [F5_7, F5_5, F5_3],
                                [['asphalt:', '250mm'], ['subbase:', '250mm'],
                                 ['crushed rock 0/32', '1100mm'], ['subsoil']],
                                [asphalt, subbase, t032, tsubsoil],
                                'F5: crushed rock 0/32',
                                'out/section_F5.png']

        self.section_F6_args = ['F6_front',
                                'F6_front_thaw',
                                [F6_9, F6_7, F6_5, F6_3],
                                [['asphalt:', '250mm'], ['subbase:', '250mm'], ['expanded clay:', '300mm'],
                                ['0/180mm:', '800mm'], ['subsoil']],
                                [asphalt, subbase, leca, t0180, tsubsoil],
                                'F6: Expanded clay',
                                'out/section_F6.png']

        self.section_F7_args = ['F7_front',
                                'F7_front_thaw',
                                [F7_9, F7_7, F7_5],
                                [['asphalt:', '250mm'], ['subbase:', '250mm'], ['crushed rock 22/180:', '1100mm'], ['subsoil']],
                                [asphalt, subbase, t22180, tsubsoil],
                                'F7: crushed rock 22/180',
                                'out/section_F7.png']