#!/usr/bin/env python3
"""
Test Files Creator - Creates sample files for testing File Organizer
Author: Darius04-ux
"""

import json
import zipfile
from pathlib import Path

# Handle optional dependency: Pillow
try:
    from PIL import Image, ImageDraw, ImageFont
    PILLOW_AVAILABLE = True
except ImportError:
    PILLOW_AVAILABLE = False


def create_test_files():
    """Create various test files for File Organizer testing"""
    # Obsługa polskiego i angielskiego pulpitu
    home = Path.home()
    if (home / "Desktop").exists():
        desktop = home / "Desktop"
    elif (home / "Pulpit").exists():
        desktop = home / "Pulpit"
    else:
        raise FileNotFoundError("Nie znaleziono folderu Desktop ani Pulpit w katalogu domowym użytkownika.")
    test_folder = desktop / "test_files"
    test_folder.mkdir(exist_ok=True)
    
    print(f"📁 Creating test files in: {test_folder}")
    
    # 1. Create text files
    create_text_files(test_folder)
    
    # 2. Create image files
    create_image_files(test_folder)
    
    # 3. Create document files
    create_document_files(test_folder)
    
    # 4. Create archive files
    create_archive_files(test_folder)
    
    # 5. Create code files
    create_code_files(test_folder)
    
    # 6. Create other files
    create_other_files(test_folder)
    
    print(f"✅ Test files created successfully!")
    print(f"📂 Location: {test_folder}")
    
    # List created files
    files = list(test_folder.glob("*"))
    print(f"\n📋 Created {len(files)} files:")
    for file in sorted(files):
        if file.is_file():
            print(f"   • {file.name}")

def create_text_files(folder: Path):
    """Create text document files"""
    
    # Simple text file
    (folder / "readme.txt").write_text("""
File Organizer Test Document
===========================

This is a test document for the File Organizer Pro.
It should be moved to the Documents folder.

Features tested:
- Text file organization
- Document categorization
- File moving operations

Author: Darius04-ux
""")
    
    # Another text file
    (folder / "notes.txt").write_text("""
Project Notes
=============

1. File Organizer working perfectly
2. GUI interface responsive
3. Logging system operational
4. Undo functionality tested

Next steps:
- Add more file types
- Improve UI design
- Add batch processing
""")
    
    print("📝 Created text files")

def create_image_files(folder: Path):
    """Create sample image files."""
    if not PILLOW_AVAILABLE:
        print("⚠️  Pillow (PIL) not available, creating placeholder image files.")
        (folder / "sample_image.png").write_bytes(b"PNG placeholder")
        (folder / "test_photo.jpg").write_bytes(b"JPEG placeholder")
        return

    # Create a simple PNG image
    img = Image.new('RGB', (400, 300), color='lightblue')
    draw = ImageDraw.Draw(img)

    # Add some text
    try:
        font = ImageFont.load_default()
    except IOError:
        # If default font is not available, proceed without it
        font = None

    draw.text((50, 100), "Test Image", fill='darkblue', font=font)
    draw.text((50, 130), "File Organizer Pro", fill='darkblue', font=font)
    draw.text((50, 160), "Sample PNG File", fill='darkblue', font=font)

    # Draw some shapes
    draw.rectangle([50, 200, 150, 250], outline='red', width=3)
    draw.ellipse([200, 200, 300, 250], outline='green', width=3)

    img.save(folder / "sample_image.png")

    # Create another image (JPG)
    img2 = Image.new('RGB', (300, 200), color='lightgreen')
    draw2 = ImageDraw.Draw(img2)
    draw2.text((50, 80), "JPEG Test File", fill='darkgreen', font=font)
    draw2.text((50, 110), "For File Organizer", fill='darkgreen', font=font)
    img2.save(folder / "test_photo.jpg", "JPEG")
    print("🖼️  Created image files")

