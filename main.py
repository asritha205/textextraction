import easyocr
import pandas as pd
reader = easyocr.Reader(['en'], gpu = True)
results = reader.readtext('/workspace/textextraction/movieposter.jpeg')

df=pd.DataFrame(results, columns=['bbox','text','conf'])
l=len(df)
s=""
for i in range(l):
  s=s+df['text'][i]+" "
print(s)

from googletrans import Translator

translator = Translator()

translated_text = translator.translate(s, dest='ko')
print(translated_text.text)