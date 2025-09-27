# extensions.py
# This script maps common file extensions to their corresponding media (MIME) types.

def main():
    # Prompt user to enter the file name
    # strip included will remove leading/trailing spaces while lower will converts all characters in a string to lowercase.
    filename = input("File name: ").strip().lower()

    # Dictionary mapping extensions to MIME types
    mime_types = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip",
    }

    # Find the last '.' to check extension
    if "." in filename:
        ext = filename[filename.rfind("."):]
        # Output the corresponding MIME type, or default if not found
        print(mime_types.get(ext, "application/octet-stream"))
    else:
        # If no extension is present
        print("application/octet-stream")


if __name__ == "__main__":
    main()
