[IMG]
Contents
Spodoptera litura (common cutworm) is a polyphagous agricultural pest worldwide and causes enormous losses to a myriad of economical crops. It has evolved high resistance to multiple chemical insecticides. It poses a necessity for development of alternative strategies for S. litura control. Recently, RNA interference (RNAi) technology has emerging as a promising strategy for pest insect management. In this project, we attempted to express artificial microRNA (amiRNA) targeting the chitin synthase 1 (SlCHS1) gene of S. litura from the genome of tobacco plastid. To protect the degradation of amiRNA caused by highly active nuclease in S. litura, amiRNA was delivered by a bacteriophage MS2 virus-like particle (VLP)-based delivery system. To better understand the plastid-mediated RNAi approach for S. litura management, we established models of S. litura distribution in China and predicted the structure of CHS1.
## 1 Distribution of Spodoptera litura
1.1 Current distribution of Spodoptera litura
An important omnivorous or polyphagous pest found all throughout the world is Spodoptera litura. The subtropical and temperate regions of Asia and Oceania are the primary distribution areas for this insect. It is harmful throughout the year. India, Pakistan, Bangladesh, South Korea, Japan, Thailand, Philippines, Australia, New Zealand, and the United States (only Hawaii) are among the nations that are particularly impacted. The current global distribution map of Spodoptera litura (PRODLI) [World distribution] | EPPO Global Database is shown below.
[IMG] ...
In China, S. litura is primarily found in the Yangtze River Basin, South and Southwest China, with less distribution in North, Northeast, and Northwest China.Next, PLASTID PESTICIDES™ shall mostly address Spodoptera litura's distribution within China.
1.2 Simulation prediction of potential distribution areas of Spodoptera litura.
According to recent research, the most significant climatic element influencing Spodoptera litura distribution is the lowest temperature during the coldest month.Temperature is a key environmental component that influences how insects develop. As a result of present global warming, pests will appear earlier, multiply in quantity and generation in the field, and prolong the damage period, all of which will pose a severe danger to food security.It is essential to implement targeted preventive and control measures, guarantee the safety of food production, and anticipate how agricultural pests will react to global warming and changes in their distribution areas in order to deal with the impact of climate change on agricultural pests and illnesses.Consequently, PLASTID PESTICIDES™ intend to carry out study on Spodoptera litura in China.
Modeling predictions of potential distribution areas.In species distribution modeling, the goal of the MaxEnt model is to predict a species’ potential distribution area using known species distribution data (e.g., species’presence records) and environmental variables (e.g., climate, land use, etc.).The MaxEnt model uses the maximum entropy principle to generate the least biased distribution predictions, provided that the model satisfies known constraints.
The model form of MaxEnt is:
[IMG] ...
Among these,
P(y|x) is the probability of species existence given environmental conditions
fi(x) is a characteristic function related to environmental conditions, indicating how environmental conditions affect the distribution of species.
λi is the weight of the characteristic function
Z(x) is the normalization factor.
Dataset preparation
The S. litura distribution data set uses part of the S. litura distribution data in mainland China from https://www.gbif.org/. The climate time series data uses the data from https://www.worldclim.org/ Historical climate data.Here, climate data uses three indicators: maximum temperature, minimum temperature, and average temperature.Import the corresponding data set into ArcMap software, and the visualization results are as follows:
[IMG]
Figure 2: Training set sampling points.
Since the historical meteorological data is global data, it is necessary to cut out China’s areas on the climate map.By using the Extract By Mask function in SDM TOOLBOX, import China’s map vector information to complete the cutting.
The use of Maxent software
The produced Spodoptera litura distribution data should be imported into Maxent software, along with climatic data. Epochs should be set to 500, and cross-validation should be used for the machine learning evaluation method.Following testing, the training set and testing were carried out following eighteen ground iterations.The set's AUC is 0.98, indicating a higher degree of accuracy in the results prediction.
[IMG] ...
Figure 3. AUC values of the training set and test set after 18 rounds of iterations.
The anticipated area and miss rate as a function of cumulative threshold are displayed in the graph below. Training presence records and test records—if test data is used—are the basis for calculating the missing rate.The omission rate ought to be near the anticipated omissions because of how the cumulative threshold is defined.
[IMG] ...
Figure 4. Missing rate and prediction area as a function of cumulative threshold.
Some common thresholds and corresponding omission rates are as follows. If test data are available, binomial probabilities are calculated exactly if the number of test samples is at most 25, otherwise using a normal approximation to the binomial. These are 1-sided p-values for the null hypothesis that test points are predicted no better than by a random prediction with the same fractional predicted area. The "Balance" threshold minimizes 6 * training omission rate + .04 * cumulative threshold + 1.6 * fractional predicted area.
Table 1. Common thresholds and corresponding miss rates.
| Cumulative
threshold
| Cloglog
threshold
| Description
| Fractional
predicted area
| Training omission
rate
| Test omission rate
| P-value
| 1
| 0.009
| Fixed cumulative value 1
| 0.241
| 0
| 2.41E-01
| 5
| 0.064
| Fixed cumulative value 5
| 0.132
| 0
| 1.33E-01
| 10
| 0.116
| Fixed cumulative value 10
| 0.089
| 0.056
| 0
| 8.94E-02
| 5.011
| 0.064
| Minimum training presence
| 0.132
| 0
| 1.32E-01
| 16.227
| 0.206
| 10 percentile training presence
| 0.061
| 0.056
| 0
| 6.10E-02
| 16.227
| 0.206
| Equal test sensitivity and specificity
| 0.061
| 0.056
| 0
| 6.10E-02
| 16.227
| 0.206
| Maximum training sensitivity plus specificity
| 0.061
| 0.056
| 0
| 6.10E-02
| 41.701
| 0.6
| Equal test sensitivity and specificity
| 0.02
| 0.0278
| 0
| 2.00E-02
| 41.701
| 0.6
| Maximum test sensitivity plus specificity
| 0.02
| 0.0278
| 0
| 2.00E-02
| 2.475
| 0.03
| Balance training omission, predicted area and threshold value
| 0.173
| 0
1.73E-01
| 12.139
| 0.146
| Equate entropy of threshold and original distributions
| 0.077
| 0.056
| 0
| 7.75E-02
#### Analysis and conclusion of the results.
The figure below displays the forecast results following the eighteenth iteration.
[IMG] ...
Figure 5. Predicted structure distribution map of S. litura.
The purple sample denotes the testing position, and the white square indicates the sample training position. The warmer the color value, the more suitable for the survival of the species. Through observation, it can be seen that the color around some observation points in the eastern and southern coastal areas is close to 1, and in the central and southeastern areas, the color value is close to 1. The color in coastal areas is generally higher than 0.6. These findings suggest that S. litura has an obvious tendency to spread to the surrounding areas.
2. Model construction in the RNAi process.
### 2.1 Assembling AGO and siRNA into a RISC structure.
The specific principle is as follows. In transgenic tobacco, there exists long dsRNA. After being ingested by Spodoptera litura and entering the target cells, the long dsRNA is processed by the RNase-III enzyme cutter in the target cells into small interfering RNA (siRNA) with a length of 20-25 nucleotides. Subsequently, the Argonaute protein (AGO) assembles these siRNAs to form an RNA-induced silencing complex (RISC), which
mediates the degradation of endogenous mRNA that is complementary to its guide strand, thus achieving the purpose of pest control.
Here, PLASTID PESTICIDES™ use AlphaFold3 to conduct predictive modeling of the RNA-induced silencing complex (RISC) formed by the assembly of siRNAs by the Argonaute protein (AGO), and the result is consistent with that of Dinshaw J. Patel (2014).
[IMG]
### 2.1 Assembling AGO and siRNA into a RISC structure.
The specific principle is as follows. In transgenic tobacco, there exists long dsRNA. After being ingested by Spodoptera litura and entering the target cells, the long dsRNA is processed by the RNase-III enzyme cutter in the target cells into small interfering RNA (siRNA) with a length of 20-25 nucleotides. Subsequently, the Argonaute protein (AGO) assembles these siRNAs to form an RNA-induced silencing complex (RISC), which mediates the degradation of endogenous mRNA that is complementary to its guide strand, thus achieving the purpose of pest control.
Here, PLASTID PESTICIDES™ use AlphaFold3 to conduct predictive modeling of the RNA-induced silencing complex (RISC) formed by the assembly of siRNAs by the Argonaute protein (AGO), and the result is consistent with that of Dinshaw J. Patel (2014).
[IMG] 图片1.jpg
Figure 6: Crystal structure of Aa-Ago with externally bound siRNA.
2.2 SlCHS1 protein structure prediction.
In the prevention and control of Spodoptera litura, RISC silences the SICHS gene and inhibits the synthesis of SlCHS1, so that the larvae cannot develop into pupae normally and the adults cannot completely molt, thereby preventing and controlling Spodoptera litura.
The cDNA sequence of SlCHS1 (GenBank accession number: high.[5]
We used swiss-model (https://swissmodel.expasy.org) to predict the protein structure of SICHS1 (Figure 7), and the Global Model Quality Estimate was 0.73.
[IMG] 图片2.jpg
Figure 7. Predicted structure of SICHS1
To determine the contours of favoured regions, data was extracted from 12,521 non redundant experimental structures (pairwise sequence identity cutoff 30%, X-ray resolution cutoff 2.5Å) as culled from PISCES. Histograms with a binning of 4 degrees were then used to count Φ (Phi; C-N-CA-C) / Ψ (Psi; N-CA-C-N) occurences for all displayed categories. The number of observed Φ / Ψ pairs determines the contour lines
Figure 8 Ramachandran Plots. （a）General (No Proline or Glycine) （b）Glycine Only（c）Proline Only （d）Pre-Proline Only
References
Qin Houguo, Wang Dudong, Ding Jian, et al. List of host plants of Spodoptera litura. Journal of Jiangxi Agricultural Sciences, 2006, (05): 51-58. DOI: 10.19386/j.cnki.jxnyxb.2006.05 .017．
BAJPAI NK, BALLAL CP, RAO NS, et al. Competitive interaction be tween two ichneumonid parasitoids of Spodoptera litura［J］． Bio Control, 2006, 51:419-438．
Zhang Wenxiu, Zhou Qinghua, Yang Liu, Wang Dongqi, Wu Pinghua, Qin Guangming, Cai Gaolei, Fu Hongyang, Zhou Yang. Simulation and prediction of the impact of climate change on the potential geographical distribution areas and overwintering boundaries of Spodoptera litura [J]. China Plant Protection Guide, 2023, 43(2):31-39.
Yuan YR, Pei Y, Chen HY, Tuschl T, Patel DJ. A potential protein-RNA recognition event along the RISC-loading pathway from the structure of A. aeolicus Argonaute with externally bound siRNA. Structure. 2006 Oct;14(10):1557-65. doi: 10.1016/j.str.2006.08.009. PMID: 17027504; PMCID: PMC4692372.
Yu, H.-Z.; Li, N.-Y.; Xie, Y.-X.; Zhang, Q.; Wang, Y.; Lu, Z.-J. Identification and Functional Analysis of Two Chitin Synthase Genes in the Common Cutworm, Spodoptera litura. Insects 2020, 11, 253.
the MaxEnt model
Maxent software can be used to model species niches and distributions by applying a machine-learning technique called maximum entropy modeling. From a set of environmental (e.g., climatic) grids and georeferenced occurrence localities, the model expresses a probability distribution where each grid cell has a predicted suitability of conditions for the species. Under particular assumptions about the input data and biological sampling efforts that led to occurrence records, the output can be interpreted as predicted probability of presence (cloglog transform), or as predicted local abundance (raw exponential output).
[IMG]
ArcMap
ArcMap is where you display and explore GIS datasets for your study area, where you assign symbols, and where you create map layouts for printing or publication.ArcMap represents geographic information as a collection of layers and other elements in a map. Common map elements include the data frame containing map layers for a given extent plus a scale bar, north arrow, title, descriptive text, a symbol legend, and so on.
Extract by Mask
Extract by Mask using ArcGIS It is possible to select a specific area of a raster using another layer (raster or entity) as a template whose extension delimits the extent of the output raster. The output raster will maintain its attribute table, bounded to the extension that PLASTID PESTICIDES™ have imposed.
[IMG]
SDM TOOLBOX
SDM toolbox is a python-based ArcGIS toolbox for spatial studies of ecology, evolution and genetics. SDMtoolbox consists of a series python scripts (92 and growing) designed to automate complicated ArcMap (ESRI) analyses. A large set of the tools were created to complement MaxEnt species distribution models (SDMs) or to improve the predictive performance of MaxEnt models (for an overview, see chapter 5 in the user guide Running a SDM in MaxEnt: from Start to Finish). MaxEnt uses maximum entropy to model species’ geographic distributions using presence-only data (Phillips et al. 2006) and has become one of the most prevalent methods due to its high predictive performance, computational efficiency and ease of use. SDMtoolbox is not limited to analyses of MaxEnt models and many tools are also available for use on other data (i.e. haplotype networks) or the results of other SDM methods.
[IMG]
AUC
AUC, short for area under the ROC (receiver operating characteristic) curve, is a relatively straightforward metric that is useful across a range of use-cases. In this blog, PLASTID PESTICIDES™ present an intuitive way of understanding how AUC is calculated.
