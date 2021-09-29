#executing deeptf_run.py

rule deeptf:
    input:
        expand(os.path.join(DATA_DIR,"deeptf_{sample}.csv"), sample=config["samples"])
    output:
        touch('DeepTF_analysis.done')    

rule deeptf_execute:
    input:
        expand(os.path.join(DATA_DIR,"{sample}_protein.fasta"), sample=config["samples"])
    output:
        expand(os.path.join(DATA_DIR,"deeptf_{sample}.csv"), sample=config["samples"])
    shell:
        "python ../Python_scripts/deeptf_run.py -i {input} -o {output}"