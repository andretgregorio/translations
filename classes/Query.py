class Query(object):
    def __init__(self, translation):
        self.key = translation.key
        self.feature = translation.feature
        self.value = translation.value
        self.locale = translation.locale
        self.translation_status = translation.translation_status
    
    def write(self, transaction_type):
        if transaction_type.lower() == 'insert':
            return self.insert_query()
        elif transaction_type.lower() == 'update_value':
            return self.update_value_query()
        elif transaction_type.lower() == 'update_translation_status':
            return self.update_translation_status_query()
        else:
            raise ValueError(f'Invalid argument for --query param. Argument found: "{transaction_type}". Accepted arguments are: "insert", "update_value" and "update_translation_status"')
            
    
    def update_translation_status_query(self):
        return f"""UPDATE translations SET `translation_status`= {self.translation_status} WHERE `value`='{self.value}' and `key`='{self.key}' and `locale`='{self.locale}' and feature='{self.feature}';"""
    
    def update_value_query(self):
        return f"""UPDATE translations SET `value`='{self.value}' WHERE `key`='{self.key}' and `locale`='{self.locale}' and feature='{self.feature}';"""

    def insert_query(self):
        return f"""INSERT INTO translations (`key`, `feature`, `value`, `locale`, `translation_status`) VALUES ('{self.key}', '{self.feature}', '{self.value}', '{self.locale}', {self.translation_status});"""