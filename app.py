from flask import Flask, render_template, request, jsonify
import googlemaps
import networkx as nx

app = Flask(__name__)

# Set up Google Maps API
API_KEY = 'api_here'  # Replace with your actual API key
gmaps = googlemaps.Client(key=API_KEY)

# Function to fetch coordinates using Geocoding API
def get_coordinates(address):
    geocode_result = gmaps.geocode(address)
    if geocode_result:
        location = geocode_result[0]['geometry']['location']
        return (location['lat'], location['lng'])
    return None

# Function to get distance and travel duration using Distance Matrix API
def get_distance_duration(origin, destination):
    matrix = gmaps.distance_matrix(origins=origin, destinations=destination, mode="driving", traffic_model="best_guess", departure_time="now")
    if matrix['rows'][0]['elements'][0]['status'] == 'OK':
        distance = matrix['rows'][0]['elements'][0]['distance']['value']
        duration = matrix['rows'][0]['elements'][0]['duration_in_traffic']['value']
        return distance, duration
    return None, None

# Function to search for places using Places API
def search_places(query, location):
    places_result = gmaps.places_nearby(location=location, keyword=query, radius=1000)  # radius in meters
    if places_result['results']:
        return places_result['results']
    return None

@app.route('/')
def index():
    return render_template('index.html', api_key=API_KEY)

@app.route('/find_route', methods=['POST'])
def find_route():
    source = request.json['source']
    destination = request.json['destination']

    # Get coordinates for source and destination
    source_coords = get_coordinates(source)
    destination_coords = get_coordinates(destination)

    if not source_coords or not destination_coords:
        return jsonify({'error': 'Invalid addresses'})

    # Get distance and duration
    distance, duration = get_distance_duration(source_coords, destination_coords)

    # Create graph and calculate shortest path using Dijkstra's algorithm
    graph = nx.Graph()
    graph.add_node("Source", pos=source_coords)
    graph.add_node("Destination", pos=destination_coords)
    graph.add_edge("Source", "Destination", weight=distance)

    try:
        shortest_path = nx.dijkstra_path(graph, source="Source", target="Destination", weight='weight')
        shortest_distance = nx.dijkstra_path_length(graph, source="Source", target="Destination", weight='weight')
    except nx.NetworkXNoPath:
        return jsonify({'error': 'No route found between the source and destination'})

    return jsonify({
        'shortest_path': shortest_path,
        'shortest_distance': shortest_distance,
        'duration': duration,
        'source_coords': source_coords,
        'destination_coords': destination_coords
    })

@app.route('/search_places', methods=['POST'])
def find_places():
    query = request.json['query']
    city = request.json['city']

    # Get coordinates for the city
    city_coords = get_coordinates(city)

    if not city_coords:
        return jsonify({'error': 'Invalid city name'})

    # Search for places
    places = search_places(query, city_coords)

    return jsonify({'places': places})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
