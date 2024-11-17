from openai import OpenAI
from django.conf import settings

EMBEDDING_MODEL = "text-embedding-ada-002"

openai_client = OpenAI(
    api_key=settings.OPENAI_API_KEY,  # this is also the default, it can be omitted
)


def get_embedding(text: str):
    text = text.replace("\n", " ")
    return (
        openai_client.embeddings.create(
            input=[text],
            model=EMBEDDING_MODEL,
        )
        .data[0]
        .embedding
    )

    # print(response)
    # return response.data[0]["embedding"]
