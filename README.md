# MySQL in GitHub Codespace with Docker

This project runs a MySQL 8 database inside a GitHub Codespace using Docker and Docker Compose. It includes basic usage examples like importing/exporting data and running SQL queries.

---

## 🚀 Getting Started

### 1. Open in GitHub Codespaces

Click **Code > Codespaces > Create codespace** (or use the green "Code" button in GitHub).

### 2. Start MySQL with Docker Compose

In the Codespace terminal, run:

```bash
docker-compose up -d

### 3. Connect to Mysql

docker exec -it mysql-dev mysql -u myuser -p

### 3. Some commands

1. SHOW DATABASES;
2. USE testdb;
3. CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100)
);
4.INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');
5.SELECT * FROM users;

#### Export

6.docker exec mysql-dev mysqldump -u myuser -pmypass testdb > backup.sql

#### Import 

docker cp backup.sql mysql-dev:/backup.sql
docker exec -i mysql-dev mysql -u myuser -pmypass testdb < /backup.sql