def create_document_files(folder: Path):
    """Create document-like files"""
    
    # Create a fake PDF (just text with .pdf extension)
    pdf_content = """
%PDF-1.4 (This is a fake PDF for testing)
File Organizer Pro - Test Document
==================================

This file simulates a PDF document.
In real usage, this would be a proper PDF file.

The File Organizer should move this to Documents folder.

Test completed successfully!
"""
    (folder / "test_document.pdf").write_text(pdf_content)
    
    # Create RTF file
    rtf_content = r"""{\rtf1\ansi\deff0 {\fonttbl {\f0 Times New Roman;}}
\f0\fs24 File Organizer Test RTF Document\par
\par
This is a Rich Text Format document for testing.\par
\par
Features:\par
- RTF formatting\par
- Document organization\par
- File type detection\par
\par
Author: Darius04-ux\par
}"""
    (folder / "report.rtf").write_text(rtf_content)
    
    print("📄 Created document files")

def create_archive_files(folder: Path):
    """Create archive files"""
    
    # Create a ZIP file
    zip_path = folder / "test_archive.zip"
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        # Add some content to the zip
        zipf.writestr("readme.txt", "This is content inside the ZIP file")
        zipf.writestr("data.json", '{"test": "data", "file": "organizer"}')
        zipf.writestr("folder/nested_file.txt", "Nested file content")
    
    # Create another archive (fake RAR)
    (folder / "backup.rar").write_bytes(b"RAR archive placeholder for testing")
    
    print("📦 Created archive files")

def create_code_files(folder: Path):
    """Create code files"""
    
    # Python file
    python_code = '''#!/usr/bin/env python3
"""
Sample Python script for File Organizer testing
"""

def hello_world():
    print("Hello from File Organizer test!")
    print("This Python file should go to Code folder")

if __name__ == "__main__":
    hello_world()
'''
    (folder / "sample_script.py").write_text(python_code)
    
    # JavaScript file
    js_code = '''// Sample JavaScript file for testing
console.log("File Organizer Pro - JavaScript Test");

function organizeFiles() {
    console.log("This JS file should go to Code folder");
    return "File organization complete!";
}

organizeFiles();
'''
    (folder / "app.js").write_text(js_code)
    
    # HTML file
    html_code = '''<!DOCTYPE html>
<html>
<head>
    <title>File Organizer Test</title>
</head>
<body>
    <h1>File Organizer Pro</h1>
    <p>This HTML file should be moved to Code folder</p>
    <p>Testing file organization...</p>
</body>
</html>
'''
    (folder / "index.html").write_text(html_code)
    
    print("💻 Created code files")

def create_other_files(folder: Path):
    """Create other miscellaneous files"""
    
    # JSON data file
    json_data = {
        "app_name": "File Organizer Pro",
        "version": "1.0",
        "author": "Darius04-ux",
        "test_files": [
            "readme.txt",
            "sample_image.png",
            "test_document.pdf"
        ],
        "features": [
            "File organization",
            "GUI interface",
            "Undo functionality",
            "Logging system"
        ]
    }
    (folder / "config.json").write_text(json.dumps(json_data, indent=2))
    
    # XML file
    xml_content = '''<?xml version="1.0" encoding="UTF-8"?>
<fileorganizer>
    <name>File Organizer Pro</name>
    <author>Darius04-ux</author>
    <description>Test XML file for file organization</description>
    <files>
        <file type="image">sample_image.png</file>
        <file type="document">test_document.pdf</file>
        <file type="archive">test_archive.zip</file>
    </files>
</fileorganizer>
'''
    (folder / "data.xml").write_text(xml_content)
    
    # Log file
    log_content = '''2025-01-01 10:00:00 - INFO - File Organizer started
2025-01-01 10:00:01 - INFO - Scanning folder for files
2025-01-01 10:00:02 - INFO - Found 15 files to organize
2025-01-01 10:00:03 - INFO - Created Images folder
2025-01-01 10:00:04 - INFO - Moved sample_image.png to Images/
2025-01-01 10:00:05 - INFO - Created Documents folder
2025-01-01 10:00:06 - INFO - Moved test_document.pdf to Documents/
2025-01-01 10:00:07 - INFO - Organization completed successfully
'''
    (folder / "organizer.log").write_text(log_content)
    
    print("📋 Created other files")

if __name__ == "__main__":
    print("🚀 File Organizer Pro - Test Files Creator")
    print("=" * 50)
    
    try:
        create_test_files()
        print("\n✅ All test files created successfully!")
        print("🎯 Now you can test the File Organizer with these files!")
        
    except Exception as e:
        print(f"❌ Error creating test files: {e}")
        print("💡 Try running as administrator if you get permission errors")
