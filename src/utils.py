from dash import html, dcc
import dash_bootstrap_components as dbc
from src.lorem import lorem

def create_side_nav_content(nav_data, idprefix:str=""):
    """
    Common content for both versions of side navbar
    idprefix, different between bar and drawer, must be used for all ids to avoid duplication errors
    """
    nav_content = [html.Div(
        [
            html.H4("Navigation"),
            html.P("Auto-generated from the page registry, but appears in a rather random order"),
            html.Ul(
                children=[create_side_navbar_link(entry) for entry in nav_data],
            )
        ] + 
        [   
            html.H4("Button with callback"),
            html.P("The callback must handle both the fixed navbar button id and the popup button id"),
            dbc.Button("Press here", color="primary", id=f"{idprefix}-button1"),
            html.P("Button has not been pressed", id=f"{idprefix}-button1-count")
        ] + \
        [   
            html.H4("Long text to show scrolling"),
        ] + \
        [html.P(lorem) for _ in range(6)]
    )]
    return nav_content

# --------------------------------------------
def create_side_navbar_link(nav_entry):
    link = html.Li( 
            dcc.Link(nav_entry["name"], href=nav_entry["path"]),
        )
    return link
