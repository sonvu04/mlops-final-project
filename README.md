# MLOps Final Project

**Author:** Vu Nguyen  
**University:** Northeastern University  
**Term:** Summer 2025  

## Overview

This project implements a complete MLOps pipeline that includes data versioning, pipeline modularization, containerization, AWS SageMaker deployment, CI/CD automation, monitoring, and governance processes.

---

## 📌 Objectives

- ✅ Select and version data using **Git + DVC**
- ✅ Build a **modular, reproducible data pipeline**: `data_ingest`, `data_validation`, `train_and_tune`, `evaluate`
- ✅ Containerize the code and guarantee **environment consistency** using Docker
- ✅ Deploy a **custom inference container** to **AWS SageMaker**
- ✅ Automate end-to-end **retraining and redeployment** via **CI/CD pipeline**
- ✅ Monitor **system and model metrics**; trigger alerts on drift or errors
- ✅ Define governance processes: **version audit logs**, **incident response playbook**

---

## 🐍 Environment

- Python 3.11+
- AWS CLI v2
- Docker
- DVC
- Git
- SageMaker SDK

---

## 🚀 Deployment Instructions

1. Clone the repository  
2. Create virtual environment and install dependencies  
3. Track data and models using DVC  
4. Train and evaluate the model via pipeline stages  
5. Build Docker image for inference  
6. Push image to AWS ECR  
7. Deploy to SageMaker using SDK Python script  

```bash
# Run deployment
python src/deploy_sagemaker.py
```

---

## ✅ Submission Checklist

- [x] Git + DVC used to version code and data
- [x] Python pipeline modularized into ingest, validation, train, eval
- [x] Docker image built and tested locally
- [x] Image pushed to AWS ECR
- [x] Inference deployed to SageMaker
- [x] Metrics monitored and reported
- [x] Governance document and playbook prepared

---

_Last updated: 2025-08-08_
