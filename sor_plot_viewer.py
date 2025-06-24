import json
import matplotlib.pyplot as plt

# Open and read the JSON file
open_route = "C:/otdr_data/SOR/"
save_route = "C:/otdr_data/SVG/"

######### FILE 1
filename = "sample-340.sor"
filename = filename.replace(".sor", ".json")
with open(open_route+filename, 'r') as file:
    datafile = json.load(file)

km = []
loss = []

for el in datafile:
    km.append(el["km"])
    loss.append(el["loss"])

x = km
y = loss

fig, ax = plt.subplots()
ax.plot(x, y)

ax.set(xlabel="Location (km)", ylabel="Magnitude (dB)", title="sample-340.svg")
ax.grid()

fig.savefig(save_route+"sample-340.svg", format="svg")
plt.show()

######### FILE 2
filename = "metadata_sor.sor"
filename = filename.replace(".sor", ".json")

with open(open_route+filename, 'r') as file:
    datafile = json.load(file)

event = []

def find_keyevents(data):
    if "KeyEvents" in data:
        ke = data["KeyEvents"]
        if "num events" in ke:
            ne = ke["num events"]
            for i in range(ne):
                eventId = "event " + str(i+1)
                event.append( ke[eventId])


#titledata = datafile["filename"]

find_keyevents(datafile)
#print(event)

#inizialise a list for each value in event
type = []
distance = []
slope = []
splice_loss = []
refl_loss = []
comments = []
end_of_prev = []
start_of_curr = []
end_of_curr = []
start_of_next = []
peak = []
for el in event:
    type.append(el["type"])
    distance.append(el["distance"])
    slope.append(el["slope"])
    splice_loss.append(el["splice loss"])
    refl_loss.append(el["refl loss"])
    comments.append(el["comments"])
    end_of_prev.append(el["end of prev"])
    start_of_curr.append(el["start of curr"])
    end_of_curr.append(el["end of curr"])
    start_of_next.append(el["start of next"])
    peak.append(el["peak"])
