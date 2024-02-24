from dash import callback, Output, Input

# Close the sidebar drawer when a link is clicked (when the URL changes)
# An example of a server side callback - clientside would be better really for this

@callback(    # https://dash.plotly.com/basic-callbacks
    Output("components-navbar-drawer", "is_open", allow_duplicate=True),
    Input("main-url","href"),
    prevent_initial_call=True,
)
def close_drawer(href):
    return False
