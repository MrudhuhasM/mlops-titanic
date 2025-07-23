

# MLOps Titanic Survival 🚢🔍

A production-grade end-to-end ML pipeline that takes the classic Titanic dataset, builds a survival prediction model, and ships it as a scalable, monitored service on GCP.

---

## 🎯 Project Goal

1. **Data Contracts & Quality**  
   Define schemas and enforce data gates with Pandera & Great Expectations.  
2. **Reproducible Training**  
   Parameterized training pipelines with MLflow tracking & model registry.  
3. **Serving & Monitoring**  
   Batch & real-time inference APIs (FastAPI + Ray Serve) with drift alerts.  
4. **LLM Augmentation (Future)**  
   Layer on retrieval-augmented LLM explanations/agents.  
5. **Governance & Cost Control**  
   Continuous observability, responsible-AI safeguards, and inference cost tuning.

---

## 🏗️ Architecture (v0)

```
\[Dev Laptop]
│
▼
\[MinIO ← Prefect ← MLflow] → \[FastAPI → GKE/Cloud Run]
│
▼
GCP Stack

```

> _📌 Diagram pending: `docs/architecture_v0.png`_

---

## 🛠️ Tech Stack

- **Language & Packaging**: Python 3.11 + `uv` for dependency management  
- **Config**: Hydra (multirun for `local` vs `gcp` profiles)  
- **Data Validation**: Pandera & Great Expectations  
- **Orchestration**: Prefect (local & Cloud Run)  
- **Experiment Tracking**: MLflow (tracking server + model registry)  
- **Serving**: FastAPI (prediction API) + Ray Serve (autoscaling LLM/ML endpoints)  
- **Infrastructure**: GCP (GKE Autopilot, Cloud Storage, Secret Manager)  
- **Logging & Observability**: structlog (JSON) → GCP Logging & Metrics  

---

## 🚀 Roadmap

1. **Phase 0: Orientation & Scoping**  
   - Repo init, tooling decisions, architecture diagram  
2. **Phase 1: Scaffold & Data Contracts**  
   - Project layout, CI, Pandera schema, GE suite, data versioning  
3. **Phase 2: Reproducible Training & CI/CD**  
4. **Phase 3: Batch + Real-Time Serving + Drift Monitoring**  
5. **Phase 4: Retrieval-Augmented LLM Integration**  
6. **Phase 5: Fine-Tuning & Domain Adaptation**  
7. **Phase 6: Observability, Governance & Responsible AI**  
8. **Phase 7: Scalability & Cost Optimization**  
9. **Phase 8: Capstone Demo & Interview Pack**

---
