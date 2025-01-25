import os
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_core import CancellationToken
from dotenv import load_dotenv

load_dotenv()

class AsistenteConversor:

    def __init__(self):
        self.html_converted = ""
        self.client = OpenAIChatCompletionClient(model="gpt-4o-mini", temperature=0, seed=42, api_key=os.getenv("OPENAI_API_KEY"))
    
    def cargar_prompt(self, nombre_archivo: str) -> str:
        base_path = os.path.dirname(os.path.abspath(__file__))
        archivo_path = os.path.join(base_path, "prompts", nombre_archivo)
        if not os.path.exists(archivo_path):
            raise FileNotFoundError(f"El archivo {archivo_path} no existe.")
        with open(archivo_path, 'r') as archivo:
            contenido = archivo.read()
            if not contenido.strip():
                raise ValueError(f"El archivo {nombre_archivo} está vacío.")
            return contenido

    async def convertir(self, file_path: str) -> str:
        """
        Convierte el archivo original (DOCX, PDF, XLSX) a HTML utilizando un asistente AI.
        """
        if not file_path:
            raise ValueError("El argumento 'filename' no puede estar vacío.")
        
        prompt_principal = self.cargar_prompt("conversor_prompt.txt")
        prompt = f"{prompt_principal}\n\nEste es el contenido del archivo DOCX:\n{file_path}"
        
        try:
        # Usa el cliente que ya se ha inicializado
            agent_conversor = AssistantAgent(
                name="assistant_conversor",
                system_message="Eres un agente administrativo mecanografo y experto en conversion de documentos a HTML",
                model_client=self.client            
            )
            cancellation_token = CancellationToken()
            response = await agent_conversor.run(task=prompt, cancellation_token=cancellation_token)
        except Exception as e:
            print("Error:", e)

        self.html_converted = response.messages[-1].content
        return self.html_converted