include:
    '/home/justin/Master/Attribute_prediction/PathoFact/rules/Universal/Preprocessing.smk'
include:
    '/home/justin/Master/Attribute_prediction/PathoFact/rules/Universal/SignalP.smk'
include:
    '/home/justin/Master/Attribute_prediction/PathoFact/rules/Virulence/Virulence.smk'
include:
    '/home/justin/Master/Attribute_prediction/PathoFact/rules/Virulence/Combine_Virulence_SignalP.smk'
include:
    '/home/justin/Master/Attribute_prediction/PathoFact/rules/Toxin/Toxin.smk'
include:
    '/home/justin/Master/Attribute_prediction/PathoFact/rules/Toxin/Combine_Toxin_SignalP.smk'
include:
    '/home/justin/Master/Attribute_prediction/PathoFact/rules/Universal/Preprocessing_contig.smk'
include:
    '/home/justin/Master/Attribute_prediction/PathoFact/rules/AMR/AMR.smk'
include:
    '/home/justin/Master/Attribute_prediction/PathoFact/rules/AMR/Plasmid.smk'
include:
    '/home/justin/Master/Attribute_prediction/PathoFact/rules/AMR/Phage.smk'
include:
    '/home/justin/Master/Attribute_prediction/PathoFact/rules/AMR/Combine_MGE_AMR.smk'
include:
    '/home/justin/Master/Attribute_prediction/PathoFact/rules/Universal/Combine_PathoFact.smk'
include: 
    '/home/justin/Master/Attribute_prediction/PathoFact/rules/Universal/Clean_up.smk'

rule Pathofact:
    input:
        expand(
            [
                os.path.join(DATA_DIR,"{project}/PathoFact_intermediate/AMR/{sample}_AMR_MGE_prediction_detailed.tsv"),
                os.path.join(DATA_DIR,"{project}/PathoFact_report/Toxin_gene_library_{sample}_report.tsv"),
                os.path.join(DATA_DIR,"{project}/PathoFact_report/PathoFact_{sample}_predictions.tsv"),
                os.path.join(DATA_DIR,"{project}/logs/{sample}_compressed.zip")
            ],
            project=config["pathofact"]["project"], sample=config["samples"]
        )
    output:
        touch('PathoFact_analyis.done')
        