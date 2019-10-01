class Query(object):
    def __init__(self, key, feature, value, locale):
        self.key = key
        self.feature = feature
        self.value = value
        self.locale = locale
    
    def write(self, transaction_type):
        if transaction_type.lower() == 'insert':
            return self.insert_query()
        elif transaction_type.lower() == 'update':
            return self.update_query()
            
    
    def update_query(self):
        return f"""UPDATE translations SET `value`='{self.value}' WHERE `key`='{self.key}' and `locale`='{self.locale}' and feature='{self.feature}';"""
    
    def insert_query(self):
        return f"""INSERT INTO translations (`key`, 'feature', `value`, 'locale') values('{self.key}', '{self.feature}', '{self.value}', '{self.locale}');"""