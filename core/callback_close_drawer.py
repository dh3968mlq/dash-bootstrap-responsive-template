from dash import Output, Input, clientside_callback, State, ALL

# Close the sidebar drawer when a link is clicked (when the URL changes)
# Custom drawers must be given an id {"type":"drawer", "page": ...}
# https://dash.plotly.com/pattern-matching-callbacks
clientside_callback(
    """
        function(href, custom_already_open) { 
            if (custom_already_open.length > 0) {
                return [false, [false] ]
            } else {
                return [false, [] ]
            } 
        }
    """,     # Javascript
    Output("page-default-drawer", "is_open", allow_duplicate=True),
    Output({"type":"drawer", "page": ALL}, "is_open", allow_duplicate=True),
    Input("main-url","href"),
    State({"type":"drawer", "page": ALL}, "is_open"),
    prevent_initial_call=True,
)
