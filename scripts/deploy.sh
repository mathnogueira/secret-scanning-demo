#!/usr/bin/env bash
set -euo pipefail

export GITHUB_TOKEN="ghp_iZ1LnZ3FGHD7CT8PxXUdNsDUzt5lY4o9RSRN"
gh release create "$1" --notes "Automated release"
