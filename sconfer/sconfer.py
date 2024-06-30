import sys
import json
import os

def validate_json(data, required_keys):
    """
    Validate if the provided data contains all required keys.
    """
    if not isinstance(data, dict):
        return False
    for key in required_keys:
        if key not in data:
            return False
    return True

def load_json(file_path):
    """
    Load and parse JSON file, allowing for comments.
    """
    with open(file_path, 'r') as file:
        content = file.read()
        content = '\n'.join([line for line in content.split('\n') if not line.strip().startswith('//')])
        try:
            return json.loads(content)
        except json.JSONDecodeError:
            raise ValueError(f"File {file_path} is not a valid JSON file.")

def main():
    if len(sys.argv) != 4:
        print("Usage: sconfer.py <template> <inbounds> <outbounds>")
        sys.exit(1)

    template_path, inbounds_path, outbounds_path = sys.argv[1], sys.argv[2], sys.argv[3]

    if not os.path.exists(template_path):
        print(f"Template file {template_path} does not exist.")
        sys.exit(1)
    if not os.path.exists(inbounds_path):
        print(f"Inbounds file {inbounds_path} does not exist.")
        sys.exit(1)
    if not os.path.exists(outbounds_path):
        print(f"Outbounds file {outbounds_path} does not exist.")
        sys.exit(1)

    try:
        template = load_json(template_path)
        inbounds = load_json(inbounds_path)
        outbounds = load_json(outbounds_path)
    except ValueError as e:
        print(e)
        sys.exit(1)

    # required_template_keys = ["log", "dns", "inbounds", "outbounds", "route", "experimental"]
    required_template_keys = ["inbounds", "outbounds"]
    if not validate_json(template, required_template_keys):
        print("Template file format is incorrect.")
        sys.exit(1)

    if "inbounds" not in inbounds or not isinstance(inbounds["inbounds"], list):
        print("Inbounds file format is incorrect.")
        sys.exit(1)

    if "outbounds" not in outbounds or not isinstance(outbounds["outbounds"], list):
        print("Outbounds file format is incorrect.")
        sys.exit(1)

    # Merge inbounds and outbounds into the template
    template["inbounds"] = inbounds["inbounds"]
    template["outbounds"] = outbounds["outbounds"]

    # Determine output file name
    template_name = os.path.splitext(os.path.basename(template_path))[0]
    inbounds_name = os.path.splitext(os.path.basename(inbounds_path))[0]
    outbounds_name = os.path.splitext(os.path.basename(outbounds_path))[0]
    output_file_name = f"{template_name}_{inbounds_name}_{outbounds_name}.json"

    # Write the merged content to the output file
    with open(output_file_name, 'w') as output_file:
        json.dump(template, output_file, indent=2)

    print(f"Output written to {output_file_name}")

if __name__ == "__main__":
    main()