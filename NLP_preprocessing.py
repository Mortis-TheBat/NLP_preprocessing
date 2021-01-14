import spacy
from PIL import Image
import en_core_web_sm
#import Image
from pytesseract import image_to_string


img = Image.open("/home/nani/Desktop/Projects/pancard.png")
#print(img)
my_text = image_to_string(img)

#import pytesseract
#python -m spacy download en_core_web_md  <- Download "en" using this

nlp = en_core_web_sm.load()
#Assuming we have extrated text from images
#my_text = "Some random super big text or paragraph i have no idea about. But anyway I found it on the internet."

my_doc = nlp(my_text)

#Type check
type(my_doc)


print('Before PreProcessing n_Tokens: ', len(my_doc))

#Printing the tokens
#for token in my_doc:
#	print(token.text)
	
my_doc_cleaned = [token for token in my_doc if not token.is_stop and not token.is_punct]

print('After PreProcessing n_Tokens: ', len(my_doc_cleaned))

print(my_doc_cleaned)

