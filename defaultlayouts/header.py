from dash import dcc, html
import dash_bootstrap_components as dbc
from core import iconbuttons

def home_link(label):
        return dcc.Link(
            label,
            href="/",
            style={"color":"var(--bs-body-color)", "textDecoration":"none"}
        )
# --------------------------------------------
def header_left_column():
    hl = dbc.Stack(
        [                   
            iconbuttons.hamburger(),
            html.H2(home_link("Dash Bootstrap Responsive Template"), className="wide-only ms-2"), 
            html.H3(home_link("DBC Template"), className="narrow-only ms-2"), 
        ],
        direction="horizontal"
    )
    return hl
# --------------------------------------------
def header_right_column():
    hr = dbc.Stack(
        children=[
            iconbuttons.lightswitch(),
            dcc.Link(
                children=html.Img(
                    src="/static/github-mark.svg", 
                    height="40px", 
                    style={"margin":"14px", "fill":"var(--bs-primary)"}
                ),
                href="https://github.com/dh3968mlq/dash-bootstrap-responsive-template",
                target="_blank",
            ),
        ],
        direction="horizontal",
        className="ms-auto"     # Right aligns the content
    )
    return hr
# --------------------------------------------
def header():
    header = dbc.Stack(
                children=[
                    header_left_column(),
                    header_right_column(),
                ],
                direction="horizontal",
        className="page-header",
    )
    return header