import numpy as np
import matplotlib.pyplot as plt

# Given constants
T0 = -13   # Base temperature (°C)
k = 1.09e-6  # Thermal diffusivity (m²/s)

# Time and frequency
seconds_per_day = 24 * 60 * 60 
w = (2*np.pi) / (seconds_per_day * 365)   # Yearly frequency (rad/s)

months = [
    (31, -20.5), (28, -20.25), (31, -20), (30, -17.5), (31, -13), (30, -10), (31, -7.5), (31, -7), (30, -9), (31, -12), 
    (30, -16), (31, -19)
]


# Depth range (h)
h = np.linspace(-0.1, 20, 100)  # Depth in meters

# Compute temperature as a function of depth
def temperature(t, delT):
    return T0 + delT * np.exp(-h * np.sqrt(w / (2 * k))) * np.sin(w * t - h * np.sqrt(w / (2 * k)))

# Plotting
plt.figure(figsize=(8, 6))

i = 0
days_past = 0

for month, delT in months:
    days_past += (month/2) # halfway through the month
    t = days_past * seconds_per_day # seconds past
    i+=1
    days_past += (month/2) # adding the other half
    plt.plot(temperature(t, delT), -h, label=str(i))


plt.xlabel("Temperature (°C)")
plt.ylabel("Depth (m)")
plt.xlim(-20,-6)
plt.title("Temperature Variation with Depth")
plt.legend()
plt.grid()
plt.show()

x = np.arange(np.pi/4, 4*np.pi, 0.1)
y = 7*np.sin((x+3*np.pi)/2) - 14

plt.figure(figsize=(8,6))
monthS = np.arange(1,13)
delTs = []
for month, delT in months:
    delTs.append(delT)

plt.plot(x,y)
plt.plot(monthS, delTs)
plt.xlabel("Month (1 corresponds to January)")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Fluctuation Variations with Month")
plt.show()
