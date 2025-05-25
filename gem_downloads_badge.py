from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/downloads/<gem_name>')
def get_downloads(gem_name):
    url = f'https://rubygems.org/gems/{gem_name}'
    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            return jsonify({
                "schemaVersion": 1,
                "label": "Downloads",
                "message": "Gem not found",
                "color": "red",
                "namedLogo": "rubygems",
                "style": "for-the-badge",
                "logoColor": "E9573F",
                "labelColor": "fefefe"
            }), 404
        
        soup = BeautifulSoup(response.text, 'html.parser')
        downloads_span = soup.find('span', class_='gem__downloads')
        if downloads_span:
            total_downloads = downloads_span.text.strip().replace(',', '')
            return jsonify({
                "schemaVersion": 1,
                "label": "Downloads",
                "message": total_downloads,
                "color": "000000",
                "namedLogo": "rubygems",
                "style": "for-the-badge",
                "logoColor": "E9573F",
                "labelColor": "fefefe"
            })
        
        return jsonify({
            "schemaVersion": 1,
            "label": "Downloads",
            "message": "Count not found",
            "color": "red",
            "namedLogo": "rubygems",
            "style": "for-the-badge",
            "logoColor": "E9573F",
            "labelColor": "fefefe"
        }), 404

    except requests.RequestException:
        return jsonify({
            "schemaVersion": 1,
            "label": "Downloads",
            "message": "Error fetching data",
            "color": "red",
            "namedLogo": "rubygems",
            "style": "for-the-badge",
            "logoColor": "E9573F",
            "labelColor": "fefefe"
        }), 500

if __name__ == '__main__':
    app.run()
