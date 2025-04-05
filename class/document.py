class Document:
    def __init__(self, text):
        self.original_text = text
        self.text = text
        self.words = text.split()

    def __len__(self):
        return len(self.words)
    
    def __contains__(self, word):
        return word in self.words
    
    def add_word(self, word):
        self.words.append(word)
        self.text = " ".join(self.words)

    def remove_word(self, word):
        if word in self.words:
            self.words.remove(word)
            self.text = " ".join(self.words)

    def replace_word(self, old_word, new_word):
        self.words = [new_word if w == old_word else w for w in self.words]
        self.text = " ".join(self.words)

    def reset_text(self):
        self.text = self.original_text
        self.words = self.original_text.split()
    
doc = Document("Hello world this is a new test Are you good")
print(len(doc))
print("test" in doc)
doc.add_word("Dear")
doc.remove_word("new")
print(doc.text)
doc.replace_word("good", "great")
print(doc.text)
doc.reset_text()
print(doc.text)
