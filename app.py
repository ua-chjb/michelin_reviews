import dash
import dash_bootstrap_components as dbc
# from whitenoise import WhiteNoise

from index import lyt

app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.MINTY])
# app.config.suppress_callback_exceptions = True
# app.scripts.config.serve_locally=True
server = app.server
# server.wsgi_app = WhiteNoise(server.wsgi_app, root='static/')

server = app.server

app.layout = lyt

if __name__ == '__main__':
    app.run_server(debug=True, 
        # host='0.0.0.0'
        port='8050'
        )