from flask import Flask, request, jsonify, render_template_string
import random

app = Flask(__name__)

# HTML template for the interactive web page
page_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Real Estate API Interactive Page</title>
</head>
<body>
    <h1>Welcome to the Real Estate API</h1>
    <p>Interact with the API endpoints below:</p>
    
    <h2>Estimate Property Value</h2>
    <form method="GET" action="/value">
        <label>Location: <input type="text" name="location" required></label><br>
        <label>Size (sq ft): <input type="number" name="size" required></label><br>
        <label>Bedrooms: <input type="number" name="bedrooms" required></label><br>
        <label>Bathrooms: <input type="number" name="bathrooms" required></label><br>
        <label>Age (years): <input type="number" name="age" required></label><br>
        <input type="submit" value="Get Estimated Value">
    </form>
    <hr>
    
    <h2>Price Trend Analysis</h2>
    <form method="GET" action="/trend">
        <label>Location: <input type="text" name="location" required></label><br>
        <input type="submit" value="Get Price Trend">
    </form>
    <hr>

    <h2>Compare Property Values</h2>
    <form method="GET" action="/compare">
        <label>Locations (comma-separated): <input type="text" name="locations" required></label><br>
        <input type="submit" value="Compare Locations">
    </form>
    <hr>

    <h2>Market Insights</h2>
    <form method="GET" action="/insights">
        <label>Location: <input type="text" name="location" required></label><br>
        <input type="submit" value="Get Market Insights">
    </form>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(page_template)

@app.route("/value", methods=["GET"])
def get_estimated_value():
    location = request.args.get("location")
    size = request.args.get("size")
    bedrooms = request.args.get("bedrooms")
    bathrooms = request.args.get("bathrooms")
    age = request.args.get("age")
    
    if not all([location, size, bedrooms, bathrooms, age]):
        return jsonify({"error": "Missing parameters. Please provide 'location', 'size', 'bedrooms', 'bathrooms', and 'age'."}), 400
    
    # Simulated complex estimation formula for demonstration
    estimated_value = (int(size) * 1200 + int(bedrooms) * 60000 + int(bathrooms) * 50000 - int(age) * 1000) + random.randint(15000, 75000)
    
    return render_template_string(page_template + f"""
    <h3>Estimated Property Value</h3>
    <p>Location: {location}</p>
    <p>Size (sq ft): {size}</p>
    <p>Bedrooms: {bedrooms}</p>
    <p>Bathrooms: {bathrooms}</p>
    <p>Age (years): {age}</p>
    <p><strong>Estimated Value: ${estimated_value:,}</strong></p>
    """)

@app.route("/trend", methods=["GET"])
def get_price_trend():
    location = request.args.get("location")
    
    if not location:
        return jsonify({"error": "Missing parameter. Please provide 'location'."}), 400
    
    monthly_changes = [round(random.uniform(-2.5, 3.5), 2) for _ in range(12)]
    average_change = sum(monthly_changes) / len(monthly_changes)
    
    return render_template_string(page_template + f"""
    <h3>Price Trend Analysis</h3>
    <p>Location: {location}</p>
    <p>Monthly Price Changes (%): {monthly_changes}</p>
    <p><strong>Average Change Last 12 Months (%): {round(average_change, 2)}</strong></p>
    """)

@app.route("/compare", methods=["GET"])
def compare_locations():
    locations = request.args.get("locations")
    
    if not locations:
        return jsonify({"error": "Missing parameter. Please provide 'locations' (comma-separated)."}), 400
    
    locations_list = locations.split(',')
    comparison_data = {}
    
    for loc in locations_list:
        avg_value = random.randint(300000, 1000000)
        comparison_data[loc.strip()] = f"${avg_value:,}"
    
    formatted_comparison = "".join([f"<p>{loc}: {val}</p>" for loc, val in comparison_data.items()])
    
    return render_template_string(page_template + f"""
    <h3>Comparison of Property Values</h3>
    {formatted_comparison}
    """)

@app.route("/insights", methods=["GET"])
def get_market_insights():
    location = request.args.get("location")
    
    if not location:
        return jsonify({"error": "Missing parameter. Please provide 'location'."}), 400
    
    average_price = random.randint(400000, 900000)
    median_price = random.randint(350000, 850000)
    top_neighborhoods = [f"Neighborhood {i}" for i in range(1, 4)]
    
    formatted_neighborhoods = "".join([f"<li>{neigh}</li>" for neigh in top_neighborhoods])
    
    return render_template_string(page_template + f"""
    <h3>Market Insights</h3>
    <p>Location: {location}</p>
    <p>Average Price: ${average_price:,}</p>
    <p>Median Price: ${median_price:,}</p>
    <ul>Top Performing Neighborhoods: {formatted_neighborhoods}</ul>
    """)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)