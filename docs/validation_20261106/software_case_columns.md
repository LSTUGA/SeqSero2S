# Test result column definitions

Each row in `software_cases.tsv` is one executed software workflow case, not an independent biological replicate.

| Column | Meaning |
|---|---|
| serotype | Expected canonical serotype label from the relevant source BioSample. |
| run | SRA run accession for the raw-read isolate associated with the case, including assembly cases. |
| biosample | BioSample accession establishing isolate identity; supplementary nanopore has its own identity. |
| role | Primary matched assembly/Illumina isolate, or supplementary nanopore control. |
| round | Execution group and software stage: complete matrix, quality encoding, compressed assemblies, or final installed package. |
| variant | Descriptive identifier for the command/input variant; see its recorded command in the corresponding JSON. |
| returncode | Child SeqSero2S process exit status; zero indicates normal process completion. |
| software_pass | Exit 0, one valid TSV row, and required allele assembly/stage checks passed. |
| reported_serotype_match | Literal predicted-serotype equality with the metadata label; not an independent accuracy estimate. |
| predicted_profile | Reported O:H1:H2 antigenic profile; a dash is an uncalled antigen. |
| predicted_serotype | Literal predicted-serotype report field, including incomplete identifications. |
| st | Reported MLST sequence type; dash means no sequence type assigned. |
| seconds | Monotonic wall-clock seconds for this process, including its external tools; concurrent cases overlap. |
| source_sha256 | SHA-256 of the exact executed script, including installed shebang where applicable. |
| output | Run-output directory relative to this validation folder. |
