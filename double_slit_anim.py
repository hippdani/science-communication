import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation


hz = 400
vert = 800
freq = 10 #spatial frequency = periods per horizontal screen
a_ovr_lam = 0.5 #slit width divided by wavelength
lam = hz/freq #wavelength

slit1_pos = 0.45
slit2_pos = 0.55

fig = plt.figure()
#col = np.zeros((vert, hz//2), dtype=float)
xx, yy = np.meshgrid(range(vert), range(hz//2), indexing = "ij")
plane = np.cos(yy/hz*2*np.pi*freq)
sphere = np.cos(np.sqrt((xx-vert/2)**2+yy**2)/hz*2*np.pi*freq)
colr = np.hstack((plane, sphere))

ims = plt.imshow(colr)

def update(frame):
    # for each frame, update the data stored on each artist.
    print(frame)
    phase = frame/40*np.pi*2
    plane = np.cos(yy / hz * 2 * np.pi * freq - phase)
    sphere1 = np.cos(np.sqrt((xx - vert*slit1_pos) ** 2 + yy ** 2) / hz * 2 * np.pi * freq - phase)
    angle1 = np.arctan2(xx-vert*slit1_pos,yy)
    sphere1 *= np.sinc(np.pi * a_ovr_lam * np.sin(angle1)) #fraunhofer diffraction for single slit
    sphere2 = np.cos(np.sqrt((xx - vert*slit2_pos) ** 2 + yy ** 2) / hz * 2 * np.pi * freq - phase)
    angle2 = np.arctan2(xx - vert*slit2_pos, yy)
    sphere2 *= np.sinc(np.pi * a_ovr_lam * np.sin(angle2))  # fraunhofer diffraction for single slit
    colr = np.hstack((plane, sphere1+sphere2))
    # update the scatter plot:
    ims.set_data(colr)
    return (ims)


ani = animation.FuncAnimation(fig=fig, func=update, frames=40, interval=30)
ani.save(filename=r"C:\Users\dhipp\Documents\PhD\Projekte\PR\TU_Reel_Oct2026/pillow_example.gif", writer="pillow", fps=30)
plt.show()

