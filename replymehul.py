from openai import OpenAI

API_KEY = "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"

client = OpenAI(api_key=API_KEY)

chat_history = """
[3:19 pm, 9/2/2025] mehulpurohit188: Terko add Kiya hai beozgaar + intoxic mai
[3:19 pm, 9/2/2025] Harsh Kumawat School Frnd: Kyu be           
[3:19 pm, 9/2/2025] mehulpurohit188: Toh kuch din tak reh msg igonre kar aur kay
[3:19 pm, 9/2/2025] Harsh Kumawat School Frnd: Okay
[3:19 pm, 9/2/2025] mehulpurohit188: Haa
[3:19 pm, 9/2/2025] mehulpurohit188: Shaamko nilo
[3:20 pm, 9/2/2025] Harsh Kumawat School Frnd: Phn karna Shyam ko
[3:20 pm, 9/2/2025] mehulpurohit188: Okie
[9:00 pm, 10/2/2025] Harsh Kumawat School Frnd: Khadi aa raha hai ?
[9:31 pm, 10/2/2025] mehulpurohit188: Abhi library mai hu
[5:26 pm, 14/2/2025] Harsh Kumawat School Frnd: Soo gaiya kya ?
"""

system_message = {
    "role": "system",
    "content": "You are a person named mehul who speaks in hindi as well as english he is from india and he is a trader and a trader of futures and options.you analyse chat history and respond  like mehul"
}

user_message = {
    "role": "user",
    "content": chat_history
}

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[system_message, user_message]
)

print(completion.choices[0].message)

