class worfklow_dict:
    def __init__(self):
        self.help_general = {
            "input": "In case of vcf, the input file must end with .csv and in case of plink, it must end with .p.csv.(see ./example_files/example_vcf_input.csv)",
            "outdir": "Path to the directory, where all the outputs will be stored. If the directory is not present, it will be created.",
            "sample_map": "Path to the sample map file(must end with .map).Format:first column as sample id and second column as population id.Required only if the input is vcf.",
            "color_map": "Path to the file containing population name as first column and color in hex codes as second column.Must end with .map",
            "outprefix": "prefix of the outputs generated by the workflow",
            "max_chrom": "Maximum number of chromosomes to be considered for the analyses, note that the workflow deals only with the autosomal chromosomes.",
            "allow_extra_chrom": "set this argument to true if the chromosome id contains a string, default: false",
            "chrom_length_map": "If the inputs are plink binary files, map file is needed to set the chromosome id and its respective size in the vcf header, If not provided, the greatest coordinate for each chromosome will be considered as its total size. The file must end with .map.",
            "chrom_id_map": "in case, chromosome id is string, provide a .map file: original chromosome id in first column and its corresponding numerical chromosome id in second column",
            "fasta": "If the inputs are plink binary files, fasta file is needed to set the reference allele in the converted vcf files. If not provided, the major allele will be set as the reference allele for all positions for all analyses",
            "outgroup": "The population id to be used as an outgroup in the following analyses: 1). treemix --> as a root in ML phylogenetic tree, 2). Fst- and IBS-based NJ clustering --> as a root, 3). signature of selection --> to determine the ancestral and derived alleles",
            "window_size": "window size to be used for the various analyses --> summary statistics, tajimas's D, pi, fst, sweepfinder2",
            "step_size": "step size to be used for the analysis of vcftools",
            "indiv_summary": "whether to calculate individual-based and population-based sumamry statistics"
        }

        self.param_general = {
            "input": "null",
            "outdir": "scalepopgn",
            "sample_map": "null",
            "color_map": "null",
            "outprefix": "scalepopgen",
            "max_chrom": 29,
            "allow_extra_chrom": False,
            "chrom_length_map": "null",
            "chrom_id_map": "null",
            "fasta": "null",
            "outgroup": "null",
            "window_size": 50000,
            "step_size": 50000,
            "indiv_summary": False
        }

        self.help_indi_filtering = {
            "apply_indi_filters": "Perform sample filtering?",
            "king_cutoff": "Threshold of relatedness to remove samples",
            "mind": "Threshold of missing genotypes to remove samples",
            "rem_indi": "Remove custom samples",
        }

        self.param_indi_filtering = {
            "apply_indi_filters": False,
            "king_cutoff": "null",
            "mind": "null",
            "rem_indi": "null",
        }

        self.help_snp_filtering = {
            "apply_snp_filters": "Perform site filtering?",
            "rem_snps": "Remove custom sites",
            "maf": "Threshold of minor allele frequency to remove sites",
            "min_meanDP": "Lower threshold of average depth to remove sites",
            "max_meanDP": "Upper threshold of average depth to remove sites",
            "hwe": "Threshold of HWE p-value to remove sites",
            "max_missing": "Threshold of missing genotypes to remove sites",
            "minQ": "Threshold of quality to remove sites",
            "indiv_summary": "Calculate sample-based summary statistics?",
        }

        self.param_snp_filtering = {
            "apply_snp_filters": False,
            "rem_snps": "null",
            "maf": "null",
            "min_meanDP": "null",
            "max_meanDP": "null",
            "hwe": "null",
            "max_missing": "null",
            "minQ": "null",
        }

        self.help_genetic_structure = {
            "genetic_structure": "Perform analyses of genetic structure? Setting this to false, will skip all the analyses mentioned below",
            "rem_indi_structure": "Remove custom samples",
            "ld_filt": "Filter sites based on linkage disequilibrium using plink2? Setting this to False, will skip the step of LD filtering",
            "ld_window_size": "Window size for LD filtering",
            "ld_step_size": "Step size for LD filtering",
            "r2_threshold": "Threshold of r2 for LD filtering",
            "smartpca": "Perform principal component analysis",
            "smartpca_param": "Additional parameters for PCA",
            "pca_plot_yml": "The yml file to plot interactive PCA results",
            "marker_map": "Marker shapes for PCA plot",
            "chrom_map": "Map file to replace chromosome ids (see ./example_files/oldchrom_newchrom.map)",
            "admixture": "Perform analysis with Admixture?",
            "start_k": "Starting K-value for Admixture",
            "end_k": "Ending K-value for Admixture",
            "admixture_args": "Set additional parameters of ADMIXTURE tools",
            "admixture_colors": "Custom colors for Admixture plot",
            "admixture_plot_pop_order": "Order of populations for Admixture plot",
            "admixture_plot_yml": "The yml file to plot interactive Admixture results",
            "pairwise_global_fst": "Calculate pairwise Fst distances between each pair of populations",
            "fst_plot_yml": "The yml file to plot interactive Fst-based NJ tree",
            "ibs_dist": "Calculate 1-ibs distances between each pair of samples",
            "ibs_plot_yml": "The yml file to plot interactive IBS-based NJ tree",
        }

        self.param_genetic_structure = {
            "genetic_structure": False,
            "rem_indi_structure": "null",
            "ld_filt": False,
            "ld_window_size": 50,
            "ld_step_size": 10,
            "r2_threshold": 0.1,
            "smartpca": False,
            "smartpca_param": "null",
            "pca_plot_yml": "scalepopgen/extra/plots/pca.yml",
            "marker_map": "null",
            "chrom_map": "null",
            "admixture": False,
            "start_k": 2,
            "end_k": 21,
            "admixture_args": "--cv=5",
            "admixture_colors": "scalepopgen/extra/hexcolorcodes.txt",
            "admixture_plot_pop_order": "null",
            "admixture_plot_yml": "scalepopgen/extra/plots/admixture.yml",
            "pairwise_global_fst": False,
            "fst_plot_yml": "scalepopgen/extra/plots/fst_nj.yml",
            "ibs_dist": False,
            "ibs_plot_yml": "scalepopgen/extra/plots/ibs_nj.yml",
        }

        self.help_treemix = {
            "treemix": "whether to run the treemix workflow",
            "k_snps": "windows of size n SNPs to be grouped together for treemix analysis",
            "treemix_args": "Set additional parameters of treemix tools",
            "n_bootstrap": "number of bootstrapping to run for treemix analyis (without migration edge)",
            "set_random_seed": "whether to set the seed for random number generation",
            "n_mig": "total number of migration edges to be added, set this to zero to skip adding migration edges",
            "n_iter": "number of iterations to be carried out for each migration edge value",
            "rand_k_snps": "whether or not to randomized the values of k_snps for each iteration of n_iter",
        }

        self.param_treemix = {
            "treemix": False,
            "k_snps": 500,
            "treemix_args": "null",
            "n_bootstrap": 5,
            "set_random_seed": True,
            "n_mig": 4,
            "n_iter": 3,
            "rand_k_snps": True,
        }

        self.help_general_sig_sel = {
            "min_sample_size": "minimum sample size per population to be required to be included in signature of selection analyses",
            "skip_pop": "the path to the text file containing population IDs to be excluded from all the analyses of this section",
            "skip_outgroup": "whether or not to include outgroup in the signature of selection analyses",
            "selection_plot_yml": "the path to the yaml file containing the parameters to plot interactive Manhattan plot",
            "perc_threshold": "cutoff to consider regions as candidates of selection",
        }

        self.param_general_sig_sel = {
            "min_sample_size": "null",
            "skip_pop": "null",
            "skip_outgroup": False,
            "selection_plot_yml": "scalepopgen/extra/plots/manhattanplot.yml",
            "perc_threshold": 0.01,
        }

        self.help_vcftools_sel = {
            "skip_chromwise": "whether to run vcftools separately for each chromosome for each population, setting this to true will concatenate the chromosomes for each population before running the analysis",
            "pairwise_local_fst": "whether to calculate pairwise fst in windows or for each SNPs for every possible pair of population",
            "fst_one_vs_all": "whether to calculate pairwise fst in windows for each SNPs for pairwise comparison, where another population in pair is the the pooled samples excluding the population which it is being compared with",
            "tajimas_d": "whether to calculate Tajima's D statistic",
            "pi_val": "whether to calculate pi values",
        }

        self.param_vcftools_sel = {
            "skip_chromwise": False,
            "pairwise_local_fst": False,
            "fst_one_vs_all": False,
            "tajimas_d": False,
            "pi_val": False,
        }

        self.help_sweepfinder2 = {
            "est_anc_alleles": "whether to run the workflow to detect ancestral alleles using est-sfs",
            "anc_alleles_map": "the map file containing information about ancestral allele at each SNP position",
            "sweepfinder2": "whether to run sweepfinder2 workflow",
            "sweepfinder2_model": "the type of model in sweepfinder2 to run",
            "grid_space": "user-defined space between grid-points, option g of SweepFinder2",
            "grid_points": "user-defined number of equally spaced points to be tested, option G of SweepFinder2",
            "recomb_map": "the path to the file containing information about recombination map file as required by sweepfinder2, if not provided, recombination file will be created using default recombination rate value",
        }

        self.param_sweepfinder2 = {
            "sweepfinder2": False,
            "sweepfinder2_model": "l",
            "est_anc_alleles": False,
            "anc_alleles_map": "null",
            "grid_space": 50000,
            "grid_points": "null",
            "recomb_map": "null",
        }

        self.help_phasing = {
            "skip_phasing": "whether to skip the phasing step",
            "phasing_panel": "a map file containing first column as chromosome id and second column as the path to its respective vcf reference panel",
            "phasing_map": "a map file containing first column as chromosome id and second column as the path to its recombination map file",
            "beagle5": "phase genotypes using beagle5",
            "burnin": "maximum burnin iterations (in beagle5)",
            "iteration": "phasing iterations (in beagle5)",
            "ne": "effective population size (in beagle5)",
            "impute": "impute ungenotyped markers",
            "beagle5_args": "set additional parameters of beagle5 tool",
            "shapeit5": "phase genotypes using shapeit5",
            "shapeit5_args": "set parameters of shapeit5 tool",
        }

        self.param_phasing = {
            "skip_phasing": False,
            "phasing_panel": "null",
            "phasing_map": "null",
            "beagle5": False,
            "burnin": 3,
            "iteration": 12,
            "ne": 100000,
            "impute": False,
            "beagle5_args": "null",
            "shapeit5": True,
            "shapeit5_args": "null",
        }

        self.help_selscan = {
            "ihs": "whether to run ihs analysis as implemented in selscan",
            "xpehh": "whether to run xpehh analysis as implemented in selscan",
            "selscan_map": "path to a map file containing first column as chromosome id and second column as the path to its recombination map as required by selscan",
            "ihs_args": "arguments for ihs analysis in selscan",
            "xpehh_args": "arguments for xpehh analysis in selscan",
            "ihs_norm_args": "additional arguments to normalize ihs score",
            "xpehh_norm_args": "additional arguments to normalize xpehh score",
        }

        self.param_selscan = {
            "ihs": False,
            "xpehh": False,
            "selscan_map": "null",
            "ihs_args": "null",
            "xpehh_args": "null",
            "ihs_norm_args": "null",
            "xpehh_norm_args": "null",
        }

        self.tool_args = {
            "admixture_args": [
                "--seed",
                "-m",
                "--method",
                "-a",
                "--acceleration",
                "-C",
                "-c",
                "-B",
                "--cv",
            ],
            "treemix_args": [
                "-noss",
                "-cor_mig",
                "-se",
            ],
            "beagle5_args": [
                "phase-states",
                "imp-states",
                "cluster",
                "ap",
                "gp",
                "err",
                "em",
                "window",
                "overlap",
                "seed",
            ],
            "shapeit5_args": [
                "--seed",
                "--pedigree",
                "--haploids",
                "--mcmc-iterations",
                "--mcmc-prune",
                "--mcmc-noinit",
                "--pbwt-modulo",
                "--pbwt-depth",
                "--pbwt-mac",
                "--pbwt-mdr",
                "--pbwt-window",
                "--hmm-window",
                "--hmm-ne",
                "--filter-maf",
            ],
            "ihs_args": [
                "--alt",
                "--cutoff",
                "--ehh-win",
                "--gap-scale",
                "--ihs-detail",
                "--maf",
                "--max-extend",
            ],
            "xpehh_args": [
                "--alt",
                "--cutoff",
                "--ehh-win",
                "--gap-scale",
                "--ihs-detail",
                "--maf",
                "--max-extend",
            ],
            "ihs_norm_args": [
                "--bins",
                "--bp-win",
                "--crit-percent",
                "--crit-val",
                "--min-snps",
                "--qbins",
                "--winsize",
            ],
            "xpehh_norm_args": [
                "--bins",
                "--bp-win",
                "--crit-percent",
                "--crit-val",
                "--min-snps",
                "--qbins",
                "--winsize",
            ],
        }
        self.dict_list = [
            self.param_general,
            self.param_indi_filtering,
            self.param_snp_filtering,
            self.param_genetic_structure,
            self.param_treemix,
            self.param_general_sig_sel,
            self.param_vcftools_sel,
            self.param_sweepfinder2,
            self.param_phasing,
            self.param_selscan,
        ]

        self.citation_dict = {
            "apply_indi_filters": [
                "./bibtex/plink.bibtex",
                "./bibtex/vcftools.bibtex",
            ],
            "apply_snp_filters": [
                "./bibtex/plink.bibtex",
                "./bibtex/vcftools.bibtex",
            ],
            "ld_filt": ["./bibtex/plink.bibtex"],
            "pca": ["./bibtex/eigensoft.bibtex"],
            "admixture": ["./bibtex/admixture.bibtex"],
            "pairwise_global_fst": ["./bibtex/plink.bibtex", "./bibtex/toytree.bibtex"],
            "ibs_dist": ["./bibtex/plink.bibtex", "./bibtex/ete3.bibtex"],
            "treemix": ["./bibtex/treemix.bibtex"],
            "selscan": ["./bibtex/selscan.bibtex"],
            "beagle5": ["./bibteX/beagle.bibtex"],
            "shapeit5": ["./bibtex/shapeit5.bibtex"],
            "fst": ["./bibtex/vcftools.bibtex"],
            "tajimas_d": ["./bibtex/vcftools.bibtex"],
            "pi_val": ["./bibtex/vcftools.bibtex"],
            "ihs": [
                "./bibtex/ihs.bibtex",
                "./bibtex/selscan.bibtex",
                "./bibtex/ehh.bibtex",
            ],
            "xpehh": [
                "./bibtex/xpehh.bibtex",
                ".bibtex/selscan.bibtex",
                "./bibtex/ehh.bibtex",
            ],
        }
