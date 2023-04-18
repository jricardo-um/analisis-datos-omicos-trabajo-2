# Info

Initial data sources:

- [uniprotkb/Q9BYF1](https://www.uniprot.org/uniprotkb/Q9BYF1/entry) downloaded sequence as [Q9BYF1.fasta](./Q9BYF1.fasta).
- [uniref/50_Q9BYF1](https://www.uniprot.org/uniref/UniRef50_Q9BYF1)
  - [clusters with 90% identity](https://www.uniprot.org/uniref?query=%28cluster:UniRef50_Q9BYF1%29%20AND%20%28identity:0.9%29) downloaded representatives as [Q9BYF1_c50_i90.fasta](./Q9BYF1_c50_i90.fasta).
  - each cluster's sequences downloaded if needed

TODO: align, compare and download needed groups individually.

NOTE: Isoform 2 only found on infected cells, replaces first 356 residues with `MREAGWDKGG`. Therefore, it's probably in there where the virus spike protein binds.

# Log

## [flow_1](https://usegalaxy.eu/u/jricardo.alonso_um.es/h/adoentrega1)

Use `blastp` human ACE2 against representative ACE2, filtered by `bitscore`>`1300`. Output column reference:

| Column | NCBI name  | Description                                  |
| ------ | ---------- | -------------------------------------------- |
| 2      | saccver    | Subject accession dot version (database hit) |
| 12     | bitscore   | Bit score                                    |
| 25     | salltitles | All subject title(s), separated by a '<>'    |

Afterwards, all cluster members from the cluster are downloaded to a file via a python script:

```bash
./download_cluster_members.py \
 table='./Galaxy6-[Q9BYF1_c50_i90_blastp_filter].tabular' \
 index=0 \
 fasta='./Q9BYF1_members.fasta' \
 uniprot_only
```

The process is repeated with the new database and the species are searched for evidence. To group the results, the following python script is used:

```bash
./group_by_species.py \
 table='./Galaxy11-[Q9BYF1_members_blastp_filter].tabular' \
 tsv=./FINAL.tsv
```

## flow_2

Workflow:

- add family name to species with `species.py` script for more structured search.

- search in scienteific literature for all possible species.

- anotate results in table from `flow_1` or below if entry missing.

| Species                                            | SARS-CoV-2<br>transmission |
|:--------------------------------------------------:|:--------------------------:|
| Snow leopard<br/>(Uncia uncia)                     | no                         |
| Northern treeshrew<br/>(Tupaia belangeri)          | yes                        |
| Egyptian fruit bat<br/>(Rousettus<br/>aegyptiacus) | yes                        |
| Tiger<br/>(Panthera tigris)                        | yes                        |

Info from:

- [Receptor recognition and cross-species infections of SARS coronavirus - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0166354213002222)

- [Susceptibility of ferrets, cats, dogs, and other domesticated animals to SARS-CoV-2](https://doi.org/10.1126/science.abb7015)

- [In Vitro and Animal Models for SARS-CoV-2 research - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0165614720301292)

- [First Reported Cases of SARS-CoV-2 Infection in Companion Animals](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7315787/)

- [Evidence for SARS-CoV-2 Infection of Animal Hosts](https://www.mdpi.com/2076-0817/9/7/529)

- [An Overview of SARS-CoV-2 and Animal Infection](https://www.frontiersin.org/articles/10.3389/fvets.2020.596391/full)

- [Receptor recognition and cross-species infections of SARS coronavirus - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0166354213002222?via%3Dihub)

## [flow_3](https://usegalaxy.eu/u/jricardo.alonso_um.es/h/adoentrega3) ([old](https://usegalaxy.eu/u/jricardo.alonso_um.es/h/adoentrega3test))



EOF
