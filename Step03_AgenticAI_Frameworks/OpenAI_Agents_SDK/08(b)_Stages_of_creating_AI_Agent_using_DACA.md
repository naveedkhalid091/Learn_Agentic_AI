## Stages of Creating AI Agent or Application using DACA Design Pattern:

🔄 **Correct Sequence:** App → Container → Kubernetes → Cloud

### **1. You build your app/Agent:**

- First, you write your AI logic (code) using a programming language. For AI projects, **Python** is the most popular and suitable.
- Second, you have to choose an Agentic Framefork for builting an Agent. **Exmaples**: `OpenAI Agents SDK`, `CrewAI`, `LangChain` etc.
- Third, you choose web/API framework like **FastAPI** to **expose your app as an API**.This step is important so others machines (websites, mobile apps, clients) can access your agent via HTTP requests (like POST and GET).

🧠 Without FastAPI (or something like Flask, Django, etc.), your Python AI code is just code — you can’t call it from a mobile app, a website, or another microservice.

✅ With FastAPI, your app becomes accessible to others via API endpoints (URLs).

### **2. Containerization:**

- After building your app, the next step is to **containerize it**.
- Containerization means packaging your app along with **everything it needs** (code, Python, dependencies, libraries) into a single unit called a **container**.
- This makes sure your app runs the **same way everywhere**— whether on your laptop, a server, or someone else’s computer.
- The most common tool is **Docker**, but here we are using **Rancher Desktop**, which includes Docker features and local Kubernetes.
- **Steps:**
  1.  Write a **Dockerfile** — a file that tells how to build your container.
  2.  Build your app’s image using **Rancher Desktop**.
  3.  Run your image as a **container** and test it locally.
- ✅ Now your app is portable and consistent on any machine.
- 🔁 “It works on my machine” problem is solved!

🔄 **Quick Clarification: FastAPI vs Container Access**

- **FastAPI:** Makes your app accessible via network (API) & it is needed so others (or systems) can call your app.
- **Container:** Makes your app run the same on any machine it is needed so that it doesn’t break due to different setups

### **3. Kubernetes (Using Rancher Desktop's Local K8s):**

- Once you've containerized your app, you might want to run multiple copies of it.
  For Example:

  ```yaml
  replicas: 1
  ```

  At first, only one copy (pod) is running.
  But later traffic increases — 100 users are trying to access your agent.
  You update the same YAML file:

  ```yaml
  replicas: 5
  ```

  Kubernetes then spins up 5 separate Pods (all based on your original image) — now your app can handle more users in parallel.
  This is the manual configuration in Kubernetes but if you wanted to have automatic scalling or configuration then you can enable **Autoscaling in Kubernetes**
  through **HPA (Horizontal Pod Autoscaler)** as follows:

  This configuration says: Start with 1 Pod. If CPU usage goes above 70%, scale up to a maximum of 10 Pods.

  ```yaml
  apiVersion: autoscaling/v2
  kind: HorizontalPodAutoscaler
  metadata:
  name: my-ai-agent-hpa
  spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: my-ai-agent
  minReplicas: 1
  maxReplicas: 10
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
  ```

**Note: You don't need to seperately install Kubernetes and Docker seperately if you have Rancher Desktop installed. For local development, Rancher Desktop is your full-stack DevOps environment.It makes working with containers and Kubernetes super easy for new developers.**

### **4. Cloud Deployment:**

- Once your app works well locally (in containers and Kubernetes), you move to the cloud so anyone can access it from anywhere.
- Cloud platforms like AWS, Google Cloud, Azure, or Render provide services to host your containers and Kubernetes clusters.
- You have two strategies to deploy on the cloud.
  1. Use a Managed Kubernetes service (like AWS EKS, Google GKE) : But keep in your mind that even you choose this strategy, you will still be managing HPA (Autoscalling), Managing Secrets/configs, Writing Deployment YAMLs etc.
  2. deploy your own Kubernetes cluster on a cloud VM.
- The goal of the cloud is to make your app scalable, available 24/7, and accessible globally.

Note: Kubernetes with Dapr can handle 10 million consurrent users in an agentic system, supported by thier proven scalability, real world case studies.
For More information you need to read it from the Panaversity Page. [Learn Agentic AI using Dapr Agentic Cloud Ascent (DACA) Design Pattern](https://github.com/panaversity/learn-agentic-ai/tree/main)
