# Data
We have taken the primary sequence source from [UniProtKB/P15144](https://www.uniprot.org/uniprotkb/P15144/entry) :
  - [P15144.fasta](./P15144-fasta)

With these file we began this study about the infection of coronviruses in other potentially infective species. P15144 is the ID code of human aminopeptidase (h(APN)) in UniProt database. The h(APN) is the well know receptor of Human-Cov-229E which is a virus knows to cause a common cold. There are another species that have this receptor with their genetic sequences. 

# Methodology 

Initially we used the `blastp` function on the initial fasta document to allign all the sequences. The idea is allign the h(APN) sequence with the same receptor in other species and compare those results to get the most similar species from the point of view of the receptors sequences. Once we got this we are going to past the format of the document from tabular data to `.fasta` for other operation. 
In the second step, we will search for species that have a closer relationship with the virus and those that do not. In this case, we have divided the dataset into three parts. We will take into account those sequences that have between 70% and 99.99% similarity to our human aminopeptidase sequence. Less than 70-60% would lose a lot of genetic information. The 100% sequence would represent the h (APN) sequence. We will divide this dataset into three fasta files, one for 70-80%, 80-90%, and 90-99.99%. When searching the literature, we see how there is no evidence of cases in which these animals have been infected with the 229E coronavirus from the 80-90% dataset. Therefore, we will choose to study only the 70-80% and 90-99.99% datasets.

# Human coronavirus 229E

|Species|Evidence|
|-------|--------|
|Macaca mulatta|No|
|Pan troglodytes|No|
|Mandrillus leucophaeus|No|
|Macaca fascicularis|No|
|Theropitecus gelada|No|
|Gorilla gorilla gorilla|No|
|pongo abelii|No|
|Chlorocebus sabaeus|No|
|Rhinopithecus bieti|No|
|Colobus angolensis palliatus|No|
|Diceros bicornis minor|No|
|Marmota monax|No|
|Marmota flaviventris|No|
|Oryctolagus cuniculus|No|
|Ceratotherium simum simum |No|
|Pteropus vampyrus|Si|
|Choloepus didactylus|No|
|Camelus ferus|No|
|Hipposideros armiger|Si|
|Camelus dromedarius|Si|
|Vicugna pacos|Si|
|Mus musculus|Si|
