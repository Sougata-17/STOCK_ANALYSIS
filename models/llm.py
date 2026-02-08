from groq import Groq
from config.settings import GROQ_API_KEY, MODEL_NAME, TEMPERATURE, MAX_TOKENS

client = Groq(api_key=GROQ_API_KEY)


def call_llm(system_prompt, user_prompt, memory=None):
    """
    Call Groq LLM with optional conversation memory.
    """

    messages = [
        {"role": "system", "content": system_prompt}
    ]

    # ---- Add memory messages (if any) ----
    if memory:
        messages.extend(memory)

    # ---- Current user prompt ----
    messages.append(
        {"role": "user", "content": user_prompt}
    )

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=messages,
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS
    )

    return response.choices[0].message.content
