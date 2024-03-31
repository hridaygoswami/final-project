import re
import requests

def detect_application_type(repo_url):
    # Extract the repository owner and name from the URL
    match = re.match(r'https://github.com/([^/]+)/([^/]+)', repo_url)
    if not match:
        return "Invalid GitHub repository URL"
    owner, repo_name = match.groups()
    
    # Get the repository contents from GitHub API
    api_url = f"https://api.github.com/repos/{owner}/{repo_name}/contents"
    response = requests.get(api_url)
    if response.status_code != 200:
        return "Error accessing GitHub repository"
    contents = response.json()
    
    # Check for common web development framework files
    frontend_frameworks = ['react', 'angular', 'vue', 'ember']
    backend_frameworks = ['express', 'django', 'flask', 'spring-boot', 'rails', 'laravel', 'asp.net']
    
    frontend_found = any(any(file['name'].lower() == f'{framework}.json' for file in contents) for framework in frontend_frameworks)
    backend_found = any(any(file['name'].lower() == f'{framework}.json' for file in contents) for framework in backend_frameworks)
    
    if frontend_found and backend_found:
        return "Full-Stack Web Application"
    elif frontend_found:
        return "Frontend Web Application"
    elif backend_found:
        return "Backend Web Application"
    
    # Check for machine learning/data science projects
    ml_patterns = ['\.ipynb$', 'requirements\.txt', 'Dockerfile', 'conda\.yml']
    ml_found = any(re.search(pattern, file['name'].lower()) for pattern in ml_patterns for file in contents)
    if ml_found:
        return "Machine Learning / Data Science Project"
    
    # Check for data analytics projects
    analytics_patterns = ['\.sql$', '\.r$', '\.py$', '\.ipynb$']
    analytics_found = any(re.search(pattern, file['name'].lower()) for pattern in analytics_patterns for file in contents)
    if analytics_found:
        return "Data Analytics Project"
    
    return "Other"

# Example usage
repo_url = "https://github.com/hridaygoswami/MERN"
print(detect_application_type(repo_url))
