# Gestión del Conocimiento en las Organizaciones

## Sistemas de recomendación. 
## Modelos Basados en el Contenido

Implementación desarrollada en Python 2.7.   
Alumno: Carlos Javier Delgado Hernández  

# Modo de uso  
 Para ejecutar el programa es necesario invocarlos con los siguientes argumentos:

- `-t TEXT`: Especifica la ruta del texto a analizar.  
- `-f FILE`: Si desea imprimir el análisis hacia un fichero, especifica el nombre de dicho fichero donde guardar la información (Si no se especifica este argumento, el programa enviará la información a la terminal como comportamiento por defecto). 
- `-m MODE`: Visualizar o escribir la información que desea:
  - `table`: Extrae solo la información del texto que contiene la tabla con TF, IDF, TF-IDF asociado a cada artículo y su documento
  - `cosine`: Extrae la matriz de relaciones cosenos entre artículos.
  - `all`: Extrae toda la información. Es el comportamiento por defecto.  
  
# Ejemplos de uso
Imprime la matriz de relaciones coseno del documento 1  
````bash
carlos@DESKTOP-8U45C2U:~/dev/GCO_SC_Contenido$ python main.py -t examples/documents-01.txt -m cosine
               D0        D1        D2        D3        
Documento 0    1.0       0.130744  0.0       0.344031  

Documento 1    0.130744  1.0       0.153846  0.231326  

Documento 2    0.0       0.153846  1.0       0.0       

Documento 3    0.344031  0.231326  0.0       1.0   
````  
Guarda en el fichero `doc1Cosine.txt` la matriz de relaciones coseno del documento 1  
````bash
carlos@DESKTOP-8U45C2U:~/dev/GCO_SC_Contenido$ python main.py -t examples/documents-01.txt -f doc1Cosine.txt -m cosine
carlos@DESKTOP-8U45C2U:~/dev/GCO_SC_Contenido$ cat doc1Cosine.txt
               D0        D1        D2        D3        
Documento 0    1.0       0.130744  0.0       0.344031  
Documento 1    0.130744  1.0       0.153846  0.231326  
Documento 2    0.0       0.153846  1.0       0.0       
Documento 3    0.344031  0.231326  0.0       1.0       
carlos@DESKTOP-8U45C2U:~/dev/GCO_SC_Contenido$ 
````

Imprime la tabla asociado al documento 4 
````bash
carlos@DESKTOP-8U45C2U:~/dev/GCO_SC_Contenido$ python main.py -t examples/documents-04.txt -m table
/*-------------------- Documento 0 --------------------*/

Indice   Termino         TF         IDF        TF-IDF    
0        and             2          0.0        0.0       
1        palate          1          0.693147   0.693147  
2        apple           1          0.693147   0.693147  
3        acidity         1          0.0        0.0       
4        citrus          1          0.693147   0.693147  
5        unripened       1          0.693147   0.693147  
6        brisk           1          0.693147   0.693147  
7        alongside       1          0.693147   0.693147  
8        sage            1          0.693147   0.693147  
9        fruit           1          0.693147   0.693147  
10       dried           2          0.693147   1.386294  
11       expressive      1          0.693147   0.693147  
12       brimstone       1          0.693147   0.693147  
13       offering        1          0.693147   0.693147  
14       broom           1          0.693147   0.693147  
15       aromas          1          0.693147   0.693147  
16       overly          1          0.693147   0.693147  
17       tropical        1          0.693147   0.693147  
18       herb            1          0.693147   0.693147  
19       the             1          0.693147   0.693147  
20       include         1          0.693147   0.693147  
21       isn't           1          0.693147   0.693147  

/*-------------------- Documento 1 --------------------*/

