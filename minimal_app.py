import chainlit as cl

@cl.on_chat_start
async def start():
    await cl.Message(content="Upload a file!").send()

@cl.on_message
async def handle_message(message: cl.Message):
    files = message.elements
    if files:
        for file in files:
            if file.content:
                await cl.Message(content=f"Received file: {file.name}, size: {len(file.content)} bytes").send()
            else:
                await cl.Message(content=f"Received file: {file.name}, but content is missing!").send()
    else:
        await cl.Message(content="No file uploaded.").send()