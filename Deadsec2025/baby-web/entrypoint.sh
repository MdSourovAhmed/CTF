#!/bin/bash
# Start file cleanup in background
while true; do
  find /var/www/html/uploads/ -mindepth 1 -mmin +15 -delete
  sleep 30
done &

# Start Apache in foreground
exec apache2-foreground
