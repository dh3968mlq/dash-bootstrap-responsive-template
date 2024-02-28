import dash_bootstrap_components as dbc
from dash import html, page_container, dcc

def createlayout(
        headercontents=None,
        leftsidebarcontents=None,
        popupcontents=None,
        rightsidebarcontents=None,
        footercontents=None,
        header_height=50,       # Must correspond to value set in styles.css
        footer_height = 30      # Ditto
):
    layout = dbc.Container(   
        children= [
            html.Div(children=headercontents, className="page-header"),
            html.Div(children=leftsidebarcontents, className="page-navbar"),
            dbc.Offcanvas(
                id="page-default-drawer",
                children=popupcontents,
                style={   # Styling .page-navbar in CSS doesn't seem to work to do this...
                    "top":f"{header_height}px",
                    "bottom":f"{footer_height}px",
                }
            ),
            html.Div(children=rightsidebarcontents, className="page-aside"),
            html.Div(children=page_container, className="page-body"),
            html.Div(children=footercontents, className="page-footer"),
            dcc.Location(id="main-url"),
        ],
        fluid=True,
    )
    return layout
