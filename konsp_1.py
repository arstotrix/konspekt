i=0
def get_text(filename):
    with open (filename, encoding='utf-8')as file_object:
        text = file_object.read()
        return text
def tokenize(text):
    words = text.split()
    return words
def get_constr(words):
    constr_list = []
    for i, token in enumerate(words):
        splitted = token.split('_')
        #if len(splitted) == 2:
        #    word = splitted[0]
        #    pos = splitted[1]
        word, pos = '_'.join(splitted[:-1], splitted[:-1])
        if pos == 'A':
            next_word = words[i+1]
            if next_word.endswith('_S'):
                constr_list.append(word + ' ' + next_word[:-2])
            

    return constr_list
def get_text(constr, fname):
    with open (fname, w) as f:
        f.writelines(constr_list)
        #for constr in constr_list:
        #   f.write(constr + '\n')

def main():
    #pipeline
    raw_text = get_text("sample_tagged_text.txt")
    print(raw_text[:100])
    tokens = tokenize(raw_text)
    print(tokens[:20])
    get_constr(tokens)
    for entry in constr_list:
        print(entry)
        write_results (constr_list, 'constr.txt')

