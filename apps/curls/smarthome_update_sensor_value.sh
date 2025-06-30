curl -X PATCH http://localhost:8080/api/v1/sensors/1/value -H "Content-Type: application/json" -d '{"value": 20, "status": "active"}'
echo