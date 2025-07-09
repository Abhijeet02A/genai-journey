#Python basics

ai_tools = ['chatgpt', 'bard', 'claude', 'gemini']
for tool in ai_tools:
    print(tool, "**")

post = {
    "post_id": "12345",
    "title": "Exploring AI Tools",
    "content": "This post discusses various AI tools available today.",
}

for key, value in post.items():
    print(f"{key}: {value}")


def welcome_user(name):
    print(f"Welcome, {name}!", "Enjoy your journey!") #Printing with formulated string

welcome_user("Abhijit") #Calling the function with a name