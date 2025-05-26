## Dapr Agentic Cloud Ascent (DACA):

Design pattern by Sir Zia Khan for building and deploying AI Agents at planet-scale with minimal budget

### 1. **Overview:**

DACA defines a step-by-step guide to create and deploy cloud-native AI Agents capable of supporting 10 million concurrent instances cost-efficiently.

- 1.1 **Goals:**

  - **High Concurrency:** Handle millions of simultaneous agents.
  - **Minimal Cost:** Leverage cloud-native scalability and pay-as-you-go.
  - **Portability:** Run uniformly across any cloud provider.

## **DACA Architecture:**

The DACA architecture is a design pattern for building, managing, and enabling communication between AI agents using a combination of modern technologies. **It consists of three main parts/layers**:

1. Presentation Layer (UI part) :
2. Business Logic & Agentic workflows layer:
   - Python
   - OpenAI Agents SDK
   - FastAPI
   - Docker (we will be using Rancher Desktop instead of Docker Desktop)
   - Dapr
   - A2A Communication protocol
   - MCP
3. Data Layer:

### **1. Presentation Layer (UI part):**

- In this part UI is created either through Next.js or Chainlit or Streamlit, here users will interect with our App.

### **2. Business Logic & Agentic workflows layer:**

In this part we have to use following technologies to create an effective agent.

i). **Python:** Python is a versatile programming language used to write the code for the agents and the system. It serves as the foundation for developing the agents.
ii). **OpenAI Agentic SDK:** A Software Development Kit (SDK) from OpenAI designed for creating agentic systems—agents that can act autonomously and perform tasks independently. This SDK provides the tools and frameworks needed to build intelligent agents with capabilities like decision-making, reasoning, or natural language processing.

**Note:** You can sucessfully create Agents with above two technologies and deploy on chainlit but DACA's objective will not be fulfilled here. That's why the another technologies are needed to fulfill the DACA objective.

iii). **FastAPI**: Now we need to connect/expose our agent from our local machine to any external interface or with the world i.e. with WhatsApp, through Messaging APIs. So to expose our agent externally, we need FastAPI.

iv). **Docker Desktop/Rancher Desktop:** It enables the cloud's environment locally and create the microservices.
Let's understand how to create microservices, consider if your App contains following services:

    1.  User management service (handles sign-up, login, profiles)
    2.  Catalog service (manages product listings)
    3.  Order service (processes purchases)

    You could:
      - Put all three in one container (that’s a monolith in Rencher Desktop), or
      - Split them into three containers (each is a microservice).

- **Why split into microservices?** - If the order service crashes, the login and catalog services keep running.
- **If orders spike**, you spin up more order containers without touching the others.

Note: Upto this Stage you will have containerized AI Agent.

v) **Dapr (SideCar Container):**

Dapr is a small helper container that runs along with each of your microservices created above (This is called sideCar container because it is linked with each microservice).

Instead of letting your microservices store or manage user data directly via APIs, you use Dapr to send and get data from the database. This keeps your services clean and stateless, meaning microservices don’t hold any users data themselves.

Without Dapr:
Each microservice talks to the database on its own, adding more code and complexity.

With Dapr:
Your mircoservice just tells Dapr what to do — like “save this user” or “get this order” — and Dapr handles the rest.

This makes your app easier to build, faster to scale, and less likely to crash under load.

vi) **A2A Communication protocol?**

A2A communication stands for Agent-to-Agent communication launched by Google with over 50 partners. It’s a way for different AI agents (think of them as smart computer programs) to talk to each other, even if they were made using different tools or platforms. Imagine you have two friends who don’t speak the same language—they’d need a translator to chat. Similarly, AI agents from different systems need a “translator” to understand each other, and A2A communication acts like that translator. It helps these agents share information, work together, and solve problems as a team.

In simple terms, A2A communication is like a phone line between AI agents. It lets them connect and cooperate, no matter where they come from, so they can do bigger and better things together.

### **How to Enable A2A Communication:**

A2A communication is made possible through something called the **Agent2Agent (A2A) protocol.** This protocol is like a set of instructions or rules that AI agents follow to talk to each other. Here’s how it works, broken down into easy steps:

- Finding Out What Each Agent Can Do:

  - First, the AI agents introduce themselves to each other. They say, “Hey, here’s what I’m good at!” For example, one agent might be great at finding information, while another is awesome at making pictures. This step is called discovering capabilities. It’s like people telling each other their skills before starting a group project.

- Agreeing on How to Talk:

  - Next, the agents figure out how they’ll communicate. They decide on a “language” or format they both understand, like agreeing to send messages in simple text. This step is called negotiating interaction. It’s similar to friends deciding whether to text or call when planning something together.

- Working Together:

  - Once they’ve agreed on how to talk, the agents can start helping each other with tasks. They share what they need to, but they don’t have to show how they do their own work—like keeping their secret recipes private. This is the collaboration part, where they team up to get things done.

**Why It’s Cool:**

A2A works with something called MCP (Model Context Protocol), which lets AI agents connect to outside tools and data (like the internet or databases). When A2A and MCP team up, AI agents can not only talk to each other but also grab extra info or tools they need to be even more helpful.

