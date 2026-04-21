# Campus Buzz - Event Submission System

**Group 13** | Hybrid Architecture (3 Container-based Services + 3 Serverless Functions)

## Project Overview
Campus Buzz is a campus event submission platform. Users can submit event information through a simple web form. The system use:
- 3 container-based microservices for core services
- 3 serverless functions for workflow processing

## System Architecture

### Container-based Services (Docker / Manual Start)
- **presentation_service** (Port 5000): Frontend UI + API gateway
- **workflow_service** (Port 5001): Business logic & approval workflow
- **data_service** (Port 5002): Data storage and persistence

### Serverless Functions
- **submission_function.py** (Port 5003)
- **processing_function.py** (Port 5004)
- **result_function.py** (Port 5005)

## How to Run (Run 1 and 2 separately, or directly run 3)
cd ~/campusbuzz-system
### 1. Start 3 Container-based Services 
```bash
# Terminal 1 - Presentation Service
cd presentation_service
python3 app.py

# Terminal 2 - Workflow Service
cd workflow_service
python3 app.py

# Terminal 3 - Data Service
cd data_service
python3 app.py
```
### 2. Start 3 Serverless Functions
```bash
# Terminal 4 - Submission Function
cd functions
python3 submission_function.py

# Terminal 5 - Processing Function
cd functions
python3 processing_function.py

# Terminal 6 - Result Function
cd functions
python3 result_function.py
```
### 3. Run all services and logs in the background.
```bash

# Presentation
cd presentation_service
nohup python3 app.py > presentation.log 2>&1 &

# Workflow
cd ../workflow_service
nohup python3 app.py > workflow.log 2>&1 &

# Data
cd ../data_service
nohup python3 app.py > data.log 2>&1 &

# Functions
cd ../functions
nohup python3 submission_function.py > submission.log 2>&1 &
nohup python3 processing_function.py > processing.log 2>&1 &
nohup python3 result_function.py > result.log 2>&1 &

# check the logs
tail -f presentation_service/presentation.log \
         workflow_service/workflow.log \
         data_service/data.log \
         functions/submission.log \
         functions/processing.log \
         functions/result.log
```

### Frontend Access:
http://47.114.108.240:5000
