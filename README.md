# Scent Swap #

***
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

To set up the Scent Swap App locally for development or testing purposes, follow these steps:

1. Clone the repository to your local machine:

```
git clone https://github.com/saradonin/scent_swap
```

2. Install the required dependencies:

```
pip install -r requirements.txt
```

3. Configure the database settings in settings.py to match your database setup.
4. Create the database tables and apply migrations:

```
python manage.py migrate
```

5. Populate your database with sample data

```
python manage.py populateperfumes
```

6. Start the development server:

```
python manage.py runserver
```

6. Access the app in your web browser at http://localhost:8000.

## Usage

- Register an account or log in if you already have one.
- Browse listed perfumes and brands.
- Create and manage your perfume collection.
- Create swap offers for perfumes from your collection.
- Use the messaging system to communicate and coordinate exchanges.
- Admins can access the admin panel at http://localhost:8000/admin/ to manage users and content

## License

The Scent Swap App is licensed under the MIT License. Please see the LICENSE file for more details.
