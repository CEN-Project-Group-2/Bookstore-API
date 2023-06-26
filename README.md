# Bookstore-API

This is an open-source API for a fictional bookstore named "Geek Text". This project is for Group 2 Summer 2023 CEN4010.

## Setup

Follow the instructions below to run the API locally:

1. Clone the repository: Clone the repository from GitHub using GitHub Desktop or the terminal.

2. Configure the environment:
   - Copy the `.env-example` file and rename the copy to `.env`.
   - Fill in the variables in the `.env` file.

3. Install all the required packages 
   ```
   pip install -r requirements.txt
   ```

4. Creating dummy data

   The following command will create 15 records in all tables. If you want more or less, try changing the parameter

   ```
   python manage.py seed djangoBookStoreApi --number=15
   ```

5. Start the server:
   - Run the following command in Bash (MacOS/Linux) or Powershell (Windows):
     ```
     python manage.py runserver
     ```

## Managing Packages

Once you add a new package, make sure to add it and its version number to requirements.txt by running

```
pip freeze > requirements.txt
```

## Making a SQL Migration

### Migration Template
To create a template for a SQL migration, run the following command:
```
python manage.py makemigrations
```
After running this command, you can write the migration.

### Running Migration
To apply all unran migrations to the database, use the following command:
```
python manage.py migrate
```
Be cautious as mistakes in the migration may require a rollback or even wiping the database.