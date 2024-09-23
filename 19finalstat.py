#finaly sttement in raise exception
def process_file():
    try:
        f=open("C:\\Users\\USER\\Downloads\\Desktop\\ML\\python\\1lesson(codebasics)\\13funnt.txt")
           
    except FileNotFoundError as e:
        print("exception occured")
    except ZeroDivisionError as e:
        print("exception occured")
    finally:
        print("finally block is executed")
        f.close()



#ask gpt its not working ok mark this also














