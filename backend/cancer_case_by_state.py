import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output


file_path = "D:/vue/backend/melanoma_data.csv"


import os
if not os.path.exists(file_path):
    raise FileNotFoundError(f"Error: 找不到文件 {file_path}，请检查路径是否正确！")


melanoma_df = pd.read_csv(file_path)


melanoma_df["Year"] = pd.to_numeric(melanoma_df["Year"], errors='coerce')
melanoma_df["Count"] = pd.to_numeric(melanoma_df["Count"], errors='coerce')


app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Melanoma Cancer Cases by State"),
    dcc.Dropdown(
        id="state-dropdown",
        options=[{"label": state, "value": state} for state in melanoma_df["State_Territory"].unique()],
        value=melanoma_df["State_Territory"].unique()[0],
        clearable=False
    ),
    dcc.Graph(id="melanoma-bar-chart")
])

@app.callback(
    Output("melanoma-bar-chart", "figure"),
    Input("state-dropdown", "value")
)
def update_graph(selected_state):
    filtered_df = melanoma_df[melanoma_df["State_Territory"] == selected_state]
    fig = px.bar(
        filtered_df, x="Year", y="Count", color="Sex",
        title=f"Melanoma Cancer Cases in {selected_state}",
        labels={"Count": "Number of Cases", "Year": "Year"}
    )
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
