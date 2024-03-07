from dash import html, dcc, page_registry
from dash import callback, Output, Input, ctx
import dash_bootstrap_components as dbc
from defaultlayouts.lorem import lorem

def side_nav_content(idprefix:str=""):
    """
    Common content for both versions of side navbar
    idprefix, different between bar and drawer, must be used for all ids to avoid duplication errors
    """
    nav_data = page_registry.values()
    nav_content = [
            html.H4("Navigation"),
            html.P("Auto-generated from the page registry"),
            html.H5("Pages"),
            html.Ul(
                children=[side_navbar_link(entry) for entry in nav_data
                          if entry["path"][:7] != "/posts/" ],
            ),
            html.H5("Posts"),
            html.Ul(
                children=[side_navbar_link(entry) for entry in nav_data
                          if entry["path"][:7] == "/posts/" ],
            ),
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
def side_navbar_link(nav_entry):
    link = html.Li( 
            dcc.Link(nav_entry["name"], href=nav_entry["path"]),
        )
    return link
# --------------------------------------------
def side_navbar():
    contents = [
            html.H3("Left sidebar"),
            html.P("This sidebar is replaced with a pop-up drawer (dbc.Offcanvas) when screen width is below 1200px"),
            html.P("The sidebar and drawer can contain common content or different content. " + 
                   "This text is in the sidebar only, and everything below is common between the sidebar and drawer."
            ),
    ] + side_nav_content(idprefix="bar")
    return contents
# --------------------------------------------
def navbar_drawer():
    contents = [
            html.P("Uses dbc.Offcanvas"),
            html.P("This drawer becomes available when screen width is below 1200px"),
    ] + side_nav_content(idprefix="drawer")
    return contents
# --------------------------------------------
def popup_title():
    return "Left side popup"
# --------------------------------------------
# Callback handles and updates both the sidebar and drawer instances of the button and message
@callback(    # https://dash.plotly.com/basic-callbacks
    Output("bar-button1-count", "children"),
    Output("drawer-button1-count", "children"),
    Output("bar-button1","n_clicks"),
    Output("drawer-button1","n_clicks"),
    Input("bar-button1","n_clicks"),
    Input("drawer-button1","n_clicks"),
    prevent_initial_call=True,
)
def increment_button1_clicks(nclicks_bar, nclicks_drawer):
    trigger = ctx.triggered_id
    nclicks = nclicks_bar if trigger == "bar-button1" else nclicks_drawer
    text = f"Button has been clicked {nclicks} times"
    return text, text, nclicks, nclicks
