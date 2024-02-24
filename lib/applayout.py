'''
Create layout
Some layout is defined in styles.css
'''
import dash_bootstrap_components as dbc
from dash import page_container, dcc, html
from lib.lorem import lorem
from lib import utils

# -- Replicate variables (custom properties) defined in styles.css as required
header_height = 70    
footer_height = 40
navbar_width=300

def create_home_link(label):
        return dcc.Link(
            label,
            href="/",
            style={"color":"black", "textDecoration":"none"}
        )
# --------------------------------------------
def create_header_left_column(nav_data):
    hl = html.Div(
        [
            html.H2(create_home_link("Dash Bootstrap Responsive Template"), className="wide-only vertical-center"),
            html.H3(create_home_link("DBC Template"), className="narrow-only vertical-center"),
        ],
    )
    return hl
# --------------------------------------------
def create_header_right_column(nav_data):
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
                html.Img(
                    src="/static/radix-icons--hamburger-menu.svg", 
                    height="40px", 
                    style={"margin":"14px"},
                    id="drawer-hamburger-button",
                    className="narrow-only"
                ),
            ],
            className="ms-auto"     # Right aligns the content
        )
    return hr
# --------------------------------------------
def create_header(nav_data):
    header = html.Div(
        children=[
            dbc.Stack(
                children=[
                    create_header_left_column(nav_data),
                    create_header_right_column(nav_data),
                ],
                direction="horizontal",
            ),
        ],
        className="page-header",
    )
    return header
# --------------------------------------------
def create_side_navbar(nav_data):
    navbar = html.Div(
        children=
        [
            html.H2("Left sidebar"),
            html.P("This sidebar is replaced with a pop-up drawer when screen width is below 1200px"),
        ] + utils.create_side_nav_content(nav_data),
        className="page-navbar",
        id="page-navbar"
    )
    return navbar
# --------------------------------------------
def create_navbar_drawer(nav_data):
    drawer = dbc.Offcanvas(
        id="components-navbar-drawer",
        children=
        [
            html.H2("Left side drawer"),
            html.P("Uses dbc.Offcanvas"),
            html.P("This drawer becomes available when screen width is below 1200px"),
        ] + utils.create_side_nav_content(nav_data),
        className="page-navbar-drawer narrow-only",
        style={   # Styling .page-navbar in CSS doesn't seem to work to do this...
            "top":f"{header_height}px",
            "bottom":f"{footer_height}px",
        }
    )
    return drawer
# --------------------------------------------
def create_aside():
    aside = html.Div(
        children=[

            html.H2("Right SideBar"),
            html.P("This sidebar disappears when screen width is below 1500px")
        ] + \
        [html.H3("Long text to show scrolling")] + \
        [html.P(lorem) for _ in range(6)],
        className="page-aside",
    )
    return aside
# --------------------------------------------
def create_body():
    body = html.Div(   
            children=page_container,
            className="page-body"
    )
    return body
# -----------------------------------------------------------
def create_footer():
    footer = html.Div(
        children=[
            html.H4("Footer area",
                      style={"color":"black", "textDecoration":"none"},
                      className="vertical-center",)
        ],
        className="page-footer",
    )
    return footer
# -----------------------------------------------------------
def get_layout(nav_data):
    layout = dbc.Container(   
        children= [
            create_header(nav_data),
            create_side_navbar(nav_data),
            create_navbar_drawer(nav_data),
            create_aside(),
            create_body(),
            create_footer(),
            dcc.Location(id="main-url"),
        ],
        fluid=True,
    )
    return layout
