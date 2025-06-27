import json
import matplotlib.pyplot as plt


class Sor_plot(object):
    def __init__(self, sor_file):
        self.open_route = "/data/host/SOR/"
        self.save_route_svg = "/data/host/SVG/"
        self.save_route_jpg= "/data/host/JPG/"
        self.filename2 = "metadata_sor.sor"
        self.sor_file = sor_file.replace(".sor", ".json")
        self.svg_filename = self.save_route_svg+sor_file.replace(".sor", ".svg")
        self.jpg_filename = self.save_route_svg+sor_file.replace(".sor", ".jpg")
        
    

        
    def save_svg(self, filename:str, ax):
        ax.savefig(self.svg_filename, format="svg")
        ax.savefig(self.jpg_filename, format="jpg")
        return self.jpg_filename
        
    ## Graph
    def plot_graph(self):
        with open(self.open_route + self.sor_file, 'r') as file:
            data = json.load(file)    
        
         # Extract frequency and power values
        frequencies = [point["km"] for point in data["points"]]
        powers = [point["loss"] for point in data["points"]]
        ml_elements = [point.get("otdr_events", "") for point in data["points"]]

        #Clean previous picture
        plt.clf()
        
        plt.plot(frequencies, powers, linewidth=0.5, color='green')
        # Create the plot
        plt.plot(frequencies, powers)

        # Add labels and title    
        plt.xlabel("Location (km)")
        plt.ylabel("Magnitude (dB)")
        plt.title(self.sor_file)

        # Annotate points with non-empty 'ml' labels
        for i, ml in enumerate(ml_elements):
            if ml:
                plt.annotate(ml, (frequencies[i], powers[i]))


        # Set the size of the window
        manager = plt.get_current_fig_manager()
        #manager.window.state('zoomed')
        manager.resize(1920, 1080)
        
        # Show the plot
        #plt.show() 
        
        picture = self.save_svg(self.sor_file, plt);
        plt.close()
        return picture

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
            
