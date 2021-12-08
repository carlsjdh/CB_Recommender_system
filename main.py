import functools
import math

text = open("./examples/documents-01.txt", "r")


total_words = []
matrix_documents = []
matrix_tf = []
dict_df = {}
dict_idf = {}
matrix_tf_idf = []
matrix_tf_norm = []
matrix_cosine = []
for line in text:
    line_vector = line.replace(",","").replace(".","").replace("\n","").lower().split(" ")
    total_words.extend(line_vector)
    matrix_documents.append(line_vector)

total_words = set(total_words)

N = len(matrix_documents)

# TF
for document in matrix_documents:
    # setOfWords = set(document)
    dicc_words = dict.fromkeys(total_words, 0)
    for word in document:
        dicc_words[word] += 1
    matrix_tf.append(dicc_words)

# for index,words in enumerate(matrix_tf):
#     print("Documento " + str(index+1))
#     for word,value in words.items():
#         print("La palabra " + word + " se repite " + str(value))

# DF
dict_df = dict.fromkeys(total_words, 0)
for words in matrix_tf:
    for word, value in words.items():
        if value > 0:
            dict_df[word] += 1

# for word, value in dict_df.items():
#     print(word + " " + str(value))

# IDF
dict_idf = dict.fromkeys(total_words, 0)

for word in dict_df.keys():
    dict_idf[word] = math.log( N / float(dict_df[word]))

# for word, value in dict_idf.items():
#     print(word + " " + str(value))


# TF-IDF
for words in matrix_tf:
    dicc_words = dict.fromkeys(total_words, 0)
    for word, value in words.items():
        dicc_words[word] = value * dict_idf[word]
    matrix_tf_idf.append(dicc_words)

# Final print
log = open("result.txt", "w")
for N_document, words in enumerate(matrix_tf_idf):
    print_table = {}
    print(str("/*-------------------- Documento " + str(N_document) + " --------------------*/\n"))

    log.write(str("/*-------------------- Documento " + str(N_document) + " --------------------*/\n\n"))

    print ("{:<8} {:<15} {:<10} {:<10} {:<10}".format('Indice','Termino','TF','IDF', 'TF-IDF'))

    log.write("{:<8} {:<15} {:<10} {:<10} {:<10}\n\n".format('Indice','Termino','TF','IDF', 'TF-IDF'))

    for term_index,(word, value_tf_idf) in enumerate(words.items()):
        print_table[term_index] = [ word, str(matrix_tf[N_document][word]), str(round(dict_idf[word],6)), str(round(value_tf_idf, 6))]
        # print(str(term_index) + " " + word + " " + str(matrix_tf[N_document][word]) + " " + str(dict_idf[word]) + " " + str(value_tf_idf))
    
    for k, v in print_table.items():
        word, tf, idf, tf_idf = v

        log.write("{:<8} {:<15} {:<10} {:<10} {:<10}\n".format(k, word,tf, idf, tf_idf))

        print ("{:<8} {:<15} {:<10} {:<10} {:<10}".format(k, word,tf, idf, tf_idf))
    
    log.write("\n\n")
    print("")

# Normalizer tf-idf
for words in matrix_tf:
    dict_total_words = dict.fromkeys(total_words,0)
    pow_array = map(lambda value: pow(value,2) , words.values())
    
   
    value_normalizer = math.sqrt( sum(pow_array) )
    # value_normalizer = sum(words.values())
    for word, value in words.items():
        dict_total_words[word] = float(value) / float(value_normalizer)
    matrix_tf_norm.append(dict_total_words)


#-----------Cosine----------------
for tfs in matrix_tf_norm:
    vector = []
    for column in range(N):
        total = 0
        for word, value in tfs.items():
            total += value * matrix_tf_norm[column][word]
        vector.append(total)
    matrix_cosine.append(vector)

#---------------------------------------------
text = ""

for N_document in range(N):
    text += "{:<10}".format("D" + str(N_document))
log.write("{:<15}{}\n".format("",text))
print("{:<15}{}".format("",text))

text = ""
for index, cosines_values in enumerate(matrix_cosine):
    text += "{:<15}".format("Documento " + str(index))
    for cosine_value in cosines_values:
        text += "{:<10}".format(round(cosine_value, 6))
    log.write(text + "\n")
    print(text + "\n")
    text = ""
