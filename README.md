⚡ Step 1: Prerequisites

Make sure Python 3.10+ is installed

Install pip packages:

pip install fastapi uvicorn

▶️ Step 2: Running the Backend

Open a terminal in the project root folder

Run the FastAPI server:

uvicorn api:app --reload

You should see:

Uvicorn running on http://127.0.0.1:8000

🌐 Step 3: Testing the API

Open a browser or Postman

Visit the endpoint:

http://127.0.0.1:8000/scan

Optional: specify current position:

http://127.0.0.1:8000/scan?current_x=0&current_y=0

Expected JSON response:

{
"grid": [[12.4, 18.5, 33.1], [20.3, 45.6, 39.8]],
"best_spot": { "x": 1, "y": 1, "speed": 45.6 },
"current_position": { "x": 0, "y": 0 },
"suggestion": "Move right"
}

📱 Step 4: Flutter Integration

Flutter endpoint:

GET http://<your-pc-ip>:8000/scan?current_x=<int>&current_y=<int>

Replace <your-pc-ip> with your computer’s local IP

Example Dart snippet for Flutter:

import 'dart:convert';
import 'package:http/http.dart' as http;

void fetchScan() async {
final response = await http.get(
Uri.parse("http://192.168.1.5:8000/scan?current_x=0&current_y=0")
);

if (response.statusCode == 200) {
final data = jsonDecode(response.body);
print("Best Spot: ${data['best_spot']}");
print("Suggestion: ${data['suggestion']}");
} else {
print("Failed to fetch data");
}
}

🔄 Step 5: Notes

Currently uses simulated network data (generate_grid())

Later, you can replace with real speed measurements

ML integration can enhance prediction without scanning every point

main.py is optional and used for local testing without API

🧪 Step 6: Testing Locally

Run main.py to test AI logic

Run api.py to test FastAPI backend

Flutter team can now consume the API for UI testing
