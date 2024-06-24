import requests
from bs4 import BeautifulSoup
import re

def fetch_codechef_solved_problems(username):
    # URL of the user's profile page
    url = f"https://www.codechef.com/users/{username}"

    # Send a request to fetch the page content
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to fetch the profile page. Status code: {response.status_code}")
        return None

    # Parse the page content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Convert the soup object to a string
    page_content = str(soup)

    # Use regex to find the "Total Problems Solved" line and extract the number
    match = re.search(r'Total Problems Solved:\s*(\d+)', page_content)

    if match:
        total_solved = int(match.group(1))
        return total_solved
    else:
        print("Total Problems Solved section not found.")
        return None

# Example usage
username = "sanjaysrocks"
total_solved = fetch_codechef_solved_problems(username)
if total_solved is not None:
    print(f"Total Problems Solved by {username}: {total_solved}")
else:
    print("Could not retrieve the total number of solved problems.")
