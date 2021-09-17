from happytransformer import HappyGeneration

happy_gen = HappyGeneration("microsoft", "codebert")


result = happy_gen.generate_text("Artificial intelligence will ")
print(result)
print(result.text)
from happytransformer import GENSettings

args = GENSettings(no_repeat_ngram_size=2)
print("Hello! My name is bella tell  me what to do <3 ")  
result = happy_gen.generate_text(input)
print(result)
print(result.text)