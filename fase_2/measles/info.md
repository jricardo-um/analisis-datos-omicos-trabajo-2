# Data
We have taken the primary sequence source from [UniProtKB/P15144](https://www.uniprot.org/uniprotkb/P15144/entry) :
  - [P15144.fasta](./P15144-fasta)

With these file we began this study about the infection of coronviruses in other potentially infective species. P15144 is the ID code of human aminopeptidase (h(APN)) in UniProt database. The h(APN) is the well know receptor of Human-Cov-229E which is a virus knows to cause a common cold. There are another species that have this receptor with their genetic sequences. 

# Methodology 

Initially we used the `blastp` function on the initial fasta document to allign all the sequences. The idea is allign the h(APN) sequence with the same receptor in other species and compare those results to get the most similar species from the point of view of the receptors sequences. Once we got this we are going to past the format of the document from tabular data to `.fasta` for other operation. 
In the second step, we will search for species that have a closer relationship with the virus and those that do not. In this case, we have divided the dataset into three parts. We will take into account those sequences that have between 70% and 99.99% similarity to our human aminopeptidase sequence. Less than 70-60% would lose a lot of genetic information. The 100% sequence would represent the h (APN) sequence. We will divide this dataset into three fasta files, one for 70-80%, 80-90%, and 90-99.99%. When searching the literature, we see how there is no evidence of cases in which these animals have been infected with the 229E coronavirus from the 80-90% dataset. Therefore, we will choose to study only the 70-80% and 90-99.99% datasets.
It is the binding domains that change their conformation before and after fusion. In the early stages of binding, the receptor binding site is blocked, allowing the virus to protect itself as an immune recognition mechanism. As the conformation progresses, the binding site is exposed, and data suggest that the RBD promotes post-fusion conversion. The shape of the S protein after fusion is characterized by a bundle of 6 helices, formed by the internal triple helix HR1 and the HR2 helix packed inside the structure. The S2 subunit is elongated, and the structural changes during conversion and post-fusion are more extensive.
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
The first human coronavirus was isolated from the B814 strain in 1965. It was discovered in the respiratory tract of patients with the common cold during studies on nasal samples. The 229E species was isolated from cultured standard tissues. This virus is generally associated with upper respiratory tract diseases, accounting for a total of 15-30% of common cold cases in humans.
This coronavirus uses an S protein (called spike protein) that mediates the binding to the receptor and subsequent fusion of the virus to the host cell. The receptor, which we will study below, has a binding domain (RBD) but the system by which the S protein maintains its function once it binds is unknown. The receptor in animals such as humans is called aminopeptidase (h(APN)), and was discovered by studying crystal structures in X-rays focusing only on the receptor's binding domain. This study reveals that the interaction between both structures occurs in a highly specific manner.
This protein has hydrophilic subunits that, in its study, reveal part of its helical core in the solvent. The binding between this protein and its receptor is very specific and structurally conserved within members of the Alphacoronavirus family, even when they bind to different receptors in different locations. This, along with interspecies jumping, could suggest a mechanism for acquiring new receptor interactions. The functional domain of the S protein is composed of an N-terminal S1 domain that contains the receptor binding domain (RBD) and a C-terminal S2 region that mediates membrane fusion. This is a trimer that maintains this structure before and after fusion with the cell.


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
- [Infected set clustal2](./All_infected_clustal2.png)
- [Infected set only nucleottide differences](./All_infected_nucleotide-png)

In the case of those species that are seen to be infected, and could potentially pass on the coronavirus 229E, we can see that we have many nucleotides represented with different colors. In the image, we see a grid of different colors, one for each nucleotide. If we color it with the clustal2 color system, we can see in more detail (in blue) the nucleotides that are the same in the sequences. With the application, we can also see each of the nucleotides that are different at the same level in the 4 compared sequences. In the case of the species that are seen to be infected, we have more different nucleotides, especially in the final part of the sequences. This makes their similarity to the protein different. We could say that the infectivity potential of human coronavirus 229E is given by some very conserved areas that are more involved in the functionality of the protein.

- [No infected set full colored](./All_no_infected_fullcolor.png)
- [No infected set clustal2](./All_no_infected_clustal2.png)
- [No Infected set only nucleotide](./All_no_infected_nucleotide.png)


In the case of the species that do not get infected, we have many more conserved sequences. As we can see in clustal2, there are many more areas of blue color, indicating repeated nucleotides. If we look at the nucleotides at the specific level, there are fewer different nucleotides. Although we can see that at the end of the sequence, there are areas with different nucleotides. We also observe that the conserved areas mostly coincide with those sequences that do get infected, with the exception of a few. We could say that it is these differences in conserved areas that generate a change in the functional structure of the protein, allowing infection. In both data sets, we can see that there are more conserved sequences in the anterior part of the sequences than in the posterior part. This may indicate that one area may be structural nucleotides and others functional nucleotides, with more similar sequences in the functional ones.
