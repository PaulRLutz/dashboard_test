# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import datetime

app = Dash(__name__)

df = pd.DataFrame({
    "Date": ["05/02/21", "05/03/21","05/03/21","05/04/21", "05/05/21","05/06/21",],
    "Sales" : [1,2,5,2,4,1]
})
fig = px.line(df, x="Date", y="Sales", title="Line Graph")
fig2 = px.bar(df, x="Date", y="Sales", title="Bar Graph")

app.layout = html.Div(children=[
    html.H1(children="Hello Dash"),

    html.Div(children="Dashboard"),

    dcc.Graph(
        id='example-graph',
        figure=fig
    ),
    dcc.Graph(
        id='example-graph2',
        figure=fig2
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
