import re
import os

def convert_ruby_to_json(input_path, output_path):
    
    with open(input_path, 'r', encoding='utf-8') as infile:
        content = infile.read()

    
    
    json_content = re.sub(r':(\w+)\s*=>', r'"\1":', content)

    with open(output_path, 'w', encoding='utf-8') as outfile:
        outfile.write(json_content)

    print(f"Successfully converted '{input_path}' to JSON at '{output_path}'")

if __name__ == "__main__":
    
    if os.path.exists('task1_d.json'):
        convert_ruby_to_json('task1_d.json', 'task1_d_fixed.json')
    else:
        print("Error: Source file 'task1_d.json' not found.")