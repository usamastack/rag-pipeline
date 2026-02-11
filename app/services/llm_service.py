from openai import OpenAI
from app.core.config import get_settings

settings = get_settings()

class LLMService:
    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)

    def generate_answer(self, query: str, context: list[str], model: str = "gpt-4-turbo-preview") -> str:
        # Construct prompt
        context_str = "\n\n".join(context)
        system_prompt = """You are a helpful AI assistant. Use the following pieces of context to answer the user's question.
If you don't know the answer, just say that you don't know, don't try to make up an answer.
Keep the answer concise and clean."""
        
        user_prompt = f"Context:\n{context_str}\n\nQuestion: {query}"

        # Call OpenAI
        response = self.client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.1
        )
        
        return response.choices[0].message.content

    async def generate_answer_with_provider(self, provider: str, query: str, context: list[str]) -> dict:
        context_str = "\n\n".join(context)
        system_prompt = f"You are a helpful AI assistant powered by {provider}. Use the provided context to answer the question."
        user_prompt = f"Context:\n{context_str}\n\nQuestion: {query}"
        
        start_time = __import__("time").time()
        
        # Mock implementation for other providers if keys not available
        # In a real scenario, use respective SDKs (anthropic, google-generativeai, etc.)
        if provider.lower() == "openai" or provider.lower().startswith("gpt"):
             response = self.client.chat.completions.create(
                model="gpt-4-turbo-preview" if "4" in provider else "gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ]
            )
             content = response.choices[0].message.content
             usage = response.usage.total_tokens
        else:
            # Placeholder for others
            content = f"[{provider} (Mocked)] Based on the context, here is the answer..."
            usage = 0
            
        end_time = __import__("time").time()
        
        return {
            "provider": provider,
            "answer": content,
            "latency": round(end_time - start_time, 2),
            "tokens": usage
        }

llm_service = LLMService()
