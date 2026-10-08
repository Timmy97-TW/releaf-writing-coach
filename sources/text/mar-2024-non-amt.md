[IMG]
Home  Non-Agrobacterium Mediated Transformation
Non-Agrobacterium Mediated Transformation
An alternative to established Plant Genetic Engineering methods
Contents
Introduction
Understanding Agrobacterium-Mediated Transformation
Designing an Orthogonal Virulence Plasmid
Removal of Pathogenic Genes
Selecting Virulence Genes
Selecting Novel Bacteria Chassis
Building an Orthogonal Virulence Plasmid
An Orthogonal Virulence Plasmid
Outlook
References
Introduction
In the quest for sustainable materials and innovative agricultural practices, Taraxacum kok-saghyz (TKS), commonly known as the Russian dandelion, has emerged as a promising source of natural rubber. This subproject proposes a novel strategy for improving transformation efficiency in TKS: Non-Agrobacterium Mediated Transformation (non-AMT). By utilizing innovative bacterial chassis distinct from Agrobacterium, this method seeks to unlock the potential of TKS for increased rubber production, enhanced biomass, and other traits essential for sustainable agriculture, as described by Dr. Eickmeyer. The dense patent landscape surrounding Agrobacterium-based transformation poses significant challenges, particularly for small companies and startups that may lack the resources to navigate these complexities. As Vanessa Kuhl aptly noted,
> It is an insane amount of work to read through the claims and all the patents and see whether what you are planning somehow infringes one of the patents on this long list.
- Vanessa Kuhl
By developing non-AMT methods, our project not only circumvents the restrictive patents associated with Agrobacterium-based methods but also fosters new avenues for innovation. This approach provides vital alternatives to existing technologies, democratizing plant transformation and enabling smaller enterprises to engage in agricultural biotechnology without the burden of navigating complex intellectual property issues. Dheeraj Rathore emphasizes the importance of this shift, stating,
> Innovation and alternatives are key [...] to overcome the existing patent issue.
- Dheeraj Rathore
Understanding Agrobacterium-Mediated Transformation
Bacteria based plant transformation revolves around two main parts, the virulence (vir) genes, which facilitate plant transformation and the Transfer-DNA (T-DNA), which is the DNA region actually transformed to the host plant. The T-DNA thereby is the DNA, which is being transformed into the host cell. It is recognized by the transformation machinery because it is flanked by border motifs on both sides. The native T-DNA of Agrobacterium rhizogenes K599 carries root-inducing genes, which trigger the pathogenic hairy root phenotype in the host plant. The regions responsible for this phenotype are the rol and ORF 12-14 genes.
In scientific applications, the native transformation system is separated, making use of a binary plasmid system. Therefore, the native virulence plasmid does not contain a T-DNA, being disarmed. The Gene of interest (Goi) is located on a second, so-called binary plasmid, where the Goi is flanked by the T-DNA borders, making it possible to transform it. This system greatly simplifies plant transformation, since only the (often) smaller binary plasmid needs to be exchanged. Commercially available A. tumefaciens strains are therefore often disarmed, for example the commonly used strain GV3101, which means it does not contain any pathogenic genes on its virulence plasmid. However, it is vital that the origin of the binary plasmid is chosen with care, since a compatibility with the virulence plasmid is required. If the origins are not compatible, a bacteria culture will lose one of the plasmids over time.
The situation of the vir genes on the other hand is more complex, as one set of virulence genes is found on Agrobacterium's megaplasmid, while other virulence genes can be found on the chromosome. Firstly, virA codes for a receptor-kinase, which possesses a periplasmic domain and a linker domain, which enables the protein to sense phenolic compounds and monosaccharides respectively. These compounds are released when plant tissue is damaged, enabling the bacterium to specifically sense the presence of wounded and likely susceptible plants with virA. In the presence of these compounds VirA autophosphorylates, and passes its phosphate on to VirG, activating this protein. VirG again is a transcription factor, whose expression is controlled by two promoters, whereby one is activated by a low PH-environment, found in the apoplast of plant cells, while the other is induced by phenolic compounds (1). However, all of these induction processes are not directly dependent on the mentioned compounds, since their recognition is facilitated in a large part, by a chromosomal signal cascade.
VirG functions as a master regulator for the virulence genes that, upon activation, triggers the expression of key vir genes necessary for successful infection and transfer of the T-DNA into the host cell. A multitude of genes have been shown to be indispensable for successful plant transformation, being the virB, virC, virD and virE clusters (2). These vir genes encode a set of proteins with distinct functionality: virC and virD are involved in T-DNA excision and processing, virE coats and protects the T-DNA during its transfer, while the virB operon forms the Type IV Secretion System (T4SS) responsible for delivering the T-DNA into plant cells (3). Therefore, when considering our non-AMT approach we placed great care on ensuring genetic homologues of these genes to be present on our final virulence plasmid.
Designing an Orthogonal Virulence Plasmid
To efficiently enable novel bacteria to facilitate plant transformation, a virulence plasmid is required, with its genes decoupled from the donor's chromosomal background. Therefore, we needed to consider a multitude of factors when designing our decoupled virulence plasmid: high transformation efficiency, easy induction of the virulence region, genomic decoupling, and the use of root-inducing genes in the T-DNA are key factors. High transformation efficiency is especially important for producing fast, high-quality results in both laboratory and industrial settings, minimizing the need for labor-intensive screenings. An easy induction of the virulence region significantly increases ease of handling in the lab, since balancing multiple different inductors at the same time, might prove challenging. Moreover, since non-agrobacteria will lack the chromosomal machinery to register the native inductors, these cannot be used to induce virG. Therefore, chromosomal decoupling is highly important, since it enables researchers later on to easily transfer the virulence plasmid to a different bacterial chassis, enabling fast adaptation and research for novel plant species. Lastly the inclusion of the root inducing genes of Agrobacterium rhizogenes K599 is of great interest to us.
A recent publication from Cao et al. showed an extremely fast stable transformation protocol for T. kok-saghyz, which serves as the basis of our rapid stable transformation protocol. Crucially, they show an increased transformation efficiency for A. rhizogenes, compared to other Agrobacteria (4). We hypothesize this to be due to the specific set of root inducing genes present on its T-DNA, specifically ORF13a.
Removal of Pathogenic Genes
Literature has shown that Agrobacterium rhizogenes K599 works for the "extremely simplified cut-dip-budding" method. We hypothesize this effectiveness is due to the specific set of root-inducing genes present in A. rhizogenes K599, particularly the presence of ORF13a. However, formation of the "hairy root" phenotype is pathogenic, significantly affecting the growth and overall health of T. kok-saghyz (5). It is therefore desirable to remove these root-inducing genes once successful bud formation has occurred. The solution we propose for this problem is the implementation of the well-known and extensively characterized Cre/Lox system. Our approach involves flanking the root-inducing (Ri) genes with loxP sites and regulating the expression of Cre-recombinase using a heat-inducible plant promoter (e.g., BBa_K5088050, BBa_K5088051). When activated, Cre would cut the DNA at both loxP sites, thereby excising the root-inducing genes. It is critical that these promoters are tightly regulated, as even minor levels of Cre expression could prematurely excise the Ri genes. Once the buds have successfully formed, we can remove the pathogenic Ri genes at any chosen time by applying a heat shock to the plant, which activates Cre expression and excises the undesirable genes. This allows us to harness the benefits of A. rhizogenes K599 while eliminating its negative impacts on plant health. To test Cre functionality in dandelion we built a test construct (Figure 1). Sadly, we were not able to test this construct, due to time constraints of the iGEM season.
[IMG]
Figure 1: SBOL depiction of a construct for testing Cre activity (e.g. BBa_K5088651, BBa_K5088652)
This construct enables us to test the functionality of cre, as well as the functionality of the corresponding promoter. The CDS of the Cre-recombinase is deliberately oriented opposite to the other Transcription units, in order to prohibit read-through-events onto the CDS. When expressed, Cre will cut the DNA at the LoxP sites and in the process cut out the TU of Cre and mCherry. In the same way the promoter will be assembled with the CDS of eGFP, thereby allowing for eGFP expression. This allows us to measure the Cre recombinase activity, based on the eGFP fluorescence intensity.
Selecting Virulence Genes
Since the desirable virulence plasmid shall be fully orthogonal and easily inducible, the first virulence gene we investigated was virG, being the master switch for the virulence region. However, since it is controlled by two promoters as well as by virA, it must be decoupled from these factors, to be easily inducible. To achieve this goal we first decided to exchange both promoters in front of virG against a Taurin inducible promoter, analogous to iGEM Marburg 2023. This allows us to induce a plant transformation at any point in time we desire, as well as modulate the expression strength of virG. On the other hand this chemically inducible promoter should have no cross-reactions in an in planta context, since taurin is rarely found in plants, being mostly native to animals. However, for virG to not only be expressed, but to be in an active state, it needs to be phosphorylated. In nature this is catalyzed by virA, which would not be present in our system. This is undesirable for our approach, since we want an easy induction system, therefore we want to limit the amount of inductors needed to one (Taurin). Luckily when introducing a N54D mutation into virG, the novel aspartate mimics the charge of the phosphate, which would usually bind in the adjacent position 52D. This mutation prevents phosphorylation of virG, but also changes the activity of virG to become permanently active (6).
As stated previously a set of virulence clusters has been identified that are necessary for plant transformation events to occur. These are the transcription units (TU) virB, virC, virD and virE. These compounds play a vital role in the facilitation of T-DNA in the cell, so we decided to include these genes on our virulence plasmid. We further settled on the inclusion of virJ, since it has been reported, for plant transformation to occur, either the chromosomal acvB needs to be present or virJ. Here we settled on virJ, being already part of the native virulence cluster of some bacterial strains (7, 8).
Selecting Novel Bacteria Chassis
When conducting non-AMT, selecting the right bacterial chassis is just as important as having a suitable virulence plasmid. Dheeraj Rathore emphasized that the compatibility between the bacteria and the host plant is vital for successful non-AMT. He explained that low compatibility with a plant can significantly impair transformation efficiency. He particularly recommended working with Ensifer adhaerens and Sinorhizobium meliloti. Consequently, we placed special emphasis on these two bacteria in our work. Additionally, we wanted to identify other bacteria found in the rhizosphere of plants that had either been reported to transform plants or had close relatives capable of doing so with different virulence plasmids. Therefore, our list included the following strains:
- • Ochrobactrum cytisi DSM-19778
- • Ensifer fredii DSM-5851
- • Mesorhizobium mediterraneum DSM-11555
- • Sinorhizobium meliloti 1021
- • Sinorhizobium meliloti 2011
- • Sinorhizobium meliloti AK83
- • Sinorhizobium meliloti BL225C
- • Sinorhizobium meliloti 102F34
- • Ensifer adhaerens Casida A
- • Mesorhizobium loti MAFF303099
- • Rhizobium etli CFN42
- • Rhizobium leguminosarum NORWAY
- • Neorhizobium galegae HAMBI 1141S
Building an Orthogonal Virulence Plasmid
To construct a fully orthogonal virulence plasmid, we decided to use PKL2299 (addgene #186332), as a template for the virulence clusters, since it harbors all the needed transcription units (TU). However, PKL2299 does neither contain a T-DNA with root inducing genes, nor does it possess a constitutive variant of virG (9). Therefore, we decided to synthesize the virG TU containing only a taurin inducible promoter and the N80D mutation. This mutation is identical to the N54D mutation, since our virG variant is based on the elongated virG variant of pTiBo542i. The root inducing genes were taken from the T-DNA of Agrobacterium rhizogenes K599.
For the backbone we settled on the use of the ColE1 as a high-copy origin in E. coli, due to its readily availability and widespread usage also in the iGEM community, for example in the iGEM distribution kit. As a second origin the pVS1 ori was chosen, being also readily available in the iGEM community, and an established single copy origin for rhizobia. Lastly, based on our previous antibiotic resistance tests, we decided to employ the gentamicin as a selection marker for our final construct.
To build the virulence plasmid we based our approach on standardized Golden Gate cloning, specifically the Marburg collection (10). Thereby, employing the usage of the restriction enzymes BsaI and BsmbI. However, since the required virulence and root inducing genes harbor 22 BsmbI restriction sites, which we deemed to be infeasible to domesticate. Therefore, we exchanged BsmbI in our cloning approach for PaqCI, which only harbored one restriction site over all the TUs discussed.
In the first step, all Transcriptional units were amplified, while domesticating BsaI and PaqCI restriction sites, utilizing PCR. The amplified parts were then ligated using Golden Gate reaction. However, since we were not able to gain access to an established heat-inducible plant promoter in time for this project, we had to assemble the T-DNA construct without any Cre-recombinase functionality. Therefore, after the first cloning round we got a selection of 10 level 2 parts for the construction of the orthogonal virulence plasmid.
- • TU virJ: BBa_K5088700
- • TU Taurin inducible virG N80D: BBa_K5088701
- • TU virE: BBa_K5088702
- • TU virD: BBa_K5088703
- • TU virC: BBa_K5088704
- • TU TU virB: BBa_K5088705
- • gentamicin resistance cassette BBa_K5088706
- • pVS1: BBa_K5088707
- • T-DNA with root inducing genes: BBa_K5088708
- • ColeE1: BBa_K2877001
From these parts we went on and tried to build the final virulence plasmid BBa_K5088720. Here we proudly present our in silico design for
An Orthogonal Virulence Plasmid
[IMG]
Figure 2: Plasmid map of the in silico designed, decoupled, virulence plasmid BBa_K5088720
This over 38 kb plasmid is hypothesized to be an orthogonal plasmid, able to facilitate plant transformation in novel bacteria chassis. We hope that future iGEM teams may continue our work in bringing this plasmid to fruition.
Outlook
Looking ahead, the orthogonal virulence plasmid designed in our project holds significant promise for enhancing non-agrobacterium mediated transformation (non-AMT) in plant synthetic biology. Future iterations of this plasmid could focus on further optimization and modification to increase its efficiency and versatility. Firstly incorporating the proposed Cre/lox system could significantly improve plant survival after transformation. Therefore, controlling Cre/lox expression by an already well established heat inducible promoters like HSP 18.2 might prove useful. Moreover, the design of the plasmid could include additional features, such as more sophisticated regulatory elements that allow for enhanced control over T-DNA expression. In addition, the engineering of T-DNA borders could lead to higher rates of integration and stability within plant genomes. Another potential enhancement could be the incorporation of additional virulence genes, which could broaden the range of plant species that can be effectively transformed. Future teams may explore different combinations of these genes to identify the most effective configurations for specific plant hosts. As the patent landscape continues to evolve, our plasmid design offers an alternative to the established models of plant transformation, particularly for young startups and small, financially constrained biotechnology companies. This adaptability will be crucial for fostering innovation and advancing the field of plant synthetic biology. Overall, the modifications and advancements to the virulence plasmid envisioned for the future will contribute to a more effective toolkit for plant transformation, enabling the exploration of novel applications in sustainable agriculture and biotechnology. The foundation laid by our project aims to inspire ongoing research and development both within and outside the iGEM community.
References
1
S. Winans. Transcriptional induction of an Agrobacterium regulatory gene at tandem promoters by plant-released phenolic compounds, phosphate starvation, and acidic growth media.
American Society for Microbiology, 2016.
CrossrefGoogle Scholar
2
M. Thompson, L. Kirkpatrick, G. Geiselman, L. Waldburger, A. Pearson, M. Szarzanowicz, K. Vuu, K. Markel [...] P. Shih, A. Weisberg. Genetically refactored Agrobacterium-mediated transformation.
Cold Spring Harbor Laboratory, 2023.
CrossrefGoogle Scholar
3
S. Subramoni, N. Nathoo, E. Klimov, Z. Yuan. Agrobacterium tumefaciens responses to plant-derived signaling molecules.
Frontiers Media SA, 2014.
CrossrefGoogle Scholar
4
X. Cao, H. Xie, M. Song, L. Zhao, S. Deng, Y. Tian, G. Li, Z. Lang, J. Zhu. Extremely simplified cut-dip-budding method for genetic transformation and gene editing in Taraxacum kok-saghyz.
Innovation Press Co., Limited, 2023.
CrossrefGoogle Scholar
5
D. Lankitus, Y. Zhang, M. Ariyaratne, D. Barker, S. McNulty, N. Amstutz, L. Zhao, B. Iaffaldano, K. Cornish. Agrobacterium rhizogenes–induced Altered Morphology and Physiology in Rubber Dandelion after Genetic Transformation.
American Society for Horticultural Science, 2022.
CrossrefGoogle Scholar
6
S. Jin, Y. Song, S. Pan, E. Nester. Characterization of a virG mutation that confers constitutive virulence gene expression in Agrobacterium.
Wiley, 2006.
CrossrefGoogle Scholar
7
S. Pan, S. Jin, M. Boulton, M. Hawes, M. Gordon, E. Nester. An Agrobacterium virulence factor encoded by a Ti plasmid gene or a chromosomal gene is required for T‐DNA transfer into plants.
Wiley, 2006.
CrossrefGoogle Scholar
8
V. Kalogeraki, S. Winans. The octopine-type Ti plasmid pTiA6 of Agrobacterium tumefaciens contains a gene homologous to the chromosomal virulence gene acvB.
American Society for Microbiology, 2016.
CrossrefGoogle Scholar
9
Q. Zhang, Y. Zhang, M. Lu, Y. Chai, Y. Jiang, Y. Zhou, X. Wang, Q. Chen. A Novel Ternary Vector System United with Morphogenic Genes Enhances CRISPR/Cas Delivery in Maize.
Oxford University Press (OUP), 2019.
CrossrefGoogle Scholar
10
D. Stukenberg, T. Hensel, J. Hoff, B. Daniel, R. Inckemann, J. Tedeschi, F. Nousch, G. Fritz. The Marburg Collection: A Golden Gate DNA Assembly Framework for Synthetic Biology Applications in Vibrio natriegens.
American Chemical Society (ACS), 2021.
CrossrefGoogle Scholar
Contents
Introduction
Understanding Agrobacterium-Mediated Transformation
Designing an Orthogonal Virulence Plasmid
Removal of Pathogenic Genes
Selecting Virulence Genes
Selecting Novel Bacteria Chassis
Building an Orthogonal Virulence Plasmid
An Orthogonal Virulence Plasmid
Outlook
References
