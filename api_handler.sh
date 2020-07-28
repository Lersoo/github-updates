GITHUB_USERNAME=$(grep GITHUB_USERNAME .env | cut -d '=' -f2)
GITHUB_BEARER_TOKEN=$(grep GITHUB_BEARER_TOKEN .env | cut -d '=' -f2)

query_response=$(curl -s -u $GITHUB_USERNAME:$GITHUB_BEARER_TOKEN https://api.github.com/notifications)

python3 response_handler.py $query_response
