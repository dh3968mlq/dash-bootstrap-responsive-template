from dash import clientside_callback, Input, Output

# This does not update plotly graph templates - needs to be done in a separate callback
# See pages/sample_graph.py for how to do this

clientside_callback(
    """ 
    function(nclicks) {
       document.documentElement.setAttribute('data-bs-theme', (nclicks % 2) ? 'dark' : 'light');
       return nclicks  
    }
    """,
    Output("core-lightswitch", "n_clicks"),
    Input("core-lightswitch", "n_clicks"),
    prevent_initial_call = True
)