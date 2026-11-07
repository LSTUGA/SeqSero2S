# Software review and Paratyphi B correction validation

Validation date: November 6, 2026 (America/New_York). Base: `89f1f5aca7a8819ee96239592fedd2e737036ada`. The final CLI SHA-256 is recorded in [the correction summary](validation_20261106/paratyphi_b_summary.json).

## Software fixes

The changes replace shell command interpolation with literal subprocess arguments and Python filesystem operations; isolate SPAdes/BLAST work paths; preserve external-command failures; protect existing output directories; fix single-end BWA samse; stream FASTQ input; restore working directories correctly; handle compressed assembly/long-read formats; put stringMLST logs in the run directory; correct the updater's database location; and modernize packaging and CLI checks.

The Biopython requirement was already `~=1.73` (>=1.73,<2) and is unchanged. The starting checkout already used samtools bam2fq. No credit is claimed for introducing either upstream change. Related tracker items: [#1](https://github.com/LSTUGA/SeqSero2S/issues/1), [#3](https://github.com/LSTUGA/SeqSero2S/issues/3), [#4](https://github.com/LSTUGA/SeqSero2S/issues/4), [#5](https://github.com/LSTUGA/SeqSero2S/issues/5).

Historical software validation completed 70 genuine-tool workflow cases and 63 report-equivalence comparisons, plus nine CLI checks, three utility/fault checks and the then-current 20 regressions. The matrix includes full reads and BioSample-matched assemblies for Oranienburg SRR41031109 / GCA_062021734.1, Braenderup SRR41491010 / GCA_062075697.1 and Cerro SRR41464335 / GCA_062070734.1. A separate genuine nanopore control SRR39048279 supplies long-read format checks. Derived header, interleaving, compression and quality-encoding variants preserve source sequence content. These transformations are not additional independent isolates.

Those 70 historical cases span recorded revisions, including stages before the final gzip-assembly repair; the final nine installed-package core cases used the then-final code. They are not presented as 70 reruns of the current Paratyphi B patch. The current final code separately passed all nine core cases with all seven compared fields unchanged. The Braenderup assembly's incomplete `I -:e,h:e,n,z15` call is retained; software execution success is not biological accuracy.

The exact original Debian/GCC installation failure, SRR2200041 header reproducer, and Galaxy/SRR9043663/Python 3.13 deployment were not recreated. Python 3.8/3.11/3.12/3.13 CI is configured; local execution used Python 3.12.16. Remote CI results must be assessed separately.

## Paratyphi B variant correction

The public collection linked by [issue #6](https://github.com/LSTUGA/SeqSero2S/issues/6) and [the original report](https://github.com/denglab/SeqSero2/issues/58) contains 18 Illumina libraries covering 16 EnteroBase uberstrain identifiers, plus a legacy seven-gene-only record. All 18 run accessions match ST28 entries in Hawkey et al. (2024), [Supplementary Data 7](https://doi.org/10.1038/s41467-024-54418-4). They are not the reporter's private isolates or complete 602-strain survey.

Complete normalized SRA archives supplied 19,661,605 pairs and 4,919,225,740 bases. Acquisition performed no trimming or subsampling. Archive verification, FASTQ structure, mate identities, SRA spots/reads-written counts, and independent ENA BioSample/base-count metadata were checked. The existing k-mer workflow retains its R1 selection gate and selected-base cap. ENA read_count equals pairs for ERR424902 and ERR129861, but individual reads for the other 16; this inconsistency was retained rather than used to drop data.

Original EnteroBase assembly download returned HTTP 401. NCBI BioSample matching found 16 records: 15 accessible assemblies and suppressed GCA_023463535.1. Two libraries had no matching assembly in that lookup. The 15 downloaded NCBI assemblies passed published MD5 checks; identity to the inaccessible EnteroBase assemblies is not asserted.

The original marker references differ at fragment position 252. The recovered ST28 sequence has five additional substitutions, including at 248 and 271. These two nearby changes remove all reference 27-mers spanning the distinguishing base. Both original scores therefore tied: 336/530 = 63.396226% in the assemblies and 17 read libraries; ERR424902 had 430/530 = 81.132075% shared read matches. Neither marker had matching variant-specific reference 27-mers. The caller suppressed its ambiguity note and retained plain Paratyphi B. Alignment favored positive 286/291 versus negative 285/291 identities, explaining the microassembly result.

The correction adds [paired probes in that context](PARATYPHI_B_MARKERS.md), takes the maximum per variant and explicitly labels tied/missing evidence unresolved. The new negative-state probe is a designed G252A counterpart, not a claimed natural negative ST28 isolate. All 377 preexisting k-mer entries are unchanged; two entries are added. A full-CLI mixed-state test also exposed and verified the terminal-chunk extraction correction.

Fresh final-code execution passed:

- 18/18 paired-read k-mer cases and 15/15 assembly k-mer cases now call `Paratyphi B var. L(+) tartrate+`, positive 100% versus negative 89.811321% overlap.
- 18/18 microassembly cases retain the positive variant call.
- Two genuine negative-marker controls, NCTC 8299 / SRR7522871 / ST5113 and 173-73 / ERR12737465 / ST86, remain negative in both read modes. Both were selected before outcomes from Supplementary Data 1 entries recording the negative-specific SNP Present.
- Nine prior three-serotype cases retain all seven compared report fields. Two installed-command real-data checks pass. This totals 66 genuine-tool cases, not 66 independent isolates.
- Three source-CLI and two installed-CLI synthetic controls pass. Designed negative, mixed and missing-marker states are separated from genuine sample evidence.
- All 28 regression tests pass. The verified wheel was installed in native seqsero with --no-deps; pip check passed.

All 55 rechecked cohort/control input FASTQ and assembly files retained their acquisition hashes. All six non-serotype fields remain unchanged in the 51 cohort cases: O, H1, H2, identification, antigenic profile and ST. ERR403700 remains MLST-unresolved in both read modes; GCA_023215155.1 remains MLST-unresolved in assembly mode. These exceptions were retained.

This validates marker-state handling for the linked collection and tested controls; it does not independently establish fermentation phenotype, full-gene function, ONT accuracy or universal ST28 accuracy. The marker-panel addition needs scientific review before release.

## Runtime and reproduction

Native macOS ARM64; Python 3.12.16; Biopython 1.88; BWA 0.7.19; Samtools 1.25; BLAST 2.17.0; SPAdes 4.3.0; SRA Toolkit 3.4.1; Bedtools 2.31.1; seqtk 1.5; SalmID 0.1.23; stringMLST 0.6.3; MLST 2.35.0. MLST was installed from verified upstream source because its native Conda recipe could not resolve; the other tools reused the native environment.

Run regressions from the repository root with `python -m unittest discover -s tests -v`. Regenerate the bundled database with `python bin/SeqSero2_update_kmer_database.py` when changing probe sequences.

For each read accession in [the manifest](validation_20261106/sample_manifest.json), retrieve complete normalized SRA using `prefetch --type sra --verify yes RUN`, extract with `fasterq-dump --split-files RUN`, then run `SeqSero2S.py -m k -t 2 -i RUN_1.fastq RUN_2.fastq -d NEW_OUTPUT` and repeat with `-m a` in a different fresh directory. Download assembly URLs in the same manifest, verify their published MD5 and run `-m k -t 4 -i ASSEMBLY.fna`. Inputs and bulky run products are not included in this PR.

## Inspectable evidence

- [Historical software cases](validation_20261106/software_cases.tsv), [column definitions](validation_20261106/software_case_columns.md) and [summary](validation_20261106/software_summary.json).
- [All 18 corrected score comparisons](validation_20261106/paratyphi_b_sample_scores.tsv) and [definitions](validation_20261106/paratyphi_b_score_columns.md).
- [Final 51-case cohort commands/results](validation_20261106/paratyphi_b_workflows.json), [negative controls](validation_20261106/paratyphi_b_controls.json) and [summary](validation_20261106/paratyphi_b_summary.json).
- [Input/accession manifest](validation_20261106/sample_manifest.json) and [evidence formatting notes](validation_20261106/README.md).
