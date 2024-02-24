from dash import clientside_callback, Input, Output, State

# Toggle display of the navigation drawer when the hamburger button is clicked
# An example of a clientside callback

clientside_callback(   # https://dash.plotly.com/clientside-callbacks
    """function(n_clicks, is_already_open) { return !is_already_open }""",     # Javascript
    Output("components-navbar-drawer", "is_open", allow_duplicate=True),
    Input("drawer-hamburger-button", "n_clicks"),
    State("components-navbar-drawer", "is_open"),
    prevent_initial_call=True,
)
