#executing bprom_run.py

rule bprom:
    input:
        expand(os.path.join(DATA_DIR,"bprom_{sample}.csv"), sample=config["samples"])
    output:
        touch('BPROM_analysis.done')    

rule bprom_execute:
    input:
        expand(os.path.join(DATA_DIR,"{sample}_upstream.fasta"), sample=config["samples"])
    output:
        expand(os.path.join(DATA_DIR,"bprom_{sample}.csv"), sample=config["samples"])
    shell:
        "python ../Python_scripts/bprom_run.py -i {input} -o {output}"