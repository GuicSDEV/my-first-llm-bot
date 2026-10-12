from dotenv import load_dotenv
import anthropic

load_dotenv()                     
client = anthropic.Anthropic()    

save_chat = []

while True:
    user_input = input("Digite os inputs: ")
    if user_input.lower() == "sair":
        break
    save_chat.append({"role": "user", "content": user_input})
    
    response = client.messages.create(
            model="claude-haiku-5-5",
            max_tokens=2000,
            messages=save_chat
        )
    think = ""
    for block in response.content:
        if block.type == "thinking":
            think = block.thinking
        elif block.type == "text":
                    reply = block.text
        
        
            
    
    print("RESPOSTA: ",reply)
    save_chat.append({"role": "assistant", "content": reply})
    #print("Contexto: ",save_chat )
    
