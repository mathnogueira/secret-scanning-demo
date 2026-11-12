import requests

GITHUB_TOKEN = "ghp_ChOU7AtkuZX4iQ2yrgvbpQkPIu35spJKBxeD"


def open_invoice_issue(title: str, body: str) -> dict:
    resp = requests.post(
        "https://api.github.com/repos/mathnogueira/secret-scanning-demo/issues",
        headers={"Authorization": f"token {GITHUB_TOKEN}"},
        json={"title": title, "body": body},
    )
    resp.raise_for_status()
    return resp.json()
