import requests
from datetime import datetime, timezone

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

def get_repo_name(url):
    """Extract repository name from GitHub URL"""
    return url.strip().rstrip('/').replace('.git', '').split('/')[-1]

def get_relative_time(iso_time):
    """Convert ISO datetime to relative time"""
    if not iso_time:
        return 'Unknown'
    
    updated_time = datetime.fromisoformat(iso_time.replace('Z', '+00:00'))
    now = datetime.now(timezone.utc)
    diff = now - updated_time
    seconds = diff.total_seconds()
    
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

def get_repo_info(url):
    """Get repository information from GitHub API"""
    if 'github.com' not in url:
        return {'error': 'Only GitHub repositories are supported'}
    
    parts = url.strip().rstrip('/').replace('.git', '').split('/')
    if len(parts) < 5:
        return {'error': 'Invalid GitHub URL format'}
    
    owner = parts[3]
    repo = parts[4]
    api_url = f'https://api.github.com/repos/{owner}/{repo}'
    
    token = get_github_token()
    headers = {
        'User-Agent': 'Gitalyzer/1.0',
        'Accept': 'application/vnd.github.v3+json'
    }
    if token:
        headers['Authorization'] = f'token {token}'
    
    try:
        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return {
                'last_updated': get_relative_time(data.get('updated_at')),
                'description': data.get('description', '')
            }
        else:
            return {'error': f'API request failed with status {response.status_code}'}
    except Exception as e:
        return {'error': f'Error fetching repository info: {str(e)}'} 