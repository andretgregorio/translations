class Value:
    def __init__(self, text, fallback_text):
        self.main = normalize_string(text)
        self.fallback = normalize_string(fallback_text)
    
    def get(self):
        if str(self.main) != 'nan' and self.main != None:
            return self.main
        else:
            return self.fallback


def normalize_string(text):
    return text.strip().replace("'", "''")