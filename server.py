import dash

app_var = dash.Dash(__name__, 
                    # suppress_callback_exceptions=True
                    )

server_var = app_var.server
