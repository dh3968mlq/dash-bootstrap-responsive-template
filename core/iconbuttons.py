from dash import html

# -- https://community.plotly.com/t/dash-bootstrap-components-responsive-template/82743/7
def hamburger():
    iconlink = html.I(
        className="bi bi-list fs-1 me-3 narrow-only",
        id="drawer-hamburger-button",
        title="Show pop-up menu",
        n_clicks=0
    )   
    return iconlink

def lightswitch():
    iconlink = html.I(
        className="bi bi-brightness-high fs-1 me-3",
        id="core-lightswitch",
        title="Switch light/dark theme",
        n_clicks=0
    )   
    return iconlink