# https://plotly.com/python/discrete-color/
import plotly
import plotly.express as px
# https://plotly.com/python/shapes/
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# https://plotly.com/python/shapes/
# Create Subplots for each bay in the ship.
#fig = make_subplots(rows=len(ship), cols=1)

#mapColor = {1: 'lightblue', 2: 'blue', 3: 'lightgreen'}
values    = px.colors.qualitative.Light24
keys      = list(range(1,len(values)+1))
mapC      = dict(zip(keys, values))
ship = [[] for i in range(2)]

class drawShip:
  def __init__(self, cargoMap = ship, colorMap = mapC):
    self.cargoMap    = ship
    self.colorMap    = mapC
    #self.fig         = go.Figure()
    self.fig         = make_subplots(rows=len(ship), cols=1)

  def draw(self):
    maxlin  = 0
    maxcol  = 0
    # Ploting each bay.
    for i in range(0,len(ship)):           # Number of bays
      for j in range(0,len(ship[i])):      # Number of lines on bay i
        if (j > maxlin):
          maxlin = j+1
        for k in range(0,len(ship[i][j])): # Number of cells on line j
          if (k > maxcol):
            maxcol = k+1

          self.fig.add_trace(go.Scatter(
                         x=[(2*k+1)/2],
                         y=[(2*j+1)/2],
                         text=[str(ship[i][j][k])],
                         mode="text",
                         ), row=i+1, col=1)

          self.fig.add_trace(go.Scatter(
                             x=[k,k,k+1,k+1,k],
                             y=[j,j+1,j+1,j,j],
                             fill="toself",
                             opacity=0.4,
                             fillcolor=mapC[ship[i][j][k]]
                             ), row=i+1, col=1)

          #self.fig.add_shape( # filled Rectangle
          #                type='rect',
          #                x0=k,
          #                y0=j,
          #                x1=k+1,
          #                y1=j+1,
          #                opacity=0.4,
          #                line=dict(
          #                color="black",
          #                width=2
          #                ),fillcolor=mapC[ship[i][j][k]],
          #                row=i+1, col=1)

    # Set axes properties
    self.fig.update_xaxes(range=[0, maxlin+2], showgrid=True)
    self.fig.update_yaxes(range=[0, maxcol+2])
    self.fig.update_shapes(dict(xref='x', yref='y'))
    self.fig.update_layout(showlegend=False)
    self.fig.show()


ship = [[] for i in range(2)]

# Ship Bay 1
ship[0].append([1, 1, 1, 1]) # line 1
ship[0].append([2, 2, 3, 2]) # line 2
ship[0].append([2, 3, 3, 2]) # line 3

# Ship Bay 2
ship[1].append([1, 4, 5, 5]) # line 1
ship[1].append([2, 5, 6, 7]) # line 2
ship[1].append([4, 5, 6, 7]) # line 3

print("len(ship) = ",len(ship))
print("len(ship[0]) = ",len(ship[0]))
print("len(ship[0][0]) = ",len(ship[0][0]))

s1 = drawShip(ship,mapC)
s1.draw()
