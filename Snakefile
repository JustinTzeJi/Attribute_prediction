#Snakefile

configfile: "config.yaml"

DATA_DIR=config["output"]["directory"]


include:
    'Snakemake/gb_processor.smk'
include:
    'Snakemake/bprom.smk'
include:
    'Snakemake/deeptf.smk'
include:
    'Snakemake/pathofact.smk'

rule all:
    input:
        expand(
            [
                os.path.join(DATA_DIR,"bprom_{sample}.csv"),
                os.path.join(DATA_DIR,"deeptf_{sample}.csv"),
                os.path.join(DATA_DIR,"{project}/PathoFact_intermediate/AMR/{sample}_AMR_MGE_prediction_detailed.tsv"),
                os.path.join(DATA_DIR,"{project}/PathoFact_report/Toxin_gene_library_{sample}_report.tsv"),
                os.path.join(DATA_DIR,"{project}/PathoFact_report/PathoFact_{sample}_predictions.tsv"),
                os.path.join(DATA_DIR,"{project}/logs/{sample}_compressed.zip")
            ],
                project=config["pathofact"]["project"], sample=config["samples"]
        )