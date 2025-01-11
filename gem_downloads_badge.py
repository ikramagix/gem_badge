from flask import Flask, jsonify, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/downloads/<gem_name>')
def get_downloads(gem_name):
    url = f'https://rubygems.org/gems/{gem_name}'
    response = requests.get(url)
    if response.status_code != 200:
        return jsonify({"error": f"Gem '{gem_name}' not found"}), 404
    
    soup = BeautifulSoup(response.text, 'html.parser')
    downloads_span = soup.find('span', class_='gem__downloads')
    if downloads_span:
        total_downloads = downloads_span.text.strip().replace(',', '')
        return jsonify({"gem_name": gem_name, "downloads": total_downloads})
    return jsonify({"error": "Downloads count not found"}), 404

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
