# Books Giveaway API

The Books Giveaway API is a platform that enables book enthusiasts to share and exchange their favorite books with others. This API allows users to list books for giveaway, browse available books, and manage their book collections.

### Prerequisites

Before you can run the Books Giveaway API, ensure you have the following prerequisites installed:

- Python 3.x
- pip3 (for managing Python packages)
- Git (for cloning the repository)

### Installation & Setup

 - git clone https://github.com/Chachanidze29/BooksGiveAway.git
 - cd BooksGiveAway
 - run docker compose up --build
 - run docker-compose exec api sh and inside shell run python3 manage.py makemigrations & python3 manage.py migrate
 - open browser and open localhost:8000 (http://0.0.0.0:8000/ instead of 0.0.0.0 use localhost)