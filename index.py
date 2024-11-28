class Transaction:
    db = dict()            # data will be committed to this database
    transactions = dict()  # pending transactions are stored here before a commit
    ongoing = False        # flag for detecting an ongoing transaction

    def __init__(self):
        return

    def begin_transaction(self):
        # starts a new transaction, only 1 can occur at a time
        # put() must be called after this function
        if self.ongoing == False:
            self.ongoing = True
            print("Starting a new transaction.")
        else:
            print("Error: A transaction is already in progress.")
            # raise Exception("A transaction is already in progress.")

    def put(self, key:str, value:int):
        # throw an exception if a transaction hasn't been started
        if self.ongoing == False:
            print("Error: A transaction has not been started. Cannot add new data.")
            # raise Exception("A transaction has not been started. Cannot add new data.")
        
        # creates a new key with the provided value if it doesn't already exist
        # otherwise, update the value of an existing key
        else:
            self.transactions[key] = value

    def get(self, key:str):
        # return the value associated with the key
        if key in self.db:
            return print(self.db[key])
        
        # if the key doesn't exist, return null
        else:
            return print(None)

    def commit(self):
        if self.ongoing == False:
            print("Error: A transaction has not been started. No data to commit.")
            # raise Exception("A transaction has not been started. No data to commit.")
        
        # add values to the final dictionary
        for k,v in self.transactions.items():
            if k in self.db:
                self.db[k] = v
            else:
                self.db[k] = v

        # empty transactions cache
        self.transactions.clear()

        # end the transaction
        self.ongoing = False
        print("The transaction has been committed.")

    def rollback(self):
        # this should delete all changes made after the last commit 
        self.transactions.clear()
        print("Removed uncommitted changes.")

if __name__ == '__main__':
    t = Transaction()
    t.get("A")
    t.put("A",5)
    t.begin_transaction()
    t.put("A",5)
    t.get("A")
    t.put("A",6)
    t.commit()
    t.get("A")
    t.commit()
    t.rollback()
    t.get("B")
    t.begin_transaction()
    t.put("B",10)
    t.rollback()
    t.get("B")