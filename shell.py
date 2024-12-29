from lexer import Lexer
from parser import Parser
from interpreter import Interpreter
from data import Data

base=Data()

while(True):
    text=input("DarloScript: ")
    tokenizer=Lexer(text)
    tokens=tokenizer.tokenize()
    print(tokens)
    parser=Parser(tokens)
    tree=parser.parse()
    print(tree)

    interpreter=Interpreter(tree,base)
    result=interpreter.interpret()
    print(result)

    #lexer->parser->interpreter




    