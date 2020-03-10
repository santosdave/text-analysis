print('My simple text analysis software\n')
txt = user_input("")


def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count

   
def text_analysis():
         
        txt=txt   
        lines = 0
        letters = 0
        Spaces = 0

            for line in open(txt):
                lines += 1
                Spaces += len(line)
                for letter in line:
                    if letter != ' ' and letter != '\n':
                        letters += 1

            print("Lines:" , lines)
            print("Letters:" , letters)
            print("Spaces:" , ((Spaces - letters) - lines) + 1)
            print("Words:" , ((Spaces - letters) + 1))

            
            c = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()_+,./|\?:/<>{}[]"
            for char in c:
                with open(txt) as f:
                    text = f.read()
                #perc = 100 * count_char(txt, char) / len(txt)
                #print("{0} - {1}%".format(char, round(perc, 3)))
                n = count_char(text, char)
                if char in text:
                    print("{0} - {1}".format(char, n))
                else:('')    
        except:
            print('Make sure that the file and its extension are correct!')
text_analysis()            
