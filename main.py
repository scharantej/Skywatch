
# main.py
from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import folium
import branca

app = Flask(__name__)

# Load data
terrain_data = pd.read_csv('terrain_data.csv')
altitude_data = pd.read_csv('altitude_data.csv')

# Merge data
data = pd.merge(terrain_data, altitude_data, how='inner')

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# Results page
@app.route('/results', methods=['POST'])
def results():
    # Get data from form
    terrain = request.form['terrain']
    altitude = request.form['altitude']

    # Query for points with high altitude and visible ocean
    query = data[(data['terrain'] == terrain) & (data['altitude'] > altitude) & (data['visible_ocean'] == True)]

    # Create map
    map = folium.Map(location=[37.7749, -122.4194], zoom_start=12)

    # Add markers to map
    for _, row in query.iterrows():
        folium.Marker([row['latitude'], row['longitude']], tooltip=f"Altitude: {row['altitude']}, Terrain: {row['terrain']}, Visible Ocean: {row['visible_ocean']}").add_to(map)

    return render_template('results.html', map=map)

if __name__ == '__main__':
    app.run(debug=True)
