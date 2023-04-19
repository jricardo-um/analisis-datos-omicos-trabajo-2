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

Next, after reviewing the literature, we will study the sequences of those species that are more closely related and those that are not. First, we will perform a general scan of the sequence using `Sequence Logo`, as we mentioned earlier. We will do this for both the species that are infected and those that are not infected.

- [Infected](./Galaxy78-[Difference_bt_infected_SL.png].png)
- [No infected](./Galaxy79-[Difference_bt_no_infected_SL.png].png)

This study is very general, because the layout of the image that this tool provides does not facilitate the interpretation of specific nucleotides. However, we can see that there are nucleotides that appear strongly conserved. The letters that appear alone are those that are repeated a lot among sequences. As we advance, the size and thickness of the letter varies according to how it is repeated among the sequences. In the case of animals that can be infected by 229E, we see that there are many letters grouped in the final sections. This means that there is a lot of variation in nucleotides in these areas. However, we see that in the first part, the variation is lower.

In the second case, we see more blue letters than green and black ones. The color scheme follows the following pattern: blue letters are related to the most conserved nucleotides in the sequence. We see that the sequences that do not get infected have more of these types of nucleotides because they have a greater similarity to the original sequence. This is different for the infected sequence. Green letters have an intermediate conservation level, and black letters are those that are not conserved among the different types.

To finish, we will analyze the sequences in a specific way. Using the NGPhylogeny application, we can see the sequences in depth, from the point of view of the most conserved nucleotides. Later, we can see a generated phylogenetic tree for the different datasets.

- [Infected set full colored](./ALl_infected_fullcolor.png)
- [Infected set only nucleottide differences](./All_infected_nucleotide-png)


- [No infected set full colored](./All_no_infected_fullcolor.png)
- [No Infected set only nucleotide](./All_no_infected_nucleotide.png)



