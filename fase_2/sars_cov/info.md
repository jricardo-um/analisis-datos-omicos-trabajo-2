# host protein sequence

Initial data sources:

- [uniprotkb/Q9BYF1](https://www.uniprot.org/uniprotkb/Q9BYF1/entry) downloaded sequence as [Q9BYF1.fasta](./Q9BYF1.fasta).
- [uniref/50_Q9BYF1](https://www.uniprot.org/uniref/UniRef50_Q9BYF1)
  - [clusters with 90% identity](https://www.uniprot.org/uniref?query=%28cluster:UniRef50_Q9BYF1%29%20AND%20%28identity:0.9%29) downloaded representatives as [Q9BYF1_c50_i90.fasta](./Q9BYF1_c50_i90.fasta).
  - each cluster's sequences downloaded if needed

TODO: align, compare and download needed groups individually.

NOTE: Isoform 2 only found on infected cells, replaces first 356 residues with `MREAGWDKGG`. Therefore, it's probably in there where the virus spike protein binds.

NCBI BlastP column reference

| Column | NCBI name  | Description                                  |
| ------ | ---------- | -------------------------------------------- |
| 1      | qaccver    | Query accession dot version                  |
| 2      | saccver    | Subject accession dot version (database hit) |
| 3      | pident     | Percentage of identical matches              |
| 4      | length     | Alignment length                             |
| 5      | mismatch   | Number of mismatches                         |
| 6      | gapopen    | Number of gap openings                       |
| 7      | qstart     | Start of alignment in query                  |
| 8      | qend       | End of alignment in query                    |
| 9      | sstart     | Start of alignment in subject (database hit) |
| 10     | send       | End of alignment in subject (database hit)   |
| 11     | evalue     | Expectation value (E-value)                  |
| 12     | bitscore   | Bit score                                    |
| 13     | sallseqid  | All subject Seq-id(s), separated by a ';'    |
| 14     | score      | Raw score                                    |
| 15     | nident     | Number of identical matches                  |
| 16     | positive   | Number of positive-scoring matches           |
| 17     | gaps       | Total number of gaps                         |
| 18     | ppos       | Percentage of positive-scoring matches       |
| 19     | qframe     | Query frame                                  |
| 20     | sframe     | Subject frame                                |
| 21     | qseq       | Aligned part of query sequence               |
| 22     | sseq       | Aligned part of subject sequence             |
| 23     | qlen       | Query sequence length                        |
| 24     | slen       | Subject sequence length                      |
| 25     | salltitles | All subject title(s), separated by a '<>'    |

> Search for evidence

| Species    | Sars-CoV | Sars-CoV-2 |
| ---------- | -------- | ---------- |
| cat        | yes      | yes        |
| mice       | low      | no/low     |
| hamster    | yes      | yes        |
| ferrets    | yes      | yes        |
| primates   |          | yes        |
| pigs       |          | no         |
| chickens   |          | no         |
| ducks      |          | no         |
| dogs       |          | yes/low    |
| raccoon    | yes      |            |
| palm civet | yes      |            |
| monkey     | yes      |            |
| bat        | yes      | yes        |
| rat        | no       |            |
| tiger      | yes      | yes        |
| lion       | yes      | yes        |
| mink       | yes      | yes        |
| rabbit     |          | no         |
|            |          |            |
|            |          |            |
|            |          |            |
|            |          |            |
|            |          |            |

Info from:

- [Receptor recognition and cross-species infections of SARS coronavirus - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0166354213002222)

- [Susceptibility of ferrets, cats, dogs, and other domesticated animals to SARS-CoV-2](https://doi.org/10.1126/science.abb7015)

- [In Vitro and Animal Models for SARS-CoV-2 research - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0165614720301292)

- [First Reported Cases of SARS-CoV-2 Infection in Companion Animals](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7315787/)

- [Evidence for SARS-CoV-2 Infection of Animal Hosts](https://www.mdpi.com/2076-0817/9/7/529)

- [An Overview of SARS-CoV-2 and Animal Infection](https://www.frontiersin.org/articles/10.3389/fvets.2020.596391/full)

- 

Interesting: [Receptor recognition and cross-species infections of SARS coronavirus - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0166354213002222?via%3Dihub)
