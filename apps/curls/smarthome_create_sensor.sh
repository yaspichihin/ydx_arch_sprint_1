curl -X POST http://localhost:8080/api/v1/sensors -H "Content-Type: application/json" -d '{"name": "Living Room Temperature", "type": "temperature", "location": "Living Room", "unit": "°C"}'
echo