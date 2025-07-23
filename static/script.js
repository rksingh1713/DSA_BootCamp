document.getElementById('routeForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const source = document.getElementById('source').value;
    const destination = document.getElementById('destination').value;

    fetch('/find_route', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ source, destination }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
        } else {
            document.getElementById('distance').innerHTML = `<strong>Shortest Distance:</strong> ${data.shortest_distance} meters`;
            document.getElementById('duration').innerHTML = `<strong>Estimated Travel Time:</strong> ${data.duration / 60} minutes`;

            // Display the map and route
            const map = new google.maps.Map(document.getElementById('map'), {
                zoom: 7,
                center: { lat: data.source_coords[0], lng: data.source_coords[1] }
            });

            const directionsService = new google.maps.DirectionsService();
            const directionsRenderer = new google.maps.DirectionsRenderer();
            directionsRenderer.setMap(map);

            const request = {
                origin: new google.maps.LatLng(data.source_coords[0], data.source_coords[1]),
                destination: new google.maps.LatLng(data.destination_coords[0], data.destination_coords[1]),
                travelMode: google.maps.TravelMode.DRIVING,
            };

            directionsService.route(request, function(result, status) {
                if (status == 'OK') {
                    directionsRenderer.setDirections(result);
                } else {
                    alert('Could not display the route. Try again.');
                }
            });
        }
    })
    .catch(error => console.error('Error:', error));
});
