import dash
from dash import dcc, html
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# ===== DATA =====
airport_data = {
    'Year': [2021, 2022, 2023, 2024],
    'Total_Passengers': [1757979, 6340684, 9423410, 8922292],
    'Domestic_Passengers': [1273049, 1873688, 2053366, 2752484],
    'International_Passengers': [484930, 4466996, 7370044, 6169808]
}
df_airport = pd.DataFrame(airport_data)

umrah_data = {
    'Year': [2021, 2022, 2023, 2024],
    'Total_Visitors': [355236, 1099634, 742540, 1032340],
    'Male_Visitors': [228179, 742879, 503806, 378194],
    'Female_Visitors': [127057, 356755, 238734, 654146]
}
df_umrah = pd.DataFrame(umrah_data)

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
monthly_data = {
    'Month': months,
    '2022': [68696, 86133, 99996, 415724, 94713, 40086,
             7311, 100397, 63266, 42756, 41120, 39436],
    '2023': [41223, 40187, 124784, 266530, 68399, 15901,
             30555, 51097, 35938, 21514, 26260, 20152],
    '2024': [58449, 57046, 171678, 365374, 97137, 22806,
             42469, 70741, 50741, 30485, 36864, 28550]
}
df_monthly = pd.DataFrame(monthly_data)

# ===== APP =====
app = dash.Dash(__name__)

app.layout = html.Div([

    # Header
    html.Div([
        html.H1('🕌 Madinah City Intelligence Report',
                style={'color': 'white', 'textAlign': 'center',
                       'margin': '0', 'padding': '20px'}),
        html.P('Airport Traffic & Pilgrim Visitor Analysis 2021-2024',
               style={'color': '#d4a843', 'textAlign': 'center',
                      'margin': '0', 'paddingBottom': '15px'})
    ], style={'backgroundColor': '#1e3a5f'}),

    # Row 1 - KPI Cards
    html.Div([
        html.Div([
            html.H3('9.4M', style={'color': '#d4a843', 'margin': '0'}),
            html.P('Peak Passengers 2023', style={'margin': '0', 'fontSize': '12px'})
        ], style={'backgroundColor': '#1e3a5f', 'color': 'white',
                  'padding': '20px', 'borderRadius': '10px',
                  'textAlign': 'center', 'flex': '1', 'margin': '10px'}),

        html.Div([
            html.H3('5x', style={'color': '#d4a843', 'margin': '0'}),
            html.P('Passenger Growth 2021-2023', style={'margin': '0', 'fontSize': '12px'})
        ], style={'backgroundColor': '#1e3a5f', 'color': 'white',
                  'padding': '20px', 'borderRadius': '10px',
                  'textAlign': 'center', 'flex': '1', 'margin': '10px'}),

        html.Div([
            html.H3('April', style={'color': '#d4a843', 'margin': '0'}),
            html.P('Peak Umrah Month (Ramadan)', style={'margin': '0', 'fontSize': '12px'})
        ], style={'backgroundColor': '#1e3a5f', 'color': 'white',
                  'padding': '20px', 'borderRadius': '10px',
                  'textAlign': 'center', 'flex': '1', 'margin': '10px'}),

        html.Div([
            html.H3('2024', style={'color': '#d4a843', 'margin': '0'}),
            html.P('Females Overtook Males!', style={'margin': '0', 'fontSize': '12px'})
        ], style={'backgroundColor': '#1e3a5f', 'color': 'white',
                  'padding': '20px', 'borderRadius': '10px',
                  'textAlign': 'center', 'flex': '1', 'margin': '10px'}),

    ], style={'display': 'flex', 'padding': '20px'}),

    # Row 2 - Chart 1 and Chart 2
    html.Div([
        html.Div([
            dcc.Graph(figure=px.bar(
                df_airport, x='Year', y='Total_Passengers',
                title='Madinah Airport — Total Passengers 2021-2024',
                color='Total_Passengers',
                color_continuous_scale=['#d4a843', '#1e3a5f'],
                text='Total_Passengers'
            ).update_traces(texttemplate='%{text:,}', textposition='outside')
             .update_layout(plot_bgcolor='white', showlegend=False))
        ], style={'flex': '1', 'margin': '10px'}),

        html.Div([
            dcc.Graph(figure=go.Figure(data=[
                go.Bar(name='Domestic', x=df_airport['Year'],
                       y=df_airport['Domestic_Passengers'], marker_color='#2d6a4f'),
                go.Bar(name='International', x=df_airport['Year'],
                       y=df_airport['International_Passengers'], marker_color='#1e3a5f')
            ]).update_layout(
                title='Domestic vs International Passengers',
                barmode='group', plot_bgcolor='white'))
        ], style={'flex': '1', 'margin': '10px'}),
    ], style={'display': 'flex', 'padding': '0 20px'}),

    # Row 3 - Chart 3 and Chart 4
    html.Div([
        html.Div([
            dcc.Graph(figure=px.line(
                df_umrah, x='Year', y='Total_Visitors',
                title='Madinah — Umrah Visitors Trend 2021-2024',
                markers=True, color_discrete_sequence=['#1e3a5f']
            ).update_layout(plot_bgcolor='white'))
        ], style={'flex': '1', 'margin': '10px'}),

        html.Div([
            dcc.Graph(figure=go.Figure(data=[
                go.Bar(name='Male', x=df_umrah['Year'],
                       y=df_umrah['Male_Visitors'], marker_color='#1e3a5f'),
                go.Bar(name='Female', x=df_umrah['Year'],
                       y=df_umrah['Female_Visitors'], marker_color='#c1440e')
            ]).update_layout(
                title='Male vs Female Umrah Visitors',
                barmode='group', plot_bgcolor='white'))
        ], style={'flex': '1', 'margin': '10px'}),
    ], style={'display': 'flex', 'padding': '0 20px'}),

    # Row 4 - Chart 6 Monthly
    html.Div([
        dcc.Graph(figure=go.Figure(data=[
            go.Scatter(x=months, y=df_monthly['2022'], mode='lines+markers',
                      name='2022', line=dict(color='#1e3a5f')),
            go.Scatter(x=months, y=df_monthly['2023'], mode='lines+markers',
                      name='2023', line=dict(color='#2d6a4f')),
            go.Scatter(x=months, y=df_monthly['2024'], mode='lines+markers',
                      name='2024', line=dict(color='#c1440e'))
        ]).update_layout(
            title='Monthly Umrah Visitors Peak Analysis 2022-2024',
            plot_bgcolor='white'))
    ], style={'padding': '0 30px 30px 30px'}),

    # Footer
    html.Div([
        html.P('Data Source: GASTAT & GACA Saudi Arabia | Author: Bushra Sadaf | PDPL Compliant',
               style={'textAlign': 'center', 'color': 'white', 'margin': '0', 'padding': '15px'})
    ], style={'backgroundColor': '#1e3a5f'})

], style={'fontFamily': 'Arial', 'backgroundColor': '#f5f5f5'})

if __name__ == '__main__':
    app.run(debug=True)