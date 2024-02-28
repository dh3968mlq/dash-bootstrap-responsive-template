from dash import html
import dash_bootstrap_components as dbc

def create_footer():
    footer = dbc.Stack(
        children=html.H4("Footer area",
            style={"color":"black", "textDecoration":"none"},
            className="ms-2",
        )
    )
    return footer