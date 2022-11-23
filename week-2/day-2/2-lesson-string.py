text = "My name is Umidjon"

print(text)
print(text[:2])
print(text[3:7])
print(text[8:10])
print(text[11:])
print("-"*100)

print(text[-7:])
print("-"*100)


text_len = len(text)
print(text_len)
print("-"*100)

text = text.upper()
print(text)
print("-"*100)

text = text.lower()
print(text)
print("-"*100)

text = text.title()
print(text)
print("-"*100)

text = text.replace("Umidjon", "Odiljon")
print(text)
print("-"*100)
