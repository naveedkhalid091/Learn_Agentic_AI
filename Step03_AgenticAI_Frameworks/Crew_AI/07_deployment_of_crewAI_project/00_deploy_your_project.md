## CrewAI Deployment Guide

**Summary**

This guide walks you through the three methods to deploy your CrewAI project—covering free-tier limits, prerequisites, and detailed, easy-to-follow steps. Whether you're a developer familiar with CI/CD or a non-technical user, you'll find the right deployment path here.

### 1. Prerequisites & Free-Tier Limits

**Enterprise Account Required:** Deployment services are paid. However, you can deploy one project for free and process up to 50 requests before upgrading.

**Deciding to Upgrade:** Monitor usage; once you hit the free limit or need higher throughput, purchase CrewAI services.

### 2. Deployment Methods

#### 2.1 Deploy via GitHub (CI/CD)

1. Push your project to GitHub.
2. Connect your GitHub repo in the CrewAI dashboard.
3. Enable CI/CD: every new commit triggers an automatic deploy.

```txt
**Best For: Developers who want automated, code-driven workflows.**
```

#### 2.2 Deploy using CrewAI’s Chatbot

1. Chat with the CrewAI bot and specify your requirements.
2. Provide project keys when prompted.
3. Review the generated graphical flow and agent details.
4. Confirm to deploy.

```
Best For: Non-technical users seeking a guided, no-code experience.
```

2.3 Deploy via Pre-defined Patterns

- Use built-in templates and patterns in CrewAI to scaffold and deploy common workflows quickly.

```
Best For: Rapid prototyping with standard, battle-tested flows.
```

### 3. Step-by-Step Deployment (GitHub CI/CD Example)

Follow these steps to create, configure, and deploy a sample "poem-flow" project.

1. Create Your Project

```bash
crewai create flow ProjectName
```

2. Enter Project Directory

```bash
cd ProjectName
```

3. Open in IDE

```bash
code . # or cursor .
```

4. Configure Environment

- Edit .env:

```bash
    GEMINI_API_KEY=YOUR_KEY_HERE
    MODEL=gemini/gemini-2.0-flash
```

5. (Optional) Write Code

   - Skip if using the ready-made poem-flow example.

6. Sync Dependencies

```bash
uv sync
```

- Ensures all packages match pyproject.toml & uv.lock.
- Keeps environment clean and reproducible.

7. Activate Virtual Environment

```bash
# Windows (CMD)
.venv\Scripts\activate.bat
# PowerShell
.\.venv\Scripts\Activate.ps1
```

8. Run Locally

```bash
uv run kickoff
```

- For poem-flow, add a return statement in **save_poem** to emit JSON:

```py
return {"poem": self.state.poem,
"sentence_count": self.state.sentence_count,
"author": "Your Name"}
```

9. Configure `run_crew` Command

- In your pyproject.toml under [project.scripts], add:

```py
run_crew = "project1.main:kickoff"
```

10. Push to GitHub

```bash
# Push Direclty from the IDE or use the below commands
git add .
git commit -m "Prepare for deployment"
git push origin main
```

11. Link & Deploy on CrewAI

- Log in to CrewAI dashboard.
- Connect your GitHub repo.
- Click Deploy.
- Wait for build and deployment to complete.

### 4. Post-Deployment & Testing

- **API Endpoint:** A FastAPI URL is generated, e.g.:https://your-project-id.crewai.com
- **Docs UI:** Append /docs to explore and test endpoints:

```txt
https://your-project-id.crewai.com/docs
```

- **Testing:** Use the Swagger UI to send test requests. (Testing techniques covered in next chapters.)

### 5. Tips & Best Practices

- Environment Consistency: Always run uv sync before deployment.
- Version Control: Keep code, config, and lockfiles committed.
- Isolation: Activate .venv to avoid global package conflicts.
- Monitoring: Track usage to know when to upgrade.
