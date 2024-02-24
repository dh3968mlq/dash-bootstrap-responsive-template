'''
Create layout
Some layout is defined in styles.css
'''
import dash_bootstrap_components as dbc
from dash import page_container, dcc, html
from src.lorem import lorem
from src import utils

# -----------------------------------------------------------
def get_layout(nav_data):
    layout = dbc.Container(   
        children= page_container,
        fluid=True,
    )
    return layout
