from dash import register_page, dcc, html
import dash_bootstrap_components as dbc

register_page(__name__, title='Dash Bootstrap Starter Kit')

header_height = 70    
footer_height = 40

layout = [
    html.Div(
        children=dcc.Markdown('''

## A page with a custom sidebar

This page has been rendered from markdown 
using dcc.Markdown()   

'''
        ),
        className='page-body'
    ),
    # --- The custom sidebar
    html.Div(
        children=html.H4("Custom sidebar layout"),
        className='page-navbar'
    ),
    # -- The custom pop-up drawer
    dbc.Offcanvas(
        id={"type":"drawer", "page": __name__},
        children=
        [
            html.H2("Custom drawer"),
            html.P("Uses dbc.Offcanvas"),
        ], 
        className="page-navbar-drawer narrow-only",
        style={   # Styling .page-navbar in CSS doesn't seem to work to do this...
            "top":f"{header_height}px",
            "bottom":f"{footer_height}px",
        }
    )
]