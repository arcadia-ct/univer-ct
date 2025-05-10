import os

# Path to the index.html file
index_file_path = "index.html"

# The old and new script tags
old_script_tag = '<script src="config.js"></script>'
new_script_tag = '<script src="https://onlinect.sharepoint.com/sites/ArcadiaTeam/Shared%20Documents/General/KYC/00-univerct/config.js"></script>'

# Read the index.html file
if os.path.exists(index_file_path):
    with open(index_file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Replace the old script tag with the new one
    updated_content = content.replace(old_script_tag, new_script_tag)

    # Write the updated content back to the file
    with open(index_file_path, "w", encoding="utf-8") as file:
        file.write(updated_content)

    print(f"Updated {index_file_path} successfully.")
else:
    print(f"File {index_file_path} not found.")