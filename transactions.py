from classes.main import Main
import sys

args = sys.argv
if len(args)==2:
    try:
        f = open(args[1],'r')
        content = f.read()
        content_list = content.splitlines()
        m = Main()
        m.check_ops(content_list)
        m.print_lines()
    except FileNotFoundError:
        print("ERRO: Arquivo não encontrado")
    except:
        raise
elif len(args) == 1:
    m = Main()
    while True:
        s = input()
        if s == "exit":
            break
        elif s == "print":
            m.print_lines()
        else:
            m.check_lines(s)
    m.print_lines()
else:
    print("ERRO: Este script roda com nenhum ou apenas um parâmetro (O arquivo com as operações)")