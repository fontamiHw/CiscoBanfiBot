import json
import matplotlib.pyplot as plt


class Sor_plot(object):
    def __init__(self):
        self.open_route = "/data/host/SOR/"
        self.save_route_svg = "/data/host/SVG/"
        self.save_route_jpg= "/data/host/JPG/"
        self.filename2 = "metadata_sor.sor"
        self.data = None
        self.ax = plt.subplots()
    
    def convert_json(self, filename):
        return filename.replace(".sor", ".json")
        
    def save_svg(self, filename:str):
        svg_filename = self.save_route_svg+filename.replace(".sor", ".svg")
        self.ax.savefig(svg_filename, format="svg")
        self.ax.savefig(self.save_route_jpg+filename.replace(".sor", ".jpg"), format="jpg")
        return svg_filename
        # plt.show()
        
    ## Graph
    def plot_graph(self, sor_file:str):
        with open(self.open_route + self.convert_json(sor_file), 'r') as file:
            self.data = json.load(file)

        km = []
        loss = []

        for el in self.data:
            km.append(el["km"])
            loss.append(el["loss"])

        self.ax.plot(km, loss)
        self.ax.grid()
        self.ax.set(xlabel="Location (km)", ylabel="Magnitude (dB)", title=sor_file)
        return self.save_svg(sor_file)

    ## Event
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

            self.ax.plot(x, y, color="red", linewidth=0.5)
            i+=1
            plt.text(valx, 50, "Event "+str(i))
            
