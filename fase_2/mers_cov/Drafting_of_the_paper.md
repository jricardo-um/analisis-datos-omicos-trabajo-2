# Mers-CoV Virus Section

> [UniProt P27487 entry](https://www.uniprot.org/uniprotkb/P27487/entry)

Sequence downloaded to [P27487.fasta](https://github.com/jricardo-um/analisis-datos-omicos-trabajo-2/blob/main/fase_2/mers_cov/Sequences_origin/P27487.fasta).

> Workflow GitHub: https://usegalaxy.org/u/ricksho315/h/omicproject

Sequences downloaded with a 90% of similitude [P27487_similar.fasta](https://github.com/jricardo-um/analisis-datos-omicos-trabajo-2/blob/main/fase_2/mers_cov/Sequences_origin/P27487_similar.fasta)

MERS-CoV (Middle East Respiratory Syndrome Coronavirus) is a beta coronavirus that causes severe respiratory illnesses in humans. It is believed to have originated in animals, possibly camels, and is primarily transmitted to humans through contact with infected animals or their respiratory secretions. It can also spread among people through close contact, such as caring for infected patients.

# [Structure of MERS-CoV spike receptor-binding domain complexed with human receptor DPP4](./https://www.nature.com/articles/cr201392#Sec2)

In this study, the structure of the Middle East Respiratory Syndrome-CoV (MERS-CoV) S protein and its interaction with the DPP4 protein on the surface of host cells was investigated. It was found that the S protein of the virus binds to the DPP4 protein to enter host cells. Identification of the critical residues involved in the binding between these proteins will help in the development of antiviral treatments for MERS-CoV.

The paper is focused on the identification of critical residues in the S protein of MERS-CoV that are important for viral binding and entry into host cells. Mutations in certain residues were found to significantly reduce binding to the DPP4 protein and the efficiency of viral entry into host cells. The results suggest that the interaction between the virus S protein and the DPP4 protein is crucial for viral entry.

The molecular structure of the MERS-CoV S protein and its interaction with the cellular DPP4 receptor. The researchers identified specific residues in the S protein of the virus that are critical to its ability to bind to the DPP4 receptor and enter host cells.

The MERS-CoV S protein consists of two main subdomains: the core and the receptor-binding subdomain. The core is structurally similar to that of the SARS-CoV S protein, while the receptor-binding subdomain is markedly different. This helps explain the differences in receptor specificity between MERS-CoV and SARS-CoV.

The study also revealed that the S protein of MERS-CoV specifically binds to cleavages 4 and 5 of the β-propeller domain of DPP4. This binding occurs due to complementarity of charges and shapes at the binding interface. The positive charges on the outer surface of DPP4 blades 4 and 5 interact with the negative charges on the surface of the virus S-protein, while the short alpha helix between DPP4 blades 4 and 5 binds to the concave, hydrophobic surface of the S-protein.

Furthermore, the enzymatic site of DPP4 was found to be far from the binding site of the MERS-CoV S protein, which explains why DPP4 enzyme inhibitors do not block virus entry into cells. Finally, the importance of structural differences between DPP4 and the ACE2 receptor in determining cell tropism and pathogenesis of MERS-CoV and SARS-CoV in living hosts is discussed.

# Work and study to find reservoirs of the Mers-CoV virus

MERS-CoV can cause a wide range of respiratory symptoms, ranging from mild cold-like symptoms to severe pneumonia with respiratory failure, and in some cases, death. Patients with chronic illnesses or weakened immune systems are at higher risk for severe complications.

Pathological studies in animals infected with MERS-CoV have shown changes in the lungs, such as thickening of alveolar septa, infiltration of inflammatory cells such as lymphocytes and histiocytes, and presence of exudates in alveolar and bronchial spaces. These pathological changes can vary from acute lesions in the early days of infection to chronic or reparative lesions in later stages.

We have a file with the sequence DPP4, dipeptidyl peptidase-4, or also called CD26 is an enzyme found on the surface of many cells in the human body and plays an important role in the regulation of metabolic function and the immune system. DPP4 is a protein that belongs to the family of peptidase enzymes, which are responsible for the hydrolysis of peptides and proteins in the body.
The study of this protein is related to the way it attacks the Mers-CoV virus, as the MERS-CoV Spike protein is found on the surface of the Middle East respiratory syndrome virus (MERS-CoV), which is a type of coronavirus that causes severe respiratory disease in humans. This Spike protein is responsible for the entry of the virus into human cells during infection.

The MERS-CoV Spike protein has been shown to interact with the DPP4 protein on the surface of human cells as the virus receptor. The MERS-CoV Spike protein specifically binds to the DPP4 protein on the cell surface as a crucial step for virus entry into host cells. This interaction is required for MERS-CoV infection and is a key step in the viral infection process.

Once the MERS-CoV Spike protein binds to the DPP4 protein on the cell surface, it triggers a series of events that allow entry of the virus into the host cell, including fusion of the viral envelope with the cell membrane and release of the virus' genetic material into the cell. This leads to virus replication and the spread of infection.
The interaction between the MERS-CoV Spike protein and the DPP4 protein is a potential target for the development of therapeutic and preventive strategies against MERS-CoV infection. For example, inhibitors of the Spike protein and the DPP4 protein have been investigated as possible approaches to block viral entry into cells and prevent MERS-CoV infection. However, more research is still needed to fully understand the interaction between these proteins and their potential application in the treatment or prevention of MERS-CoV infection.

# Mers-CoV and and its relationship with animals and humans

MERS-CoV is a zoonotic virus (transmitted between animals and humans). It is believed that humans can be infected by direct contact but at present it has only been shown to occur  with infected dromedary camels in the Middle East or their milk, urine or other body fluids.  Bats are a likely original reservoir; coronaviruses similar to MERS-CoV have been identified in bats (Rousettus aegyptiacus), but epidemiologic evidence of their role in transmission is lacking.

[Visual description of how a dromedary acts as a reservoir.](./Visual_description_of_how_a_dromedary_acts_as_a_reservoir.jpg)

Several animal species have been evaluated to model human MERS-CoV infection, including rabbits, ferrets, Syrian hamsters and mice, but have been found not to be susceptible to the virus. This was due to the function and distribution of the DPP4 receptor. The structure of the receptor is diverse, but is conserved in humans and non-human primates, making non-human primates an ideal model for infection. The DPP4 receptor of a small non-human primate such as the rhesus macaque and callithrix jacchus have a high similitud and this indicates that they may be future reservoirs due to the high sequence overlap of the DPP4 protein.

[Transmission between animals and humans](./https://www.frontiersin.org/articles/10.3389/fvets.2016.00088/full)

In this section we will try to discover possible reservoirs of this virus from the DPP4 protein, a reservoir being a place where an organism or substance can remain latent, persistent or active, and from where it can be released or transmitted to other organisms.

For this, we will use the sequence of the DPP4 protein present in Homo sapiens. We will use the `Blastp` tool present on the Galaxy server in order to align with the different species whose sequences are similar or intrinsically related to the spread of the virus. These sequences that we are going to match can be found in a protein database such as Uniprot, which is the one we have used.

## [Scores of similitud between species and human protein DPP4](./Galaxy84-blastp_secuencias_final_score.txt)

The sequences of animals most closely related to the human DPP4 protein and those sequences belonging to animal species known to have been infected have been chosen.

We have found different types of animal species which could be a possible reservoir and have a high relation with the human protein:

|  Uniprot   | Species               | Result | Paper                                                                                               |
|------------| --------------------- | ------ | --------------------------------------------------------------------------------------------------- |
|A0A0D9RSY5  | Chlorocebus sabaeus   | No     | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7706928/                                               |
|F6VRB0      | Rhesus macaque        | No     | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7107340/                                               | 
|A0A2K6UUT9  | Saimiri boliviensis   | No     | \~                                                                                                  |
|A0A2K5F6W0  | Aotus nancymaae       | No     | \~                                                                                                  |
|A0A2K5LB19  | Cercocebus atys       | No     | \~                                                                                                  |
|F7IHU4      | Callithrix jacchus    | No     | https://journals.plos.org/plospathogens/article?id=10.1371/journal.ppat.1004250#s2                  |
|A0A6D2X1C5  | Pan troglodytes       | No     | \~                                                                                                  |
|G3SI68      | Gorilla gorilla       | No     | \~                                                                                                  |
|A0A2Z5CWD9  | Carollia perspicillata| Yes    | https://pubmed.ncbi.nlm.nih.gov/25114257/                                                           |
|A0A2Z5CWD4  | Epomops buettikoferi  | Yes    | https://pubmed.ncbi.nlm.nih.gov/25114257/                                                           |
|A0A2R9CCY4  | Pan paniscus          | No     | \~                                                                                                  |
|H2P7N3      | Pongo abelii          | No     | \~                                                                                                  |
|A0A8I3Q958  | Canis lupus familiaris| No     | https://www.mdpi.com/2076-2615/13/4/624                                                             |
|A0A075T9L1  | Camelus dromedarius   | Yes    | https://www.sciencedirect.com/science/article/abs/pii/S2213260014701584?via%3Dihub                  |
|A0A075T9L7  | Ovis orientalis       | No     | https://www.eurosurveillance.org/content/10.2807/1560-7917.ES2013.18.50.20662                       |
|A0A4W2EX30  | Bos taurus indicus    | No     | https://www.eurosurveillance.org/content/10.2807/1560-7917.ES2013.18.50.20662                       |
|A0A452FGS0  | Capra aegagrus hircus | No     | https://www.eurosurveillance.org/content/10.2807/1560-7917.ES2013.18.50.20662                       |
|A0A2Z5CWB8  | Rousettus aegyptiacus | Yes    | https://wwwnc.cdc.gov/eid/article/19/11/13-1172_article | https://pubmed.ncbi.nlm.nih.gov/25114257/ |
|\~          | Oryctolagus cuniculus | No     | https://pubmed.ncbi.nlm.nih.gov/25810539/                                                           |
|M3XN99      | Mustela putorius furo | No     | https://journals.asm.org/doi/10.1128/JVI.02935-13                                                   |
|A0A075TJ59  | Mesocricetus auratus  | No     | https://pubmed.ncbi.nlm.nih.gov/23844250/                                                           |
|P28843      | Mus musculus          | No     | https://pubmed.ncbi.nlm.nih.gov/24197535/                                                           |
|            |                       |        |                                                                                                     |
|            |                       |        |                                                                                                     |

The result section indicates whether the species can act right now with the data obtained as a reservoir, seeing that only the dromedary and the African bat act as such 
and species that do not have a paper associated with them are those for which no study has been carried out that can confirm their capacity as a reservoir of Mers-Cov virus.

After reading several studies confirming that most of the animals studied so far do not act as reservoirs of the Mers-Cov virus, but only suffer from it. We will analyse the conserved regions of the DPP4 of the most characteristic species and try to predict whether they can act as reservoirs, as no studies have been carried out on the species we will be dealing with. 

[Cross-species transmission, evolution and zoonotic potential of coronaviruses](./https://www.frontiersin.org/articles/10.3389/fcimb.2022.1081370/full)

It should be noted that the case of the spread of alpha and beta variants viruses in marine mammals has also been studied, but no conclusive data have been found that they act as a reservoir. What has been concluded is that coronavirus-contaminated discharges into water bodies should be properly treated in order to prevent the [spread of the virus to marine fauna. ](./https://www.sciencedirect.com/science/article/pii/S0048969720368777)

We will take the sequence of the species we are studying that are reservoirs and those that are not, compare with the results using a `sequenceLogo` after aligning the sequences using Galaxy's `ClustalW` tool and interpret the results in order to see which regions are common to which species and guess whether they may act as reservoirs.

## Possible reservoirs and interpretation

We have aligned the sequences of species that can act as reservoirs and the sequences of species that cannot. We will then compare which regions of the protein are conserved between the two cases by using a sequenceLogo.

Therefore, if we see that the unstudied sequences have certain regions in common with the positive species, we could venture to say that they could act as reservoirs, pending an experimental study to confirm this.

This sequenceLogo comes from `WebLogo3`, the colours blue, green and black are used to represent different ranges of amino acid or nucleotide conservation in the sequence, which can be measured in terms of bits of information.

   - Blue: used to highlight the most conserved amino acids or nucleotides in the sequence, i.e. those that have the most information in common with the reference sequence used.
   - Green: used to highlight amino acids or nucleotides that have intermediate conservation in the sequence.
   - Black: used to highlight the least conserved amino acids or nucleotides in the sequence, i.e. those that have less information in common with the reference sequence used.
Sometimes we have different symbols stacked on top of each other, this is because these amino acids appear in different sequences in the same position. 

Furthermore, we have to take into account that in a sequence logo generated by WebLogo3, larger and thicker letters indicate a higher frequency of occurrence of that amino acid or nucleotide in the sequence, while smaller and thinner letters indicate a lower frequency of occurrence.

[SequenceLogo of positive cases](https://github.com/jricardo-um/analisis-datos-omicos-trabajo-2/blob/main/fase_2/mers_cov/Sequence_Logo/Galaxy112-%5BGalaxy-Rgenetics_Sequence_Logo_Positive_Case_output.png%5D.png)

[SequenceLogo of negative cases](https://github.com/jricardo-um/analisis-datos-omicos-trabajo-2/blob/main/fase_2/mers_cov/Sequence_Logo/Galaxy111-%5BGalaxy-Rgenetics_Sequence_Logo_Negative_Case_output.png%5D.png)

The Nucleotide display scale shall be used to view the sequences in a more informative way.

sequences of [Species which have been shown to be reservoir species](https://github.com/jricardo-um/analisis-datos-omicos-trabajo-2/blob/main/fase_2/mers_cov/Alignment/Galaxy107-%5BClustalW_Positive__fasta%5D.fasta)

[Conserved domains in positive cases](https://ngphylogeny.fr/data/displaymsa/33efed1db158003a)

Sequences of [Species not proven to be reservoirs](https://github.com/jricardo-um/analisis-datos-omicos-trabajo-2/blob/main/fase_2/mers_cov/Alignment/Galaxy109-%5BClustalW_Negative__fasta%5D.fasta)

[Conserved domains in negative cases](https://ngphylogeny.fr/data/displaymsa/cddf1149445feab4)

With these results we could venture to say  there are some regions that could be the ones that do that the species that can act as a reservoir. However, more experiments and further research in this field would be required to provide conclusive data.
