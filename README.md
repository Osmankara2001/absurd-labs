# 🧪 Absurd Labs

A fun multi-agent AI application that turns three random words into a ridiculous invention.

## How It Works

Enter three unrelated words and watch three AI agents collaborate:

1. **Crazy Inventor:** Creates a ridiculous invention.
2. **Grumpy Engineer:** Criticizes the invention with humor.
3. **Greedy Investor:** Tries to market the invention.

The agents run sequentially using LangGraph and generate responses through the real OpenAI API.

## Tech Stack

- Python 3.13
- FastAPI
- LangGraph
- OpenAI API
- Docker & Docker Compose
- HTML, CSS, JavaScript

## Getting Started

### Requirements

- Docker Desktop
- An OpenAI API key

### Installation

Clone the repository and navigate to the project directory.

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

Start the application:

```bash
docker compose up --build
```

Open your browser:

http://localhost:8000

## API

**POST /invent**

Example request:

```json
{
  "words": ["potato", "slipper", "wifi"]
}
```

The API returns the invention, engineer's critique, and investor's pitch.

## Notes

- The application uses real OpenAI API calls, which may incur costs.
- AI responses are generated in Turkish.
- No database or user authentication is required.

## License

No license has been specified yet.