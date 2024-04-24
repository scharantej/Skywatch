## Flask Application Design

**HTML Files**

1. `index.html`:
   - Displays a map of San Francisco using Google Maps API.
   - Includes a form with inputs for terrain and altitude data.
   - Contains JavaScript code to fetch data from the server and display markers on the map.

2. `results.html`:
   - Shows the result of the query.
   - Displays markers on the map representing the points with the highest altitude and visible ocean.

**Routes**

1. `/`:
   - Renders the `index.html` file.

2. `/results`:
   - Receives terrain and altitude data from the form in `index.html`.
   - Processes the data and identifies points with high altitude and visible ocean.
   - Renders the `results.html` file with the results.