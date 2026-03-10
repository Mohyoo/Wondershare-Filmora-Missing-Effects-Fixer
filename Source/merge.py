import os
import json

def merge_filmora_configs_with_categories():
    # Final structure template
    # We use a generic name so it doesn't conflict with specific packs
    merged_data = {
        "pack_info": {
            "id": 1038, 
            "version": "1.0.0",
            "name": "DefaultPackage", # Using the standard name helps compatibility
            "titles": {"en": "All Effects"}
        },
        "resources": {}
    }

    json_files = [f for f in os.listdir('.') if f.endswith('.json') and f != 'Merged_Config.json']
    
    if not json_files:
        print("No JSON files found.")
        return

    print(f"Merging {len(json_files)} files while preserving categories...\n")

    for file_name in json_files:
        try:
            with open(file_name, 'r', encoding='utf-8') as f:
                data = json.load(f)
                resources = data.get("resources", {})
                
                for res_id, content in resources.items():
                    # We keep the original content exactly as is
                    # This preserves 'cat_ids', 'res_type', and 'name'
                    if res_id not in merged_data["resources"]:
                        merged_data["resources"][res_id] = content
                    else:
                        # If duplicate ID exists, keep the one with higher version
                        existing_v = merged_data["resources"][res_id].get("version", "0.0.0")
                        new_v = content.get("version", "0.0.0")
                        if new_v > existing_v:
                            merged_data["resources"][res_id] = content
                            
                print(f"Included resources from: {file_name}")
                
        except Exception as e:
            print(f"Skipped {file_name} due to error: {e}")

    output_file = 'Merged_Config.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        # separators=(',', ':') removes extra spaces to keep the file size smaller
        json.dump(merged_data, f, indent=4, ensure_ascii=False)

    print(f"\nDone! Total unique effects: {len(merged_data['resources'])}")
    print("Output file is: " + output_file)
    print("Rename it and move it to:")
    print(r"C:\ProgramData\Wondershare Filmora\Default Effects\DefaultPackage\Config.json")
    print("The effects should now all appear, and in their original categories.")

if __name__ == "__main__":
    merge_filmora_configs_with_categories()