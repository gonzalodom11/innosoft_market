import numpy as np
import matplotlib.pyplot as plt

# Define the parameters for the phasors
VR = 1.25  # Amplitude of VR (in volts)
VC = 2.0    # Amplitude of VC (in volts)
phi_vc = -2 * np.pi * 116e-6 * 1000  # Phase difference for VC (radians)

# Calculate the components of the phasors
VR_real = VR  # Real part of VR
VR_imag = 0   # Imaginary part of VR (reference)

VC_real = VC * np.cos(phi_vc)  # Real part of VC
VC_imag = VC * np.sin(phi_vc)  # Imaginary part of VC

# Sum of phasors
V_total_real = VR_real + VC_real
V_total_imag = VR_imag + VC_imag

# Plot the phasors
plt.figure(figsize=(8, 8))

# Plot VR
plt.quiver(0, 0, VR_real, VR_imag, angles='xy', scale_units='xy', scale=1, color='b', label="$V_R$ (Reference)")

# Plot VC
plt.quiver(0, 0, VC_real, VC_imag, angles='xy', scale_units='xy', scale=1, color='r', label="$V_C$")

# Plot the sum of phasors
plt.quiver(0, 0, V_total_real, V_total_imag, angles='xy', scale_units='xy', scale=1, color='g', label="$V_{total}$")

# Add annotations for phasors
plt.text(VR_real / 2, VR_imag / 2, "$V_R$", color='b')
plt.text(VC_real / 2, VC_imag / 2, "$V_C$", color='r')
plt.text(V_total_real / 2, V_total_imag / 2, "$V_{total}$", color='g')

# Configure the plot
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.xlim(-2.5, 2.5)
plt.ylim(-2.5, 2.5)
plt.grid()
plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel("Real Axis")
plt.ylabel("Imaginary Axis")
plt.title("Phasor Diagram in Binomic Form")
plt.legend()
plt.show()

# Print phasor values in binomic and polar forms
print(f"VR = {VR_real} + j{VR_imag} (Binomic Form)")
print(f"VC = {VC_real:.2f} + j{VC_imag:.2f} (Binomic Form)")
print(f"V_total = {V_total_real:.2f} + j{V_total_imag:.2f} (Binomic Form)")

VR_magnitude = np.sqrt(VR_real**2 + VR_imag**2)
VC_magnitude = np.sqrt(VC_real**2 + VC_imag**2)
V_total_magnitude = np.sqrt(V_total_real**2 + V_total_imag**2)

VR_angle = np.arctan2(VR_imag, VR_real)
VC_angle = np.arctan2(VC_imag, VC_real)
V_total_angle = np.arctan2(V_total_imag, V_total_real)

print(f"VR = {VR_magnitude:.2f}∠{VR_angle:.2f} rad (Polar Form)")
print(f"VC = {VC_magnitude:.2f}∠{VC_angle:.2f} rad (Polar Form)")
print(f"V_total = {V_total_magnitude:.2f}∠{V_total_angle:.2f} rad (Polar Form)")
