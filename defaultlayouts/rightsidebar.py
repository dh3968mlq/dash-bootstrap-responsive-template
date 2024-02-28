from dash import html
from defaultlayouts.lorem import lorem

def create_aside():
    aside = [
        html.H3("Right SideBar"),
        html.P("This sidebar disappears when screen width is below 1500px"),
        html.H3("Long text to show scrolling")
    ] + \
    [html.P(lorem) for _ in range(6)]
    return aside