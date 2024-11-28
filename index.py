class Transaction:
    db = dict()
    transactions = dict()
    ongoing = False

    def __init__(self):
        print("A new object has been initialized.")

    def begin_transaction(self):
        # starts a new transaction, only 1 can occur at a time
        # put() must be called after this function
        if self.ongoing == False:
            self.ongoing = True
            print("Starting a new transaction.")
        else:
            raise Exception("A transaction is already in progress.")

    def put(self, key:str, value:int):
        # throw an exception if a transaction hasn't been started
        if self.ongoing == False:
            raise Exception("A transaction has not been started. Cannot add new data.")
        
        # creates a new key with the provided value if it doesn't already exist
        # otherwise, update the value of an existing key
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
            raise Exception("A transaction has not been started. No data to commit.")
        
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
    t1 = Transaction()
    t1.get("A")
    # print(t1.put("A",5))
    t1.begin_transaction()
    t1.put("A",5)
    print(t1.get("A"))
    t1.put("A",6)
    t1.commit()
    t1.get("A")
    # t1.commit()
    t1.get("B")
    t1.begin_transaction()
    t1.put("B",10)
    t1.rollback()
    t1.get("B")