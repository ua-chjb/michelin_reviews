import dash
import dash_bootstrap_components as dbc

from index import lyt
from callbacks import callbacks_baby

app = dash.Dash(__name__)

app.layout = lyt

callbacks_baby(app)

if __name__ == '__main__':
    app.run_server(debug=True, port='8050')