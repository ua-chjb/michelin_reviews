import dash
import dash_bootstrap_components as dbc
# from whitenoise import WhiteNoise

from server import server_var, app_var
from index import lyt

server = server_var

app_var.layout = lyt

if __name__ == '__main__':
    app_var.run_server(debug=True, 
        # host='0.0.0.0'
        port='8070'
        )