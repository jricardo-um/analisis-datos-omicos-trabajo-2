# Data
We have taken the primary sequence source from [UniProtKB/P15144](https://www.uniprot.org/uniprotkb/P15144/entry) :
  - [P15144.fasta](./P15144-fasta)

With these file we began this study about the infection of coronviruses in other potentially infective species. P15144 is the ID code of human aminopeptidase (h(APN)) in UniProt database. The h(APN) is the well know receptor of Human-Cov-229E which is a virus knows to cause a common cold. There are another species that have this receptor with their genetic sequences. 

# Methodology 

Initially we used the `blastp` function on the initial fasta document to allign all the sequences. The idea is allign the h(APN) sequence with the same receptor in other species and compare those results to get the most similar species from the point of view of the receptors sequences. Once we got this we are going to past the format of the document from tabular data to `.fasta` for other operation. 
In the second step, we will search for species that have a closer relationship with the virus and those that do not. In this case, we have divided the dataset into three parts. We will take into account those sequences that have between 70% and 99.99% similarity to our human aminopeptidase sequence. Less than 70-60% would lose a lot of genetic information. The 100% sequence would represent the h (APN) sequence. We will divide this dataset into three fasta files, one for 70-80%, 80-90%, and 90-99.99%. When searching the literature, we see how there is no evidence of cases in which these animals have been infected with the 229E coronavirus from the 80-90% dataset. Therefore, we will choose to study only the 70-80% and 90-99.99% datasets.
## List of species 
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

After selecting the datasets we are going to use, based on the literature, we proceed to carry out a deeper study of the genetic sequences of the receptors of each animal species. In this case, we have selected three animal species from the dataset that have a 70-80% similarity. In these three animal species, according to scientific literature, cases of 229E infection have been observed, in fact, they are the animals where more pathological cases have been confirmed. On the other hand, we have decided to use three species that are closer to 100% similarity with the original sequence. These species are:

## List of target species

|Species|similarity(%)|
|-------|----------|
|Macaca mulatta|94.938|
|Pan troglodytes|98.656|
|Mandrillus leucophaeus|94.215|
|Camelus dromedarius|76|
|Vicugna pacos|79|
|Mus musculus|76.319|

After finishing the literature search, we decided to use these three species to conduct the study of the 229E receptor sequence. To do this, we first performed an analysis of the sequences with the usegalaxy.com application using the `sequence Logo` tool. Next, we used the NGPhylogeny application that performs multiple alignments and phylogenetic trees. From this, we will identify the sequence differences between the different receptors. For this, we will create two datasets, one with all the species that are infected, and another with those that are not infected.

# Human coronavirus 229E

# Results and Discussion

First of all we are goping to see a mapp with all the allignemnts of the sequences from different species that we got in the blastp. 

- [Picture 1](./consurf_colored_seq.pdf)

As we can see in the image, we have very repeated patterns, which could be considered conserved, among the sequences. In this case, we are observing the entire alignment of the blastp tool against the sequence of our receptor protein. Therefore, we do not yet have a specific image of which species have a greater capacity for infection, and the difference between receptor structures. According to the color diagram that appears below, those nucleotides marked in purple are related to the conserved sequences. Those with a red-colored F are predictions of residues that may be functional for the protein. In contrast, the blue S residues are structural residues.



