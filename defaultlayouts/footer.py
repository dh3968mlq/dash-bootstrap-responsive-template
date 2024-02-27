from dash import html

def create_footer():
    footer = [
        html.H4("Footer area",
            style={"color":"black", "textDecoration":"none"},
            className="vertical-center",)
    ]
    return footer