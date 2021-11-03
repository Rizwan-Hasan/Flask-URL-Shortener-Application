# Base image
FROM mysql:8

USER root

# Adding schema
ADD schema.sql /docker-entrypoint-initdb.d

# Expose port 3306
EXPOSE 3306