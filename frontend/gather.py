import os
import fnmatch
import zipfile
from pathlib import Path

# Define which file extensions to include
INCLUDE_PATTERNS = ['*.py', '*.js', '*.jsx', '*.ts', '*.tsx', '*.html', '*.css', '*.json']

# Define which directories or files to exclude (like git, node_modules, binaries)
EXCLUDE_DIRS = ['node_modules', 'dist', '__pycache__', '.git', 'build']
EXCLUDE_FILES = ['*.min.js', '*.map', '*.lock', '*.log']

def should_include_file(file_name):
    """ Check if the file matches any of the include patterns. """
    return any(fnmatch.fnmatch(file_name, pattern) for pattern in INCLUDE_PATTERNS)

def should_exclude(file_path):
    """ Check if the file or directory should be excluded. """
    parts = file_path.split(os.sep)
    return any(part in EXCLUDE_DIRS for part in parts) or any(fnmatch.fnmatch(file_path, pattern) for pattern in EXCLUDE_FILES)

def collect_code_files(root_dir):
    """ Recursively collect code files from the directory. """
    code_files = []
    for dirpath, _, filenames in os.walk(root_dir):
        if should_exclude(dirpath):
            continue
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            if should_include_file(filename) and not should_exclude(file_path):
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    code_files.append({
                        'file_path': file_path,
                        'content': content
                    })
    return code_files

def summarize_code(files):
    """ Summarize the collected files for AI input. """
    summary = {}
    for file in files:
        file_path = file['file_path']
        file_name = os.path.basename(file_path)
        lines_of_code = len(file['content'].splitlines())
        summary[file_path] = {
            'file_name': file_name,
            'lines_of_code': lines_of_code,
            'content_snippet': file['content'][:500]  # Show first 500 characters of content
        }
    return summary

def zip_project_files(files, zip_name='project_code.zip'):
    """ Optionally, zip the collected files for easier sharing. """
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for file in files:
            zipf.writestr(file['file_path'], file['content'])

def main():
    project_root = input("Enter the root directory of the project: ")
    collected_files = collect_code_files(project_root)
    
    # Print summary for AI context understanding
    code_summary = summarize_code(collected_files)
    for file_path, details in code_summary.items():
        print(f"File: {file_path}, Lines of code: {details['lines_of_code']}")
        print(f"Snippet:\n{details['content_snippet']}\n")
    
    # Optionally, zip the project for later use
    zip_project_files(collected_files)

if __name__ == "__main__":
    main()
