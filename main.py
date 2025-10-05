import requests
import json
import time

def fetch_github_data():
    try:
        username = input("Enter your Githhub username: ")
        url = f"https://api.github.com/users/{username}/events"
        for i in range(5):
            response = requests.get(url)
            if response.status_code == 200:
                events = response.json()
                for event in events:
                    event_type = event.get("type")
                    repo = event.get("repo", {}).get("name")
                    date = event.get("created_at")
                    if event_type == "PushEvent":
                        message = "Pushed to a repository"
                    elif event_type == "PullRequestEvent":
                        message = "Worked on a pull request"
                    elif event_type == "WatchEvent":
                        message = "Starred a repository"
                    elif event_type == "ForkEvent":
                        message = "Forked a repository"
                    else:
                        message = event_type
                    print(f"[{date}] {message} — {repo}")
            elif response.status_code == 429:
                time.sleep(60)
                print("Rate limit exceeded, retry after some time..")
            else:
                print(f"Failed to fetch data: {response.status_code}")
                return None
    except Exception as e:
        print(f"An error occurred: {e}")

fetch_github_data()