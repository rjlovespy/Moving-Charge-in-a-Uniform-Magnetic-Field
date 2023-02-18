from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np 

m, q, Bx = 1, 1, 1
v, theta = 10, np.pi/4 

def dS_dt(S, t):
    x, y, z, vx, vy, vz = S
    dx_dt = vx
    dy_dt = vy
    dz_dt = vz
    dvx_dt = 0
    dvy_dt = (q*vz*Bx)/m
    dvz_dt = -(q*vy*Bx)/m
    return [dx_dt, dy_dt, dz_dt, dvx_dt, dvy_dt, dvz_dt]

t = np.linspace(0, 20, 1001)
S0 = (0, 0, 0, v*np.cos(theta), v*np.sin(theta), 0)
sol = odeint(dS_dt, S0, t)
x, y, z, vx, vy, vz = sol.T[0], sol.T[1], sol.T[2], sol.T[3], sol.T[4], sol.T[5]

fig = plt.figure()
ax= fig.add_subplot(projection="3d")
ax.plot(x,y,z, color="red",label="Trajectory")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title("When θ = π/4")
ax.grid(which="major")
ax.grid(which="minor",linestyle="--")
ax.minorticks_on()
fig.tight_layout()
plt.legend()
plt.show()