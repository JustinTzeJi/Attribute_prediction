#executing gb_fetcher.py and gb_parser.py

rule gb_process:
    input:
        expand(
            [
                os.path.join(DATA_DIR,"{sample}_upstream.fasta"),
                os.path.join(DATA_DIR,"{sample}_protein.fasta"),
                os.path.join(DATA_DIR,"{sample}.fna")
            ], 
            sample=config["samples"])
    output:
        touch('gb_process.done')    

rule gb_fetch:
    input:
        expand("{sample}", sample=config["samples"])
    output:
        expand(os.path.join(DATA_DIR,"{sample}.gb"), sample=config["samples"])
    params:
        email = config["output"]["entrez_email"]
    shell:
        "python ../Python_scripts/gb_fetcher.py -i {input} -o {output} -e {params.email}"


rule gb_parser:
    input:
        expand(os.path.join(DATA_DIR,"{sample}.gb"), sample=config["samples"])
    output: 
        upstream = expand(os.path.join(DATA_DIR,"{sample}_upstream.fasta"), sample=config["samples"]),
        protein = expand(os.path.join(DATA_DIR,"{sample}_protein.fasta"), sample=config["samples"]),
        fna = expand(os.path.join(DATA_DIR,"{sample}.fna"), sample=config["samples"])
    shell:
        "python ../Python_scripts/gb_parser.py -i {input} -ou {output.upstream} -op {output.protein} -of {output.fna}"