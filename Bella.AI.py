print("Welcome to BELLA.AI  - Flamestopian AI Program")
 # WELCOME MESSAGE
print("Welcome")  #  PRINTS WELCOME 
text = input("Enter text >")
print("BELLA.AI Checking HAP-GEN 1.0")
try:
    from happytransformer import HappyGeneration
except:
    print("Import Error. Please 'pip install happytransformer' and try again.")
    input("> ")
print("CHECKING AI") # CHECKS GEN
happy_gen = HappyGeneration("GPT-NEO", "EleutherAI/gpt-neo-1.3B") # GETS AI
# Checks generator
result = happy_gen.generate_text(text)
print(result)
print(result.text) # PRINTS RESULT
print("BELLA: THANK YOU FOR USING BELLA.AI 1.0")