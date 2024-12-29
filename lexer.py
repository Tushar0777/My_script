from tokens import Integer,Float,Operation,Declaration,Variable,Boolean,Comparison,Reserved

class Lexer:
    digits="0123456789"
    operations="+-/*()="
    stopword=[" "]
    letters="abcdefghijklmnopqrstuvwxyz"
    declarations=["make"]
    boolean=["and","or","not"]
    comparisons=[">","<",">=","<=","?="]
    specialCharacters="><=?"
    reserved=["if","else","do","elif","while"]


    def __init__(self, text):
        self.text=text
        self.idx=0
        self.tokens=[]
        self.char=self.text[self.idx]
        self.token=0

    def tokenize(self):
        while self.idx<len(self.text):
           # print(self.idx)
           # self.idx+=
           if self.char in Lexer.digits:
               self.token=self.extract_num()
         

           elif self.char in Lexer.operations:
               self.token=Operation(self.char)
               self.move()
           elif self.char in Lexer.stopword:
               self.move()
               continue
           

           elif self.char in Lexer.letters:
               word=self.extract_word()

               if word in Lexer.declarations:
                   self.token=Declaration(word)
               elif word in Lexer.boolean:
                   self.token=Boolean(word)
               elif word in Lexer.reserved:
                   self.token=Reserved(word)

               else:
                   self.token=Variable(word)
            
           elif self.char in Lexer.specialCharacters:
               comparisonOperator=""
               while self.char in Lexer.specialCharacters and self.idx<len(self.text):
                   comparisonOperator+=self.char
                   self.move()

               self.token=Comparison(comparisonOperator)
                   

           self.tokens.append(self.token)

        return self.tokens

    def extract_num(self):
        number=""
        isFloat=False
        while(self.char in Lexer.digits or self.char==".") and (self.idx<len(self.text)):
            if self.char==".":
                isFloat=True
            
            number+=self.char
            self.move()

        return Integer(number) if not isFloat else Float(number)
    
    def extract_word(self):
        word=""
        while self.char in Lexer.letters and self.idx <len(self.text):
            word+=self.char
            self.move()

        return word
        



    def move(self):
        self.idx+=1
        if(self.idx<len(self.text)):
            self.char=self.text[self.idx]




# class Token:
#     def __init__(self,type,value):
#         self.type=type
#         self.value=value

#     def __repr__(self):
#         return str(self.value)

# class Integer(Token):
#     def __init__(self,value):
#         super().__init__("INT",value)

# class Float(Token):
#     def __init__(self,value):
#         super().__init__("FLT",value)
    
# class string(Token):
#     pass

# class Operation(Token):
#     def __init__(self,value):
#         super().__init__("OPERATION",value)

# class Declaration(Token):
#     def __init__(self,value):
#         super().__init__("DECL",value)

# class Variable(Token):
#     def __init__(self,value):
#         super().__init__("VAR",value)