from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

data = open("Electron.dat", "r").read()

def find_all(a_str, sub):
	start = 0
	while True:
		start = a_str.find(sub, start)
		if start == -1: return
		yield start
		start += len(sub)

event_indices = list(find_all(data, "Event"))
event_indices.append(len(data))

intensity = []

for line in data.split("\n"):
	if line and line.split()[-1] == "eIoni":
		intensity.append(float(line.split()[5]))

dEmax = max(intensity)
dEmin = min(intensity)
colors = np.array(intensity)
norm=plt.Normalize(colors.min(), colors.max())

event_list = ["1", "2", "3", "4", "5"]
track_list = ["1"]
for eachEvent in range(0, len(event_indices) - 1):
	event = data[event_indices[eachEvent]:event_indices[eachEvent+1]]
	event_id = event.split("\n")[0]
	entries = event.split("\n")
	x = []
	y = []
	z = []
	dE = []

	if event_id.split()[-1] in event_list:
		track_indices = list(find_all(event, "Track ID = "))
		track_indices.append(len(event))
		for eachTrack in range(0, len(track_indices) - 1):
			track = event[track_indices[eachTrack]:track_indices[eachTrack+1]]
			track_id = track.split("\n")[0].split(",")[0]
			tracks = track.split("\n")
			if tracks[0].split(",")[0].split()[-1] in track_list:
				plt_track_id = track_id
				print event_id, track_id
				for entry in range(0, len(tracks)):
					charge = tracks[entry]
					if charge:
						if charge.split()[-1] == "eIoni":
							print charge
							x.append(float(charge.split()[1]))
							y.append(float(charge.split()[2]))
							z.append(float(charge.split()[3]))
							dE.append(float(charge.split()[5]))
	else:
		continue

	fig = plt.figure()
	ax = fig.add_subplot(111, projection="3d")
	ax.set_title(event_id + " " + plt_track_id)
	ax.set_xlabel("X Axis")
	ax.set_ylabel("Y Axis")
	ax.set_zlabel("Z Axis")

	for xp, yp, zp, c in zip(x, y, z, colors):
	    sc = ax.scatter(xp, yp, zp, c=c, cmap=plt.cm.jet , marker="o", norm=norm)
	plt.colorbar(sc)
	plt.show()
