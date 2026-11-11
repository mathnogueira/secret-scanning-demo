const { Octokit } = require("@octokit/rest");

const octokit = new Octokit({ auth: "ghp_iZ1LnZ3FGHD7CT8PxXUdNsDUzt5lY4o9RSRN" });

module.exports = octokit;
