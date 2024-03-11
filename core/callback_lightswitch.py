from dash import clientside_callback, Input, Output

# https://hellodash.pythonanywhere.com/adding-themes/color-modes
# This does not update plotly graph templates - needs to be done in a separate callback
# See pages/sample_graph.py for how to do this

clientside_callback(
    """ 
    function(nclicks) {
       document.documentElement.setAttribute('data-bs-theme', (nclicks % 2) ? 'dark' : 'light');
       return (nclicks % 2) ? [true, 'dark'] : [false, 'light']
    }
    """,
    Output("main-navbar", "dark"),   # It looks like the light/dark switching needs to be done explicitly for a navBar
    Output("main-navbar", "color"),  # Ditto
    Input("core-lightswitch", "n_clicks"),
    prevent_initial_call = True
)