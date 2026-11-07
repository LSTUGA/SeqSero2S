# paratyphi_b_sample_scores.tsv column definitions

Each row is one complete Illumina library from the issue-linked collection: 18 libraries covering 16 EnteroBase uberstrain identifiers. Rows are not all independent isolates.

- `run`: public read-run accession.
- `biosample`: sample accession used to link source metadata and any available assembly.
- `baseline_positive_percent`, `baseline_negative_percent`: pre-fix positive/negative marker reference 27-mer overlap percentages; not nucleotide identity.
- `corrected_positive_percent`, `corrected_negative_percent`: maximum positive/negative probe overlap percentages after the fix. Each probe has 530 distinct reference 27-mers counting both orientations. The read scorer retains its existing R1 selection behavior.
- `corrected_read_kmer_serotype`: actual corrected paired-read k-mer serotype output.
- `read_ST`: corrected paired-read k-mer MLST call; `-` means unresolved.
- `corrected_microassembly_serotype`: actual corrected microassembly serotype output.
- `micro_ST`: corrected microassembly MLST call; `-` means unresolved.
- `assembly`: BioSample-matched NCBI assembly accession, `NA` when none was downloaded. Identity to inaccessible EnteroBase assemblies is not asserted.
- `corrected_assembly_serotype`: actual corrected assembly k-mer output, `NA` when no assembly was run.

All variant labels are marker-based software predictions, not independently measured fermentation phenotypes. The designed negative comparison probe is not a claimed natural negative ST28 isolate.
