# Traffic Route Optimization Using Dijkstra's Algorithm and Google Maps API

## Project Overview
This project aims to find the shortest route between two locations using Dijkstra’s Algorithm and visualize the route on a map using the Google Maps JavaScript API. The web-based application allows users to input a source and destination, calculates the shortest path, and displays the route on an interactive map with traffic data, distance, and estimated travel time.

## Table of Contents
1. [Technology Stack](#technology-stack) 
2. [Project Structure](#project-structure) 
3. [Installation Guide](#installation-guide) 
4. [How It Works](#how-it-works)   
5. [API Integration](#api-integration)  
6. [Frontend Components](#frontend-components)
7. [Backend Components](#backend-components)
8. [Running the Application](#running-the-application)
9. [Improvements and Extensions](#improvements-and-extensions)
10. [Troubleshooting](#troubleshooting)

## Technology Stack
**Backend:**
- **Python:** Core language for implementing the shortest path algorithm and handling API calls.
- **Flask:** A lightweight web framework to handle routing and server-client communication.
- **Google Maps API:** Used for geocoding, distance calculation, and fetching traffic-aware data.

**Frontend:**
- **HTML:** To create the structure of the web pages.
- **CSS:** For styling and visual design.
- **JavaScript:** To handle map rendering, form interaction, and communication with the backend.
- **Google Maps JavaScript API:** To display the map and plot the route.

## Project Structure
```bash
/project
    /static
        - style.css  # CSS for frontend design
        - script.js  # JavaScript for map rendering and AJAX
    /templates
        - index.html  # Main HTML page for user input and map display
    - app.py  # Flask application (backend logic)
```
- `app.py`: The main Python file that starts the Flask server, handles API calls, and processes user requests.
- `/static`: Contains static assets like CSS and JavaScript files.
- `/templates/index.html`: The main HTML file for the user interface.

## Installation Guide
**Requirements:**
- Python 3.x
- Flask (`pip install flask`)
- Google Maps API key (obtainable from the Google Cloud Console)

**Steps:**
1. Clone the repository or download the project.
2. Install required dependencies using pip:
   ```bash
   pip install flask googlemaps networkx
   ```
3. Replace `API_KEY` in `app.py` with your own Google Maps API key.
4. Run the Flask application:
   ```bash
   python app.py
   ```
5. Open your browser and go to `http://127.0.0.1:5000/`.

## How It Works
1. **User Input:** The user enters the source and destination addresses in a web form.
2. **Backend Processing:**
   - Flask handles the request and calls the Google Maps Geocoding API to get geographical coordinates (latitude and longitude).
   - The Distance Matrix API fetches distance between points, considering real-time traffic data.
   - Dijkstra’s Algorithm computes the shortest path based on distance.
3. **Frontend Display:**
   - The Google Maps JavaScript API renders the map.
   - The route is drawn on the map between source and destination.
   - The shortest distance and travel time are displayed on the webpage.

## API Integration
**Google Maps API:**
- **Geocoding API:** Converts addresses into geographical coordinates.
- **Distance Matrix API:** Retrieves driving distance and duration between two points.
- **Google Maps JavaScript API:** Used in the frontend to display maps and plot routes.

## Frontend Components
1. **HTML (`templates/index.html`):**
   - A form for user input of source and destination addresses.
   - A div for displaying the map.
   - A section to show distance and travel time.

2. **CSS (`static/style.css`):**
   - Provides basic styling for form, map, and layout.
   - Ensures responsive display of the map.

3. **JavaScript (`static/script.js`):**
   - Handles form submissions and sends data to Flask backend using Fetch API.
   - Receives route data to render on the map.

## Backend Components
1. **Flask (`app.py`):**
   - Routing: Handles user requests (`/` for main page, `/find_route` for path calculation).
   - Google Maps Integration: Uses Python's `googlemaps` library for Geocoding and Distance Matrix APIs.
   - Dijkstra's Algorithm: Utilizes NetworkX library to calculate shortest paths.

2. **Core Functions in `app.py`:**
   - `get_coordinates(address)`: Converts address to latitude/longitude using Geocoding API.
   - `get_distance_duration(origin, destination)`: Retrieves driving distance/duration using Distance Matrix API.
   - `find_route()`: Main function that calculates shortest path based on user inputs.

## Running the Application
Once setup is complete:
1. Start Flask server:
   ```bash
   python app.py
   ```
2. Navigate to `http://127.0.0.1:5000/`.
3. Input source and destination addresses.
4. Click "Find Route" to view:
   - Route displayed on map.
   - Shortest distance and estimated travel time.

## Improvements and Extensions
- Real-time Route Updates: Incorporate dynamic traffic changes with alternate routes.
- Multiple Waypoints: Allow intermediate stops for optimized multi-point routes.
- Different Travel Modes: Extend options for walking, cycling, or public transit routes.
- User Authentication: Implement login features to save frequently used routes.
- Error Handling: Enhance handling of invalid addresses or API failures.
- Performance Optimization: Use caching for frequent routes to reduce API calls.

## Troubleshooting
**Common Issues:**
1. **Google Maps API Errors:**
   - Ensure correct configuration of API key in `app.py`.
   - Verify required permissions (Geocoding, Distance Matrix, Maps JavaScript) are enabled.

2. **Server Not Starting:**
   - Confirm all dependencies are installed (check `requirements.txt`).
   - Ensure you’re running Python 3.x.

3. **Map Not Displaying:**
   - Check inclusion of Google Maps JavaScript API in HTML with a valid key.
   - Inspect browser console for JavaScript errors.

This project demonstrates how to use Dijkstra’s Algorithm for route optimization integrated with Google Maps API for real-time traffic-aware routing, providing users an efficient way to visualize their routes on an interactive map.




## How To Install On Linux System to Host It

Before you begin, ensure you have the following:

- A Linux-based system (e.g., Ubuntu)
- A **Google Maps API Key**
- A domain or public IP address (optional but recommended)
- Basic knowledge of Linux commands

## 1. Update System Packages

Start by updating your system to ensure all packages are up-to-date:

```bash
sudo apt-get update
sudo apt-get upgrade
2. Install Required Software
2.1 Install Python and Pip
The application requires Python 3 and Pip, a package manager for Python. To install them, run:

bash
Copy code
sudo apt-get install python3 python3-pip
2.2 Install Flask and Other Python Packages
Next, install Flask and the required Python libraries:

bash
Copy code
pip3 install flask googlemaps gunicorn networkx
2.3 Install Nginx
Nginx will serve as the reverse proxy for your Flask application:

bash
Copy code
sudo apt-get install nginx
3. Set Up the Flask Application
3.1 Clone or Create Your Flask App
Navigate to the directory where you want to host the application and clone this repository or create a new one.

bash
Copy code
git clone https://github.com/your-repo-url/flask-app.git
cd flask-app
3.2 Test the Flask App
Run the Flask app to ensure it works:

bash
Copy code
python3 app.py
The app should be accessible locally at http://localhost:5000.

3.3 Update Flask for Production
In the app.py, ensure the Flask app binds to 0.0.0.0 to be accessible over the network:

python
Copy code
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
4. Set Up Gunicorn
Gunicorn is a production-ready WSGI HTTP server for Python web applications.

4.1 Install Gunicorn
bash
Copy code
pip3 install gunicorn
4.2 Run Gunicorn
To serve the Flask app using Gunicorn, navigate to your app's directory and run:

bash
Copy code
gunicorn --bind 127.0.0.1:5000 app:app
Replace app:app with your app’s entry point (i.e., the filename app.py and the Flask app object app).
5. Configure Nginx as a Reverse Proxy
Nginx will forward incoming traffic to Gunicorn, which will serve your Flask app.

5.1 Edit Nginx Configuration
Open the default Nginx configuration file:

bash
Copy code
sudo nano /etc/nginx/sites-available/default
Replace the content or modify it with the following configuration:

nginx
Copy code
server {
    listen 80;
    server_name your_server_ip_or_domain;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
5.2 Test Nginx Configuration
bash
Copy code
sudo nginx -t
If no errors, restart Nginx:

bash
Copy code
sudo systemctl restart nginx
5.3 Open Ports in the Firewall
Allow port 80 for HTTP traffic:

bash
Copy code
sudo ufw allow 'Nginx Full'
sudo ufw enable
6. Set Up Gunicorn as a Systemd Service (Optional)
To ensure Gunicorn runs automatically and restarts after a reboot, you can configure it as a systemd service.

6.1 Create a Gunicorn Service File
bash
Copy code
sudo nano /etc/systemd/system/flaskapp.service
Add the following content:

ini
Copy code
[Unit]
Description=Gunicorn instance to serve Flask app
After=network.target

[Service]
User=your_linux_username
Group=www-data
WorkingDirectory=/path/to/your/app
ExecStart=/usr/local/bin/gunicorn --workers 3 --bind 127.0.0.1:5000 app:app

[Install]
WantedBy=multi-user.target
6.2 Enable and Start the Service
bash
Copy code
sudo systemctl daemon-reload
sudo systemctl start flaskapp
sudo systemctl enable flaskapp
Check the status of the service:

bash
Copy code
sudo systemctl status flaskapp
7. Access Your Application
Your application should now be running and accessible via your server's public IP address or domain name:

URL: http://your-server-ip-or-domain
Checking Logs for Troubleshooting
Nginx logs:

bash
Copy code
sudo tail -f /var/log/nginx/error.log
Gunicorn logs:

bash
Copy code
sudo journalctl -u flaskapp
8. Additional Considerations
8.1 Setting Up HTTPS with Let's Encrypt (Optional)
You can secure your app using HTTPS with Let's Encrypt:

Install Certbot:

bash
Copy code
sudo apt-get install certbot python3-certbot-nginx
Run Certbot to generate SSL certificates:

bash
Copy code
sudo certbot --nginx -d your_domain
Certbot will configure Nginx to serve your app via HTTPS.

8.2 Debugging 502 Bad Gateway Errors
If you encounter a 502 Bad Gateway error, try these steps:

Ensure Gunicorn is running:

bash
Copy code
ps aux | grep gunicorn
Check Nginx error logs:

bash
Copy code
sudo tail -f /var/log/nginx/error.log
Restart both services:

bash
Copy code
sudo systemctl restart nginx
sudo systemctl restart flaskapp
9. Conclusion
You have successfully set up the Traffic Route Optimization app using Flask, Gunicorn, and Nginx on a Linux server. You can further enhance the deployment by adding HTTPS for security and monitoring logs for any issues.

git chechout -b Day_1 Assignment
