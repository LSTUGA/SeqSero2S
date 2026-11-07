# Paratyphi B marker sequence contexts

The marker decision compares the best dt-positive probe score with the best dt-negative probe score. It does not use MLST to assign a variant. Equal or missing evidence is reported as `Paratyphi B (tartrate variant unresolved)` with an explanatory note.

The original two 291-base gntR/STM3356-associated reference probes are retained without alteration. Two additional probes cover the ST28 context reported in [SeqSero2S issue #6](https://github.com/LSTUGA/SeqSero2S/issues/6) and [SeqSero2 issue #58](https://github.com/denglab/SeqSero2/issues/58):

- `gntR-family-regulatory-protein_dt-positive_ST28-context__291`: the sequence independently recovered from all 15 public BioSample-matched NCBI assemblies in the linked collection, also matching the reporter's proposed sequence. Relative to the original positive probe it has substitutions at fragment positions 114, 118, 140, 248, and 271, while retaining G at position 252.
- `gntR-family-regulatory-protein_dt-negative_ST28-context__291`: a designed counterpart in the same context with position 252 changed from G to A, the difference between the original positive and negative probes. This is an allele-state comparison probe, **not a claimed naturally occurring negative ST28 isolate**. Including both states makes the comparison symmetric and avoids favoring the positive state merely because its flanking context is represented.

All coordinates are 1-based within the probe fragments, not chromosome coordinates. Each pair differs at only position 252. The new probes each produce 530 distinct 27-mers counting both orientations, including 54 variant-discriminating k-mers. All existing reference sequences and preexisting k-mer sets are unchanged. The bundled `antigens.pickle` is regenerated with `SeqSero2_update_kmer_database.py` and contains 379 keys instead of 377.

The former score assignment depended on dictionary order when multiple probes for one variant were present. Taking the maximum within each variant group makes the result independent of that order in both k-mer and microassembly workflows.

Assembly k-mer extraction also includes the terminal sequence chunk. Previously, its exclusive slice endpoint omitted that chunk, producing an incomplete score for a marker on a short terminal contig. This matters when comparing both marker states, including the synthetic mixed-state control.

These changes classify the marker state; they do not independently measure fermentation phenotype or establish whole-gene functionality. New sequence contexts may still be unresolved and should not be inferred from ST alone. See the [validation report and sample-level evidence](VALIDATION.md).
