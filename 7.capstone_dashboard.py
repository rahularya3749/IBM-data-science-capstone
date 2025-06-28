# Import required libraries
import pandas as pd
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[
    html.H1('SpaceX Launch Records Dashboard', style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
    html.Br(),

    # Task 1: Dropdown for Launch Site selection
    dcc.Dropdown(id='site-dropdown',
                 options=[
                     {'label': 'All Sites', 'value': 'ALL'},
                     {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
                     {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'},
                     {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
                     {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'}
                 ],
                 value='ALL',
                 placeholder="Select a Launch Site here",
                 searchable=True),
    html.Br(),

    # Task 2: Pie chart for success rate
    html.Div(dcc.Graph(id='success-pie-chart')),
    html.Br(),

    # Task 3: Range slider to select payload
    html.P("Payload range (Kg):"),
    dcc.RangeSlider(id='payload-slider',
                    min=0, max=10000, step=1000,
                    marks={0: '0 Kg', 1000: '1000 Kg', 2000: '2000 Kg', 3000: '3000 Kg', 4000: '4000 Kg',
                           5000: '5000 Kg', 6000: '6000 Kg', 7000: '7000 Kg', 8000: '8000 Kg',
                           9000: '9000 Kg', 10000: '10000 Kg'},
                    value=[min_payload, max_payload]),

    # Task 4: Scatter chart for payload vs success
    html.Div(dcc.Graph(id='success-payload-scatter-chart')),
])

# Task 2: Callback function to update the success pie chart based on selected launch site
@app.callback(
    Output(component_id='success-pie-chart', component_property='figure'),
    Input(component_id='site-dropdown', component_property='value')
)
def get_pie_chart(entered_site):
    filtered_df = spacex_df
    if entered_site == 'ALL':
        fig = px.pie(filtered_df, values='class', names='Launch Site', title='Launch Success by Site')
    else:
        # Filter data for the selected site and calculate success/failure
        filtered_df = spacex_df[spacex_df['Launch Site'] == entered_site]
        success_count = filtered_df['class'].value_counts()
        fig = px.pie(
            names=['Success', 'Failure'], 
            values=[success_count.get(1, 0), success_count.get(0, 0)],
            title=f'Success vs Failure for {entered_site}'
        )
    return fig

# Task 4: Callback function to render the scatter plot based on selected site and payload range
@app.callback(
    Output(component_id='success-payload-scatter-chart', component_property='figure'),
    [
        Input(component_id='site-dropdown', component_property='value'),
        Input(component_id="payload-slider", component_property="value")
    ]
)
def get_scatter_chart(selected_site, selected_payload_range):
    min_payload, max_payload = selected_payload_range

    if selected_site == 'ALL':
        filtered_df = spacex_df[(spacex_df['Payload Mass (kg)'] >= min_payload) &
                                (spacex_df['Payload Mass (kg)'] <= max_payload)]
        fig = px.scatter(filtered_df, 
                         x='Payload Mass (kg)', 
                         y='class', 
                         color='Booster Version Category', 
                         title='Payload vs. Success for All Sites',
                         labels={'class': 'Launch Outcome (0=Failed, 1=Successful)', 
                                 'Payload Mass (kg)': 'Payload Mass (kg)'},
                         hover_data=['Launch Site'])
    else:
        filtered_df = spacex_df[(spacex_df['Launch Site'] == selected_site) &
                                (spacex_df['Payload Mass (kg)'] >= min_payload) & 
                                (spacex_df['Payload Mass (kg)'] <= max_payload)]
        fig = px.scatter(filtered_df, 
                         x='Payload Mass (kg)', 
                         y='class', 
                         color='Booster Version Category', 
                         title=f'Payload vs. Success for {selected_site}',
                         labels={'class': 'Launch Outcome (0=Failed, 1=Successful)', 
                                 'Payload Mass (kg)': 'Payload Mass (kg)'},
                         hover_data=['Launch Site'])

    return fig

# Run the app
if __name__ == '__main__':
    app.run_server()
