from dash import html
import dash_bootstrap_components as dbc

def footer():
    footer = dbc.Stack(
        children=html.H4("Footer area",
            style={"color":"var(--bs-body-color)", "textDecoration":"none"},
            className="ms-2",
        )
    )
    return footer