# Docker Compose MySQL Setup

This repository contains a Docker Compose configuration for MySQL 8.0 with initialization data.

## Configuration

The Docker Compose setup includes:
- MySQL 8.0
- Initialization SQL script with sample data
- Persistent volume for database data

## Connection Details

- **Host**: localhost
- **Port**: 3306
- **Database**: mydatabase
- **Username**: user
- **Password**: password
- **Root Password**: rootpassword

## Usage

Start the MySQL container:
```
docker-compose up -d
```

Stop the MySQL container:
```
docker-compose down
```

To reset the database completely (including deleting all data):
```
docker-compose down -v
```

## SQL Initialization

The database is initialized with the SQL scripts located in the `sql/` directory. The scripts create sample tables and populate them with data.
