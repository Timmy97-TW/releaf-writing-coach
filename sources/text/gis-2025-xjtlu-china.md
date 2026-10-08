[IMG] Loading
Loading...
[IMG] Header Banner Image
Project Description
## Introduction
In our project, the modeling component plays a crucial role in connecting different aspects. Through modeling, we were able to organically integrate human practice, wet lab, and hardware development into a unified framework. First, in the human practice aspect, by modeling the distribution and dynamics of Ulva prolifera, we provided quantitative support and decision-making guidance for practical ecological conservation efforts. Second, in the wet lab aspect, the model helped us optimize protein expression and regulatory strategies, ensuring the stability and effectiveness of synthetic biology experiments. Finally, in the hardware development aspect, the model provided theoretical guidance for hardware design.
Overall, the model not only helped us explain ecological processes and provided quantitative insights for experimental design but also documented our exploratory and iterative thought process. It has been instrumental in supporting the smooth progress of the entire project.
[IMG]
Fig1. Model framework mind map.
## Distribution and Dynamics Modeling of Ulva prolifera
Through these two models, we addressed the origin and spread of Ulva prolifera spores. First, the MaxEnt model helped us predict where Ulva might appear under different environmental conditions, highlighting potential risk zones. Next, the Growth and Trajectory Tracking model simulated how spores drift, grow, and gather under ocean currents, illustrating the journey from their source to bloom hotspots. Ultimately, the Distribution and Dynamics Modeling of Ulva prolifera section made a key contribution to the project by providing an in-depth understanding of the distribution and dynamics of Ulva, offering crucial decision-making insights, especially in identifying high-risk areas and predicting bloom trends.
[IMG]
Fig2. Mind map of distribution and dynamics modeling of Ulva prolifera.
#### MaxEnt (Maximum Entropy) Model for the Distribution of Ulva prolifera
##### Description
To predict the potential distribution of Ulva prolifera under different environmental conditions and identify high-risk outbreak zones, we developed a species distribution model based on MaxEnt. This model allows us to evaluate possible suitable habitats on a global scale and provides scientific support for assessing bloom risks. By linking these predictions with conservation and management strategies, our work can help guide early intervention, reduce the ecological and economic damage caused by green tides, and contribute to the sustainable protection of marine ecosystems.
##### Materials and Method
In this study, the occurrence data of Ulva prolifera were sourced from the Global Biodiversity Information Facility (GBIF). We first conducted rigorous data cleaning, which included removing missing or erroneous geographical coordinates, excluding records located on land, and deleting duplicate points to ensure the accuracy and independence of the data. To minimize bias caused by spatial autocorrelation, we performed spatial thinning at a scale consistent with the resolution of the environmental variables, retaining only one occurrence record per grid cell. Additionally, to improve the match with current environmental data, we prioritized records from the past two decades. After these considerations, a total of 272 usable data points were selected as source data for Ulva prolifera.
Environmental variables were selected from the Bio-ORACLE V3.0 database. After eliminating highly correlated variables, the final predictive data used included Bathymetry, Sea Surface Temperature, Phosphate concentration, Dissolved oxygen, Sea surface salinity, Nitrate concentration, Silicate concentration, Photosynthetically Active Radiation, Chlorophyll concentration, pH, and Current direction for the period 2020-2030, which are factors closely related to Ulva prolifera growth. All environmental factors were standardized to the WGS84 projection coordinate system and processed using QGIS to ensure they only covered marine areas.
| MaxEnt Output Variables
| Corresponding Environmental Factors (Bio-ORACLE)
| terrain
| Bathymetry
| temp
| Sea surface temperature
| phosphate
| Phosphate concentration
| dissolved_oxygen
| Dissolved oxygen
| salinity
| Sea surface salinity
| nitrate
| Nitrate concentration
| silicate
| Silicate concentration
| current_velocity
| Current velocity
| par
| Photosynthetically Active Radiation (PAR)
| current_direction
| Current direction
| chlorophyll
| Chlorophyll concentration
| ph
| pH
Table 1: Bioclimatic variables used for modeling Ulva prolifera distribution.
[IMG]
Fig3. Workflow for MaxEnt Model.
##### Results
The model's prediction results indicate that under future climate change scenarios (2020–2030), Ulva prolifera will still exhibit a broad potential suitable habitat globally. High suitability areas (red-yellow) are mainly distributed in the shallow coastal waters of temperate and subtropical regions, including the Yellow Sea and East China Sea in China, the coast of Japan, the North Sea of Europe, the west coast of the United States, and parts of South American seas. These areas share common characteristics such as suitable temperatures, higher nutrient levels, and abundant sunlight, all of which meet the growth requirements of Ulva prolifera. Compared to the current distribution, the model predicts that new potential suitable habitats may emerge in high-latitude regions (such as parts of the North Atlantic and North Pacific coasts), while some low-latitude regions show a decline in suitability due to rising sea temperatures. This also suggests that our mitigation strategy is not only applicable to the Yellow Sea but also provides valuable reference for managing potential green tide occurrences globally in the future. Therefore, it is evident that our project has long-term applicability and potential.
[IMG]
Fig4. All bioclimatic variables used for modeling Ulva prolifera distribution.
##### discussion and analysis
(1) Model Validation
The model was trained using 272 occurrence points and 10,272 background points, and the results show excellent discriminative performance. The AUC value of the training set is 0.952, significantly higher than the random prediction value of 0.5, indicating that the model is highly reliable in distinguishing occurrence points from background points. The regularized training gain is 2.564, suggesting that the model is able to capture rich environmental information. Analysis of omission rates at different thresholds shows that the model's predictions align closely with theoretical expectations, with an omission rate of 0.099 at the "10% occurrence point threshold", indicating that the model can still effectively cover the actual occurrence points while limiting the prediction range. ROC curve results further confirm the model's high fit, strong robustness in prediction output, and its reliability for inferring the potential distribution of Ulva prolifera.
[IMG]
Fig5. Receiver operating characteristic (ROC) curve for Ulva prolifera.
(2) Variable Contribution
The analysis of variable contribution and permutation importance shows significant differences in the influence of different environmental factors on model predictions. As indicated in the table, Bathymetry is the most important explanatory factor, suggesting that Ulva prolifera primarily relies on shallow marine environments, and large-scale blooms are unlikely to occur in deep-sea areas. Other environmental factors have varying degrees of impact on the distribution trends of Ulva prolifera.
| Variable
| Percent contribution
| Permutation importance
| terrain
| 46.8
| 76.3
| temp
| 14.6
| 8.9
| phosphate
| 13.2
| 6.3
| dissolved_oxygen
| 7.9
| 3.8
| salinity
| 5.2
| 1.8
| nitrate
| 3.0
| 0.4
| silicate
| 2.6
| 1.1
| current_velocity
| 2.4
| 0.0
| par
| 2.0
| 0.7
| current_direction
| 1.4
| 0.0
| chlorophyll
| 0.5
| 0.0
| ph
| 0.3
| 0.6
Table 2. Variable Contribution to Model.
(3) Quantitative Analysis
We conducted a quantitative analysis of the MaxEnt prediction results using two approaches: binary and suitability-weighted.
- Binary Suitable Area
Given a threshold of T = 0.5, the output raster was binarized. Areas with a suitability value greater than 0.5 were considered as definite potential distribution zones, while areas with a value less than 0.5 were considered non-distribution zones. The total area of potential suitable habitats globally was 4.73×10⁶ km² (accounting for 1.31% of the ocean).
$$ \text{Area}^{\text{binary}}(T) = \sum_{i,j} \begin{cases} A_{i,j}, & Z_{i,j} \geq T \\ 0, & Z_{i,j} < T \end{cases}$$
- Weighted / Suitability-Integrated Area
To reduce threshold sensitivity, we further integrated the pixel area using suitability as a weight, preserving the gradient of suitability strength. The output represents the area of "equivalent 100% suitability." At the same time, we maintained the strength-weighting and introduced the threshold T = 0.5. The equivalent area is 3.55×10⁶ km² (accounting for 0.98% of the ocean).
$$ \text{Area}^{\text{weighted}}(T) = \sum_{i,j} \begin{cases} Z_{i,j} \cdot A_{i,j}, & Z_{i,j} \geq T \\ 0, & Z_{i,j} < T \end{cases} $$
[IMG]
Fig6. Comparison of suitable area under different suitability scores.
##### Limitations
- Data Sources The available marine environmental data still have limitations in spatial resolution and predictive accuracy. Some regions suffer from missing layers or inconsistent boundaries. These uncertainties may affect the reliability of the model predictions to some extent, particularly when interpreting species distribution at local scales.
- Considerations The quantitative analysis in this study mainly focuses on the influence of environmental factors on Ulva prolifera distribution, but does not incorporate the species' own dispersal and bloom mechanisms (such as drift diffusion, reproductive cycles) into the modeling process. Additionally, short-term disturbance factors, such as extreme weather events (e.g., storms, anomalously high temperatures), have not been considered, which could lead to an underestimation of actual bloom risks.
- Quantitative Analysis Due to the limited number of valid distribution records for Ulva prolifera worldwide, the quantitative analysis in this study primarily relies on statistical methods. The prediction results reflect the cumulative area of potential suitable habitats throughout the year, rather than the dynamic distribution during specific seasons or bloom events. Therefore, the model is currently unable to capture seasonal characteristics or the specific spatiotemporal processes of green tide outbreaks, and further optimization and validation are required using high temporal resolution monitoring data.
#### Growth and Trajectory Tracking Model of Ulva prolifera Spores
##### Description
Our study aims to achieve accurate prediction and control of Ulva prolifera blooms. We describe the whole process from spore release to large-scale outbreaks, and predict arrival times and accumulation hotspots. This provides a scientific basis for early warning and management. Using the Python Parcels particle-tracking framework, we combined ocean current data with the growth dynamics of Ulva to simulate spore release, drifting, growth, and bloom formation.
Through our field interviews in Qingdao (link to HP page), we learned that current control methods mainly rely on remote sensing and manual removal. These measures lack predictive ability and are often affected by weather and climate conditions. This feedback from local experts and stakeholders guided our modeling work. By connecting modeling with conservation practices, we hope our results can support more scientific, proactive, and effective strategies to protect fisheries, ensure maritime safety, and safeguard the marine ecosystem.
Our model aims to:
- Predict the potential locations of Ulva prolifera blooms in specific periods and regions;
- Provide quantitative support for future green tide forecasting and management, contributing to more scientific and effective control strategies.
##### Materials and Method
In building the model, we primarily used high-resolution ocean hydrodynamic data from the Copernicus Marine Environment Monitoring Service (CMEMS). We extracted surface current fields (u and v components) for the study area (22.5°N–40°N, 116°E–130°E) during June–August 2025. These data were applied to simulate the drifting pathways of Ulva prolifera spores. In addition, we referred to published literature and historical monitoring data to support later model validation.
For technical implementation, we employed the Python Parcels package as the particle-tracking framework, combined with xarray for data reading and processing, and matplotlib for visualization. A growth model of Ulva prolifera—driven by temperature and light conditions—was embedded into the Parcels kernel function, allowing us to simulate both drifting and growth simultaneously.
We also introduced several simplifying assumptions about Ulva prolifera spores:
- Spores are treated as passive particles, drifting only with the flow field;
- Effects of wind, waves, and human activities are ignored;
- Vertical oceanic processes are not considered.
The workflow of the model is as follows:
[IMG]
Fig7. Workflow for Growth and Trajectory Tracking Model.
##### Results
Due to time limitations, we developed the particle-tracking model and the Ulva prolifera growth model separately, presenting them in a simplified manner. In the particle-tracking component, we temporarily used a constant growth rate in place of the full growth function; fully integrating the two models will be an important direction for future research.
Part 1 Particle-tracking Model
Based on the ocean current simulation data downloaded from CMEMS, we visualized the surface current velocity in the east–west direction of the study area, providing preparation for the subsequent particle dynamics simulation.
[IMG]
Fig8. Visualization of surface velocity.
Due to limited availability of Ulva prolifera growth data and time constraints, we assumed an initial growth rate of 0.1/day based on literature and the existing growth model, rather than directly embedding the full growth function. Within the longitude range (119.4–120.3) and latitude range (34.736979–36.035745), we randomly released 20 particles and carried out particle-tracking simulations for 7 to 16 days to observe changes in their spatial positions. The results are shown below:
[IMG]
Fig9. The Movement Trajectory Map of the Enteromorpha Spore within 7-16 Days.
These trajectories indicate that most particles, driven by eastward and northeastward currents, were transported offshore. A smaller portion temporarily remained near the coast under the influence of nearshore currents and eddies, forming localized high-density areas. Some trajectories gradually converged toward Qingdao and its adjacent offshore waters, suggesting that this region may be a key area for green tide outbreaks.
Part 2 Ulva prolifera Model
According to the growth and bloom mechanism of Ulva prolifera, we simplified the growth model into a minimal feasible framework “spore → attached thallus (juvenile/adult).” The transition is driven by a temperature- and light-dependent specific growth rate, together with a developmental clock that determines when adult thalli appear.
- Spore pool
- Attached biomass (Logistic growth + new attachments + mortality)
$$B_{t+1} = B_t + \left[ \mu_t \left(1 - \frac{B_t}{K}\right) - m_B \right] B_t + p_{att} S_t b_0 $$
- Temperature–light driven specific growth rate
$$\mu_t = \mu_{\max} f_T(T_t) f_I(I_t)$$
- temperature function $f_T$
- light function $f_I = \frac{I}{K_I + I}$
- Developmental clock (minimum development constraint)
$$ D_{t+1} = D_t + \frac{\mu_t}{\mu_{\max}} \quad (0 \sim 1/\text{day})$$
Adult determination:
$B \geq B_{thr}, \quad D \geq D_{req}$
Assumptions for parameters and variables:
| Symbol
| Name
| Unit
| Estimated value
| Bthr
| Biomass threshold
| gDW·m-2
| 5
| Dreq
| Development requirement (dimensionless)
| /
| 10
| S0
| Initial spore abundance
| cells·m-2
| 107
| B0
| Initial thallus biomass
| gDW·m-2
| 0
| Tt
| Temperature input
| °C
| 20
| It
| Irradiance input (dimensionless)
| /
| 100
| patt
| Daily spore attachment probability
| d-1
| 0.02
| mS
| Spore mortality rate
| d-1
| 0.05
| mB
| Thallus mortality rate
| d-1
| 0.03
| b0
| Initial embryo dry mass
| gDW
| 10-6
| K
| Carrying capacity
| gDW·m-2
| 200
| μmax
| Maximum specific growth rate
| d-1
| 0.25
| KI
| Light half-saturation constant (dimensionless)
| /
| 80
Table 1: Assumptions for parameters and variables.
[IMG]
Fig10. Daily Biomass Change Contributions
[IMG]
Fig11. Graphs of the biomass changes of Ulva prolifera over time under different temperature and light conditions
The results show that within days 0–15, attached biomass gradually declines, while both growth and mortality intensify over time. When temperature and irradiance are simultaneously at moderate–high levels and irradiance approaches the light half-saturation constant, the growth rate increases markedly and the bloom onset occurs earlier. If either light or temperature is limiting, growth slows substantially and the bloom timing is delayed.
##### discussion and analysis
By combining the two models, the particle-tracking model reveals the possible spatial migration pathways and potential aggregation zones of spores, while the growth model highlights the decisive role of environmental conditions in determining bloom timing. Therefore, fully coupling the two in the future could enable dual predictions of both the time and location of green tide outbreaks, providing a more reliable basis for early warning and management.
Part 1 Particle-tracking Model
Our simulation results suggest that most spores are transported offshore by persistent eastward and northeastward currents, while only a small fraction form temporary “retention zones” under the influence of nearshore circulations and tangential flows. These patterns are consistent with previously observed multi-site, multi-stage bloom phenomena: spores from the same source region may drift in multiple batches and along different pathways depending on tidal conditions and wind fields.
In addition, within nearshore areas with dense isobaths, spore trajectories exhibit a coexistence of “alongshore jets and offshore divergence.” When currents converge at headlands or abrupt topographic changes, local trajectory density increases significantly, indicating potential “hotspots” for thallus aggregation and bloom formation. This highlights that not only the spore source region, but also local topography and hydrodynamic features can determine bloom locations.
Although some particles converged toward Qingdao, consultation with Prof. Xuelei Zhang of the First Institute of Oceanography, Ministry of Natural Resources, and relevant literature indicate that green tides in Qingdao are not solely caused by spore drift. Local geomorphology and environmental conditions also play a critical role. This underscores that the model results must be interpreted alongside additional environmental factors to more accurately explain bloom formation.
[IMG]
Fig12. The final location where Ulva prolifera gather on the administrative map
Part 2 Ulva prolifera Growth Model
The results of the growth model show that when both temperature and light are favorable, the specific growth rate of Ulva prolifera approaches its maximum (about 0.25 d⁻¹), leading to a significantly earlier bloom. In contrast, if either light or temperature is limiting, the transition of spores into adult thalli is delayed, and the timing of the green tide outbreak is correspondingly postponed.
This indicates that Ulva prolifera blooms depend not only on oceanic transport but also on strong regulation by environmental conditions. In other words, even if spores successfully drift into a certain area, large-scale blooms are unlikely to occur without suitable temperature and light conditions.
##### Limitations and Future Work
- The growth process of Ulva prolifera has not yet been fully integrated with the particle-tracking model, which may lead to discrepancies between model outputs and real-world conditions.
- The ocean hydrodynamic data used are model-derived, with limited accuracy and resolution. In addition, particles were assumed to drift only with the surface flow, neglecting vertical mixing, tide-induced upwelling/downwelling, and buoyancy–size effects that influence depth distribution. Shoreline roughness, bottom drag, and coastal structures (e.g., breakwaters, nets) that affect currents and particle retention were also not explicitly represented.
- Parameters in the Ulva prolifera growth model were inferred from assumptions based on similar marine organisms, without direct literature support or experimental validation. The model also does not account for functional dependence on temperature, irradiance, salinity, nutrients, or shear flow. The light function is simplified to a single half-saturation parameter, without incorporating photoperiod, turbidity, or self-shading effects.
- Due to data limitations, historical green tide monitoring (remote sensing and coastal surveys) has not been systematically assimilated into the model, resulting in a lack of ensemble validation.
Despite current constraints in resolution and parameterization, the model has demonstrated feasibility and provides a foundation for further improvement with additional datasets (e.g., wind fields, salinity, nutrients). With future inclusion of wave–current coupling, high-resolution nearshore hydrodynamics, parameter assimilation, and ensemble perturbations, the model could support applications in graded early warning, outbreak prevention, and Ulva prolifera bloom management.
## Fusion protein expression and optimization model
In this modeling section, we employed three predictive models to support the experimental work. First, the optimal IPTG induction concentration model significantly reduced the time and resources required for experimental screening of induction levels. Second, we designed a model for an arginine fusion protein to predict its functionality within the adhesion module. Finally, we developed a light-inducible suicide fusion protein model and performed molecular docking and molecular dynamics simulations to assess its feasibility in the suicide module. Overall, these modeling efforts provided critical guidance and support to the experimental components of the project, enabling pre-experimental prediction and validation of each module’s feasibility and greatly facilitating optimized experimental design.
[IMG]
Fig13. Mind map of fusion protein expression and optimization model.
#### Model for Optimal IPTG Concentration
##### Description
Through literature research, we identified the key proteins Ag43 and OmpA that influence biofilm formation. Ag43 specifically mediates cell aggregation, adhesion, and biofilm development; OmpA, as a key protein for bacterial colonization and biofilm formation, significantly promotes biofilm formation on hydrophobic surfaces [16][17]. We utilize lactose operons to regulate the expression of these two exogenous genes. Determining the optimal IPTG induction concentration ensures sufficient expression of the target proteins while minimizing toxicity to host cells. To reduce experimental workload, we referred to the study by XJTLU-CHINA (2023) and employed a predictive model to estimate the optimal IPTG induction concentration range, thereby guiding experimental design and improving efficiency[18].
##### Design & Method
We use ordinary differential equations to describe the mRNA expression processes of ag43 and ompA. Then, we solve the ODE equations using Python. ag43 and ompA are initiated by the same operon and are co-transcribed on a single polycistronic mRNA. Therefore, we represent their mRNA expression level with a single variable, ${mRNA}_{AG43·ompA}$
$$[\text{IPTG}{\text{in}}]=[\text{IPTG}{\text{out}}]$$ $$\text{LacI} = \frac{[\text{LacI}_{\text{total}}]}{1 + \left(\frac{[\text{IPTG}_{\text{in}}]}{K_x}\right)^{n_1}}$$ $$O = \frac{[\text{O}_{T}]}{1 + \frac{\text{LacI}}{K_d}}$$ $$\frac{d[\text{IPTG}_{\text{in}}]}{dt} = K_{\text{input}} \cdot [\text{IPTG}_{\text{out}}] - K_{\text{output}} \cdot [\text{IPTG}_{\text{in}}]$$ $$\frac{d[\text{mRNA}_{T7poly}]}{dt} = K_{\text{poly}} \cdot O - K_{\text{mdegT7}} \cdot [\text{mRNA}_{T7poly}]$$ $$\frac{d[\text{T7 polymerase}]}{dt} = k_{\text{transT7}} \cdot [\text{mRNA}_{T7}] - r_{\text{degT7}} \cdot [\text{T7 polymerase}]$$ $$\frac{d[\text{mRNA}_{AG43·ompA}]}{dt} = \beta_{AG43·ompA} \cdot \frac{[\text{T7 polymerase}]^{n_2}}{K_{d2} + [\text{T7 polymerase}]^{n_2}} - K_{\text{mdeg}} \cdot [\text{mRNA}_{AG43·ompA}]$$
| Parameter
| Meaning
| Value
| Unit
| References
| $K_{\text{input}}$
| rate constant of IPTG enter the cell
| 0.92
| min⁻¹
| [19]
| $K_{\text{output}}$
| rate constant of IPTG export the cell
| 0.05
| min⁻¹
| [19]
| ${LacI}_{\text{total}}$
| Total concentration of LacI repressor protein
| 0.01
| µM
| [20]
| ${K_d}$
| the unbinding LacI concentration at which transcription rate of tac promoter is at half-maximum
| 5e-5
| µM
| [21]
| ${K_x}$
| dissociation constant of IPTG and LacI
| 1
| µM
| [22]
| ${n_1}$
| hill coefficient of IPTG and LacI
| 2
| [22]
| ${O}_{T}$
| Operator content
| 1
| µM
| [23]
| $K_{\text{poly}}$
| Transcription rate constant of T7 polymerase mRNA
| 6.116
| µM/min
| [23]
| $K_{\text{mdegT7}}$
| Degradation rate of T7 polymerase mRNA
| 0.462
| min⁻¹
| [24]
| $k_{\text{transT7}}$
| Translation rate constant of T7 polymerase protein
| 0.5
| min⁻¹
| [24]
| $r_{\text{degT7}}$
| Degradation rate of T7 polymerase protein
| 0.2
| min⁻¹
| [24]
| $\beta_{AG43·ompA}$
| Maximum transcription rate of AG43·ompA mRNA
| 0.0105
| µM/min
| [25]
| $K_{d2}$
| Half-maximal activation constant for AG43 / ompA expression by T7 polymerase
| 3e-6
| µM
| [25]
| ${n_2}$
| Half-maximal activation constant for AG43 /ompA expression by T7 polymerase
| 2
| [25]
| $K_{\text{mdeg}{AG43·ompA}}$
| Degradation rate of AG43 mRNA
| 0.368
| min⁻¹
| estimated from [26]
##### Results & Analysis
[IMG]
Fig14. Effect of IPTG concentration on mRNA_AG43_ompA expression
Our model prediction shows that the mRNA expression levels of ag43 and ompA tend to saturate when the IPTG concentration reaches approximately 400-600 μM. Based on this, we predicted the optimal IPTG induction concentration for the experiment. This saves valuable time and resources in the wet lab by helping avoid extensive blind screening.
#### Model of arginine fusion proteins
##### Description
To facilitate the induction of spore settlement, we reviewed the literature and found that, in experimental systems, peptides with terminally exposed arginine residues can significantly enhance the attachment of Ulva zoospores (pseudo-colonization ratio >70%)[27].
##### Materials and method
We fused short arginine-containing peptide sequences to the outer membrane protein CsgA of E. coli, thereby constructing a functional module capable of extracellular display and mediating spore settlement.
##### Results
According to the AlphaFold3 predictions, our designed Arg–OmpA fusion protein exhibits an overall structure with high confidence. The β-sheet region of the CsgA backbone retains a highly reliable structure, indicating that the fusion peptide does not disrupt the core scaffold. However, we observed that as the number of amino acids increases, the terminal arginine-containing short peptide displays low confidence in the prediction, suggesting that it belongs to an intrinsically disordered region (IDR). The purpose of this design was not to obtain a stably folded domain, but rather to allow the short peptide to remain flexible and dynamic, thereby maximizing the exposure of terminal arginine residues for interactions with the external environment (e.g., Ulva zoospore membranes).
Experimental results can be found on the Result page.
[IMG]
Fig 15. AlphaFold3-predicted structure of the Arg–CsgA fusion protein.
[IMG]
Fig16. AlphaFold3-predicted confidence level of the Arg–CsgA fusion protein.
#### Molecular Dynamics Simulation Model of Fusion Proteins
##### Design of photosuicidal proteins
###### Description
For practical biosafety considerations, we aimed to design a biological suicide switch.
Conventional bacterial optogenetic systems mainly act at the transcriptional level (e.g., controlling whether a gene is expressed), but they cannot directly regulate the presence or elimination of proteins.
- After transcription is switched off, proteins do not disappear immediately but instead rely on natural degradation (too slow, ~5–20 h) and dilution through cell division (effective during exponential growth but largely ineffective in the stationary phase).
- High heterogeneity: in the stationary phase, different subpopulations behave differently—some still divide, while others are completely inactive—making the effective protein half-life within the population unpredictable.
To address these limitations, we employed post-translational optogenetic control, thereby eliminating dependence on growth dilution. Unlike transcriptional control, post-translational regulation does not rely on the natural degradation of proteins and therefore remains effective even in the stationary phase.
From a biosafety perspective, we designed a light-activated suicide switch, in which the oat phytochrome gene was innovatively fused to tetR, enabling light-controlled bacterial survival.
###### Materials and Method
LOV2 is a light-sensing domain of oat phototropin 1 that utilizes FMN (flavin mononucleotide) as its chromophore, undergoing conformational changes upon blue-light illumination [28].
In the dark state, the FMN chromophore is tightly embedded in the PAS-fold structure, while the Jα helix remains folded and closely docked.[29]
Upon blue-light exposure, the C(4a) atom of FMN forms a covalent thioether adduct with the nearby cysteine residue C450 (a photochemical reaction), leading to local conformational rearrangements. The Jα helix unfolds and dissociates, thereby exposing previously shielded domains or functional motifs.[30]
Dark state:
Jα helix folded → embedded peptide locked → inactive / masked
Light state:
Jα helix unfolded → peptide released / exposed → binding enabled → function activated
Building on this mechanism, we introduced the LOVdeg system, derived from the AsLOV2 blue-light response module. This system destabilizes target proteins under blue-light illumination, enabling their degradation—a controllable post-translational regulatory mechanism.
Specifically, the system leverages the bacterial ClpXP protease, which recognizes unstructured C-terminal SsrA tags. The C-terminal sequence “EA-A” of LOV2 mimics the SsrA “LAA” tag but remains buried within the Jα helix in the dark state, preventing recognition. Upon blue-light exposure, the Jα helix unfolds, converting EA-A into an unstructured tail that is exposed to ClpXP, thereby triggering light-controlled degradation.
We further fused LOVdeg with tetR using a flexible linker composed of six short peptides, thereby innovatively engineering a light-activated suicide switch.
###### Results
LOVdeg was fused to tetR via a flexible linker composed of six short peptides, and the fusion construct was evaluated using AlphaFold for structural confidence. The prediction showed an overall high confidence, indicating reliable structural stability of the designed fusion protein.
[IMG]
Fig17. AlphaFold3-predicted structure of the LOVdeg-tetR fusion protein.
[IMG]
Fig 18. AlphaFold3-predicted confidence level of the Arg–CsgA fusion protein.
##### Molecular docking & Molecular Dynamics Simulation
###### Background
We designed a fusion protein (tetR-LOVdeg). To verify whether the fusion affects the main functions of tetR and LOVdeg proteins, we performed molecular docking and molecular dynamics simulations. The goal was to predict whether the fusion protein can stably bind to the tetracycline operator while ensuring that the LOVdeg function remains intact. These simulations help assess, prior to experiments, whether the fusion design might interfere with protein function, potentially causing severe leakage or failure of blue-light induction, thereby guiding experimental design.
###### Design & Method
To evaluate the binding stability of the tetR-LOVdeg fusion protein with the tetracycline operator region, we considered the molecular docking results and the outcomes of molecular dynamics simulations, including RMSD, RMSF, Rg, hydrogen bond analysis, and binding free energy.
To assess the preservation of LOVdeg function in the fusion protein, based on the mechanism of LOVdeg protein (detailed in the fusion protein design section), we believe that if the binding site of the fusion protein with FMN shows no significant difference compared to that of the standalone LOVdeg protein with FMN, its function can be considered unaffected. Therefore, we performed molecular docking of the fusion protein monomer with FMN and compared the results with the reference structure of LOV protein bound to FMN.
To ensure rigor and logical consistency, the simulations were grouped as follows:
Molecular Docking:
- Fusion protein dimer (*) with DNA
- LOVdeg protein with flavin mononucleotide (FMN) ligand
- Fusion protein monomer with flavin mononucleotide (FMN) ligand
Molecular Dynamics Simulations:
- tetR-LOV fusion protein with DNA
- tetR protein with DNA
For molecular docking, the platforms used were Hdock (for protein-DNA docking) and AutoDock Vina (for protein-small molecule ligand docking), followed by visualization using PyMOL.
Molecular dynamics simulations were performed using Gromacs, employing the standard water model and the amber99sb-ildn.ff force field, with a simulation duration of 250 ns. The simulation temperature was set to 310 K to match experimental conditions. K⁺, Mg²⁺, and Cl⁻ ions were added to mimic the intracellular environment of E. coli.
*Note: Docking and simulations were conducted using the fusion protein dimer, as TetR naturally forms a homodimer, and its dimeric state affects DNA-binding ability.
###### Results & Analysis
[IMG]
Fig19. Overall and detailed views of the fusion protein-DNA complex.
The figure shows the overall conformation of the fusion protein dimer bound to DNA from docking results on the Hdock platform, with the protein represented as blue cartoons and DNA as pink sticks. The central panel displays the complete complex structure, with dashed rectangles highlighting two enlarged HTH domains, which are the key regions interacting with the operator. In both protein monomers, the hydroxyl group of THR-26 forms polar contacts with the oxygen atoms of the DNA backbone at distances of 2.6 Å and 2.1 Å, respectively; the hydroxyl groupof TYR-42 also shows polar contact with a backbone oxygen atom at 3.0 Å, potentially forming hydrogen bonds. The amino groups of TRP-43 and ARG-28 have distances of 3.2 Å and 3.1 Å to backbone oxygen atoms, possibly indicating weak hydrogen bonds or electrostatic interactions. In one monomer, the guanidinium group of ARG-28 forms a strong electrostatic hydrogen bond interaction with the nitrogen atom of guanine. These interactions collectively maintain the stable association between the protein and DNA. Colors and symbols in the figure: yellow dashed lines represent polar contacts (≤3.5 Å); sticks colored by atom type highlight key amino acid residues and DNA bases: gray-hydrogen, blue-nitrogen, red-oxygen, orange-sulfur.
[IMG]
Fig 20. Overall and detailed views of the fusion protein monomer bound to FMN.
[IMG]
Fig 21. Overall and detailed views of LOVdeg bound to FMN.[31]
The figure shows the binding interactions between the fusion protein monomer and the FMN ligand, as well as between the LOVdeg protein and FMN. In the left panel, the fusion protein is represented by a blue cartoon, and the ligand is shown as pink sticks. In the right panel, the fusion protein is displayed as a gray cartoon, with the ligand in purple sticks. The left close-up highlights key binding residues in LOVdeg interacting with FMN, including ARG-271, ASN-269, ASN-302, GLN-274, and GLN-333. The carbonyl oxygen of ASN-302 likely forms weak dipole-dipole Van der Waals interactions with the ligand’s carbonyl oxygen. The side-chain amino groups of GLN-274 and GLN-333 form stable hydrogen bonds with the ligand’s carbonyl oxygen; additionally, GLN-274 interacts with the ligand’s nitrogen atom via dipole-dipole interactions. ARG-271’s guanidinium group establishes strong polar contacts with the ligand’s carbonyl oxygen, involving both hydrogen bonding and significant electrostatic attraction. ASN-269’s side-chain amino and carbonyl groups engage in multiple polar interactions with the ligand’s oxygen and hydrogen atoms, forming a multipoint polar binding.
Due to residue numbering differences between the fusion protein and the non-fusion protein retrieved from the database, the right close-up identifies the corresponding key LOVdeg residues in the fusion protein as ASN-302, ASN-312, GLN-274, GLN-333, ARG-271, and ARG-287. The polar groups of the two ASN residues form multiple hydrogen bonds or electrostatic interactions with corresponding ligand atoms; GLN-454 and the two ARG guanidinium groups also establish stable polar contacts with the ligand’s carbonyl oxygens, contributing to binding stability. Color and symbol meanings are the same as in Fig19.
[IMG]
Fig 22. Comparison of RMSD at the DNA binding site between fusion protein-DNA and non-fusion protein-DNA simulation systems.
[IMG]
Fig 23. Comparison of DNA RMSD between fusion protein-DNA and non-fusion protein-DNA simulation systems.
The binding site here refers to the protein’s HTH domain. The left plot shows that throughout the simulation, the RMSD of the binding site in both simulation systems mostly remains within the range of approximately 0.15–0.35 nm. The RMSD curve for the fusion protein–DNA system stabilizes around 0.25–0.3 nm, while that for the non-fusion protein–DNA system stabilizes around 0.2–0.3 nm, with minor fluctuations in between. The right plot shows that in the non-fusion protein simulation system, the DNA RMSD steadily increases over 150 ns, eventually stabilizing between 1.5 and 1.75 nm. In contrast, in the fusion protein simulation system, the DNA RMSD rises sharply during 0–50 ns, then decreases, and finally stabilizes around 1 nm at 150 ns.
[IMG]
Fig24. RMSF of the fusion protein dimer.
The different regions in the figure are marked with ellipses, highlighting the fluctuation characteristics of various functional domains or structural segments in the protein. The Loop, N/C termini, Beta Turn, and flexible linker regions are naturally flexible, showing slightly higher RMSF values. The exposed helix surface residues lack structural constraints, resulting in somewhat larger fluctuations. The Jα helix of LOVdeg is inherently flexible and undergoes unfolding upon blue light induction, leading to increased fluctuations. Additionally, residues 25–50, which correspond to the DNA binding site, exhibit local torsional changes as the protein adapts to DNA movement, causing residue fluctuations.
Comparing the curves, Monomer A and Monomer B show similar RMSF values for most residues, but slight differences appear in the Loop and exposed helix regions, indicating minor variations in local flexibility between the monomers. The DNA binding site region (residues 25–50) displays low fluctuations, while residues in the Jα helix plus Loop regions fluctuate more, yet both curves maintain an overall similar trend.
[IMG]
Fig 25. RMSF of DNA in the fusion protein–DNA and non-fusion protein–DNA simulation systems
[IMG]
Fig 26. Radius of gyration (Rg) of the core protein in the fusion protein–DNA and non-fusion protein–DNA simulation systems.
As shown in the left figure, most DNA bases exhibit RMSF values ranging from 0.2 to 0.4 nm, indicating slight overall fluctuations. The right figure shows that in the DNA-bound systems, the radius of gyration (Rg) of the protein core remains between 2.25 and 2.30 nm. The fusion protein–DNA simulation system consistently exhibits lower Rg values than the non-fusion protein–DNA system, suggesting that the core region of the fusion protein is more compact and tightly folded compared to that of the non-fusion protein.
[IMG]
Fig27. Number of hydrogen bonds between protein and DNA over time in the fusion protein–DNA simulation system and the non-fusion protein–DNA simulation system.
Fig27 shows that the number of hydrogen bonds between protein and DNA remains stable in both systems. Gromacs analysis indicates an average of 13 hydrogen bonds in the non-fusion protein–DNA simulation and 10 in the fusion protein–DNA simulation, suggesting that the fusion does not significantly disrupt key hydrogen bonds.
[IMG]
Fig 28. Binding free energy and its energy components in the fusion protein–DNA simulation system and the non-fusion protein–DNA simulation system.
[IMG]
Fig29. Energy contributions to binding free energy from the two monomeric HTH domains in the fusion protein–DNA simulation system.
Fig28 and Fig29 present the binding free energy between protein and DNA simulated using MMGBSA. In Fig28, both groups show ΔGGAS <-400 kcal/mol and ΔGSOLV > 300 kcal/mol. The ΔGSOLV > 300 kcal/mol indicates that solvent polarization offsets the electrostatic attraction within the system, meaning water molecules hinder the binding by stabilizing the system’s charges. In protein-DNA systems, the abundant negative charges result in substantial solvent polarization and compensation. The ΔGGAS < -400 kcal/mol suggests significant hydrophobic contact area, strong hydrophobic effects, and strong van der Waals interactions, which provide a strong driving force for binding. The total binding energies of the two groups are close to -90 kcal/mol, with similar energy component distributions, indicating that the LOV fusion does not significantly alter the protein’s DNA binding affinity or energy profile.
In Fig29, residues with binding free energy contributions less than -0.5 kcal/mol are shown. The side chain guanidinium group of ARG, which carries a positive charge, contributes most significantly to the total binding free energy by forming strong electrostatic and hydrogen bond interactions with the negatively charged DNA backbone or bases. TYR-42 and TRP-43 on chain B also contribute notably to the binding free energy. These two aromatic residues likely participate in binding through hydrophobic stacking and polar interactions, stabilizing the protein-DNA interface. Overall, the selected key residues include positively charged, polar, and hydrophobic side chains, which together maintain the stability of the HTH domain’s binding to DNA through multiple interaction types.
Demonstrating the stable binding of the fusion protein to the operator region：
As shown in Fig19, the LOVdeg fusion is located at the C-terminus of the tetR protein and does not cover or interfere with the binding region between the tetR HTH domain and the operon. According to literature [32], the binding site highly overlaps with that of the original, non-fused tetR protein.
Fig21 and 22 indicate that the conformations of the protein binding site and DNA at the interface remain stable throughout the simulation without significant dissociation.
Fig24 shows that most residues fluctuate within 0.2–0.35 nm, indicating overall structural stability of the fusion protein. Residues 25–50, belonging to the tetR HTH domain, undergo slight conformational adjustments to accommodate DNA dynamics. This suggests that while the binding site maintains flexibility for adaptability, it still effectively binds DNA.
Fig26 demonstrates that the core protein maintains a compact overall folding, indicating that the fusion does not affect the dimeric structure of the protein.
Fig27 shows that in the fusion protein–DNA simulation system, the presence of the LOVdeg protein and linker at the protein terminus may cause local conformational adjustments and increased flexibility, resulting in a reduced probability of forming some hydrogen bonds. Consequently, the number of protein–DNA hydrogen bonds is slightly lower than that in the non-fusion protein system.
As shown in Fig28, the binding free energy of the fusion protein-DNA complex is slightly lower, possibly due to subtle conformational changes induced by the LOVdeg fusion or linker that optimize certain non-covalent interactions. Despite the slight decrease in hydrogen bond numbers, van der Waals and other nonpolar interactions compensate, resulting in an overall increase in binding free energy. Fig29 indicates that several residues still contribute significantly to the total binding free energy, promoting protein-DNA binding to varying degrees and forming a stable complex.
Based on the comprehensive analyses above, we can conclude that the fusion protein binds stably to the operator region.
Evidence that LOVdeg function is not affected by fusion:
Fig20 and Fig21 show that the binding modes of FMN to the fusion protein monomer and to the standalon e LOV protein are very similar. In the binding site, the polar groups of FMN form stable interactions via polar contacts with polar side chains of the protein, such as ASN, GLN, and ARG, anchoring FMN firmly within the protein pocket. Meanwhile, the hydrophobic ring of FMN is surrounded by the protein backbone and hydrophobic side chains, creating a relatively enclosed hydrophobic environment that reduces water interference. This cooperative enclosure of polar and hydrophobic regions not only ensures precise positioning of FMN but also enhances the spatial confinement of the binding pocket, thus improving the local stability of both the pocket and the complex.
Additionally, as shown in Fig24, the LOVdeg-FMN binding site exhibits good structural rigidity, with binding site residues having RMSF values below 0.3 nm and minimal fluctuations, indicating structural stability around the FMN binding site. Furthermore, as discussed in the fusion protein design section, previous studies have successfully fused LOVdeg to other proteins while retaining blue light inducibility. Therefore, unless specific mutations occur, fusion generally does not disrupt FMN binding.
Therefore, we can conclude that the LOVdeg protein retains its normal FMN-binding capability and functional integrity after fusion.
###### Conclusion
Through molecular docking, molecular dynamics simulations, and MMGBSA binding free energy analysis, we demonstrate that the fusion protein binds stably to DNA and that its dimeric form remains stable. Additionally, the LOVdeg function is not significantly affected, providing a theoretical basis for subsequent experimental validation.
## Exploratory Models in Project Iteration
Through these two models, we explored the potential roles of AHL molecule diffusion and programmable biofilms in the project design. First, the AHL molecule diffusion model made an important contribution to proposing new solutions. Second, the programmable biofilm model provided us with ideas for biofilm engineering, helping us think about how to design more efficient systems. Although these two models were ultimately not adopted, they made significant contributions to the iteration of the hardware, showcasing our process of exploration, experimentation, and refinement. Ultimately, the Exploratory Models in Project Iteration section drove the continuous evolution of the project and helped lay the foundation for future research in the early stages.
[IMG]
Fig30. Mind map of exploratory models in project iteration.
#### Diffusion Model of AHL Molecules
##### Description
To control the outbreak of Ulva prolifera in Qingdao, we decided to target its microscopic reproductive units—spores—for intervention. Previous studies have shown that N-acyl-homoserine lactones (AHLs) released by biofilms can induce spore settlement in Ulva, as these signaling molecules attract zoospores, the motile reproductive stages of the algae [35]. Based on this finding, we plan to engineer E. coli to produce AHLs, thereby generating a concentration field around the buoys. To evaluate the buoy’s potential to promote spore settlement, we simulated the AHL concentration field surrounding the buoy using Fick’s second law and the convection–diffusion equation.
##### Materials and Method
Firstly, to calculate the diffusion coefficient of AHL, we referred to the Stokes-Einstein equation for estimation[36].
$$D = \frac{k_B T}{6 \pi \eta r}$$
| Symbol
| Meaning
| Unit
| $D$
| Diffusion coefficient
| m²/s
| $k_B$
| Boltzmann constant ≈ 1.38 × 10-23
| J/K
| $T$
| Absolute temperature
| K
| $\eta$
| Viscosity of medium
| Pa·s
| $r$
| Molecular radius
| m
- Quantitative modeling of AHL diffusion over time in a static water environment
Fick’s second law describes how diffusion drives concentration changes with respect to time[37]. Therefore, we applied this equation to model the temporal diffusion of AHL in a static water environment.
$$\frac{\partial C}{\partial t} = D \cdot \frac{\partial^2 C}{\partial x^2}$$
- AHL diffusion model in a marine environment
By applying the convection–diffusion equation[38], we simulated the convection–diffusion behavior of AHL in a marine environment.
$$ \frac{\partial C}{\partial t} + u \frac{\partial C}{\partial x} + v \frac{\partial C}{\partial y} = D \left( \frac{\partial^2 C}{\partial x^2} + \frac{\partial^2 C}{\partial y^2} \right) - kC $$
- Ocean tidal harmonic analysis model
To make the modeling results closer to the real-world environment, we established an AHL diffusion model in the Marine environment. The tide level data used in this study is derived from the hourly water level observation data provided by the National Marine Data and Information Service (NMDIS). This paper selects the observation data from the Qingdao tide Gauge Station in May, June and July 2022 (the outbreak period of Green algae), covering the period from May 1st to July 31st, 2022, with a time resolution of 1 hour. By inputting the sea level data of a certain period of time, the periodic changes of tide levels can be fitted through the Navier-Stokes equations[39].
$$ Z(t) = Z_0 + \sum_{j=1}^{N} H_j \cos(\omega_j t + \phi_j) $$
##### Results
The simulation results show that although the diffusion process of AHL is theoretically continuous, due to its extremely low diffusion coefficient (about 10-10m²/s), its migration efficiency in water bodies is extremely low under still water conditions. Within 24 hours, the effective diffusion range of AHL did not exceed 5 cm. In contrast, under the condition of seawater flow, relying solely on molecular diffusion is still insufficient to achieve an effective distribution of signal molecules. The convective process driven by tidal currents plays a decisive role in the spatial diffusion of AHL in the actual Marine environment. However, further simulation results show that under the current parameter conditions, it is difficult to form the expected and stable AHL concentration field around the buoy.
- Quantitative modeling of AHL diffusion over time in a static water environment
Under still water conditions, the simulation results show that the migration efficiency of AHL is extremely limited. Due to its diffusion coefficient being only at the order of 10-10m²/s , even on a 24-hour time scale, the effective diffusion radius of AHL does not exceed 5 cm, resulting in the concentration field always being confined near the release source point. It can be seen from this that in a still water environment, relying solely on molecular diffusion is insufficient to form a large-scale effective signal distribution. This means that if one hopes to induce large-scale spore deposition through AHL, additional transport mechanisms (such as convection, agitation or multi-point release) must be employed; otherwise, its range of action will be extremely limited.
Video1. AHL Simulation Results of Still Water Environment
- AHL diffusion model in a marine environment
In a flowing water environment, the simulation results show that the spatial distribution of AHL is no longer determined solely by molecular diffusion, but is significantly dominated by the convective process driven by the current. Due to the extremely low diffusion coefficient of AHL, the contribution of molecular diffusion to the overall transport is limited, while water flow becomes the main determining factor. The periodic changes in tides and flow velocities have largely replaced the production control of Escherichia coli, making it the dominant force in the distribution of AHL concentrations. The results show that AHL is rapidly diluted and transported to more distant areas within a short period of time, making it difficult to maintain a stable local signal distribution around the buoy.
Video2. AHL Simulation Results in the Presence of Convection
- Ocean tidal harmonic analysis model
The tidal harmonic analysis conducted for May 2022 demonstrates that the hindcast model (orange line) closely reproduces the observed tidal water levels (blue line). The residuals (green line) remain relatively small throughout the time series, indicating that the harmonic constituents used in the analysis adequately capture the dominant tidal dynamics at the Qingdao station. Although minor discrepancies exist, particularly during peak high and low tides, the overall consistency between observation and hindcast suggests that the tidal model provides a reliable basis for simulating hydrodynamic conditions during the Ulva prolifera bloom season.
[IMG]
Fig31. Hourly pollutant concentration at station alam (37.462°N, 122.178°E) in May 2022.
[IMG]
Fig32. Hourly pollutant concentration at station alam (37.462°N, 122.178°E) in June 2022.
[IMG]
Fig33. Hourly pollutant concentration at station alam (37.462°N, 122.178°E) in July 2022.
##### Limitation and Future Plan
The model of this study assumes that both still water and flowing water environments are under conditions of constant flow rate and direction, without further simulation of the complex Marine dynamic environment. Although we originally planned to calculate the flow velocity and direction of ocean currents through tidal harmonic analysis to achieve a more realistic dynamic simulation, the results showed that even in the preset simplified flow environment, the AHL buoy diffusion strategy was insufficient to maintain an effective signal distribution for spore capture. Therefore, this study did not further incorporate real tidal conditions into the model. In future work, we hope to introduce tidal models to build a more realistic framework for simulating the Marine environment.
#### Programmable Biofilm Model
##### Description
To ensure the efficiency and stability of the hardware capture process, we constructed a biofilm with a controllable structure based on geometric characteristics. We innovatively proposed the concept of 4-bit encoded biofilms, achieving the programmability of biofilm structures through up to four adhesion pairs[40]. In addition, we further provided antigen-antibody design schemes corresponding to four typical biofilm morphologies, thereby offering a highly migratory modeling framework for the biofilm design of other research teams.
##### Materials and method
- Biofilm shape scoring system
To quantify the capture performance and structural stability of different biofilm patterns , we have constructed a biofilm scoring system composed of three core indicators based on the geometric characteristics of the network. Any two-dimensional pattern can be abstracted as a network composed of edges (edges) and intersections (junctions), with the basic unit being the cells formed by the edges.
We propose the following three quantitative indicators:
- Connectivity Score
The average number of connections between each node and edges. A higher value indicates a more stable network framework, reflecting structural robustness.
Normalization method:
$$\text{Connectivity}_{norm} = \frac{\text{Connectivity}}{\max(\text{Connectivity})}$$
- Interface Length Score
The interface refers to the organized boundary formed by the adhesion between a pair of Nb-Ag engineered bacteria. The ratio of the total interface length to the area reflects the potential density of attachment sites per unit area and is positively correlated with capture efficiency.
Normalization method:
$$\text{Interface}_{norm} = \frac{\text{Interface Length}}{\max(\text{Interface Length})}$$
- Porosity Score
Determined by the area and distribution of unit cells, where smaller porosity and denser networks contribute to better structural integrity[41].
Normalization method:
$$ Porosity_{\text{norm}} = 1 - \frac{\text{Porosity}}{\max(\text{Porosity})} $$
For comprehensive evaluation, a weighted scoring function is introduced:
$$Score = w_1(\mathrm{Interface}_{norm}) + w_2(\mathrm{Connectivity}_{norm}) + w_3(\mathrm{Porosity}_{norm})$$
The weighting parameters($w_1$,$w_2$,$w_3$)can be adjusted according to research needs:
To emphasize capture efficiency, the weights can be set as $w_1$ : $w_2$ : $w_3$ = 0.5 : 0.3 : 0.2.
To emphasize structural robustness, the weights can be set as $w_1$ : $w_2$ : $w_3$ = 0.2 : 0.5 : 0.3.
This framework provides a unified standard for quantitative comparison across different geometric patterns. Meanwhile, we also provide radar charts of biofilm-like structures, offering a clear and intuitive visualization of the impact of each indicator on overall performance.
- Biofilm Growth Simulation
After determining the biofilm morphology, we simulated biofilm growth based on the required antigen–antibody adhesion pairs. By introducing partial differential equations (PDEs), we modeled the dynamic process of colony growth and diffusion[40].
Basic Assumptions
- There are two types of motile cells: $\rho_1$ and $\rho_2$
- Cells grow but are limited by available resources (Logistic growth).
- Cells diffuse in space.
- When the two cell types encounter each other, they bind to form immotile clusters $\rho_{12}$
- Clusters neither grow nor diffuse, but only accumulate over time.
$$\frac{\partial \rho_1}{\partial t} = g_1 \rho_1 c(\bar{\rho}) + D_1 \nabla^2 \rho_1 - \tilde{K} \rho_1 \rho_2$$ $$\frac{\partial \rho_2}{\partial t} = g_2 \rho_2 c(\bar{\rho}) + D_2 \nabla^2 \rho_2 - \tilde{K} \rho_1 \rho_2$$ $$\frac{\partial \rho_{12}}{\partial t} = 2\tilde{K} \rho_1 \rho_2$$
| Parameter
| Value
| Unit
| Description
| Maximum cell density
\(\rho_{\max}\)
| \(0.155 \pm 0.012\)
| cells/μm²
| Maximum surface cell density during population diffusion, without reaching complete space-filling (sparse spreading).
| Colony expansion rate
\(v\)
| \(3.04 \pm 0.40\)
| mm/h
| Experimentally measured colony front velocity, used to estimate \(D\) and \(g\), based on:
\(v \approx 2\sqrt{Dg}\)
| Diffusion coefficient
\(D\)
| 47
| μm²/s
| Calculated by back-solving from \(v = 3.04\ \text{mm/h}\) and the relationship \(v \approx 2\sqrt{Dg}\).
| Growth rate
\(g\)
| 14
| h⁻¹
| Estimated cell doubling rate, derived from the expansion velocity and the diffusion coefficient.
##### Results
- Biofilm shape scoring system
We adopted a robustness-prioritized weighted scoring system, from which it can be seen that the checkerboard pattern exhibits superior properties compared to the other four patterns. Therefore, we decided to use the checkerboard pattern.
[IMG]
Fig34. Bar chart analysis of biofilm scoring results.
[IMG]
Fig35. Radar chart analysis of biofilm scoring results.
- Biofilm Growth Simulation
We provided both single-colony and multi-colony simulations. It can be observed that a considerable interface is formed between the two engineered strains, where our engineered bacteria exert their function to capture spores. The results show that cells are mixed at the interface, with the total cell density increasing at the interface and decreasing on both sides
[IMG]
Fig36. Time-course simulation of single-strain growth.
[IMG]
Fig37. Time-course simulation of multi-strains growth.
- Design methods for different biofilm shapes
By spot-inoculating strains carrying specific adhesins at different positions on the agar surface, the colonies expand outward and form interfaces upon encountering each other[40]. Various geometric patterns (e.g., square, triangular, hexagonal, circular, stripe) can be achieved through concepts of geometric tiling and Voronoi tessellation. The combination of inoculation point arrangement and adhesin logic (whether an interface is formed or hidden) determines the final pattern.
- Triangular tiling
On a 2D plane, evenly spaced points are arranged to form a triangular lattice.
Algorithm:
- Use adhesin pair 1 for odd rows and adhesin pair 2 for even rows;
- Alternate adhesins horizontally within each row to ensure horizontal boundaries;
- Finally, add downward-pointing triangles to determine whether interfaces are formed vertically.
Only two pairs of adhesins are sufficient to generate arbitrary triangular lattice patterns.
- Hexagonal tiling
Inoculation points are arranged in a honeycomb-like hexagonal layout. Each hexagon has three sets of adjacent edge directions, requiring at least three or more adhesin pairs to avoid conflicts.
Supplementary algorithm: use adhesin pair A for odd rows, adhesin pair B for even rows, and adhesin pair C for the third direction. This allows clear boundary formation in the honeycomb structure.
If the number of adhesins is limited, mixed strains can also be placed within the same hexagon to “hide” interfaces.
- Checkerboard
Inoculation points are arranged in a square lattice. One pair of adhesins is sufficient to ensure that all boundaries are controllable.
- Circular (Ring)
Initial inoculation points are arranged in circular or ring-shaped patterns:
- Point + Point: produces circular arc boundaries.
- Point + Ring inoculation: produces circular boundaries.
Both experimental and simulation results show that point vs. ring (or point vs. line) inoculation can generate the expected circular or parabolic boundaries.
- Stripes (1D chains)
Inoculation points are arranged into a one-dimensional chain (horizontal or vertical). A single pair of adhesins is sufficient: alternating placement generates stripes.
##### Limitation and Future Plan
For our model, since all of our engineered strains are E. coli, we did not consider variations in growth rate that might result from introducing different plasmids. However, growth rate is also a key factor influencing interface formation. We plan to supplement experimental data on growth dynamics and subsequently refine our model accordingly.
During the iterative design process, we finally adopted a spherical hardware structure, considering both the difficulty of inoculation and the effective capture area.
For this spherical system, we proposed a new inoculation strategy — by controlling the sequence and timing of bacterial inoculation, individual cells could be guided to arrange into specific spatial patterns[42]. Previous studies have demonstrated that such an approach can effectively influence and control the structural organization of biofilms.
[IMG]
Fig38. Biofilm design Experiment Using Synthetic adhesion box[42].
However, during experiments we found that this method was only applicable to local populations within large biofilms and could not achieve global regulation; therefore, we abandoned this approach. Nevertheless, in the future, we hope to achieve programmable control at the single-cell level through further studies.
Our current model is based on a two-dimensional spatial framework, which can describe bacterial growth and diffusion on a flat surface. However, in the actual spherical hardware, the bacterial growth environment is three-dimensional, where nutrients, oxygen, and cell distribution all vary along the depth direction.
To more realistically capture this process, we plan to extend our model to three dimensions.
In the three-dimensional model, bacterial growth and diffusion will no longer be confined to a plane but will occur within a volumetric space.
Mathematically, the original two-dimensional diffusion term
$$ \nabla^2 \rho = \frac{\partial^2 \rho}{\partial x^2} + \frac{\partial^2 \rho}{\partial y^2} $$
will be extended to the three-dimensional form:
$$ \nabla^2 \rho = \frac{\partial^2 \rho}{\partial x^2} + \frac{\partial^2 \rho}{\partial y^2} + \frac{\partial^2 \rho}{\partial z^2}. $$
By setting appropriate boundary conditions and defining nutrient diffusion dynamics, we will be able to predict the volumetric distribution of cells and variations in biofilm thickness within the spherical hardware.
This extension will allow us to better understand the mechanisms of microbial community formation in a three-dimensional environment.
## Conclusion
Through the above models, we made significant progress in ecological conservation. First, the Distribution and Dynamics Modeling of Ulva prolifera helped us gain a deeper understanding of the distribution and dynamics of Ulva prolifera, identifying potential high-risk areas and providing scientific support for ecological conservation decisions. Second, the Fusion protein expression and optimization model optimized our protein expression and regulatory strategies, ensuring the stability and effectiveness of synthetic biology experiments, thus providing technical support for practical applications and advancing our solutions to address Ulva bloom outbreaks. Finally, the Exploratory Models in Project Iteration demonstrated our early-stage technical attempts through continuous exploration and iteration. Although some models were not ultimately adopted, they provided valuable insights for improving hardware and experimental designs.
Overall, these models have been a key driving force for our project. They helped us better understand ecological processes, optimize experimental designs, and provided strong support for our innovations in ecological conservation. The application of these models not only propelled the project's development but also provided crucial technological support for future ecological conservation efforts.
## References
[1]Assis, J., Fernández Bejarano, S.J., Salazar, V.W., Schepers, L., Gouvêa, L., Fragkopoulou, E., Leclercq, F., Vanhoorne, B., Tyberghein, L., Serrão, E.A., Verbruggen, H., De Clerck, O. (2024) Bio-ORACLE v3.0. Pushing marine data layers to the CMIP6 Earth system models of climate change research. Global Ecology and Biogeography. doi: 10.1111/geb.13813.
[2]GBIF.org (15 June 2025) GBIF Occurrence Download https://doi.org/10.15468/dl.37bkzr
[3]GBIF (2025) 'What is GBIF?', GBIF.org. Available at: https://www.gbif.org/what-is-gbif (Accessed: 30 August 2025).
[4]Liu, C., Newell, G. and White, M. (2016) ‘On the selection of thresholds for predicting species occurrence with presence-only data’, Ecology and Evolution, 6(1), pp. 337-348–348. doi:10.1002/ece3.1878.
[5]MedCalc Software Ltd (2025) 'ROC curve analysis', MedCalc Manual. Available at: https://www.medcalc.org/manual/roc-curves.php (Accessed: 30 August 2025).
[6]Merow C, Smith MJ, Silander JA (2013) A practical guide to MaxEnt for modeling species’ distributions: what it does, and why inputs and settings matter. Ecography, 36(10), 1058-1069.
[7]Phillips SJ, Anderson RP, Schapire RE (2006) Maximum entropy modeling of species geographic distributions. Ecological modelling, 190(3): 231-259.
[8]Steven J. Phillips, Miroslav Dudík, Robert E. Schapire. 2004. A maximum entropy approach to species distribution modeling. In Proceedings of the Twenty-First International Conference on Machine Learning, pages 655-662. PDF
[9]Steven J. Phillips, Robert P. Anderson, Miroslav Dudík, Robert E. Schapire, Mary Blair. 2017. Opening the black box: an open-source release of Maxent. In Ecography. PDF
[10]Steven J. Phillips, Robert P. Anderson, Robert E. Schapire. 2006. Maximum entropy modeling of species geographic distributions. Ecological Modelling, 190:231-259, 2006. PDF Datasets used in this paper are available in the download section
[11]Copernicus Marine Environment Monitoring Service (CMEMS) (2025) Global ocean physics analysis and forecast. Copernicus Marine Service. Available at: https://doi.org/10.48670/moi-00016 (Accessed: 15 September 2025).
[12]Hao, Y. et al. (2020) ‘Competitive advantages of Ulva prolifera from Pyropia aquaculture rafts in Subei Shoal and its implication for the green tide in the Yellow Sea’, Marine Pollution Bulletin, 157. doi:10.1016/j.marpolbul.2020.111353.
[13]OceanParcels Team (2025) Quickstart to Parcels: Running particles in an idealised field. In: Parcels Tutorials & Documentation. Available at: https://docs.oceanparcels.org/en/latest/examples/parcels_tutorial.html#Running-particles-in-an-idealised-field (Accessed: 15 September 2025).
[14]Sun, K. et al. (2020) ‘A numerical study of the Ulva prolifera biomass during the green tides in China – toward a cleaner Porphyra mariculture’, Marine Pollution Bulletin, 161. doi:10.1016/j.marpolbul.2020.111805.
[15]Universidade de Santiago de Compostela. Departamento de Química Analítica, N. e B. et al. (2019) ‘Modeling dispersal of UV filters in estuaries’. Available at: https://search.ebscohost.com/login.aspx?direct=true&db=edsoai&AN=edsoai.on1400985227&site=eds-live&scope=site (Accessed: 15 September 2025).
[16]Ma, Q. and Wood, T.K. (2009) ‘OmpA influences Escherichia coli biofilm formation by repressing cellulose production through the CpxRA two-component system’, Environmental Microbiology, 11(10), pp. 2735-2746–2746. doi:10.1111/j.1462-2920.2009.02000.x.↩︎
[17]Ageorges, V.et al. (2019) ‘Differential homotypic and heterotypic interactions of antigen 43 (Ag43) variants in autotransporter-mediated bacterial autoaggregation’, Scientific Reports, 9(1). doi:10.1038/s41598-019-47608-4.↩︎
[18]XJTLU-CHINA iGEM (2023) Available at: https://2023.igem.wiki/xjtlu-china/index.html(Accessed: 30 August 2025)↩︎
[19]TUDelft iGEM (2009) Available at: Team:TUDelft - 2009.igem.org(Accessed: 30 August 2025)↩︎
[20]Kalisky, T. et al. (2007)'Cost-benefit theory and optimal design of gene regulation functions.' Physical biology vol. 4,4 229-45. 7 Nov.Available at: doi:10.1088/1478-3975/4/4/001.↩︎
[21]Stamatakis, M. and Nikos V.M. (2009) 'Comparison of deterministic and stochastic models of the lac operon genetic network.' Biophysical journal vol. 96,3. pp. 887-906.↩︎
[22]Wright, J K et al. (1981) 'Lactose carrier protein of Escherichia coli: interaction with galactosides and protons.' Biochemistry vol. 20,22. pp. 6404-15.Available at : doi:10.1021/bi00525a019.↩︎
[23]Norton, M. et al. (2010) 'Determining the Rate of Transcription of T7 RNA Polymerase Using Single Molecule Fluorescence Imaging' Available at:https://mds.marshall.edu/etd/112/↩︎
[24]Ecuador iGEM (2021) Available at: https://2021.igem.org/Team:Ecuador (Accessed: 8 August 2025)↩︎
[25]Ikeda, R.A., Lin, A.C., and Clarke, J. (1992) 'Initiation of transcription by T7 RNA polymerase as its natural promoters.' Journal of biological chemistry Vol. 267, Issue 4,5. pp. 2640-2649Available at: https://www.sciencedirect.com/science/article/pii/S0021925818459297↩︎
[26]Kelly, J.R. et al. (2009) 'Measuring the activity of BioBrick promoters using an in vivo reference standard.' Journal of biological engineering vol. 3 4. 20 Mar.Available at: doi:10.1186/1754-1611-3-4.↩︎
[27]Interactions of Zoospores of Ulva linza with Arginine-Rich Oligopeptide Monolayers | Langmuir (no date). Available at: https://pubs.acs.org/doi/full/10.1021/la900688g# (Accessed: 24 May 2025).↩︎
[28]Zimmerman, S.P., Kuhlman, B. and Yumerefendi, H. (2016) ‘Engineering and Application of LOV2-based Photoswitches’, Methods in enzymology, 580, pp. 169–190. Available at: https://doi.org/10.1016/bs.mie.2016.05.058.↩︎
[29]An optogenetic toolbox of LOV-based photosensitizers for light-driven killing of bacteria | Scientific Reports (no date). Available at: https://www.nature.com/articles/s41598-018-33291-4#Sec7 (Accessed: 24 Augist 2025).↩︎
[30]Light-inducible protein degradation in E. coli with the LOVdeg tag | eLife (no date). Available at: https://elifesciences.org/articles/87303#s3 (Accessed: 28 August 2025).↩︎
[31]RCSB Protein Data Bank (2025) 3D structure of PDB ID 4WF0. Available at: https://www.rcsb.org/3d-view/4WF0?preset=ligandInteraction&label_asym_id=C(Accessed: 26 September 2025).↩︎
[32]Orth, P. et al. (2000) ‘Structural basis of gene regulation by the tetracycline inducible Tet repressor-operator system’, Nature Structural Biology, 7(3), pp. 215-219. doi:10.1038/73324.↩︎
[33]AmberMD (2025) Amber Models. Available at: https://ambermd.org/AmberModels.php(Accessed: 26 September 2025).
[34]JerkWin (2025) JerkWin: A Web Tool for Accelerometer Data Visualization. Available at: https://jerkwin.github.io/(Accessed: 26 September 2025).
[35]Joint, I., Tait, K. and Wheeler, G. (2007) ‘Cross-kingdom signalling: exploitation of bacterial quorum sensing molecules by the green seaweed Ulva’, Philosophical Transactions of the Royal Society B: Biological Sciences, 362(1483), pp. 1223–1233. Available at: https://doi.org/10.1098/rstb.2007.2047.↩︎
[36]Diffusion Coefficient Definition (no date). Available at: https://www.comsol.com/multiphysics/diffusion-coefficient (Accessed: 7 September 2025).↩︎
[37]‘Fick’s laws of diffusion’ (2025) Wikipedia. Available at: https://en.wikipedia.org/w/index.php?title=Fick%27s_laws_of_diffusion&oldid=1303650783#Fick's_second_law (Accessed: 7 April 2025).↩︎
[38]Convection–diffusion equation - Wikipedia (no date). Available at: https://en.wikipedia.org/wiki/Convection%E2%80%93diffusion_equation (Accessed: 24 July 2025).↩︎
[39]Navier–Stokes equations - Wikipedia (no date). Available at: https://en.wikipedia.org/wiki/Navier%E2%80%93Stokes_equations (Accessed: 24 July 2025).↩︎
[40]4-bit adhesion logic enables universal multicellular interface patterning | Nature (no date). Available at: https://www.nature.com/articles/s41586-022-04944-2 (Accessed: 28 August 2025).↩︎
[41]Shafahi, M. and Vafai, K. (2009) ‘Biofilm affected characteristics of porous structures’, International Journal of Heat and Mass Transfer, 52(3), pp. 574–581. Available at: https://doi.org/10.1016/j.ijheatmasstransfer.2008.07.013.↩︎
[42]A Synthetic Bacterial Cell-Cell Adhesion Toolbox for Programming Multicellular Morphologies and Patterns: Cell (no date). Available at: https://www.cell.com/cell/fulltext/S0092-8674(18)30844-4?_returnURL=https%3A%2F%2Flinkinghub.elsevier.com%2Fretrieve%2Fpii%2FS0092867418308444%3Fshowall%3Dtrue (Accessed: 2 June 2025).↩︎
[IMG] Back to top button
