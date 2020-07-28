GITHUB_USERNAME=$(grep GITHUB_USERNAME .env | cut -d '=' -f2)
GITHUB_BEARER_TOKEN=$(grep GITHUB_BEARER_TOKEN .env | cut -d '=' -f2)
PYTHON_SCRIPT=~/code/Lersoo/github-updates/response_handler.py

query_response=$(curl -s -u $GITHUB_USERNAME:$GITHUB_BEARER_TOKEN https://api.github.com/notifications)

python3 $PYTHON_SCRIPT $query_response
