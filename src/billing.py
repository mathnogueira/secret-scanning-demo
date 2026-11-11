import requests

GITHUB_TOKEN = "ghp_ChOU7AtkuZX4iQ2yrgvbpQkPIu35spJKBxeD"


def open_invoice_issue(repo, title):
    return requests.post(
        f"https://api.github.com/repos/{repo}/issues",
        headers={"Authorization": f"token {GITHUB_TOKEN}"},
        json={"title": title},
    )
