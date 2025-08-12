# Test commands for Anomaly Detection API

### 1. POST /prediction with `score=false`
```bash
curl -X 'POST' \
  'http://localhost:8000/predict/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "feature_vector":[0.1, 0.5],
  "score": false
}'
```
### 2. POST /prediction with `score=true`
```bash
curl -X 'POST' \
  'http://localhost:8000/predict/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "feature_vector":[0.1, 0.5],
  "score": true
}'
```
### 3. Get model information
```bash
curl -X 'GET' \
  'http://localhost:8000/model_information/' \
  -H 'accept: application/json'
```