### **Layers of Communication:**

a) **Human Interacts with the Client Agent:**

- As a human, you interact directly with a client agent. This is your point of contact—like a helpful assistant who listens to what you need and takes responsibility for making it happen. You as human interect with client agent and this client knows about you.

b) **Client Agent Interacts with Other Skilled (remote or external) Agents (A2A COMMUNICATIONS):**

- The client agent doesn’t do everything on its own. Instead, it communicates with other skilled/remote or external agents—specialized helpers with specific abilities (e.g., one might be great at producing Passports at Passport offices, ). This interaction between the client agent and the other agents is possible through A2A (Agent-to-Agent) communication protocol. It’s how the client agent gets the support it needs to fulfill your request.
-

vii) MCP:

- MCP allows AI agents—including both the client agent and the skilled agents—to connect to external tools, data, or resources (e.g., databases, the internet, or other systems). While MCP can enhance an agent’s abilities by giving it access to outside information.

**DACA Deployment Stages: The Ascent (strategy)**

We have two requirements in cloud Ascent:

- **Requirement #1:** We will make our App or Agents inside the container that should run at all stages without changing the code, including at:

- Locally at our Desktop through Rancher Desktop.
- Secondly, it should run at Hugging Face.
- Thirdly, it should run at Azure container App.
- Forth, it should run at Kubernetes with just change in configurations.

- **Requirement #2:** The App or Agent should run free at prototyping stages or with minimum cost:

## **1. Local Development: Open-Source Stack**

**Goal:** Rapid iteration with production-like features.
**Setup:**

- **Rancher Desktop with Lens:** Runs the agent app, Dapr sidecar, A2A endpoints and local services on local Kubernetes.
- **LLM APIs:** OpenAI Chat Completion, Google Gemini (free tier).
- **Agents and MCP Servers:** OpenAI Agents SDK as Dapr Actors with MCP Servers and with A2A integration.
- **REST APIs:** FastAPI.
- **Messaging:** Local RabbitMQ container.
- **Scheduling:** python-crontab, APScheduler, or Schedule or Dapr Scheduler.
- **Database:** Local Postgres container, SQLModel ORM, CockroachDB (Free tier, cloud-hosted database)
- **In-Memory Store:** Local Redis container, redis-py or Redis OM Python.
- **Dev Tools:** VS Code Dev Containers for containerized development.
- **Open Core and Managed Edges:** Uses open-source Kubernetes (Rancher Desktop) and Dapr for the core, with local open-source services (Postgres, Redis) to simulate production. Managed services like OpenAI APIs are used at the edges for prototyping LLM inference.
- **Scalability:** Single machine (1-10 req/s with OpenAI).
- **Cost:** Free, using open-source tools.

## 2. **Prototyping: Free Deployment**

**Goal:** Test and validate with minimal cost.
**Setup:**

- **Containers:** Deploy to Hugging Face Docker Spaces (free hosting, CI/CD). Both FastAPI, MCP Server, and A2A endpoints in containers.
- **LLM APIs:** Google Gemini (free tier), Responses API.
- **Messaging:** CloudAMQP RabbitMQ (free tier: 1M messages/month, 20 connections).
- **Scheduling:** cron-job.org (free online scheduler).
- **Database:** CockroachDB Serverless (free tier: 10 GiB, 50M RU/month).
- **In-Memory Store:** Upstash Redis (free tier: 10,000 commands/day, 256 MB).
- **Dapr:** Use Managed Dapr Service Catalyst by Diagrid free-tier.
- **Scalability:** Limited by free tiers (10s-100s of users, 5-20 req/s).
- **Cost:** Fully free, but watch free tier limits (e.g., Upstash’s 7 req/min cap).

## **3. Medium Enterprise Scale: Azure Container Apps (ACA)**

**Fully Managed Services:**

**Google Cloud Run:** Provides the highest level of abstraction and management, completely handling infrastructure for stateless containers.
**Azure Container Apps:** Offers serverless scaling and deep integration with Azure, simplifying container management.
**GKE Autopilot:** Automates most of the Kubernetes management tasks, focusing on application deployment and scalability.
Semi-Managed Services:

**AWS Karpenter:** While it automates scaling and integrates with AWS services, it still requires some management and configuration of the Kubernetes environment.

### **Self-Managed Services:**

- **Native Kubernetes:** Provides full control and flexibility, but requires significant management effort, including setup, scaling, updates, and maintenance.

Choosing the right Kubernetes-powered platform depends on your needs for management and control. Fully managed services like Google Cloud Run, Azure Container Apps (ACA), and GKE Autopilot offer ease of use and scalability, ideal for teams focusing on application development without worrying about infrastructure. Semi-managed services like AWS Karpenter offer a balance, with some automation while allowing for more customization. Native Kubernetes provides maximum control and customization at the cost of increased management overhead. We have chossen Azure Container Apps (AKA) because it offers a perfect balance, with native Dapr support.

For More information Read the DACA design Pattern from from Panaversity: (DACA documentation link)[https://github.com/panaversity/learn-agentic-ai/blob/main/comprehensive_guide_daca.md]