Indice   Termino         TF         IDF        TF-IDF    
0        and             2          0.0        0.0       
1        tannins         1          0.693147   0.693147  
2        already         1          0.693147   0.693147  
3        although        1          0.693147   0.693147  
4        ripe            1          0.693147   0.693147  
5        be              1          0.693147   0.693147  
6        is              2          0.693147   1.386294  
7        juicy           1          0.693147   0.693147  
8        it              1          0.693147   0.693147  
9        drinkable       1          0.693147   0.693147  
10       are             1          0.693147   0.693147  
11       firm            1          0.693147   0.693147  
12       still           1          0.693147   0.693147  
13       with            2          0.693147   1.386294  
14       filled          1          0.693147   0.693147  
15       out             1          0.693147   0.693147  
16       a               1          0.693147   0.693147  
17       will            1          0.693147   0.693147  
18       certainly       1          0.693147   0.693147  
19       freshened       1          0.693147   0.693147  
20       from            1          0.693147   0.693147  
21       acidity         1          0.0        0.0       
22       this            1          0.693147   0.693147  
23       it's            1          0.693147   0.693147  
24       structured      1          0.693147   0.693147  
25       smooth          1          0.693147   0.693147  
26       while           1          0.693147   0.693147  
27       better          1          0.693147   0.693147  
28       that            1          0.693147   0.693147  
29       berry           1          0.693147   0.693147  
30       fruits          1          0.693147   0.693147  
31       2016            1          0.693147   0.693147  
32       fruity          1          0.693147   0.693147  
33       red             1          0.693147   0.693147  
34       wine            1          0.693147   0.693147  

carlos@DESKTOP-8U45C2U:~/dev/GCO_SC_Contenido$
````  

Escribe la tabla asociada al documento 4 en el fichero `doc4Table.txt`  
````bash
carlos@DESKTOP-8U45C2U:~/dev/GCO_SC_Contenido$ python main.py -t examples/documents-04.txt -f doc4Table.txt -m table
carlos@DESKTOP-8U45C2U:~/dev/GCO_SC_Contenido$ cat doc4Table.txt 
/*-------------------- Documento 0 --------------------*/

Indice   Termino         TF         IDF        TF-IDF    

0        and             2          0.0        0.0       
1        palate          1          0.693147   0.693147  
2        apple           1          0.693147   0.693147  
3        acidity         1          0.0        0.0       
4        citrus          1          0.693147   0.693147  
5        unripened       1          0.693147   0.693147  
6        brisk           1          0.693147   0.693147  
7        alongside       1          0.693147   0.693147  
8        sage            1          0.693147   0.693147  
9        fruit           1          0.693147   0.693147  
10       dried           2          0.693147   1.386294  
11       expressive      1          0.693147   0.693147  
12       brimstone       1          0.693147   0.693147  
13       offering        1          0.693147   0.693147  
14       broom           1          0.693147   0.693147  
15       aromas          1          0.693147   0.693147  
16       overly          1          0.693147   0.693147  
17       tropical        1          0.693147   0.693147  
18       herb            1          0.693147   0.693147  
19       the             1          0.693147   0.693147  
20       include         1          0.693147   0.693147  
21       isn't           1          0.693147   0.693147  


/*-------------------- Documento 1 --------------------*/

Indice   Termino         TF         IDF        TF-IDF    

0        and             2          0.0        0.0       
1        tannins         1          0.693147   0.693147  
2        already         1          0.693147   0.693147  
3        although        1          0.693147   0.693147  
4        ripe            1          0.693147   0.693147  
5        be              1          0.693147   0.693147  
6        is              2          0.693147   1.386294  
7        juicy           1          0.693147   0.693147  
8        it              1          0.693147   0.693147  
9        drinkable       1          0.693147   0.693147  
10       are             1          0.693147   0.693147  
11       firm            1          0.693147   0.693147  
12       still           1          0.693147   0.693147  
13       with            2          0.693147   1.386294  
14       filled          1          0.693147   0.693147  
15       out             1          0.693147   0.693147  
16       a               1          0.693147   0.693147  
17       will            1          0.693147   0.693147  
18       certainly       1          0.693147   0.693147  
19       freshened       1          0.693147   0.693147  
20       from            1          0.693147   0.693147  
21       acidity         1          0.0        0.0       
22       this            1          0.693147   0.693147  
23       it's            1          0.693147   0.693147  
24       structured      1          0.693147   0.693147  
25       smooth          1          0.693147   0.693147  
26       while           1          0.693147   0.693147  
27       better          1          0.693147   0.693147  
28       that            1          0.693147   0.693147  
29       berry           1          0.693147   0.693147  
30       fruits          1          0.693147   0.693147  
31       2016            1          0.693147   0.693147  
32       fruity          1          0.693147   0.693147  
33       red             1          0.693147   0.693147  
34       wine            1          0.693147   0.693147
````  

