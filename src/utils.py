from dash import html, dcc, dbc
from src.lorem import lorem

def create_side_nav_content(nav_data):
    "Common content for both versions of side navbar"
    nav_content = [html.Div(
        [
            html.H4("Navigation"),
            html.P("Auto-generated from the page registry, but appears in a rather random order"),
            html.Ul(
                children=[create_side_navbar_link(entry) for entry in nav_data]
            )
        ] + 
        [   
            html.H4("Long text to show scrolling"),
        ] + \
        [html.P(lorem) for _ in range(6)]
    )]
    return nav_content

# --------------------------------------------
def create_side_navbar_link(nav_entry):
    link = html.Li( 
            dcc.Link(nav_entry["name"], href=nav_entry["path"]),
        )
    return link
# -------------------------------------------
def create_layout_structure(header_height=70, header_contents=html.H2("Header"),
        narrow_header_height=None, narrow_header_contents=None,
        left_sidebar_contents=html.H4("Left sidebar"),
        right_sidebar_contents=html.H4("Right sidebar"),
        body_contents=html.H2("Page Body"),
        footer_height=40, footer_contents=html.H4("Footer"),
        narrow_footer_height=None, narrow_footer_contents=None,
        fluid=True
        ):
    """
        narrow_header_contents=None : header is unchanged on narrow screens. Set to [] for no contents
    """
    # Construct header (list)
    if narrow_header_contents is None:
        header = [html.Div(children=header_contents, className="page-header")]
    else:
        header = [
            html.Div(children=header_contents, className="page-header wide-only"),
            html.Div(children=narrow_header_contents, className="page-header narrow-only"),
        ]

    # Left sidebar (list) and the offcanvas that replaces it on a narrow screen
        left_sidebar = [
            html.Div(children=left_sidebar_contents, className="left-sidebar wide-only"),
            dbc.Offcanvas(
                id="components-navbar-drawer",
                children=left_sidebar_contents,
                className="left-sidebar narrow-only",
                style={   # Styling .page-navbar in CSS doesn't seem to work to do this...
                    "top":f"{header_height}px",
                    "bottom":f"{footer_height}px",
                }
            )]

    # Right sidebar (list) 
    right_sidebar = [
            html.Div(children=right_sidebar_contents, className="right-sidebar wide-only"),
    ]

    # Body (list)
    body = html.Div(children=body_contents, className="page-body"),

    # Footer (list) 
    if footer_contents is None:
        footer = []
    elif narrow_footer_contents is None:
        footer = [html.Div(children=footer_contents, className="page-footer")]
    else:
        footer = [
            html.Div(children=footer_contents, className="page-footer wide-only"),
            html.Div(children=narrow_footer_contents, className="page-footer narrow-only"),
        ]

    layout = dbc.Container(   
        children= header + left_sidebar + right_sidebar + body + footer + \
            [dcc.Location(id="main-url")],
        fluid=fluid,
    )
    return layout
