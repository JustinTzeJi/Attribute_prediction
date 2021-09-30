# [WIP] Gene Attribute (regultory) Prediction Pipeline 
*part of my MSc project 

## Current workflow:
![alt text](dag.png "workflow")

## Overview
Integrating multiple prediction tools in a single pipeline to produce a data matrix.

1. Current integrated tools:
    - **DeepTFactor**   [[Paper](https://doi.org/10.1073/pnas.2021171118)] [[Repository](https://bitbucket.org/kaistsystemsbiology/deeptfactor/src/master/)]
    - **BPROM** [[Paper](https://www.researchgate.net/publication/259450599_V_Solovyev_A_Salamov_2011_Automatic_Annotation_of_Microbial_Genomes_and_Metagenomic_Sequences_In_Metagenomics_and_its_Applications_in_Agriculture_Biomedicine_and_Environmental_Studies_Ed_RW_Li_Nova_Sc)] [[Webtool](http://www.softberry.com/berry.phtml?topic=bprom&group=programs&subgroup=gfindb)]
    - **PathoFact** [[Paper](https://doi.org/10.1186/s40168-020-00993-9)] [[Repository](https://git-r3lab.uni.lu/laura.denies/PathoFact)]

2. Workflow system: [Snakemake](https://snakemake.github.io/)

## Pre-requisites
### Follow all the installation steps of [PathoFact](https://git-r3lab.uni.lu/laura.denies/PathoFact)

## Usage
### Activate Conda Environment
```bash
conda activate snakemake
```
### CLI 
```bash
snakemake --cores 4 --use-conda -p
```

### Configuration
1. Edit the config.yaml file
2. Create a blank files with your sample accension IDs, eg: `NC_006350.1`

### Note:
* The U amino acid is replaced to X during DeepTFactor, as U is not included in the DeepTFactor model. 