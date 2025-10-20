import requests
import json
import time


def fetch_github_data(username):
    try:
        url = f"https://api.github.com/users/{username}/events"
        for i in range(5):
            response = requests.get(url)
            if response.status_code == 200:
                events = response.json()
                activities = []
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
                    recent_activity = f"[{date}] {message} — {repo}"
                    activities.append(recent_activity)
                return activities
            elif response.status_code == 429:
                time.sleep(60)
                return ["Rate limit exceeded, retry after some time.."]
            else:
                return [f"Failed to fetch data: {response.status_code}"]
    except Exception as e:
        return [f"An error occurred: {e}"]