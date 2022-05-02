import hashlib
import datetime

class Block:
    """
    A class used to create a block

    Parameters
    ----------
    data: A string representing data in the blockl
    """
    def __init__(self, data):
        self.timestamp = self.get_timestamp()
        self.data = data
        self.hash = self.calc_hash()
        self.previous_hash = None
        self.next = None

    def calc_hash(self):
        """
        Calculates the hash code associated with a block

        Returns
        -------
        str
            A SHA-2 string
        """
        sha = hashlib.sha256()

        hash_str = self.data + self.timestamp
        hash_str = hash_str.encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()

    def get_timestamp(self):
        """
        Returns the time a block was created
        """
        return datetime.datetime.now(datetime.timezone.utc).strftime("%H:%M %d-%m-%Y")


class Blockchain():
    """
    A class for building a blockchain
    """
    def __init__(self):
        self.head = None

    def add_block(self, data):
        """
        Adds a block to the chain

        Params:
            data: a string
        """
        if data is not str:
            data = str(data)

        if self.head is None:
            self.head = Block(data)
            self.head.previous_hash = '0'
            return

        node = self.head

        # iterate to the end of the LL
        while node.next:
            node = node.next

        # set the next node to the new block
        node.next = Block(data)
        node.next.previous_hash = node.hash
     
    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.data) + " -> "
            cur_head = cur_head.next
        return out_string


blockchain = Blockchain()

blockchain.add_block('a')
blockchain.add_block('b')
blockchain.add_block('9')
blockchain.add_block('d')
blockchain.add_block(None)
blockchain.add_block(30000)

print(blockchain)

