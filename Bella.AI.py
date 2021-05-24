print("Welcome to BELLA.AI  - Flamestopian AI Program")
 # WELCOME MESSAGE
print("Welcome")  #  PRINTS WELCOME 
ID = input("Please input your ID") # ID MESSAGE
print("BELLA.AI Checking HAP-GEN 1.0")
try:
    from happytransformer import HappyGeneration
except:
    print("Import Error. Please 'pip install happytransformer' and try again.")
    input("> ")
print("SCANNING..PLEASE ENTER TEXT TO GENERATOR.BELLA_AI BUILD 52021") # CHECKS GEN
happy_gen = HappyGeneration("GPT-NEO", "EleutherAI/gpt-neo-1.3B") # GETS AI
# Checks generator
result = happy_gen.generate_text("Artificial intelligence program. Connnecting memory cores ")
print(result)
print(result.text) # PRINTS RESULT
print("BELLA: THANK YOU FOR USING BELLA.AI 1.0")