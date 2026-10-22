from dotenv import load_dotenv
import anthropic

load_dotenv()                     


class ChatBot:
        def __init__(self,system:str,client:object,model:str ="claude-haiku-5-5"):
            
            self.save_chat: list[dict[str,str]] = []
            self.model = model
            self.system = system
            self.client = client
        def enviar(self, message:str) -> str:
            self.save_chat.append({"role":"user","content":message})
            answer = self.client.messages.create(model=self.model,system = self.system ,max_tokens = 2000,messages = self.save_chat)
            reply = ""
            for block in answer.content:
                  if block.type == "text":  
                    reply += block.text
            self.save_chat.append({"role":"assistant","content":reply})
            return reply


client = anthropic.Anthropic()  
bot = ChatBot("Você é um tutor, paciente que responde em português",client)
while True:
     user_input = input("Digite os inputs: ")
     if user_input.lower() == "sair":
             break
     reply = bot.enviar(user_input)
     print(reply)
     
