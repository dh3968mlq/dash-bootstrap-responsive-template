from dash import register_page, dcc, html
import dash_bootstrap_components as dbc

register_page(module=__name__, 
              name="Page with customised sidebar",
              title='Dash Bootstrap Starter Kit')

header_height = 50    
footer_height = 30

layout = [
    html.Div(
        children=[
            dcc.Markdown('''

## A page with a custom sidebar

An example page that has a custom sidebar and pop-up drawer
                         
Some content here is rendered from Markdown, some (such as the image below) in Python

'''
            ),
        html.Img(src="/static/pexels-pixabay-262367-cropped2.jpg",width="100%",
                 className="mx-0 mb-3 rounded"),        
        ],
        className='page-body'
    ),
    # --- The custom sidebar
    html.Div(
        children=[
            html.H4("Custom sidebar layout"),
            html.P("This page has a custom left sidebar layout that replaces the default." +
                   "It is also possible to have a custom right sidebar. This page hides the default by using blank content"
            )
        ],
        className='page-navbar'
    ),
    # -- The custom pop-up drawer
    dbc.Offcanvas(
        id={"type":"drawer", "page": __name__},
        children=
        [
            html.H2("Custom pop-up"),
            html.P("This page has a custom left pop-up that replaces the default."),
            html.P("Uses dbc.Offcanvas"),
            dcc.Link("Home", href="/"),
        ],
        style={   # Styling .page-navbar in CSS doesn't seem to work to do this...
            "top":f"{header_height}px",
            "bottom":f"{footer_height}px",
        }
    ),
    # -- Custom right sidebar. This just hides the default
    html.Div(children="", className="page-aside")
]