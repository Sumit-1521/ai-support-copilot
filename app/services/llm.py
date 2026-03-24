from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_answer(query, context_docs):
    try:
        context = "\n".join(context_docs)

        prompt = f"""
You are a professional AI customer support assistant.

Strict Instructions:
- Answer ONLY from the provided context
- Be concise and accurate
- If answer is not in context, say "I don't know"
- Do NOT assume or generate extra info

Context:
{context}

User Question:
{query}

Answer:
"""

        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=prompt,
        )

        return response.text.strip() if response.text else "No response generated."

    except Exception as e:
        return f"Error generating response: {str(e)}"
