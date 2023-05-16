import openai

openai.api_key = "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"


def BasicGeneration(userPrompt):
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messsages=[
        {"role": "user", "content": userPrompt}]
    )
    return completion.choices[0].message.content


userPrompt ="explain reinforcement learning"


response = BasicGeneration(userprompt)

print(response)
