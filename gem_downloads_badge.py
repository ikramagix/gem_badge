from flask import Flask, jsonify, request
import requests
from bs4 import BeautifulSoup
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/downloads/<gem_name>')
def get_downloads(gem_name):
    logger.info(f"Fetching downloads for gem: {gem_name}")
    url = f'https://rubygems.org/gems/{gem_name}'
    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            logger.error(f"Gem not found: {gem_name}, status code: {response.status_code}")
            return jsonify({
                "schemaVersion": 1,
                "label": "Downloads",
                "message": "Gem not found",
                "color": "red",
                "logo": "simpleicons-rubygems",
                "logoColor": "E9573F"
            }), 404
        
        soup = BeautifulSoup(response.text, 'html.parser')
        downloads_span = soup.find('span', class_='gem__downloads')
        if downloads_span:
            total_downloads = downloads_span.text.strip().replace(',', '')
            logger.info(f"Successfully fetched downloads for {gem_name}: {total_downloads}")
            return jsonify({
                "schemaVersion": 1,
                "label": "downloads",
                "message": total_downloads,
                "color": "firebrick",
                "logo": "simpleicons-rubygems",
                "logoColor": "E9573F"
            })
        
        logger.warning(f"Download count not found for gem: {gem_name}")
        return jsonify({
            "schemaVersion": 1,
            "label": "Downloads",
            "message": "Count not found",
            "color": "firebrick",
            "logo": "simpleicons-rubygems",
            "logoColor": "E9573F"
        }), 404

    except requests.RequestException as e:
        logger.error(f"Error fetching data for {gem_name}: {str(e)}")
        return jsonify({
            "schemaVersion": 1,
            "label": "Downloads",
            "message": "Error fetching data",
            "color": "red",
            "logo": "simpleicons-rubygems",
            "logoColor": "E9573F"
        }), 500
