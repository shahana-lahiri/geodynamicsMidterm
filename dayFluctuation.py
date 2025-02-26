import numpy as np
import matplotlib.pyplot as plt

# Given constants
T0 = -13   # Base temperature (°C)
k = 1.09e-6  # Thermal diffusivity (m²/s)

# Time and frequency
seconds_per_day = 24 * 60 * 60 
w = (2*np.pi) / (seconds_per_day)   # Yearly frequency (rad/s)

months = [
    (0, -19), (2, -18.3), (4, -18.5), (6, -18.7), (8, -18.5), (10, -18.2),
    (12, -18.4), (14, -18.3), (16, -18.6), (18, -19.1), (20, -19.5), (22, -19.7)
]


# Depth range (h)
h = np.linspace(0, 2, 100)  # Depth in meters

# Compute temperature as a function of depth
def temperature(t, delT):
    return T0 + delT * np.exp(-h * np.sqrt(w / (2 * k))) * np.sin(w * t - h * np.sqrt(w / (2 * k)))

# Plotting
plt.figure(figsize=(8, 6))

i = 0

for month, delT in months:
    t = month * 3600 # seconds past
    i+=2
    plt.plot(temperature(t, delT), -h, label=str(month))


plt.xlabel("Temperature (°C)")
plt.ylabel("Depth (m)")
plt.xlim(-20,-6)
plt.title("Temperature Variation with Depth on 2/27/25 (Today)")
plt.legend()
plt.grid()
plt.show()

x = np.arange(0, 7*np.pi, 0.1)
y = np.sin((x/4) + (3*np.pi)/2) - 19.25

plt.figure(figsize=(8,6))
monthS = np.arange(0,23,2)
delTs = []
for month, delT in months:
    delTs.append(delT)

plt.plot(x,y)
plt.plot(monthS, delTs)
plt.ylabel("Temperature (°C)")
plt.xlabel("Hour (0 corresponding to Midnight)")
plt.title("Temperature Fluctuation with Time on 2/27/25 (Today)")
plt.show()
