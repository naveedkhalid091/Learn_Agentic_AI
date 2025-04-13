## Testing Your Deployed CrewAI Project via FastAPI’s Auto‑Generated Docs:

Follow these simple steps to explore and test your CrewAI deployment’s API endpoints:

### 1. Open the FastAPI Docs:

- Log in to your CrewAI account and copy your deployment’s base URL.
- In your browser, paste the URL and append /docs (e.g. https://your‑deployment-url/docs).

### 2. Understand the Interface:

- **Authorize Button:** Located at the top right. You need this to unlock protected endpoints.
- **Lock Icons:**
  - 🔒 indicates an endpoint requires authorization (e.g. /kickoff, /inputs, /status).
  - No lock means it’s publicly accessible (e.g. /healthcheck).

### 3. Healthcheck Endpoint

- Find the /healthcheck section (no lock icon).
- Click “Try it out”, then “Execute”.
- You’ll see the current status of your deployment.

### 4. Authorize to Test Protected Endpoints:

- Click “Authorize” button.
- In the modal, paste your Bearer token (available next to your deployment URL in CrewAI).
- Click “Authorize”, then “Close”.
- Now all 🔒 endpoints are unlocked.

### 5. Testing `/kickoff, /inputs, /status,` etc.

- Navigate to the endpoint you want to test (e.g. /kickoff).
- Click “Try it out”, fill in any required fields, then “Execute”.
- For /status, you’ll need the kickoff_id returned by your /kickoff call.

### 6. Next Steps & Integration:

- You can integrate these APIs into your own interfaces using frameworks like:

  - **Next.js** (React)
  - **Streamlit**
  - **Chainlit**

- Build a custom frontend or dashboard to call these endpoints programmatically.

That’s it! You’re now ready to explore and test every part of your CrewAI deployment via FastAPI’s docs.
