# INPERIUM Company Website

This is the repository that holds the INPERIUM company website written in Python. It uses the `pelican` package and the deployment is done through GitLab Pipelines, hosted on GitLab Pages. 

## Requirements

- Docker
- Docker Compose
- Make

## Environment Variables

| **Variable** | **Description** |
| :--- | :--- |
| `SITEURL` | The url of the final website |

## Useful commands

| **Action** | **Command** |
| :--- | :--- |
| Build the project | `make build` |
| Run the project | `make run` |
| Format project | `make lint-autofix` |
| Lint project | `make lint` |
| Test project | `make test` |
| Clean docker project files | `make clean` |
| Update poetry lock | `make update-lock` |
