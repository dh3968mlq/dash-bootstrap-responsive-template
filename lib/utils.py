from dash import html, dcc
from lib.lorem import lorem

def create_side_nav_content(nav_data):
    "Common content for both versions of side navbar"
    nav_content = [html.Div(
        [
            html.H4("Navigation"),
            html.P("Auto-generated from the page registry, but appears in a rather random order"),
            html.Ul(
                children=[create_side_navbar_link(entry) for entry in nav_data]
            )
        ] + 
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
