# Scent Swap #

The Scent Swap App is a web application designed to facilitate the exchange of perfumes and fragrances among users. It
provides a platform for perfume enthusiasts to discover new scents, list their own perfumes, and connect with others for
swaps. This repository contains the source code for the Scent Swap App.

## Features

- User Registration and Authentication: Users can create accounts and log in securely.
- Browse Scents: Discover a wide variety of scents listed in database with details such as brand, name, category and
  olfactive notes.
- User Profiles: Create and manage your collection of perfumes.
- Scent Swapping: Create scent swap offers, allowing you to try new fragrances.
- Messaging: Communicate with other users to finalize swap details and coordinate exchanges.

## Getting started

### Deployed

The deployed application is available at the link.

https://scent-swap-0f8a23c9492b.herokuapp.com

See [Usage](#usage) for

### Developement

To set up the Scent Swap App locally for development or testing purposes, follow these steps:

1. Use `develop` branch for development.

2. Clone the repository to your local machine:

```
git clone https://github.com/saradonin/scent_swap
```

3. Create .env file in root directory
```
SECRET_KEY=your_secret_key
POSTGRES_DB=your_db_name
POSTGRES_USER=your_db_user
POSTGRES_PASSWORD=your_db_password
```

4. Run the container:

```
docker-compose up
```

5. Access the app in your web browser at http://localhost:8000.

Ensure you have [Docker](https://www.docker.com/get-started/) installed before running these commands.

## Usage

- Register an account or log in using existing accounts:
  - superuser: username `admin`, login `admin`
  - user 1: username `user1`, password `password123`
  - user 2: username `user2`, password `password123`
- Browse listed perfumes and brands.
- Create and manage your perfume collection.
- Create swap offers for perfumes from your collection.
- Use the messaging system to communicate and coordinate exchanges.

## License

The Scent Swap App is licensed under the MIT License. Please see the LICENSE file for more details.

![scentswap_screen](https://github.com/saradonin/scent_swap/assets/124811561/4b6f367f-16d0-426c-b8bf-196f5c643b96)

