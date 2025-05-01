import csv
import os
import requests
from datetime import datetime, timezone
from module.repo_info import get_repo_name, get_repo_info

def get_github_token():
    """Read GitHub token from api.key file"""
    try:
        with open('api.key', 'r') as f:
            for line in f:
                if line.startswith('GITHUB_TOKEN='):
                    return line.split('=')[1].strip()
    except FileNotFoundError:
        return None
    return None

def get_relative_time(iso_time):
    """
    Convert ISO datetime to human-readable relative time.
    Example: '2024-03-14T12:34:56Z' -> '4 minutes ago'
    """
    if not iso_time:
        return 'Unknown'
    
    # Parse the ISO time string
    updated_time = datetime.fromisoformat(iso_time.replace('Z', '+00:00'))
    now = datetime.now(timezone.utc)
    
    # Calculate time difference
    diff = now - updated_time
    
    # Convert to seconds
    seconds = diff.total_seconds()
    
    # Convert to appropriate unit
    if seconds < 60:
        return f"{int(seconds)} seconds ago"
    elif seconds < 3600:
        minutes = int(seconds / 60)
        return f"{minutes} minute{'s' if minutes != 1 else ''} ago"
    elif seconds < 86400:
        hours = int(seconds / 3600)
        return f"{hours} hour{'s' if hours != 1 else ''} ago"
    elif seconds < 2592000:  # ~30 days
        days = int(seconds / 86400)
        return f"{days} day{'s' if days != 1 else ''} ago"
    elif seconds < 31536000:  # ~1 year
        months = int(seconds / 2592000)
        return f"{months} month{'s' if months != 1 else ''} ago"
    else:
        years = int(seconds / 31536000)
        return f"{years} year{'s' if years != 1 else ''} ago"

def main():
    if not os.path.exists('repos'):
        print("Error: 'repos' file not found. Please create a file named 'repos' with repository URLs.")
        return

    with open('repos', 'r') as f:
        repo_urls = [line.strip() for line in f if line.strip()]

    output_file = 'repos.analyzed.csv'
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Repo Name', 'URL', 'Last Updated', 'Description'])
        
        for url in repo_urls:
            repo_info = get_repo_info(url)
            repo_name = get_repo_name(url)
            
            if 'error' in repo_info:
                print(f"Error for {url}: {repo_info['error']}")
                writer.writerow([repo_name, url, 'Error', ''])
            else:
                writer.writerow([
                    repo_name,
                    url,
                    repo_info['last_updated'],
                    repo_info['description']
                ])

    print("\nAnalyzed Repositories:")
    print("---------------------")
    for url in repo_urls:
        repo_info = get_repo_info(url)
        repo_name = get_repo_name(url)
        if 'error' in repo_info:
            print(f"{repo_name} - Error: {repo_info['error']}")
        else:
            print(f"{repo_name}")
            print(f"  URL: {url}")
            print(f"  Last Updated: {repo_info['last_updated']}")
            if repo_info['description']:
                print(f"  Description: {repo_info['description']}")
            print()
    
    print(f"Successfully created {output_file} with {len(repo_urls)} repositories")

if __name__ == "__main__":
    main() 