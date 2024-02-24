'''
Define, for this site, the default content of the page sections
'''

import dash_bootstrap_components as dbc
from dash import page_container, dcc, html
from src.lorem import lorem
from src import utils

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
            html.H2(create_home_link("Dash Bootstrap Responsive Template"), className="wide-only vertical-center"),
            html.H3(create_home_link("DBC Template"), className="narrow-only vertical-center"),
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
def create_header():
    header = [
            dbc.Stack(
                children=[
                    create_header_left_column(),
                    create_header_right_column(),
                ],
                direction="horizontal",
            ),
        ]
    return header
# --------------------------------------------
def create_left_sidebar():
    navbar = [
            html.H2("Left sidebar"),
            html.P("This sidebar is replaced with a pop-up drawer when screen width is below 1200px"),
        ] + utils.create_side_nav_content()
    return navbar
# --------------------------------------------
def create_right_sidebar():
    aside = [

            html.H2("Right SideBar"),
            html.P("This sidebar disappears when screen width is below 1500px")
        ] + \
        [html.H3("Long text to show scrolling")] + \
        [html.P(lorem) for _ in range(6)]
    return aside
# --------------------------------------------
def create_body():
    body = html.H2("Page body placeholder"),
    return body
# -----------------------------------------------------------
def create_footer():
    footer = [
        html.H4("Footer area",
                      style={"color":"black", "textDecoration":"none"},
                      className="vertical-center",)
    ]
    return footer
