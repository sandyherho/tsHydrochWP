'''
Digital Elevation Model of central
highlands of West Papua
Sandy Herho <herho@umd.edu>
2021/03/31
'''

import pygmt

region = [136, 140, -5, -3]
grid = pygmt.datasets.load_earth_relief(resolution='30s', region=region)

fig = pygmt.Figure()
fig.grdview(
    grid=grid,
    perspective=[-130, 30],
    frame=["xaf", "yaf", "WSnE"],
    projection="M15c",
    zsize="1.5c",
    surftype="s",
    cmap="geo",
    plane="1000+ggrey",
    contourpen="0.1p",
)
fig.colorbar(perspective=True, frame=["a500", "x+lElevation", "y+lm"])
fig.show()
