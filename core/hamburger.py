from dash import html

def hamburger():
    return html.Img(
        src="/static/radix-icons--hamburger-menu.svg", 
        height="40px", 
        style={"margin":"14px"},
        id="drawer-hamburger-button",
        className="narrow-only"
    )