# Detalles de implementación  
Se ha desarrollado la clase `Recommender_CB` cuyo argumento a enviar es el texto que desea analizar.  

Cada linea del texto representa un documento, por eso introducimos cada linea en una matriz llamada `matrix_documents` al mismo tiempo que guardamos todas las palabras que encontremos en el texto  
````python
        # Divide text by words
        for line in text:
            line_vector = line.replace(",","").replace(".","").replace("\n","").lower().split(" ")
            self.total_words.extend(line_vector)
            self.matrix_documents.append(line_vector)
````  
Eliminamos la duplicidad de palabras  y guardamos el total de documentos que tenemos en `N`
````python
        # Delete duplicate words
        self.total_words = set(self.total_words)
        # Numbers of docs
        self.N = len(self.matrix_documents)
````  
Guardaremos los valores TF en una matriz de diccionarios que contendrá todas las palabras del texto perteneciente al documento correspondiente. Cuando se recorra cada palabra de un documento de la matriz, agregaramos +1 al valor asociado a la palabra dentro del diccionario y cuando finalice de recorrer todas las palabras del documento, introduciremos dicho diccionario en la matriz haciendo coincidir su índice con el índice del documento.  
````python
        # TF
        for document in self.matrix_documents:
            dicc_words = dict.fromkeys(set(document), 0)
            for word in document:
                dicc_words[word] += 1
            self.matrix_tf.append(dicc_words)
````  
Para calcular el DF simplemente creamos un nuevo diccionario con todas las palabras cuyo valor por defecto será 0 y guardaremos las veces que una palabra aparezca en el tf de cada documento.  
````python
        # DF
        self.dict_df = dict.fromkeys(self.total_words, 0)
        for words in self.matrix_tf:
            for word, value in words.items():
                if value > 0:
                    self.dict_df[word] += 1
````  

En el IDF recorreremos el DF y aplicaremos la formula del IDF (log(N/IDF)).  

````python
        # IDF
        self.dict_idf = dict.fromkeys(self.total_words, 0)

        for word in self.dict_df.keys():
            self.dict_idf[word] = math.log( self.N / float(self.dict_df[word]))
````  

En el TF-IDF recorreremos la matriz TF, calcularemos para cada palabra del documento multiplicando por el diccionario IDF y lo guardaremos en nuevo diccionario de palabras del texto. Una vez recorrido guardaremos ese diccionario en una nueva matriz que nuevamente el índice corresponderá con el documento.  

````python
        # TF-IDF
        for words in self.matrix_tf:
            dicc_words = dict.fromkeys(set(words), 0)
            for word, value in words.items():
                dicc_words[word] = value * self.dict_idf[word]
            self.matrix_tf_idf.append(dicc_words)
````  

Normalizaremos lo valores TF aplicando la formula raíz cuadrada de los valores elevados al cuadrado
````python
            pow_array = map(lambda value: pow(value,2) , words.values())
            value_normalizer = math.sqrt( sum(pow_array) )
````  

El código para normalizar consiste en recorrer TF y calcular el valor total a normalizar. Ese valor lo diviremos por los valores TF de documento y repetiremos dicho proceso en cada documento. Todos los valores se guardarán nuevamente en una matriz.  

````python
        # Normalizer tf-idf
        for words in self.matrix_tf:
            dict_total_words = dict.fromkeys(set(words),0)
            pow_array = map(lambda value: pow(value,2) , words.values())
            value_normalizer = math.sqrt( sum(pow_array) )
            for word, value in words.items():
                dict_total_words[word] = float(value) / float(value_normalizer)
            self.matrix_tf_norm.append(dict_total_words)
````  

Por último, sacaremos la relación entre documentos/artículos mediante la relación coseno entre cada par de documentos. Consiste en coger el TF normalizado de un documento y multiplicarlo entre los valores asociados a las palabras de los dos documentos, sumar esos valores y guardarlos en la matriz.  

Ejemplo:  
`matrix_cosine[1][2]` representa la relación entre el artículo 1 y el artículo 2  

`````python
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
````  

