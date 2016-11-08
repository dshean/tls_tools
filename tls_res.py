#! /usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

#Info from Riegl
#http://www.riegl.com/uploads/tx_pxpriegldownloads/DataSheet_VZ-4000_2015-03-24.pdf

beam_div = 0.15E-3 #mrad
#18 mm at exit
#75 mm at 500 m
#150 mm at 1000 m
#300 mm at 2000 m

min_ang_step = 0.002
max_ang_step = 0.280

#ang_step_a = np.array([0.002, 0.005, 0.01, 0.02, 0.05, 0.1, 0.15, 0.2, 0.280])
#ang_step_a = np.array([0.05, 0.1, 0.15, 0.2, 0.280])
ang_step_a = np.array([0.002, 0.005, 0.01, 0.02])
range_a = np.array([5, 10, 50, 100, 500, 1000, 2000, 3000, 4000, 5000])

plt.figure()

for ang_step in ang_step_a:
    dist = 2.0*range_a*np.tan(np.radians(ang_step/2.0))
    #plt.plot(range_a, dist, label='Angular Step %s$^\circ$' % ang_step)
    plt.plot(range_a, dist*100., label='Angular Step %s$^\circ$' % ang_step)

spot = 2.0*range_a*np.tan((beam_div/2.0))
#plt.plot(range_a, spot, color='k', linestyle='--', label='Spot Diameter\nAngular Step 0.0086$^\circ$')
plt.plot(range_a, spot*100., color='k', linestyle='--', label='Spot Diameter\nAngular Step 0.0086$^\circ$')

plt.title('VZ-4000 Shot Diameter/Spacing vs. Range')
plt.xlabel('Range (m)')
#plt.ylabel('Shot Diameter/Spacing (m)')
plt.ylabel('Shot Diameter/Spacing (cm)')
plt.legend(loc='upper left')
plt.savefig('vz4000_shot_diam_spacing_v_range.pdf')

