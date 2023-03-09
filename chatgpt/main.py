import openai
import typer
from decouple import config

app = typer.Typer()

@app.command()
def chat():
    """
    App to use ChatGPT through your command line terminal.
    """
    openai.api_key = config("OPENAI_APIKEY")
    chat_messages = []
    retry = False
    new_chat = True
    print()
    while True:
        if not retry:
            if new_chat:
                # System role content sets the behaviour and context for the assistant, optional
                context = set_context()
                chat_messages.append({"role": "system", "content": context})
                new_chat = False
            message = set_message()
            if message.lower() == "new":
                print("A new conversation has begun.")
                new_chat = True
                continue
            chat_messages.append({"role": "user", "content": message})
        try:
            chat = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo",
                messages = chat_messages
            )
            answer = chat["choices"][0]["message"]["content"]
            print(answer + "\n")
            chat_messages.append({"role": "assistant", "content": answer})
            retry = False
        except Exception as ex:
            print("Something happened with OpenAI API connection.")
            print(ex)
            if typer.confirm("Try again with same message?"):
                print()
                retry = True
            print()
                
def set_context() -> str:
    context = typer.prompt("Set context for ChatGPT or press the spacebar to skip")
    print()
    if context.lower() == "exit":
        confirm_exit()
        return set_context()
    if context.lower() == " ":
        print("No context set for this conversation.\n")
    return context

def set_message() -> str:
    message = typer.prompt("Me")
    print()
    if message.lower() == "exit":
        confirm_exit()
        return set_message()
    return message

def confirm_exit():
    if typer.confirm("Are you sure?"):
        print()
        raise typer.Exit()