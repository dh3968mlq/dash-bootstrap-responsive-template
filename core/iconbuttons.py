from dash import html

def hamburger():
    return html.Img(
        src="/static/radix-icons--hamburger-menu.svg", 
        height="40px", 
        style={"margin":"14px"},
        id="drawer-hamburger-button",
        className="narrow-only",
        title="Show pop-up menu",
    )

def lightswitch():
    return html.Img(
        src="/static/iconoir--sun-light.svg", 
        height="40px", 
        style={"margin":"14px"},
        id="core-lightswitch",
        title="Switch light/dark theme",
        n_clicks=0,
    )