import json
import matplotlib.pyplot as plt
fig, ax = plt.subplots()

class Sor_plot(object):
    def __init__(self):
        self.open_route = "C:/otdr_data/SOR/"
        self.save_route = "C:/otdr_data/SVG/"
        self.filename1 = "sample-340.sor"
        self.filename2 = "metadata_sor.sor"
        self.data = None
    
    def convert_json(self, filename):
        return filename.replace(".sor", ".json")
        
    def save_svg(self):
        fig.savefig(self.save_route+"sample-340.svg", format="svg")
        plt.show()
        
    ## FILE 1
    def exec_file1(self):
        with open(self.open_route + self.convert_json(self.filename1), 'r') as file:
            self.data = json.load(file)

        km = []
        loss = []

        for el in self.data:
            km.append(el["km"])
            loss.append(el["loss"])

        ax.plot(km, loss)
        ax.grid()
        ax.set(xlabel="Location (km)", ylabel="Magnitude (dB)", title="sample-340.svg")

    ## FILE 2
    def exec_file2(self):
        with open(self.open_route + self.convert_json(self.filename2), 'r') as file:
            self.data = json.load(file)

        event = []
        ke = self.data["KeyEvents"]
        ne = ke["num events"]
        for i in range(ne):
            eventId = "event " + str(i+1)
            event.append( ke[eventId])

        #print(event)
        i = 0
        for el in event:
            valx = float(el["distance"])
            x = [valx, valx]
            y = [0, 50]

            ax.plot(x, y, color="red", linewidth=0.5)
            i+=1
            plt.text(valx, 50, "Event "+str(i))
            
### MAIN ##################################################

plot = Sor_plot()
plot.exec_file1()
plot.exec_file2()
plot.save_svg()