from dash import html, dcc, page_registry
import dash_bootstrap_components as dbc
from defaultlayouts.lorem import lorem

def create_side_nav_content(idprefix:str=""):
    """
    Common content for both versions of side navbar
    idprefix, different between bar and drawer, must be used for all ids to avoid duplication errors
    """
    nav_data = page_registry.values()
    nav_content = [
            html.H4("Navigation"),
            html.P("Auto-generated from the page registry"),
            html.Ul(
                children=[create_side_navbar_link(entry) for entry in nav_data],
            )
        ] + \
        [   
            html.H4("Button with callback"),
            html.P("The callback must handle both the fixed navbar button id and the popup button id"),
            dbc.Stack(dbc.Button("Press here", color="primary", id=f"{idprefix}-button1", className="mx-auto mb-3")),
            html.P("Button has not been pressed", id=f"{idprefix}-button1-count")
        ] + \
        [   
            html.H4("Long text to show scrolling"),
        ] + \
        [html.P(lorem) for _ in range(6)]
    return nav_content

# --------------------------------------------
def create_side_navbar_link(nav_entry):
    link = html.Li( 
            dcc.Link(nav_entry["name"], href=nav_entry["path"]),
        )
    return link
# --------------------------------------------
def create_side_navbar():
    contents = [
            html.H3("Left sidebar"),
            html.P("This sidebar is replaced with a pop-up drawer (dbc.Offcanvas) when screen width is below 1200px"),
            html.P("The sidebar and drawer can contain common content or different content. " + 
                   "This text is in the sidebar only, and everything below is common between the sidebar and drawer."
            ),
    ] + create_side_nav_content(idprefix="bar")
    return contents
# --------------------------------------------
def create_navbar_drawer(header_height=70, footer_height = 40):
    contents = [
            html.H2("Left side drawer"),
            html.P("Uses dbc.Offcanvas"),
            html.P("This drawer becomes available when screen width is below 1200px"),
    ] + create_side_nav_content(idprefix="drawer")
    return contents