from dash import dcc, html
import dash_bootstrap_components as dbc
from core import hamburger

def create_home_link(label):
        return dcc.Link(
            label,
            href="/",
            style={"color":"black", "textDecoration":"none"}
        )
# --------------------------------------------
def create_header_left_column():
    hl = html.Div(
        [
            html.H2(create_home_link("Dash Bootstrap Responsive Template"), className="wide-only ms-2"), 
            html.H3(create_home_link("DBC Template"), className="narrow-only ms-2"), 
        ],
    )
    return hl
# --------------------------------------------
def create_header_right_column():
    hr = html.Div(
            children=[              
                dcc.Link(
                    children=html.Img(
                        src="/static/github-mark.svg", 
                        height="40px", 
                        style={"margin":"14px"}
                    ),
                    href="https://github.com/dh3968mlq/dash-bootstrap-starter-kit",
                    target="_blank",

                ),
                hamburger.hamburger(),
            ],
            className="ms-auto"     # Right aligns the content
        )
    return hr
# --------------------------------------------
def create_header():
    header = dbc.Stack(
                children=[
                    create_header_left_column(),
                    create_header_right_column(),
                ],
                direction="horizontal",
        className="page-header",
    )
    return header