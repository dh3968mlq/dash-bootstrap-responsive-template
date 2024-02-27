from dash import Input, Output, State, callback, ALL, no_update

# Toggle display of the navigation drawer when the hamburger button is clicked
@callback(   
    Output("page-default-drawer","is_open", allow_duplicate=True),
    Output({"type":"drawer", "page": ALL}, "is_open", allow_duplicate=True),
    Input("drawer-hamburger-button", "n_clicks"),
    State("page-default-drawer","is_open"),
    State({"type":"drawer", "page": ALL}, "is_open"),
    prevent_initial_call=True,
)
def toggle_visibility(nclicks, default_already_open, custom_already_open):
    if len(custom_already_open) > 0:    # A custom drawer is active: toggle its visibility
        return no_update, [not custom_already_open[0]]
    else:                               # Toggle the visibility of the default drawer
        return (not default_already_open), []
