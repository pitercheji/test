import numpy as np
heart_rate = np.array([78, 82, 88, 95, 104, 110, 98, 92, 85, 80, 76, 74])
mean_hr = np.mean(heart_rate)
min_hr = np.min(heart_rate)
max_hr = np.max(heart_rate)
tachycardia = heart_rate[heart_rate > 100]
print(f"Mean heart rate: {mean_hr:.2f} bpm")
print(f"Min/max: {min_hr}/{max_hr} bpm")
print(f"Tachycardia readings: {tachycardia}")
print(f"Number of tachycardic hours: {tachycardia.size}")