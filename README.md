# MB_Crypto

:pushpin: [Task Description](https://github.com/cardosorrenan/mb_crypto/blob/main/task.txt)

Please ensure that you have Docker and Docker Compose installed [Instructions](https://docs.docker.com/compose/install/linux/), running before following the steps below.

## Getting Started

Follow these steps to set up and run the project:

1. Clone the repository:

   ```bash
   git clone https://github.com/cardosorrenan/mb_crypto.git
   ```

2. Navigate to the project directory:

   ```bash
   cd mb_crypto
   ```

3. List all available commands for managing Docker, testing, and data loading:

   ```
   make help

   Usage:
   make api                 : Start the Docker containers in detached mode
   make stop                : Stop the Docker containers
   make clean-volumes       : Stop the containers and remove associated volumes
   make rebuild             : Rebuild Docker containers without using cache
   make test-all            : Run all tests
   make test-unit           : Run unit tests
   make test-integration    : Run integration tests
   make loaddata            : Load fixture data into the application
   make createsuperuser_dev : Create a development superuser
   make clean-redis         : Deletes all cached keys in the Redis database

   ```

4. Start the services:

   ```bash
   make api
   ```

## API Usage

For more details, access the Docs for the Project:

```
localhost:8000/api/docs/
```

1. Get a token for access:

   ```bash
   curl -X 'POST' \
      'http://localhost:8000/api/token/' \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'X-CSRFToken: 8snll8q6YmhbDUdWEA0h4entHN03rbmmmzYTyJ9rNiRea4llsP9PszN1bBApRpEk' \
      -d '{
      "username": "dev_user",
      "password": "dev_user"
   }'
   ```

   Note: A test user is automatically added when the container starts.

   Response:
   ```json
   {
      "refresh": "<REFRESH_TOKEN>",
      "access": "<ACCESS_TOKEN>"
   }
   ```

2. Retrieve information about a specific coin:

   ```bash
   curl -X 'POST' \
      'http://localhost:8000/api/coin_info/' \
      -H 'accept: application/json' \
      -H 'Authorization: Bearer <ACCESS_TOKEN>' \
      -H 'Content-Type: application/json' \
      -d '{
         "symbol": "BTC"
      }'
   ```

Disclaimer:

Due to Cloudflare CDN blocking my IP based on API v1, my access was limited. In case of status code 403, mocked data will be used for development purposes only. I imagine that the ideal would be to use API v4, according to the documentation at https://api.mercadobitcoin.net/api/v4/docs#section/Authentication.
