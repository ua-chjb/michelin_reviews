from dash import Input, Output, callback
from filter_dataframe import ac_flag

@callback(
    Output(component_id="placeholder", component_property="children"),
    Input(component_id="ac_bool", component_property="on")
)
def update_bool(on):
    global ac_flag
    if on:
        # global ac_flag
        ac_flag = 0
        # return ac_flag ?
    else:
        # global ac_flag
        ac_flag = -1
        # return ac_flag ?
