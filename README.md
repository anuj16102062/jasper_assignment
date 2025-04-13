# jasper_assignment
Task Manager API
Overview

This project is a FastAPI application that allows you to manage tasks. It includes endpoints for creating and retrieving tasks, along with health check functionality to ensure the system is running smoothly.
Requirements

Before running the application, make sure you have the following installed:

    Python 3.10 or higher

    PostgreSQL or your preferred database (adjust configuration accordingly)

    pip (Python package installer)

    curl or Postman for testing the API

    Alembic for database migrations

    Setup Guide
1. Clone the Repository

git clone https://github.com/anuj16102062/jasper_assignment.git
cd jasper_assignment

2. Create a Virtual Environment

It's recommended to create a virtual environment to manage your dependencies.

python3 -m venv venv

Activate the virtual environment:

    Linux:

source venv/bin/activate


3. Install Dependencies

Install all the required dependencies listed in the requirements.txt file:

pip install -r requirements.txt

4. Set Up the Database

Make sure your database is up and running. Adjust the DATABASE_URL in your config.py or .env file if needed to match your setup.
Alembic Setup

Alembic is used for handling database migrations. To set up Alembic, follow these steps:

    Set the PYTHONPATH for Alembic to locate your app module.

    If you're in the project directory, run the following command to set the PYTHONPATH:

export PYTHONPATH=$(pwd)

Alternatively, you can add this line to your .bashrc or .zshrc file to persist it across sessions.

Configure Alembic:

Open the alembic.ini file in the root directory and ensure the sqlalchemy.url points to your database. For example:

sqlalchemy.url = postgresql://username:password@localhost/dbname

Check env.py Configuration:

Open the alembic/env.py file and ensure that the Base (your ORM base) is being imported correctly. For example:

    from app.database import Base

5. Create and Apply Migrations with Alembic
1. Create a New Migration

To create a new migration file that will reflect any changes to your models, run the following command:

alembic revision --autogenerate -m "Initial task table"

    This will automatically generate a migration file in the alembic/versions/ directory.

    Make sure your models are defined correctly in your app.models module, as Alembic will use them to generate the migration script.

2. Apply Migrations

To apply the migrations to your database (this will create the necessary tables or update your schema), run:

alembic upgrade head

    This command will apply all pending migrations up to the latest version.

3. View Migration Versions

If you want to check the status of your migrations, run:

alembic current

This will display the current migration version applied to your database.
4. Revert to a Previous Migration

If you want to downgrade or revert your database to a previous migration version, use:

alembic downgrade <revision_id>

Replace <revision_id> with the desired migration ID.
6. Run the Application

Once the dependencies are installed and the database is set up, run the FastAPI app using uvicorn:

uvicorn app.main:app --reload

The application will be available at http://127.0.0.1:8000.
7. Test the Endpoints

You can test the application using Postman collection.