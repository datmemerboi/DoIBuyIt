-- brew services restart postgresql@14
-- psql -d postgres

-- CREATE USER WITH PERMISSIONS
CREATE USER DIBI_user WITH PASSWORD 'DIBI_password';

-- CREATE DATABASE
CREATE DATABASE DoIBuyIt;

-- GRANT PERMISSIONS
GRANT ALL PRIVILEGES ON DATABASE DoIBuyIt TO DIBI_user;
GRANT pg_read_server_files TO DIBI_user;

/*
SUGGESTED CSV COPY

COPY products_product
FROM '{product_csv_path}'
DELIMITER ',' CSV;
*/
