CREATE DATABASE education_db;

DO $$
BEGIN
   IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname = 'test') THEN
      CREATE USER test WITH ENCRYPTED PASSWORD 'testpassword';
      GRANT ALL PRIVILEGES ON DATABASE education_db TO test;
   END IF;
END
$$;