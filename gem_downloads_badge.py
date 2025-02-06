from flask import Flask, jsonify, request
import requests
from bs4 import BeautifulSoup
import os

app = Flask(__name__)

@app.route('/downloads/<gem_name>')
def get_downloads(gem_name):
    url = f'https://rubygems.org/gems/{gem_name}'
    response = requests.get(url)
    if response.status_code != 200:
        return jsonify({
            "schemaVersion": 1,
            "label": "Downloads",
            "message": "Gem not found",
            "color": "red"
        }), 404
    
    soup = BeautifulSoup(response.text, 'html.parser')
    downloads_span = soup.find('span', class_='gem__downloads')
    if downloads_span:
        total_downloads = downloads_span.text.strip().replace(',', '')
        return jsonify({
            "schemaVersion": 1,
            "label": "downloads",
            "message": total_downloads,
            "color": "green"
        })
    
    return jsonify({
        "schemaVersion": 1,
        "label": "Downloads",
        "message": "Count not found",
        "color": "brightgreen"
    }), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
