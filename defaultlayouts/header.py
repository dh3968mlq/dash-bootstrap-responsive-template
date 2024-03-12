from dash import dcc, html, page_registry
import dash_bootstrap_components as dbc
from core import iconbuttons

def home_link(label):
    link = dcc.Link(
        label,
        href="/",
        style={"color":"var(--bs-body-color)", "textDecoration":"none"}
    )
    return link
# --------------------------------------------
def header_left_column():
    hl = html.Span(
        [                   
            iconbuttons.hamburger(),
            html.Span(home_link("Dash Bootstrap Responsive Template"), className="fs-3 wide-only ms-2"), 
            html.Span(home_link("DBC Template"), className="fs-3 narrow-only ms-2"), 
        ],
    )
    return hl
# --------------------------------------------
def header_right_column():
    nav_data = page_registry.values()
    hr = [
        iconbuttons.lightswitch(),
        dcc.Link(
            html.I(className="bi bi-github fs-3", id="github-logo"),
            href="https://github.com/dh3968mlq/dash-bootstrap-responsive-template",
            target="_blank",
        ),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem(nav_entry["name"], href=nav_entry["path"])
                                    for nav_entry in nav_data
                                        if nav_entry["path"][:7] != "/posts/" 
            ],
            nav=True,
            in_navbar=True,
            label="Pages",
            align_end=True,
        ),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem(nav_entry["name"], href=nav_entry["path"])
                                    for nav_entry in nav_data
                                        if nav_entry["path"][:7] == "/posts/" 
            ],
            nav=True,
            in_navbar=True,
            label="Posts",
            align_end=True,
        ),
    ]
    return hr
# --------------------------------------------
def header():
    header = dbc.NavbarSimple(
        children=header_right_column(),
        brand=header_left_column(),
        fluid=True,
        id="main-navbar"
    )
    return header
