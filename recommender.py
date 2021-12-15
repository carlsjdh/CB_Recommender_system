import math

class Recommender_CB:
    def __init__(self, text):
        # Attributes
        self.total_words = []
        self.matrix_documents = []
        self.matrix_tf = []
        self.dict_df = {}
        self.dict_idf = {}
        self.matrix_tf_idf = []
        self.matrix_tf_norm = []
        self.matrix_cosine = []

        # Divide text by words
        for line in text:
            line_vector = line.replace(",","").replace(".","").replace("\n","").lower().split(" ")
            self.total_words.extend(line_vector)
            self.matrix_documents.append(line_vector)
        
        # Delete duplicate words
        self.total_words = set(self.total_words)

        # Numbers of docs
        self.N = len(self.matrix_documents)

        # # TF-total
        # for document in self.matrix_documents:
        #     dicc_words = dict.fromkeys(self.total_words, 0)
        #     for word in document:
        #         dicc_words[word] += 1
        #     self.matrix_tf.append(dicc_words)
            
        # TF
        for document in self.matrix_documents:
            dicc_words = dict.fromkeys(set(document), 0)
            for word in document:
                dicc_words[word] += 1
            self.matrix_tf.append(dicc_words)

        # DF
        self.dict_df = dict.fromkeys(self.total_words, 0)
        for words in self.matrix_tf:
            for word, value in words.items():
                if value > 0:
                    self.dict_df[word] += 1

        # IDF
        self.dict_idf = dict.fromkeys(self.total_words, 0)

        for word in self.dict_df.keys():
            self.dict_idf[word] = math.log( self.N / float(self.dict_df[word]))

        # TF-IDF
        for words in self.matrix_tf:
            dicc_words = dict.fromkeys(set(words), 0)
            for word, value in words.items():
                dicc_words[word] = value * self.dict_idf[word]
            self.matrix_tf_idf.append(dicc_words)

        # Normalizer tf-idf
        for words in self.matrix_tf:
            dict_words = dict.fromkeys(words,0)
            pow_array = map(lambda value: pow(value,2) , words.values())
            value_normalizer = math.sqrt( sum(pow_array) )
            for word, value in words.items():
                dict_words[word] = float(value) / float(value_normalizer)
            self.matrix_tf_norm.append(dict_words)

        # Cosine between documents
        for tfs in self.matrix_tf_norm:
            vector = []
            for column in range(self.N):
                total = 0
                for word, value in tfs.items():
                    if self.matrix_tf_norm[column].has_key(word):
                        total += value * self.matrix_tf_norm[column][word]
                vector.append(total)
            self.matrix_cosine.append(vector)

    def print_table(self):
        for N_document, words in enumerate(self.matrix_tf_idf):
            print_table = {}
            print(str("/*-------------------- Documento " + str(N_document) + " --------------------*/\n"))

            print ("{:<8} {:<15} {:<10} {:<10} {:<10}".format('Indice','Termino','TF','IDF', 'TF-IDF'))

            for term_index,(word, value_tf_idf) in enumerate(words.items()):
                print_table[term_index] = [ word, str(self.matrix_tf[N_document][word]), str(round(self.dict_idf[word],6)), str(round(value_tf_idf, 6))]
                # print(str(term_index) + " " + word + " " + str(matrix_tf[N_document][word]) + " " + str(dict_idf[word]) + " " + str(value_tf_idf))
            
            for k, v in print_table.items():
                word, tf, idf, tf_idf = v

                print ("{:<8} {:<15} {:<10} {:<10} {:<10}".format(k, word,tf, idf, tf_idf))

            print("")

    def write_table(self, file):
        log = open(file, "w")
        for N_document, words in enumerate(self.matrix_tf_idf):
            print_table = {}

            log.write(str("/*-------------------- Documento " + str(N_document) + " --------------------*/\n\n"))

            log.write("{:<8} {:<15} {:<10} {:<10} {:<10}\n\n".format('Indice','Termino','TF','IDF', 'TF-IDF'))

            for term_index,(word, value_tf_idf) in enumerate(words.items()):
                print_table[term_index] = [ word, str(self.matrix_tf[N_document][word]), str(round(self.dict_idf[word],6)), str(round(value_tf_idf, 6))]
            
            for k, v in print_table.items():
                word, tf, idf, tf_idf = v

                log.write("{:<8} {:<15} {:<10} {:<10} {:<10}\n".format(k, word,tf, idf, tf_idf))

            log.write("\n\n")

    def print_cosine(self):
        text = ""
        for N_document in range(self.N):
            text += "{:<10}".format("D" + str(N_document))
        print("{:<15}{}".format("",text))

        text = ""
        for index, cosines_values in enumerate(self.matrix_cosine):
            text += "{:<15}".format("Documento " + str(index))
            for cosine_value in cosines_values:
                text += "{:<10}".format(round(cosine_value, 6))
            print(text + "\n")
            text = ""

    def write_cosine(self, file):
        log = open(file, "w")
        text = ""

        for N_document in range(self.N):
            text += "{:<10}".format("D" + str(N_document))
        log.write("{:<15}{}\n".format("",text))

        text = ""
        for index, cosines_values in enumerate(self.matrix_cosine):
            text += "{:<15}".format("Documento " + str(index))
            for cosine_value in cosines_values:
                text += "{:<10}".format(round(cosine_value, 6))
            log.write(text + "\n")
            text = ""

    def write_all(self, file):
        log = open(file, "w")

        # Table
        for N_document, words in enumerate(self.matrix_tf_idf):
            print_table = {}

            log.write(str("/*-------------------- Documento " + str(N_document) + " --------------------*/\n\n"))

            log.write("{:<8} {:<15} {:<10} {:<10} {:<10}\n\n".format('Indice','Termino','TF','IDF', 'TF-IDF'))

            for term_index,(word, value_tf_idf) in enumerate(words.items()):
                print_table[term_index] = [ word, str(self.matrix_tf[N_document][word]), str(round(self.dict_idf[word],6)), str(round(value_tf_idf, 6))]
            
            for k, v in print_table.items():
                word, tf, idf, tf_idf = v

                log.write("{:<8} {:<15} {:<10} {:<10} {:<10}\n".format(k, word,tf, idf, tf_idf))

            log.write("\n\n")
        
        # Cosine
        text = ""

        for N_document in range(self.N):
            text += "{:<10}".format("D" + str(N_document))
        log.write("{:<15}{}\n".format("",text))

        text = ""
        for index, cosines_values in enumerate(self.matrix_cosine):
            text += "{:<15}".format("Documento " + str(index))
            for cosine_value in cosines_values:
                text += "{:<10}".format(round(cosine_value, 6))
            log.write(text + "\n")
            text = ""

    def print_all(self):
        self.print_table()
        self.print_cosine()
