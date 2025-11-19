from collections import defaultdict

from openai import AsyncOpenAI

from .config import settings

client = AsyncOpenAI(
    api_key=settings.OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1",
)


CONVERSATIONS = defaultdict(list)


async def answer_message(user_id: int, message: str) -> str | None:
    CONVERSATIONS[user_id].append({"role": "user", "content": message})

    response = await client.chat.completions.create(
        model="openai/gpt-oss-20b:free",
        messages=CONVERSATIONS[user_id],
        stream=False,
    )

    reply = response.choices[0].message.content  # type: ignore

    CONVERSATIONS[user_id].append({"role": "assistant", "content": reply})

    return reply


def clear_dialog(user_id: int) -> None:
    del CONVERSATIONS[user_id]
