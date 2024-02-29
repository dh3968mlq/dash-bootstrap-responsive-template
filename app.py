'''
    Dash / Bootstrap boilerplate for a basic responsive multi-page app
    Author David Harris 2024 
    # -- ... based on https://github.com/snehilvj/dmc-docs, author Snehil Vijay
'''
from dash import Dash
import dash_bootstrap_components as dbc
import gunicorn                         # Necessary for Heroku?
from core import corelayout
from defaultlayouts import header, leftsidebar, rightsidebar, footer

from core import callback_close_drawer   # The import defines the callback, no need to reference it
from core import callback_open_drawer

# -- For dbc.themes... details see https://bootswatch.com/
# -- dbc.min.css provides additional styles for Dash components. See https://hellodash.pythonanywhere.com/
app = Dash(
    __name__, 
    use_pages=True,    # A multi-page app: https://dash.plotly.com/urls
    external_stylesheets=[
                    dbc.themes.BOOTSTRAP,  
                    'https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css',
    ],
)
app._favicon = "favicon.png"            # app.title must be set page by page
server = app.server                     # Necessary for Heroku?

app.layout = corelayout.createlayout(
    headercontents=header.create_header(),
    leftsidebarcontents=leftsidebar.create_side_navbar(),
    popupcontents=leftsidebar.create_navbar_drawer(),
    rightsidebarcontents=rightsidebar.create_aside(),
    footercontents=footer.create_footer()
)

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=8050)  
