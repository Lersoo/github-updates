GITHUB_USERNAME=Lersoo
GITHUB_BEARER_TOKEN=027e768aca939ae59c2277b1cc812d0c2ca64ceb

query_response=$(curl -s -u $GITHUB_USERNAME:$GITHUB_BEARER_TOKEN https://api.github.com/notifications)

python3 response_handler.py $query_response
