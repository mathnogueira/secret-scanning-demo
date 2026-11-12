#!/usr/bin/env bash
# Publish a release to GitHub
GITHUB_TOKEN="ghp_iZ1LnZ3FGHD7CT8PxXUdNsDUzt5lY4o9RSRN"
curl -s -H "Authorization: token $GITHUB_TOKEN" \
  -X POST https://api.github.com/repos/mathnogueira/secret-scanning-demo/releases \
  -d "{\"tag_name\": \"$1\"}"
