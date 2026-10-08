# Green Chemistry
## Contents
- Overview
- Goal and Definition Scope
- Life Cycle Inventory
- Life Cycle Analysis
- Life Cycle Improvements
- Limitations
## Overview
nuCloud utilizes Terminal deoxynucleotidyl transferase to synthesize DNA. Notably, we move towards using enzymes instead of chemical compounds to do the heavy lifting of adding nucleotides into a strand. To further explore the sustainability of this approach, we compared enzymatic and chemical DNA synthesis through an informal life cycle analysis (LCA). LCA is a systematic approach used to evaluate the impacts and efficiency across all stages of a product’s life cycle, from raw material extraction to disposal. LCAs provide critical insights into resource use, waste generation, and potential ecological impacts, thus highlight key areas for improvement and comparison.
## Goal and Definition Scope
### Goal Definition
The goal of this LCA assessment is to assess the environmental impacts of the life cycle (cradle to grave or cradle to cradle, which is to be determined), process to synthesizing DNA strands, as in the context of biomanufacturnig purposes such as data storage or targeted oligonucleotide therapy. Both phosphoramidite synthesis and enzymatic synthesis will be compared to identify the greener alternative for generating DNA strands for long-term data storage.
### System, Functional Unit, and Function of the System
The system object of this assessment of synthesizing DNA strands by two alternative synthesis methods.
The functional unit is the length of DNA obtained, using theoretical stoichmetric amounts of reagents/cofactors that theoretically should produce the same length of DNA.
The function of the system is studied is the potential information storage use of the synthesized DNA strands. The end-of-life scenario of DNA strands is considered to be reusability.
### System Boundaries
The boundaries of the system comprise:
- for enzymatic synthesis:
- production of the enzyme (TdT), according to experimental procedures in Protocols
- for chemical synthesis:
- deprotection and protection of nucleotides as required for synthesis
- for both synthesis methods
- reagents, laboratory equipment employed (with EOL)
- synthesis of DNA strands
## Life Cycle Inventory
### Raw Materials
These are the reagents needed for each process.
### Chemical
For reference, here are the steps that occur:
Solid phase activation
- 3-(triethoxysilyl)propan-1-amine
Activating Agent
- DCC
Phosphoramidite synthesis
- Monomer Synthesis
- dNTP from natural sources
- pyridine
- Trimethylsilyl chloride
- Benzoyl chloride
- Phosphatidylation
- Phosphorus trichloride
- Diisopropylethylamine
- Propanenitrile, 3-hydroxy
- LDA
Chemical Synthesis
- 5’-dimethoxytrityl group removal by TCA [50 s]
- Trichloroacetic acid (TCA) (3%)
- in dichloromethane
- Couple [30 s]
- 0.1 M phosphoramidite monomer
- 0.5 M Tetrazole
- in acetonitrile
- Cap [30 s]
- acetic anhydride/pyridine/THF 1/1/8
- 17.6% w/v N-methyl imidazole
- in acetonitrile
- Wash [30 s]
- acetonitrile
- Flush [10 s]
- Argon
- Oxidize [45 s]
- 0.015 M I2 in water/pyridine/THF 2/20/78
- Wash [30 s]
- acetonitrile
- Flush [10 s]
- argon
Here are the chemicals needed to perform the major steps of chemical DNA synthesis. Steps for chemical DNA synthesis are from CHEM 413: Bioorganic Chemistry1. Below the hazards and disposal methods are taken from each chemical’s CAS form, and engineering controls are based on member’s experience and harzards listed.
[CAPTION] Table 1: Chemicals for Phosphoramidite-based DNA Synthesis
| Chemical
| CAS Hazards
| Engineering Controls Needed for Usage and Storage
| Disposal
| Trichloroacetic acid (TCA) (3%)
| Causes severe skin burns and eye damage. Very toxic to aquatic life with long lasting effects.
| Fumehood
| Dispose in accordance with national/local regulations.
| Protecting Group (DCC)
| Harmful if swallowed. Toxic in contact with skin. May cause an allergic skin reaction. Causes serious eye damage.
| Fumehood
| Dispose in accordance with national/local regulations.
| Dichloromethane
| Causes skin irritation. Causes serious eye irritation. May cause drowsiness or dizziness. Suspected of causing cancer.
| Fumehood
| Dispose in accordance with national/local regulations.
| Phosphoramidite monomer
| NA
| Schlenk lines
| Dispose in accordance with national/local regulations.
| Tetrazole
| Highly flammable liquid and vapor. Harmful if swallowed, in contact with skin or if inhaled. Causes serious eye irritation.
| Fumehood, Flammable cabinet
| Dispose in accordance with national/local regulations.
| Acetic anhydride
| Flammable liquid and vapor. Harmful if swallowed. Causes severe skin burns and eye damage. Fatal if inhaled.
| Fumehood, Flammable cabinet
| Dispose in accordance with national/local regulations.
| Pyridine
| Highly flammable liquid and vapor.
| Fumehood, Flammable cabinet
| Dispose in accordance with national/local regulations.
| THF
| Highly flammable liquid and vapor. Harmful if swallowed. Causes serious eye irritation. May cause respiratory irritation. May cause drowsiness or dizziness. Suspected of causing cancer.
| Fumehood, Flammable cabinet
| Dispose in accordance with national/local regulations.
| N-methyl imidazole
| Combustible liquid. Harmful if swallowed. Toxic in contact with skin. Causes severe skin burns and eye damage. Suspected of damaging fertility or the unborn child.
| Fumehood, Flammable cabinet
| Dispose in accordance with national/local regulations.
| Acetonitrile
| Highly flammable liquid and vapor. Harmful if swallowed, in contact with skin or if inhaled. Causes serious eye irritation.
| Fumehood, Flammable cabinet
| Dispose in accordance with national/local regulations.
| Argon
| Contains gas under pressure; may explode if heated.
| Gas tank
| Contact licensed processional waste disposal service.
| I2
| Harmful if swallowed, in contact with skin or if inhaled. Causes skin irritation. Causes serious eye irritation. May cause respiratory irritation. Causes damage to organs (Thyroid) through prolonged or repeated exposure if swallowed. Very toxic to aquatic life.
| Fumehood
| Dispose in accordance with national/local regulations.
| Ammonia hydroxide
| Causes severe skin burns and eye damage. May cause respiratory irritation. Very toxic to aquatic life. Toxic to aquatic life with long lasting effects.
| Fumehood
| Dispose in accordance with national/local regulations. Cannot be poured down drain.
Notably, many of these reagents require specialized training and engineering safety measures in place to procure and use.
### Manufacturing, Processing, Formulation
[IMG] image.png
[CAPTION] Figure 1: Example of Automated Chemical DNA Synthesis Machinery2
[CAPTION] Table 2: Materials used in Chemical Synthesis
| Material
| Description
| Filter
| standard 1/16 in X-tra fine high-density hydrophobic polyethylene sheet
| Teflon
| Used for chemical resistance
| Bottles
| Storage for reagents
| Tubing
| Connects different parts of the apparatus
| Solenoid Valves
| Control flow of reagents
| Manifold
| Distributes reagents evenly
| 10 vessels
| Storage of each solvent
| Beads
| 0.7 mg beads for 20 nmol
Steps (for 40 nmol of DNA)
- Beads washed three times with 110 ul ACN
- Dry with vacuum pulse
- Detritylation: 4 repetitions of 6 s exposure to 60 ul of TCA followed by four washes with ACN
- Dispense 25 ul of phosphoramidite bases, followed by tetrazole
- After 1 min, two washes with ACN
- 15 s exposure to 20 ul of iodine solution
- Beads given final series of five washes with ACN at end of cycle
- 0.5 ml 30% ammonium hydroxide, vials capped and heated for 1hr at 85C
- Vials are chilled, uncapped, oligomers are evaporated to dryness using 12 nozzle drying manifold
### Enzymatic
The enzymatic synthesis of DNA strands relies on the production of TdT, which requires a series of protocols to successfully isolate it from E. coli. Some of these experiments, such as cloning, transformation, and protein isolation, are routinely performed in microbiology and synthetic biology labs. Figure 2 sequentially displays the steps and protocols used to isolate TdT. In contrast, Figure 3 illustrates the process of DNA strand elongation using the solid-phase platform and the TdT isolated in Figure 2.
[IMG] INPUTS (1).png
[CAPTION] Figure 2: Flowchart showing the system boundaries considered in the LCA of enzyme production and purification.
[IMG] INPUTS (2).png
[CAPTION] Figure 3: Flowchart showing the system boundaries considered in the LCA of solid phase synthesis.
The specific experiments, along with their inputs and outputs considered for this LCA, are detailed in the following document: List of experiments to account for in LCA
We compiled the total raw materials required for TdT production from the previously mentioned document and created a file detailing all the reagents used, including their quantities, manufacturing, distribution, and waste management characteristics. From this document, Table 3 summarizes the raw materials utilized from pre-inoculum to TdT purification, along with key information concerning its analysis under the LCA framework. Note that this table includes only the raw materials and residues from experiments that contributed to the development of our prototype; thus, we didn’t include the totality of all reagents used during the iGEM season.
Here is the file with the complete information of all the raw materials: Raw Materials for TdT enzyme Production at a Laboratory Scale
[CAPTION] Table 3: Summary of complete table of stage 1. Pre-inoculum to TdT Purification
| Category
| Items
| Environmental Impact Overview
| Biological
| DNA, E. coli cells, LB Broth, SOC media, Glycine
| DNA and cells have a low-to-moderate impact, requiring special handling and disposal methods (e.g., bleach, autoclaving)3,4.
| Gels
| Agarose, Agar Powder
| Energy-intensive purification processes. Both products are often imported from overseas (Japan), contributing to a higher transportation footprint. Typically autoclaved after use5,6.
| Chemicals & Reagents
| Kanamycin, Solutions, Buffers, SDS, Acrylamide, Bis-acrylamide, Ammonium persulphate, TEMED, Comassie R250, Glacial acetic acid, Methanol, Dye, Tris base, IPTG, Imidazole, Potassium Phosphate, NaCl
| These items often require energy-intensive chemical synthesis and are typically associated with moderate-to-high ecological footprints during manufacturing. Chemical transportation involves safety concerns, slightly increasing the overall footprint. Most require chemical waste disposal, with some chemicals being toxic to the environment or needing neutralization7,8,9,10.
| Alcohols & Solvents
| Glycerol, Methanol
| Both alcohols and solvents are produced through energy-intensive processes, with moderate ecological footprints. Their transportation also contributes to their overall impact, and need to be disposed of via chemical waste management11,12.
| Salts & Buffers
| Potassium Phosphate, NaCl, Tris base
| Simple salts have low manufacturing and transportation impacts. They can typically be disposed of down the drain, with minimal ecological consequences. However, more complex chemical buffers (e.g., Tris) require chemical waste disposal13.
| Utilities
| Autoclave water and electricity consumption, energy use by machines (centrifuges, incubators, PCR machines)
| Autoclaves and other lab machinery consume significant energy, adding to the overall footprint of the laboratory processes14, 15.
| Residues
| Pipette tips, gloves, PCR tubes, Eppendorf tubes, Falcon tubes, serological pipettes, and other lab disposable materials.
| Plastic-based residues contribute significantly to the ecological footprint due to their production and non-recyclable nature. Items like gloves and pipette tips are typically discarded as biohazard waste16,17,18.
Similarly, Table 4 summarizes the raw materials used for SPS while considering their footprint. The same limitations apply as in Table 3.
[CAPTION] Table 4: Summary of complete table of stage 2. Downstream (DNA strand synthesis—SPS)
| Category
| Items
| Environmental Impact Overview
| Biological
| LB Broth, Neutravidin
| LB broth has a moderate ecological footprint due to biological extracts and salts, with autoclaving required for disposal19.
| Chemicals & Reagents
| Kanamycin, IPTG, Bis-acrylamide Urea, TEMED, APS, Primer, dNTP, NaOH, Biotinylated Primer, Biotin-PEG-SVA, CoCl2, NaOH
| These chemicals require complex synthesis processes, contributing to moderate-to-high ecological footprints. Their transportation, especially with chemical safety concerns, adds to the impact. Most require careful handling and disposal as hazardous or chemical waste7,20,21,8,3,22,23.
| Dyes & Indicators
| Dye
| Small amounts are used, leading to a relatively low manufacturing and transportation footprint. However, chemical waste disposal is still required24.
| Gases
| Nitrogen Gas
| Nitrogen is produced by fractional distillation and transported in pressurized containers, leading to a moderate ecological footprint, particularly in transportation25.
| Residues
| Pipette tips, PCR tubes, Falcon tubes (15 mL & 50 mL), Cuvettes, Kim wipes, Aluminum foil, Eppendorf tubes, Gloves
| Most of these items are plastic-based and non-recyclable, contributing significantly to laboratory waste. Gloves, in particular, have a high environmental footprint due to toxic chemicals used in production, and are typically disposed of as biohazard waste16,26.
## Life Cycle Analysis
### Chemical
Because we do not have the resources to conduct our own analysis of chemical synthesis, we will use reported values for the 12 Principles of Green Chemistry, but highlight the some below that we want to compare to enzymatic synthesis 27:
- Prevention of Waste:
- Chemical synthesis produces large amounts of organic and aqueous waste, require specialized and energy intensive methods for disposal, contributing significantly to environmental pollution.
- Atom Economy: 36% for deoxynucleoside phosphramidies, indicating inefficiency in how raw materials are converted into final products.
- Less Hazardous Chemical Synthesis: Many reagents listed above are hazardous to human health, increasing safety risks for laboratory personnel, and if realized to the environment, can be detrimental to wildlife.
- Safer solvents and Auxiliaries: The reliance on solvents such as acetonitrile, dichloromethane (DCM), triethylamine, and pyridine poses risks due to their toxicity and flammability.
- Catalysis: absence of catalysts in chemical synthesis means reactions can be less efficient and require harsher conditions, further increasing environmental impact.
Other points that contribute to increased energy usage, difficulties in handling + storage and environmental pollution:
- Safety and Handling: Given the toxic and hazardous nature of the reagents, stringent safety protocols are necessary, including the need to store solvents separately and mix them only during synthesis. This increases operational complexity and risk.
- Reaction Environment: The need for specialized equipment (e.g., fume hoods, flammable cabinets) increases the overall energy footprint and cost of the synthesis process. Additionally, the release of vapours, although dilute, still contributes to environmental pollution
- Process Time and Complexity: The multi-step nature of chemical synthesis, which often requires extensive washing and purification, adds time and resources to the overall process.
[IMG] image.png
[CAPTION] Figure 4: Oligonucleotide synthesis cycle27.
A common metric to quantify waste byproducts, leftover reactants, solvent losses, spent catalysts and catalyst supports, is E-factor28. Reports mention that chemical synthesis E-factor is 4700 Kg of waste per 1 Kg of product29. Thus, there are many ways that chemical synthesis can stand to be improved, either through enzymatic means or innovations in chemistry.
Additionally, because of the toxicity/harzadous nature of the reagents being used, the apparatus above requires solvents to be stored separately and only mixed together during synthesis. We will see below that our wet lab team can create a buffer to be used in the reaction mixture, essentially a one-pot reaction for synthesizing DNA with TdT.
The points above will be compared with enzymatic synthesis, and how nuCloud can help tackle these pain points in DNA synthesis.
### Enzymatic
Enzymatic synthesis benefits significantly that due to the enzymes’ nature, it doesn’t require as many chemicals to elongate a DNA strand compared to chemical synthesis. The only significant chemical used is NaOH, and even then, its quantities are in the microliter range. On the other hand, chemical synthesis uses phosphoramidite and involves complex chemical processes that require toxic and volatile reagents. Furthermore, enzymatic synthesis occurs in water and salt buffers, dramatically reducing the ecological footprint of the actual synthesis process30.
While the enzymatic synthesis is friendlier to the environment, it is also important to focus on the production and isolation of the enzymes doing the elongation. Using the experimental data we gathered throughout the iGEM season, we were able to quantify the amount of reagents used to produce ThTdT as well as the physical waste generated. We also considered some of the utilities involved in this process. The largest quantities of reagents used include ~1.6 L of deionized H2O, a total of 912.5 mL for solutions, and 600 mL of methanol. Other significant quantities are 200 mL of glacial acetic acid and 100 g of ammonium persulphate. Compared to chemical synthesis, the chemicals and reagents used in the enzyme production stage are less volatile and toxic.
However, the main environmental challenges arise from media used to grow the cells (950 mL of SOC), reagent transportation, and the total waste generated. Like in most laboratories, the amount of lab plastic waste is significant, around 1.695 Kg of plastic (LDPE, PVC, PP, PS, PE) in our case, and most of it cannot be reused due to contact with biohazardous substances. Moreover, to be properly disposed of, most waste must be autoclaved, which consumes significant energy and adds to the overall footprint of the laboratory processes involved. While chemical reagents, such as bleach, could be used as alternatives, this would make enzymatic synthesis dependent on toxic chemicals. That said, the disposal of organic solvents in chemical synthesis is much more environmentally taxing as it often requires inciniration or a specialized operation 31.
To address these challenges, we developed a microfluidic platform and bioreactor. The microfluidic platform reduces reaction time, improves sensitivity and control, and simplifies automation and parallelization. By precisely controlling reaction volumes, it allows us to use significantly fewer reagents, as the increased surface-to-volume ratio enhances mass transfer and accelerates reaction rates through more molecular collisions. The platform’s design also enables better control over reaction conditions, optimizing enzyme activity and increasing product detection sensitivity, thus reducing waste. Likewise, our bioreactor creates optimal growth conditions, leading to higher cell densities and greater enzyme yields, making the process more resource-effective, especially in large-scale applications.
It is also important to note that once the cells are initially transformed and start producing the plasmid of interest in our bioreactors, the process will become simpler, using fewer chemicals and generating less plastic waste. This will improve disposal efficiency and may open up recycling options during production.
In summary, by streamlining and scaling production with the microfluidic platform and bioreactor, we reduce reagent and plastic waste while improving the overall efficiency of TdT production and isolation. Learn more on our Hardware page.
[IMG] image.png
[CAPTION] Figure 5: Enzyme-catalyzed single base extension using TdT27.
## Life Cycle Improvements
### Chemical
Improvements in chemical synthesis of DNA include moving away from solvent-based methods towards mechanochemistry, by functionalization on an ionic liquid support29, to eventually a one-pot synthesis.
Of course, we can also move towards enzymatic methods, which typically require less toxic reagents, especially if biocatalysts are being used, and simpler procedures. In fact, one-pot synthesis is already archived with enzymatic synthesis, and by extension nuCloud.
### Enzymatic
Improvements in our enzymatic synthesis platform could involve testing different protocols to optimize reaction conditions and reduce the use of toxic reagents in TdT production. Exploring alternatives to harmful chemicals like acrylamide and kanamycin may also be worthwhile, as these substances contribute to a higher carbon footprint due to their energy-intensive production. Shifting to safer alternatives could lower both environmental and health impacts. Additionally, optimizing equipment like autoclaves through batch processing or integrating alternative energy sources could further reduce energy consumption. Lastly, enhancing bioreactor designs for easier cell harvesting and purification would significantly cut resource demands and waste generated.
## Limitations
This LCA-inspired page has several key limitations that need to be addressed. First, we were unable to quantify the electrical and water usage of lab equipment, such as autoclaves, bioreactors, and common devices like PCR machines, which is crucial for a clearer understanding of the process’s resource demands. Additionally, we didn’t establish a chemical synthesis control reaction to accurately measure reagent consumption and waste generation, which would have enabled a better comparison between the two in terms of plastic waste and reagent use. Another important factor we couldn’t include, due to lack of data, is the ecological footprint of transporting reagents. Finally, this page lacks a standardized unit for quantitative comparison between chemical and enzymatic methods. Using a common environmental footprint unit would have allowed for a more thorough evaluation instead of relying solely on qualitative assessments. For the next iteration of this document, the above mentioned will be included.
## References
“Chemistry 413: Bioorganic Chemistry | UBC Chemistry.” Chem.ubc.ca, 2023, www.chem.ubc.ca/chemistry-413-bioorganic-chemistry-11. Accessed 2 Oct. 2024. ↩
Sindelar, Linda E, and Joe M Jaklevic. “High-Throughput DNA Synthesis in a Multichannel Format.” Nucleic Acids Research, vol. 23, no. 6, 1 Jan. 1995, pp. 982–987, academic.oup.com/nar/article/23/6/982/2400928, https://doi.org/10.1093/nar/23.6.982. Accessed 1 Oct. 2024. ↩
University of Washington. (2020). Biohazardous Waste | EHS. Www.ehs.washington.edu. https://www.ehs.washington.edu/biological/biohazardous-waste ↩ ↩2
Public Health Agency of Canada. (2011). Pathogen Safety Data Sheets: Infectious Substances – Escherichia coli, enterotoxigenic - Canada.ca. Canada.ca. https://www.canada.ca/en/public-health/services/laboratory-biosafety-biosecurity/pathogen-safety-data-sheets-risk-assessment/escherichia-coli-enterotoxigenic.html ↩
Armisen, R. (n.d.). CHAPTER 1 - PRODUCTION, PROPERTIES AND USES OF AGAR. Www.fao.org. https://www.fao.org/4/x5822e/x5822e03.htm ↩
University of Toronto. (n.d.). Biological Waste Disposal. Environmental Health & Safety. Retrieved September 30, 2024, from https://ehs.utoronto.ca/laboratory-hazardous-waste-management-and-disposal-manual/biological-waste-disposal/ ↩
Polianciuc, S. I., Gurzău, A. E., Kiss, B., Ștefan, M. G., & Loghin, F. (2020). Antibiotics in the environment: causes and consequences. Medicine and Pharmacy Reports, 93(3). https://doi.org/10.15386/mpr-1742 ↩ ↩2
Sigma Aldrich. (2024). NMR Chemical Shifts of Impurities Charts. Merck, 1(1). https://www.sigmaaldrich.com/MX/en/technical-documents/technical-article/genomics/cloning-and-expression/blue-white-screening ↩ ↩2
Santa Cruz Biotechnology. (n.d.). Material Safety Data Sheet Tris base sc-3715 Section 1 -CHEMICAL PRODUCT AND COMPANY IDENTIFICATION PRODUCT NAME STATEMENT OF HAZARDOUS NATURE CONSIDERED A HAZARDOUS SUBSTANCE ACCORDING TO OSHA 29 CFR 1910.1200. NFPA SUPPLIER PRODUCT USE. Retrieved September 30, 2024, from https://datasheets.scbt.com/sc-3715.pdf ↩
Tolomeu, H. V., & Fraga, C. A. M. (2023). Imidazole: Synthesis, Functionalization and Physicochemical Properties of a Privileged Structure in Medicinal Chemistry. Molecules (Basel, Switzerland), 28(2), 838. https://doi.org/10.3390/molecules28020838 ↩
Bansod, Y., Crabbe, B., Forster, L., Ghasemzadeh, K., & D’Agostino, C. (2024). Evaluating the environmental impact of crude glycerol purification derived from biodiesel production: A comparative life cycle assessment study. Journal of Cleaner Production, 437, 140485. https://doi.org/10.1016/j.jclepro.2023.140485 ↩
Chen, Z., Shen, Q., Sun, N., & Wei, W. (2019). Life Cycle Assessment of Typical Methanol Production routes: the Environmental Impacts Analysis and Power Optimization. Journal of ↩
fishersci. (2021). Material Safety Data Sheet, Potassium Phosphate. Fishersci.com. https://fscimage.fishersci.com/msds/19543.htm ↩
Earth, S. (2022, July 26). The Impact Of Autoclave On Environment. Sigma Earth. https://sigmaearth.com/impact-of-autoclave/ ↩
Lopez, J. B., Jackson, D., Gammie, A., & Badrick, T. (2017). Reducing the Environmental Impact of Clinical Laboratories. The Clinical Biochemist Reviews, 38(1), 3–11. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5548370/ ↩
Umapathy, A. (2022, July 27). 7 Types of Plastic: How do they Impact our Environment? - Purpose Rising Blog. RePurpose Global. https://repurpose.global/blog/post/7-types-of-plastic ↩ ↩2
Espinoza, R. (2020, November 24). How Hazardous Waste Disposal Affects The Environment. Idrenvironmental.com. https://blog.idrenvironmental.com/how-hazardous-waste-disposal-affects-the-environment ↩
Klaudia Habek. (2024, September 9). Are Paper Towels Bad for the Environment? Reel. https://www.reelpaper.com/blogs/reel-talk/are-paper-towels-bad-for-the-environment ↩
Wikipedia. (2019b, September 3). Lysogeny broth. Wikipedia; Wikimedia Foundation. https://en.wikipedia.org/wiki/Lysogeny_broth ↩
Birk, R., Ikan, A., Benami Bravdo, Braun, S., & Oded Shoseyov. (1997). Synthesis of lsopropyl-1-thio-Β-D-glucopyranoside (IPTGlc), an inducer ofaspergillus niger b1 Β-glucosidase production. Applied Biochemistry and Biotechnology, 66(1), 25–30. https://doi.org/10.1007/bf02788804 ↩
Masjedi, S. K., Kazemi, A., Moeinnadini, M., Khaki, E., & Olsen, S. I. (2024). Urea production: An absolute environmental sustainability assessment. Science of the Total Environment, 908, 168225. https://doi.org/10.1016/j.scitotenv.2023.168225 ↩
Letchumi Thannimalay. (2013, February). Life Cycle Assessment of Sodium Hydroxide. ResearchGate; American-Eurasian Network for Scientific Information (AENSI). https://www.researchgate.net/publication/236900871_Life_Cycle_Assessment_of_Sodium_Hydroxide#full-text ↩
Parveen, N., Chowdhury, S., & Goel, S. (2022). Environmental impacts of the widespread use of chlorine-based disinfectants during the COVID-19 pandemic. Environmental Science and Pollution Research, 29(57). https://doi.org/10.1007/s11356-021-18316-2 ↩
Dorri, Y., & Kurien, B. T. (2010). Environmentally safe removal/disposal of Coomassie Brilliant Blue from gel destain and used gel stain. Analytical Biochemistry, 404(2), 193–196. https://doi.org/10.1016/j.ab.2010.05.022 ↩
NiGen. (2018, May 22). How to Separate Nitrogen From Air. NiGen; NiGen. https://nigen.com/how-separate-nitrogen-from-air-ways-extract-nitrogen/ ↩
climatiq. (2019). Emission Factor: Aluminium foil - Worldwide | Materials and Manufacturing | Metals | Global | Climatiq. Climatiq.io. https://www.climatiq.io/data/emission-factor/f9e37466-9525-4e49-9bdb-b227059095e4 ↩
Andrews, Benjamin I., et al. “Sustainability Challenges and Opportunities in Oligonucleotide Manufacturing.” The Journal of Organic Chemistry, vol. 86, no. 1, 30 Nov. 2020, pp. 49–61, https://doi.org/10.1021/acs.joc.0c02291. ↩ ↩2 ↩3
Green Chemistry and the Ten Commandments of Sustainability (Manahan). (2017, February 21). Chemistry LibreTexts. https://chem.libretexts.org/Bookshelves/Environmental_Chemistry/Green_Chemistry_and_the_Ten_Commandments_of_Sustainability_(Manahan) ↩
Johnston, Christopher, et al. “Applications of Mechanochemistry for the Synthesis of DNA on Ionic Liquid Supports.” Chemistry–Methods, vol. 1, no. 8, 5 May 2021, pp. 382–388, https://doi.org/10.1002/cmtd.202100002. ↩ ↩2
Nguyen, B., Sinistore, J., Smith, J., Arshi, P., Johnson, L., Kidman, T., Dicaprio, T., Carmean, D., & Strauss, K. (2016). Architecting Datacenters for Sustainability: Greener Data Storage using Synthetic DNA. Microsoft. https://www.microsoft.com/en-us/research/uploads/prod/2020/12/2020_07_13_EGG2020_Paper_Final.pdf ↩
Government of Canada. (2020). Cross-border Movement of Hazardous Waste and Hazardous Recyclable Materials Regulations: Guide to hazardous waste and hazardous recyclable materials classification - Canada.ca. Canada.ca. https://www.canada.ca/en/environment-climate-change/services/managing-reducing-waste/cross-border-regulations/guide-hazardous-waste-material-classification.html#app-02 ↩
[IMG]
