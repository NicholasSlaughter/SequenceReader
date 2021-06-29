
class DictionaryHelper(object):
    """description of class"""
    def Add_To_Dictionary(seq,seq_dict):
        if seq not in seq_dict:
            seq_dict[seq]=0
        seq_dict[seq]+=1
        return seq_dict[seq]

