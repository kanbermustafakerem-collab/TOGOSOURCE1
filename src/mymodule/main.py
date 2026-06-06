import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from mymodule import greet, add_numbers, load_config

def run():
    print("--- Project Started ---")
    
    config = load_config()
    theme = config.get("settings", {}).get("theme", "light")
    print(f"Loaded Active Theme: {theme}")
    
    message = greet("cmd")
    print(message)
    
    result = add_numbers(5, 10)
    print(f"Addition Result: {result}")

if __name__ == "__main__":
    run()