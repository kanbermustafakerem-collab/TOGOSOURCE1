import json
import os

def load_config():
    """Loads configuration settings from the root config.json file."""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_dir, '../../config.json')
    
    if not os.path.exists(config_path):
        return {}
        
    with open(config_path, 'r', encoding='utf-8') as f:
        return json.load(f)