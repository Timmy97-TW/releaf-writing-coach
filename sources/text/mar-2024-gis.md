[IMG]
Home  Geospatial Analysis
Geospatial Analysis
Mapping the Past, Present and Future of Natural Rubber Cultivation
Contents
Abstract
Introduction
Motivation
Data & Technical Background
Climatic Suitability Criteria
H. brasiliensis Cultivation Zones
Habitat Suitability Model for T. kok-saghyz
Natural Rubber in the Age of Climate Change
Modelling the Effects of Climate Change
Effects on Natural Rubber Production
Disease
Conclusion & Outlook
Materials and Methods
References
Abstract
The global demand for natural rubber is reshaping the landscape of agricultural cultivation, driving expansion into new regions and increasing environmental risks. Using high-resolution geospatial analysis, we mapped the global distribution of Hevea brasiliensis (natural rubber) cultivation under current and future climate scenarios, generating the most detailed model to date. This analysis highlights shifts in suitable cultivation zones driven by climate change and identifies key ecological challenges, including the potential spread of the devastating South American Leaf Blight (SALB).
As the first iGEM team to integrate Geospatial Analysis into our project, we also developed the first set of cultivation suitability parameters for Taraxacum kok-saghyz, a sustainable alternative to H. brasiliensis. Our findings provide critical insights into the future of natural rubber production and offer data-driven recommendations for diversifying the natural rubber supply chain. This research lays the groundwork for developing adaptive strategies that ensure a resilient and environmentally conscious rubber cultivation.
Introduction
Natural rubber is a crucial industrial commodity with a wide array of applications, ranging from automotive tires to medical devices. Since 2021, global consumption of natural rubber has exceeded 14 million metric tons (1). This surging demand has been matched by increases in production, leading to significant changes in cultivation worldwide.
Traditionally, rubber cultivation has been concentrated within the equatorial belt between 10°S and 10°N. However, recent decades have witnessed an expansion and shift of rubber-growing zones to higher latitudes and longitudes (2, 3). This geographical redistribution is influenced not only by the need to meet global demand but also by factors like climate change and the development of more cold-tolerant plant varieties (4, 5).
The rapid expansion of rubber monocultures into new areas has raised substantial ecological concerns (6). The transformation of diverse landscapes into extensive rubber plantations has contributed notably to deforestation, habitat fragmentation, and biodiversity loss (7, 8).
In response to these ecological challenges, remote sensing techniques have become vital tools for analysis. By utilizing satellite imagery and geospatial data, researchers can map land-use and land-cover changes, offering critical insights into the transformation of natural ecosystems into agricultural areas. This broad-scale view is crucial for evaluating agricultural sustainability and developing adaptive strategies for future land management.
Geospatial analysis is also essential for generating crop suitability maps (9). By leveraging satellite-derived data on rainfall, temperature, and solar radiation, agricultural planners can identify which crops are best suited to particular regions. This capability is particularly important for adapting to climate change, as traditional cultivation areas may become less viable due to evolving environmental conditions. Such analysis allows for the re-evaluation of existing agricultural practices and supports the development of more resilient agricultural systems.
Several studies have attempted to forecast the future potential geographical range of Para rubber (Hevea brasiliensis) using ecological niche modeling and bioclimatic stratification (10, 11, 12). While these studies provide valuable insights, they are limited in scope, focusing on specific countries or regions rather than offering a global perspective. Additionally, they do not explore the potential of alternative rubber crops to complement current production systems.
While Hevea brasiliensis is the predominant source of natural rubber, the introduction of alternative species like Taraxacum kok-saghyz could help alleviate the pressure on current rubber cultivation areas, especially as climate change renders traditional growing regions less suitable (13). Despite the promising potential of T. kok-saghyz as a complementary rubber source, no bioclimatic models have been published to identify suitable cultivation zones for this crop. Given the increasing urgency of addressing climate-induced shifts in crop viability, the development of such models is essential to diversify rubber production and reduce the environmental and economic risks associated with relying on a single crop.
Motivation
To attain a holistic understanding of rubber cultivation and its associated threats, it is essential to examine the current state of cultivation, its limitations, and the evolving future landscape. This necessitates the use of global climatic data spanning historical, present, and future scenarios to comprehend the existing suitable zones for H. brasiliensis cultivation, how these have changed over recent decades, and how they might alter under various climate change scenarios.
We first wanted to focus on the direct implications, particularly covering:
- • Impact on Agricultural Sustainability: Climate change can shift suitable growing areas, affect crop yields, and alter overall productivity (47). Such changes can disrupt the environmental conditions necessary for cultivating crops like rubber, which are critical for global economic sustainability.
- • Pest Outbreaks: Pests such as South American Leaf Blight (SALB) pose serious threats to rubber cultivation. Understanding pest dynamics is crucial for agricultural planning and protection. Changing climate conditions, including variations in temperature and precipitation, can exacerbate the risks of pest outbreaks, necessitating proactive management strategies (33).
Understanding these factors in detail is essential to predict downstream effects such as:
- • Economic Implications: Natural rubber is integral to numerous industries. Climate-induced risks can affect rubber supply chains, leading to economic losses and disruptions in sectors dependent on this raw material (7).
- • Biodiversity and Ecosystem Health: Shifts in agricultural practices due to climate change and increased pest risks can lead to further deforestation and biodiversity loss, especially in ecologically sensitive regions like tropical rainforests. These environmental changes can have profound long-term effects on ecosystems (8).
- • Global Food Security: The expansion or relocation of rubber plantations into new areas may impact food security by creating competition for land resources between food crops and cash crops like rubber (48).
In addition to analyzing current rubber cultivation zones, we sought to explore alternative rubber sources like Taraxacum kok-saghyz. By mapping suitable cultivation areas for T. kok-saghyz, our goal was to assess its potential as a complementary rubber source. Diversifying rubber production in this way could help mitigate the risks posed by climate change and pests, while providing a more resilient and sustainable solution for global rubber production.
By conducting a thorough analysis and developing predictive models of rubber cultivation, we aimed to provide essential information to support adaptation strategies. These strategies can mitigate the impact of climate change on rubber agriculture. Such insights are crucial for policymakers to make informed decisions that balance economic growth with environmental sustainability.
Data & Technical Background
To achieve our objective of analyzing rubber cultivation under current and future climatic conditions, identifying a suitable dataset was essential. Based on previously published classifications of cultivation zones, we determined that the dataset needed to include monthly measurements of precipitation and temperature. One of the problems we identified while reviewing similar models was their coarse spatial resolutions, which limited predictive accuracy for detailed analyses and prompted us to seek higher-resolution datasets.
These high-resolution climate data are indispensable for fine-scale ecological and agricultural applications, as they capture the intricate spatial and temporal variations necessary for precise cultivation mapping. We sought a dataset that not only provided such high-resolution for recent climate data, but also included historical records spanning several decades to effectively capture temporal changes and trends.
Since we were also interested in future predictions, integrating climate change predictions from global circulation models (GCMs) based on the current Coupled Model Intercomparison Project Phase 6 (CMIP6) simulations was crucial. Ideally, the chosen dataset would either incorporate these projections directly or allow for seamless integration into our analysis.
One of the problems in this regard is that state-of-the-art global climate reanalyses often represent climatic variations at coarser resolutions of 0.25° to 1°, equivalent to about 25 to 100 km at the equator.
Bridging this gap typically involves using satellite data and statistical downscaling techniques for specific regions of interest, as well as interpolation methods applied to meteorological data. Climatologies based on satellite observations or statistical downscaling are generally superior to interpolated data for this applications because they better capture small-scale climatic patterns (14). However, many such high-resolution models are not available on a global scale.
After evaluating several climate datasets, including WorldClim2 (15), CRU (16), GPCC (17) and Climatologies at High Resolution for the Earth's Land Surface Areas (CHELSA) (18), we selected the CHELSA dataset as it perfectly fits our requirements. CHELSA is based on ERA5 reanalysis data, a global atmospheric reanalysis produced by the European Centre for Medium-Range Weather Forecasts (ECMWF). It combines observational data from meteorological stations, remote sensing, and satellites – totaling roughly 87 billion raw observations – with sophisticated model simulations.
One of the key advantages of CHELSA is its high spatial resolution of 30 arc-seconds, approximately 1 km² at the equator. Additionally, the dataset spans from 1979 to 2018, offering monthly temperature and precipitation data over four decades, which is invaluable for analyzing historical climate trends and variability. CHELSA provides a range of variables essential for our analysis, including monthly mean, minimum, and maximum temperatures, monthly total precipitation values, and derived bioclimatic variables such as annual temperature range, seasonality, and precipitation of the wettest and driest quarters.
For our project, we focused on mean temperature and precipitation, as these are critical factors influencing the growth and distribution of rubber plants. Later in the analysis, we also incorporated humidity data to assess pest risk zones.
Climatic Suitability Criteria
To classify cultivation zones for natural rubber, we primarily focus on two key climatic variables: mean temperature and precipitation. This approach aligns with established models in the literature, which have demonstrated the effectiveness of these parameters in determining suitable agricultural regions (19). However, it is important to acknowledge that such suitability zone models often tend to overestimate the actual areas where cultivation is feasible. This overestimation arises because these models typically do not account for several critical factors, including topographical features, population density, soil composition, and the presence of pest hotspots, which can significantly hinder cultivation in certain regions.
While existing models for suitable cultivation zones of Hevea brasiliensis are available, they are generally confined to specific regions and lack a comprehensive global perspective (10, 11, 19). This regional limitation restricts the applicability of the models in addressing the widespread and dynamic nature of rubber cultivation. Additionally, the constantly evolving data landscape, with the emergence of newer and more accurate datasets, necessitates the continual updating and refinement of these models to maintain their relevance and accuracy.
For our analysis, we utilized the CHELSA dataset described earlier. With its high resolution of 30 arcseconds, it encompasses approximately 900 million (20,800 × 43,200) data points for each climatic condition each month, resulting in 21,565,440,000 data points being used for the cultivation classification each year, as described in Figure 1. This high resolution provides a robust foundation for assessing climatic suitability on a global scale. To determine suitable cultivation zones, we applied rule-based classifications to each raw input layer.
[IMG]
Figure 1: GIS workflow for suitability classification based on temperature and precipitation. (A) Monthly mean temperature data is converted to binary layers, averaged yearly, and classified into suitable regions. (B) Monthly total precipitation follows the same process. (C) The temperature and precipitation classifications are combined and masked, producing the final suitability map for cultivation zones.
Initially, the classification process was conducted on the entire dataset, encompassing both oceans and landmasses. However, to refine our analysis and focus solely on land areas suitable for cultivation, we employed the Global Administrative Areas (GADM) shapefile. This allowed us to accurately delineate land masses by setting oceanic regions and other non-land areas to "no data," thereby ensuring that our suitability assessments were confined to viable terrestrial environments.
These classifications were based on parameters derived from existing literature as well as those developed through our own research, as illustrated in Figure 1.
H. brasiliensis Cultivation Zones
To estimate the suitable cultivation zones for current rubber production, we reviewed literature to identify the climatic criteria essential for H. brasiliensis cultivation. Our investigation revealed that most current models rely on the parameters defined by Rivano et al. (2015) (19), which we have summarized in Table 1.
| Climatic Criterion
| Prohibitive
| Suboptimal
| Optimal
| Excessive
| Annual mean temperature (°C)
| < 23
| 23-25
| 25-28
| > 28
| Number of months with mean temperature below 23°C
| > 5
| 1-5
| 0
| -
| Annual precipitation (mm)
| < 1100
| 1100-1500
| > 1500
| -
| Number of months with precipitation below 50mm
| > 5
| 4-5
| 0-3
| -
Table 1: Climatic thresholds for Hevea brasiliensis suitability, adapted from Rivano et al. (2015) (19). The table categorizes conditions into Prohibitive, Suboptimal, Optimal, and Excessive based on annual mean temperature, intra-annual temperature (months below 23°C), annual precipitation, and intra-annual precipitation (months below 50 mm). Optimal conditions occur with temperatures between 25-28°C, precipitation over 1500 mm, and minimal months below critical thresholds.
Our classification process involved analyzing the relevant gridded climate variables separately. Specifically, we directly categorized the total annual precipitation and the mean annual temperature layers into optimal, suboptimal, and prohibitive ranges. For the monthly mean temperature and monthly precipitation data, we employed a similar categorization process but incorporated two additional steps to account for the intra-annual distribution of these variables, as illustrated in Figure 1.
Building on the classification methodology presented by Golbon et al. (2018) (10), we integrated these separate criteria into a unified classification model. By overlaying the classification outcomes of the different climatic layers, each grid cell was assigned to one of four summarizing classes:
- • AllOpt: All climatic layers are classified as optimal.
- • SubOpt: At least one layer is classified as suboptimal, with none being prohibitive.
- • SingProh: Only one climatic layer falls within the prohibitive range.
- • MultProh: More than one climatic criterion is in the prohibitive range.
[IMG]
Figure 2: Global distribution of climatic suitable zones for Hevea brasiliensis cultivation based on parameters outlined in Table 1. The map classifies regions into four categories: Prohibitive (grey), Single prohibitive (light green), Suboptimal (green), and Optimal (dark green), as determined by the integration of intra- and inter-annual temperature and precipitation layers. The model represents the base year 2018. Optimal zones for H. brasiliensis cultivation are concentrated in tropical regions of South America, Central Africa, and Southeast Asia, with suboptimal areas in neighboring regions, while prohibitive zones dominate subtropical and temperate regions, where conditions are unsuitable.
This comprehensive classification model was applied globally, resulting in the map presented in Figure 2 for the baseline year 2018. To assess the stability of these predictions and illustrate potential shifts over time, we re-ran the classification process using historical climate data for each year from 1980 to 2018. The resulting Video 1 visually highlights the observed migration of cultivation zones.
Video 1: Timelapse of H. brasiliensis suitable cultivation zones between 1980 and 2018.
Traditionally, rubber cultivation has been concentrated within the equatorial belt between 10°S and 10°N. However, recent decades have witnessed an expansion and shift of rubber-growing zones to higher altitudes and latitudes, an observation confirmed by our reanalysis models. It is important to acknowledge that these maps may overestimate the real-world feasible crop zones. A significant portion of the optimal classifications extends into regions of South America, where H. brasiliensis cultivation is widely hindered by the presence of pests like the South American Leaf Blight (SALB). Without effective mitigation strategies and the development of more resistant rubber tree varieties, the practicality of cultivating rubber in these optimal zones remains questionable.
Despite these limitations, our model represents the most up-to-date, high-resolution, global cultivation zone model for Hevea brasiliensis to date.
Habitat Suitability Model for T. kok-saghyz
To assess the viability of large-scale cultivation of our proposed natural rubber alternative crop, Taraxacum kok-saghyz (TKS), we sought to develop a habitat suitability model analogous to those used for Hevea brasiliensis. Our initial step involved a thorough review of existing literature to determine whether such a model for TKS already existed. Surprisingly, we found that no comprehensive habitat suitability model has been developed for TKS to date.
While some publications have presented maps of potential TKS cultivation zones (20), these are limited to general climatic classifications and lack detailed modeling. These maps are primarily based on the observation that TKS naturally grows in temperate regions. Utilizing broad classifications like the Köppen-Geiger climate zones, these studies have broadly highlighted all temperate areas worldwide as potential cultivation zones for TKS. However, this approach is overly simplistic and does not account for the specific climatic conditions necessary for successful cultivation.
To create a more precise and reliable model, we set out to determine the detailed parameters suitable for TKS cultivation. As a starting point, we examined specific sampling sites where TKS is known to occur naturally. We selected four sites located in the Tian Shan mountain range valley in southeastern Kazakhstan, the native habitat of TKS (21). To gain a robust understanding of the climatic conditions in these regions, we extracted and analyzed climate data spanning the last 20 years. The intra-annual and inter-annual temperature and precipitation patterns observed at these sites are displayed in Figure 3.
[IMG]
Figure 3: Native TKS habitat zone. (A) Map showing the locations of four study sites – Zhalauly, Kegen, Saryzhaz, and Tuzkol – in the Tian Shan Mountain range valley, Almaty region, southeast Kazakhstan (inset). These sites represent native habitats of Taraxacum kok-saghyz. (B) Monthly average temperature for each year from 1998 to 2018, showing intra-annual variability across the four sites. (C) Monthly average precipitation, displaying the seasonal pattern of rainfall. (D) Annual mean temperature from 1998 to 2018, with bars showing the mean and error bars indicating standard deviation. Individual data points (circles) represent outliers. (E) Total annual precipitation for each year.
Our analysis yielded several key insights. First, we observed a prolonged cold winter period, consistent with the known vernalization requirements of TKS for flowering and seed production. Additionally, total annual precipitation in the studied regions averaged around 500 mm, significantly higher than the 250-300 mm reported in the literature (22). Contrary to earlier assumptions that TKS thrives in areas with dry summers, our data revealed moderate precipitation throughout the growing season.
Recognizing that TKS may have a broader ecological amplitude than previously thought, we conducted interviews with industry and academic stakeholders, including farmers cultivating TKS. These interviews confirmed that TKS is highly adaptable, thriving under a wide range of environmental conditions. This adaptability suggests that relying solely on data from its native habitat may underestimate its potential cultivation zones.
To further assess potential cultivation parameters, we expanded our analysis to include conditions from various field trials worldwide. To this end, we conducted an extensive meta-analysis of literature, research grants, and other publications that provided specific locations or coordinates of TKS field trials. This effort culminated in Table 2, which lists all identified sites, including those obtained from our Integrated Human Practices (IHP) interviews.
| ID
| City/Region
| Latitude
| Longitude
| Year
| Country
| Source
| TkCaSim13
| Simcoe
| 42.85
| -80.27
| 2013
| Canada
| (23)
| TkCaGue13
| Guelph
| 43.53
| -80.22
| 2013
| Canada
| (23)
| TkCaSim14
| Simcoe
| 42.85
| -80.27
| 2014
| Canada
| (23)
| TkCaGue14
| Guelph
| 43.53
| -80.22
| 2014
| Canada
| (23)
| TkChXin23
| Xinjiang
| 43.95
| 87.48
| 2023
| China
| (24)
| TkUsOhi13
| Ohio
| 41.01
| -82.73
| 2013
| USA
| (25)
| TkDeStr23
| Straubing
| 48.91
| 12.63
| 2023
| Germany
| IHP
| TkDeKru23
| Kruckow
| 53.9
| 13.25
| 2023
| Germany
| IHP
| TkDeQue12
| Quedlinburg
| 51.4
| 11.8
| 2012
| Germany
| (26)
| TkDeQue13
| Quedlinburg
| 51.4
| 11.8
| 2013
| Germany
| (26)
| TkDeQue14
| Quedlinburg
| 51.4
| 11.8
| 2014
| Germany
| (26)
| TkUsSmi15
| Smithville
| 40.86
| -81.86
| 2015
| USA
| (27)
| TkUsCel15
| Celeryville
| 41.03
| -82.73
| 2015
| USA
| (27)
| TkUsWoo13
| Wooster
| 40.77
| -81.92
| 2013
| USA
| (28)
| TkNlAch15
| Achterberg
| 51.97
| 5.6
| 2015
| Netherlands
| (29)
| TkNlElb15
| Elburg
| 52.45
| 5.83
| 2015
| Netherlands
| (29)
| TkEsArk10
| Arkaute
| 42.85
| -2.62
| 2010
| Spain
| (30)
Table 2: Compilation of T. kok-saghyz field trial sites derived from our meta-analysis of literature, grant applications, and IHP interviews. The table provides detailed information on trial sites, including city/region, geographical coordinates (latitude and longitude), the year of the trial, and country of origin. The trials are distributed globally, with sites in North America (Canada, USA), Europe (Germany, Netherlands, Spain), and Asia (China). Each entry is accompanied by a corresponding source, reflecting the wide range of research conducted between 2010 and 2023.
Using the climatic data corresponding to these field trial sites, we plotted the temperature and precipitation variables for the years during which TKS was planted (Figure 4). The data revealed a much wider array of climatic conditions compared to its native habitat. To directly compare the native and field trial cultivation conditions, we combined the datasets and plotted them against each other (Figures 5A and 5B). Notably, successful field trials were conducted in regions with warmer temperatures and varying precipitation levels, demonstrating TKS's tolerance to a wider range of climatic conditions than previously thought.
[IMG]
Figure 4: Suitable cultivation conditions in reported field trials of Taraxacum kok-saghyz.
These findings highlight TKS's resilience and adaptability, suggesting it can be cultivated in a broader range of environments than its native habitat would suggest. To quantify these observations, we developed a set of cultivation parameters. We categorized these conditions into native-like, field trial-like, and prohibitive zones, represented by different shades in Figures 5C and 5D.
[IMG]
Figure 5: Comparison of TKS cultivation conditions between field trials and native habitat. (A) Annual mean temperature. (B) Annual total precipitation. (C) Cultivation parameter space showing annual mean temperature vs. total precipitation, with zones categorized as native-like, field trial-like, or prohibitive. (D) Parameter space showing months with mean temperatures below 5°C vs. months with precipitation below 70 mm, categorized similarly.
This analysis led to the establishment of, to the best of our knowledge, first set of cultivation zone parameters for TKS, as presented in Table 3. These parameters provide a more accurate and practical framework for identifying potential cultivation areas, moving beyond simplistic temperate zone classifications.
| Condition
| Prohibitive
| Native Habitat
| Field Trials
| Excessive
| Annual mean temperature (°C)
| < 1.0
| 1.0-5.0
| 5.0-12.0
| > 12.0
| Number of months with mean temperature below 5°C
| < 1
| 5-7
| 1-5
| >7
| Annual precipitation (mm)
| < 300
| 300-850
| 850-1200
| >1200
| Number of months with precipitation below 70mm
| < 2
| 8-12
| 2-8
| -
Table 3: Parameters derived from geospatial analysis of both native habitats and field trials for suitable cultivation zones of T. kok-saghyz.
Using a similar methodology as for H. brasiliensis, we applied these parameters to generate a global map of suitable cultivation zones for both H. brasiliensis and TKS (Figure 6). The map illustrates that TKS's potential cultivation zones complement those of H. brasiliensis, expanding the geographical areas suitable for natural rubber production.
[IMG]
Figure 6: Global cultivation suitability for Hevea brasiliensis and Taraxacum kok-saghyz. The map shows optimal, suboptimal, single prohibitive, and prohibitive zones for H. brasiliensis (green shades) and suboptimal, field trial-like, native-like, and prohibitive zones for T. kok-saghyz (purple).
This diversification opens opportunities for rubber cultivation in regions previously deemed unsuitable, thereby enhancing the resilience and sustainability of global rubber supply chains.
Expanding rubber cultivation to include TKS in these new regions could mitigate some of the risks associated with over-reliance on Hevea brasiliensis, such as vulnerability to climate change and pest outbreaks like the South American Leaf Blight (SALB). Moreover, it offers the potential to alleviate pressure on tropical ecosystems currently impacted by rubber plantation expansion, thereby contributing to biodiversity conservation and promoting sustainable land-use practices.
By providing a more nuanced and data-driven understanding of TKS habitat suitability, we aim for our model to serve as a valuable tool for policymakers and stakeholders interested in diversifying and securing natural rubber sources.
Natural Rubber in the Age of Climate Change
Climate change is profoundly reshaping the landscape of natural rubber production, introducing challenges that threaten the stability and sustainability of this essential commodity.
The Intergovernmental Panel on Climate Change (IPCC) Sixth Assessment Report (AR6) highlights the severe consequences of climate change on global agriculture. Without substantial mitigation and adaptation efforts, the agricultural sector will continue to experience significant disruptions due to rising temperatures, altered precipitation patterns, and more frequent extreme weather events.
One immediate impact is the shift in suitable cultivation zones for Hevea brasiliensis previously described. Changing climate conditions are pushing these zones toward higher latitudes and altitudes, affecting where rubber trees can optimally grow.
Heightened temperatures and altered rainfall regimes place additional stress on rubber trees, leading to reduced yields (31). Extreme heat accelerates the aging process of the trees, shortening their productive lifespan. Irregular rainfall disrupts the delicate balance required for optimal latex production, while prolonged droughts or excessive rainfall can further diminish productivity (32).
The increasing frequency and intensity of extreme weather events – such as typhoons, floods, and droughts – pose direct threats by causing physical damage to trees and infrastructure and hindering harvesting operations. For example, strong winds can uproot rubber trees, leading to immediate losses.
Climate change also exacerbates the proliferation of pests and diseases. Warmer temperatures and altered humidity levels create favorable conditions for threats like the South American Leaf Blight (SALB) and various insect vectors (33).
The adverse effects of climate change on rubber production extend beyond agricultural losses, impacting the livelihoods of millions of smallholder farmers and the economies of rubber-dependent regions (34). Reduced yields and increased costs of production can lead to higher prices for natural rubber, affecting downstream industries and consumers globally. Moreover, the necessity to relocate plantations to more favorable areas can result in land-use conflicts and displacement of communities, exacerbating social tensions and economic disparities (35).
[IMG]
Figure 7: Comparison of Shared Socioeconomic Pathways (SSPs) and Representative Concentration Pathways (RCPs) for CMIP6 climate scenarios. The chart displays radiative forcing levels in 2100 (W/m²) across various SSPs, categorized into Tier 1 (top priority) and Tier 2 (additional scenarios of interest). SSPs are mapped against previously used RCP scenarios from CMIP5 for reference. Image taken from the climate scenario website of the Canadian government.
Addressing the complex challenges of climate change requires a thorough understanding of both environmental and socio-economic factors. To facilitate this, the Shared Socioeconomic Pathways (SSPs) (36) were developed as a set of scenarios that complement the Representative Concentration Pathways (RCPs). While RCPs describe potential radiative forcing levels by 2100, the SSPs provide a broader perspective, examining the socio-economic drivers behind emissions and the global capacity to mitigate or adapt to climate change.
The five core SSPs illustrate different futures shaped by factors like economic growth, technological development, demographic shifts, and policy approaches (Figure 7). For our analysis of rubber cultivation under future climate scenarios, we have focused on three key SSPs – SSP1 (Sustainability), SSP3 (Regional Rivalry), and SSP5 (Fossil-Fueled Development). These pathways were selected based on Tier 1 recommendations from The Scenario Model Intercomparison Project (ScenarioMIP) (37).
Further details on the specific SSPs chosen for this project:
SSP1 – Sustainability – Taking the green road (low challenges to mitigation and adaptation)
- • The world shifts gradually, but pervasively, toward a more sustainable path, emphasizing more inclusive development that respects perceived environmental boundaries.
- • Management of the global commons slowly improves, educational and health investments accelerate the demographic transition, and the emphasis on economic growth shifts toward a broader emphasis on human well-being.
- • Driven by an increasing commitment to achieving development goals, inequality is reduced both across and within countries.
- • Consumption is oriented toward low material growth and lower resource and energy intensity.
SSP3 – Regional rivalry – A rocky road (high challenges to mitigation and adaptation)
- • A resurgent nationalism, concerns about competitiveness and security, and regional conflicts push countries to increasingly focus on domestic or, at most, regional issues.
- • Policies shift over time to become increasingly oriented toward national and regional security issues.
- • Countries focus on achieving energy and food security goals within their own regions at the expense of broader-based development.
- • Investments in education and technological development decline.
- • Economic development is slow, consumption is material-intensive, and inequalities persist or worsen over time.
- • Population growth is low in industrialized countries and high in developing countries.
- • A low international priority for addressing environmental concerns leads to strong environmental degradation in some regions.
SSP5 – Fossil-fueled development – Taking the highway (high challenges to mitigation, low challenges to adaptation)
- • This world places increasing faith in competitive markets, innovation and participatory societies to produce rapid technological progress and development of human capital as the path to sustainable development.
- • Global markets are increasingly integrated.
- • There are also strong investments in health, education, and institutions to enhance human and social capital.
- • At the same time, the push for economic and social development is coupled with the exploitation of abundant fossil fuel resources and the adoption of resource and energy intensive lifestyles around the world.
- • All these factors lead to rapid growth of the global economy, while global population peaks and declines in the 21st century.
- • Local environmental problems like air pollution are successfully managed.
- • There is faith in the ability to effectively manage social and ecological systems, including by geo-engineering if necessary.
These pathways provide a diverse set of scenarios which are critical for understanding their potential impacts on natural rubber production.
Modelling the Effects of Climate Change
To comprehensively map the effects of climate change on natural rubber cultivation, we required high-resolution future projection models. Fortunately, recent publications on CHELSA have extended the model with a selected number Global Circulation Models (GCMs) (38). These models were part of the Coupled Model Intercomparison Project Phase 6 (CMIP6), which provides a suite of climate models simulating future climate conditions based on varying greenhouse gas emission scenarios. They were specifically interesting to us, as they were used as input for the IPCC AR6 Working Group I. This selection of the specific models used aligns with the latest protocol from the Inter-Sectoral Impact Model Intercomparison Project (ISIMIP3), further ensuring consistency in our approach.
| Title
| Institution
| Priority
| GFDL-ESM4
| National Oceanic and Atmospheric Administration, Geophysical Fluid Dynamics Laboratory, USA
| 1
| UKESM1-0-LL
| Met Office Hadley Centre, UK
| 2
| MPI-ESM1-2-HR
| Max Planck Institute for Meteorology, Germany
| 3
| IPSL-CM6A-LR
| Institute Pierre Simon Laplace, France
| 4
| MRI-ESM2-0
| Meteorological Research Institute, Japan
| 5
Table 4: The models we've used to evaluate the effects of climate change on rubber cultivation zones.
We applied rule-based classifications to a selection of these five gridded climatic data projections, following a methodology similar to that described previously (see Figure 1).
Our approach employed a post-classification ensemble technique, where the classification process was conducted separately for each GCM, and the ensemble projection was determined based on the most frequent classification outcome for each grid cell.
As highlighted by Thompson et al. (2013) (39) and Stephens et al. (2012) (40), avoiding simple averaging in ensemble formation is crucial to preserve the inherent variability and information within individual models.
Using such an ensemble of models is crucial for addressing the uncertainties inherent in climate projections. Different GCMs incorporate varying assumptions, parameterizations, and structural frameworks, which result in a range of potential future climate conditions. An ensemble approach captures this diversity, offering a broader spectrum of possible outcomes and mitigating the limitations of individual models.
In regions where no absolute majority classification is achieved, we applied the priority of models as recommended by ISIMIP. This prioritization ensures that the most reliable and relevant models influence the final classification, maintaining the overall integrity and applicability of our climate impact assessments.
[IMG]
Figure 8: Ensemble classification and model confidence levels for SSP3-7.0 (2071-2100). (A) Shows the ensemble decision for rubber cultivation zones, classified as prohibitive, single prohibitive, suboptimal, or optimal. (B) Depicts the confidence level based on the number of models in agreement, ranging from 1 to 5.
Effects on Natural Rubber Production
For our analysis, we've used the three previously described SSP scenarios (SSP1-2.6, SSP3-7.0, SSP5-8.5) to assess the potential changes in Hevea brasiliensis cultivation zones. Each scenario was evaluated over three time periods: 2011-2040, 2041-2070, and 2071-2100, providing insights into short-, medium-, and long-term projections of rubber tree cultivation.
We classified cultivation suitability zones into four categories based on climate conditions: optimal, suboptimal, marginal, and prohibitive, consistent with our previous approach described in Figure 1. Figure 9A illustrates these classifications, revealing a progressive decline in optimal cultivation zones, particularly under higher emission scenarios SSP3-7.0 and SSP5-8.5, as climate change intensifies from 2041 onward.
[IMG]
Figure 9: A) Ensemble classification of rubber cultivation zones under SSP1-2.6, SSP3-7.0, and SSP5-8.5 for different timeframes. B) Corresponding model confidence levels for each scenario and timeframe.
Initially, regions such as South America, Southeast Asia, and parts of West Africa remain prominent areas for suitable cultivation. However, by the end of the century, these regions experience significant reductions and shifts in suitability. Under more aggressive warming scenarios, marginal and prohibitive zones increase, indicating a shrinking window for optimal rubber cultivation globally.
The use of an ensemble model allowed us to provide a certainty level associated with the predictions of these different CMIP6 models, as represented in Figure 9B. As expected, the certainty of these predictions decreases for projections further in the future as well as more extreme scenarios such as SSP3-7.0 and SSP5-8.5. In particular, regions further from the equator, zones that are at the forefront of the cultivation zone shift, show greater uncertainty as expected.
In order to quantify these observations, we needed to transform these maps into precise numbers that represent the actual area affected. Recognizing the distortion of area associated with map projections into 2D, we first had to re-transform these classifications onto the ellipsoid of the Earth, allowing us to find a suitable km² approximation for each point in the gridded classification data.
This resulted in Figure 10, which quantifies the changes in suitable and prohibitive zones across different SSPs and time periods. To this end, we've used the years 1981-2010 as a baseline. We observed that indeed, optimal cultivation areas shrink significantly over time, especially under SSPs with higher forcing levels, with only small areas remaining optimal by 2100.
[IMG]
Figure 10: Change in cultivation classification (given in km²) under different SSP scenarios and timeframes.
While these cross-tabulation matrices provide concrete data, they pose the challenge of being difficult to interpret at a glance. As demonstrated by Cuba (2015) (41), Sankey diagrams are superior to cross-tabulation matrices in reflecting land-use dynamics, particularly when multiple time sections are of interest. In Figure 11, we generated corresponding Sankey diagrams to illustrate the climatic suitability class shifts projected to occur under each SSP for each adjacent pair of time sections.
[IMG]
Figure 11: Sankey diagram illustrating the cultivation area change over the years, based on the data provided in Figure 10.
Under SSP1-2.6, representing a low-emission scenario, optimal cultivation areas remain relatively stable, though suboptimal and marginal areas increase slightly by mid-century. In contrast, there is a notable expansion of suboptimal zones in SSP3-7.0 and SSP5-8.5, which is likely to lead to increased cultivation uncertainty and possible productivity losses. The shifts in optimal cultivation zones reflect the impact of global warming, with regions currently suitable for rubber cultivation becoming marginal or prohibitive over the century.
Disease
Although rubber trees originate from the Amazon basin, the Americas contribute only a small portion of global rubber production, accounting for just 2.7% of the over 14 million tons produced worldwide (42). The primary reason for this limited production is the devastating impact of South American leaf blight (SALB), a fungal disease caused by Microcyclus ulei (43). SALB targets the young leaves of rubber trees, causing lesions that lead to defoliation. With repeated cycles of defoliation, the trees are progressively weakened and, in many cases, eventually destroyed. While SALB remains confined to the Americas, it poses a significant threat to rubber production in Asia and Africa, regions where the majority of global rubber is cultivated.
One of the key vulnerabilities of the Asian rubber industry lies in the genetic uniformity of the rubber trees. The high-yielding clones that dominate production globally are derived from a narrow genetic base, particularly from populations in the Pará state of Brazil where natural resistance to SALB is notably low (44). This lack of genetic diversity, exacerbated by decades of breeding in SALB-free environments, has made Asian rubber plantations especially susceptible to the potential spread of the disease (45). By contrast, M. ulei has demonstrated significant evolutionary potential, allowing it to adapt and thrive in various environmental conditions (46).
This problem is further exacerbated by the steady increase in the amount and size of monocultures of H. brasiliensis in Asia, which heightens the risk for SALB. To quantify the threat posed by SALB to current natural rubber cultivation, we employed a hotspot analysis approach, mapping the conditions where M. ulei infection could potentially occur. This analysis is based on climatic conditions suitable for the fungus.
The climatic conditions in many parts of Asian rubber sites are similar to SALB-endemic regions in Brazil. Previous studies used Geographic Information Systems (GIS) to compare the climatic records of rubber-growing countries in Asia, including Thailand, Indonesia, and Malaysia, with SALB-endemic regions, confirming the climatic suitability of SALB to these countries. To confirm this analysis, we used the parameters described in the Pest Risk Analysis for South American Leaf Blight by the FAO:
- 1. Average temperature of March, April and May (refoliation in Northern Hemisphere) is higher than 18.5°C
- 2. Average temperature of September, October and November (refoliation in Southern Hemisphere) is higher than 18.5°C.
- 3. Annual rainfall is higher than 760 mm.
- 4. There is no more than 6 consecutive months with less than 42 mm per month of rainfall.
Applying these parameters for our base year 2018 yielded Figure 12. Key regions of M. ulei suitability are concentrated in South America, especially in the Amazon basin, the Congo Basin in Africa, and parts of Southeast Asia. These regions reflect the known favorable humid and warm climates conducive to SALB development.
[IMG]
Figure 12: A) M. ulei suitable conditions modeled with parameters given by the FAO. B) Conditions overlaid with H. brasiliensis suitable cultivation zones. Both are modeled for the basis year 2018.
The regions most at risk are in South America, where large portions of suitable cultivation zones overlap with areas highly conducive to SALB outbreaks, consistent with observations from the past 100 years. However, similar overlaps occur in West Africa and Southeast Asia, further highlighting the threats faced by Hevea brasiliensis cultivation.
To ensure that these predictions were robust, we reviewed current literature and came across adapted parameters proposed by Roy et al. (2017) (33). Compared to the FAO parameters, these are on a monthly basis, allowing us to map month-to-month changes in SALB risk hotspots.
| Parameter
| Non membership range
| Membership range
| Temperature (°C)
| Minimum - 18.49 ; 36.5 - maximum
| 18.5 - 36.49
| Relative humidity (%)
| Minimum - 64.9
| 65 - maximum
| Monthly precipitation (mm)
| Minimum - 62.9
| 63 - maximum
Table 5: Parameters for M.ulei suitable zones adapted from Roy et al., 2017 (33).
Unlike our previous modeling efforts, these parameters included a humidity factor, which required the collection of additional data for all historical months. Fortunately, CHELSA provides this data, simplifying the process.
We used this to evaluate global SALB risk for each month, starting from January 1980 up to and including December 2018, totalling 468 months. This resulted in the findings shown in Video 2, providing a more fine-grained understanding of the changing conditions.
Video 2: SALB hotspot analysis (monthly)
Since leaves are only susceptible during their growth phase (up to 10-15 days), it is crucial to have not only fine-grained spatial but also temporal resolution to map SALB hotspots within the specific timeframe when trees are vulnerable. Our observations indicate that in many regions currently cultivating Hevea brasiliensis, conditions suitable for Microcyclus ulei are not optimal during refoliation in the first quarter of the year. However, we believe this is only a contributing factor and does not imply these zones are safe from SALB, as many young treelets experience multiple refoliations throughout the year.
We also applied these criteria on an annual basis to investigate the number of months where SALB conditions are met. This resulted in Video 3, which visualizes the accumulation of months with suitable conditions, ranging from year-round in deep red to lighter colors. Comparing the FAO-derived parameters in Figure 12 with the annual conditions from Table 5 (shown in Video 3) reveals a clear overlap. This highlights the significant threat to current rubber cultivation.
Video 3: SALB Hotspot analysis (annual)
The absence of a SALB outbreak in mainland and Southeast Asia is largely due to concentrated quarantine and isolation efforts by organizations such as the Asia and Pacific Plant Protection Commission (APPPC). However, this could change at any moment, as a single outbreak in this densely concentrated rubber production area could threaten the entire industry. With the shifts in temperature and precipitation caused by climate change, the region is becoming increasingly suitable for M. ulei, placing even greater pressure on the industry.
Conclusion & Outlook
Our geospatial analysis provides a detailed, high-resolution view of current and future rubber cultivation zones under various climate change scenarios. By mapping both Hevea brasiliensis and Taraxacum kok-saghyz suitability, we offer new insights into diversifying natural rubber sources to mitigate risks associated with climate change and disease outbreak. These findings highlight the urgent need for adaptive strategies to safeguard natural rubber production and enhance the resilience of global supply chains.
One key challenge facing current and future rubber cultivation is its impact on biodiversity. Expanding rubber production into new regions often leads to habitat loss, deforestation, and ecosystem disruption. Our analysis underscores the importance of balancing rubber cultivation with the preservation of biodiversity, particularly in ecologically sensitive regions. Sustainable land-use practices, including agroforestry and mixed cropping systems, should be integrated into future rubber cultivation strategies to mitigate these impacts.
While our models represent the most detailed global analysis of rubber cultivation zones to date, there is room for refinement. Incorporating additional data such as topographical maps, population density areas, and soil compositions will enhance the precision of these models.
Looking ahead, further research should focus on expanding the use of alternative rubber sources, such as T. kok-saghyz, which can reduce the ecological footprint of rubber production while enhancing the resilience of supply chains.
Our work establishes a foundation for sustainable rubber cultivation, bridging the gap between scientific research and agricultural practice. As the pressures of climate change intensify, it is essential to refine and adapt these strategies to secure a more resilient and environmentally responsible future for natural rubber production.
Materials and Methods
We utilized the CHELSA V2.1 dataset for climate data and the Global Administrative Areas (GADM) dataset for geographic boundaries. Geospatial visualization were performed using QGIS (version 3.36.3). Data processing and analysis were conducted in Python (version 3.11.6) using the libraries fiona (version 1.9.6), rasterio (version 1.3.10) and numpy (version 1.26.2).
References
1
Malaysian Rubber Council (MRC). MRC Official Website.
Website
2
A. Ahrends, P. Hollingsworth, A. Ziegler, J. Fox, H. Chen, Y. Su, J. Xu. Current trends of rubber plantation expansion may threaten biodiversity and livelihoods.
Elsevier BV, 2015.
CrossrefGoogle Scholar
3
B. Chen, X. Li, X. Xiao, B. Zhao, J. Dong, W. Kou, Y. Qin, C. Yang [...] G. Xie, G. Lan. Mapping tropical forests and deciduous rubber plantations in Hainan Island, China by integrating PALSAR 25-m and multi-temporal Landsat images.
Elsevier BV, 2016.
CrossrefGoogle Scholar
4
W. Chen, X. Wang, S. Yan, X. Huang, H. Yuan. The ICE-like transcription factor HbICE2 is involved in jasmonate-regulated cold tolerance in the rubber tree (Hevea brasiliensis).
Springer Science and Business Media LLC, 2019.
CrossrefGoogle Scholar
5
F. Azizan, I. Astuti, A. Young, A. Abdul Aziz. Rubber leaf fall phenomenon linked to increased temperature.
Elsevier BV, 2023.
CrossrefGoogle Scholar
6
H. He Pia, K. Martin. Effects of rubber cultivation on biodiversity in the Mekong Region..
CABI Publishing, 2021.
CrossrefGoogle Scholar
7
I. Häuser, K. Martin, J. Germer, P. He, S. Blagodatskiy, L. Liu HongXi, M. Krauss, A. Rajaona [...] G. Cadisch, T. Aenis. Environmental and socio-economic impacts of rubber cultivation in the Mekong region: challenges for sustainable land use..
CABI Publishing, 2015.
CrossrefGoogle Scholar
8
Y. Wang, P. Hollingsworth, D. Zhai, C. West, J. Green, H. Chen, K. Hurni, Y. Su [...] A. Ahrends, J. Xu. High-resolution maps show that rubber causes substantial deforestation.
Springer Science and Business Media LLC, 2023.
CrossrefGoogle Scholar
9
B. Peter, J. Messina, Z. Lin, S. Snapp. Crop climate suitability mapping on the cloud: a geovisualization application for sustainable agriculture.
Springer Science and Business Media LLC, 2020.
CrossrefGoogle Scholar
10
R. Golbon, M. Cotter, J. Sauerborn. Climate change impact assessment on the potential rubber cultivating area in the Greater Mekong Subregion.
IOP Publishing, 2018.
CrossrefGoogle Scholar
11
D. Ray, M. Behera, J. Jacob. Improving spatial transferability of ecological niche model of Hevea brasiliensis using pooled occurrences of introduced ranges in two biogeographic regions of India.
Elsevier BV, 2016.
CrossrefGoogle Scholar
12
R. Zomer, A. Trabucco, M. Wang, R. Lang, H. Chen, M. Metzger, A. Smajgl, P. Beckschäfer, J. Xu. Environmental stratification to model climate change impacts on biodiversity and rubber production in Xishuangbanna, Yunnan, China.
Elsevier BV, 2014.
CrossrefGoogle Scholar
13
J. van Beilen, Y. Poirier. Establishment of new crops for the production of natural rubber.
Elsevier BV, 2007.
CrossrefGoogle Scholar
14
V. Deblauwe, V. Droissart, R. Bose, B. Sonké, A. Blach‐Overgaard, J. Svenning, J. Wieringa, B. Ramesh, T. Stévart, T. Couvreur. Remotely sensed temperature and precipitation data improve species distribution modelling in the tropics.
Wiley, 2016.
CrossrefGoogle Scholar
15
S. Fick, R. Hijmans. WorldClim 2: new 1‐km spatial resolution climate surfaces for global land areas.
Wiley, 2017.
CrossrefGoogle Scholar
16
I. Harris, P. Jones, T. Osborn, D. Lister. Updated high‐resolution grids of monthly climatic observations – the CRU TS3.10 Dataset.
Wiley, 2013.
CrossrefGoogle Scholar
17
U. Schneider, A. Becker, P. Finger, A. Meyer-Christoffer, M. Ziese, B. Rudolf. GPCC's new land surface precipitation climatology based on quality-controlled in situ data and its role in quantifying the global water cycle.
Springer Science and Business Media LLC, 2013.
CrossrefGoogle Scholar
18
D. Karger, O. Conrad, J. Böhner, T. Kawohl, H. Kreft, R. Soria-Auza, N. Zimmermann, H. Linder, M. Kessler. Climatologies at high resolution for the earth’s land surface areas.
Springer Science and Business Media LLC, 2017.
CrossrefGoogle Scholar
19
F. Rivano, L. Maldonado, B. Simbaña, R. Lucero, E. Gohet, V. Cevallos, T. Yugcha. Suitable rubber growing in Ecuador: An approach to South American leaf blight.
Elsevier BV, 2015.
CrossrefGoogle Scholar
20
C. Schulze, D. Wahler, D. Prufer. Natural Rubber Biosynthesis and Physic-Chemical Studies on Plant Derived Latex.
InTech, 2012.
CrossrefGoogle Scholar
21
K. Uteulin, B. Suleimenov, K. Pachikin. The Soils of Natural (In Situ) Coenopopulations of Taraxacum kok-saghyz L.E. Rodin in Kazakhstan.
MDPI AG, 2023.
CrossrefGoogle Scholar
22
M. Ulmann. Wertvolle Kautschukpflanzen des gemässigten Klimas.
De Gruyter, 2022.
CrossrefGoogle Scholar
23
A. Moussavi, S. Cici, C. Loucks, R. Van Acker. Establishing field stands of Russian dandelion (Taraxacum Kok-saghyz) from seed in southern Ontario, Canada.
Canadian Science Publishing, 2016.
CrossrefGoogle Scholar
24
R. Chen, Q. Yan, T. Tuoheti, L. Xu, Q. Gao, Y. Zhang, H. Ren, L. Zheng, F. Wang, Y. Liu. A prediction model of rubber content in the dried root of Taraxacum kok-saghyz Rodin based on near-infrared spectroscopy.
Springer Science and Business Media LLC, 2024.
CrossrefGoogle Scholar
25
Z. Luo, B. Iaffaldano, X. Zhuang, J. Fresnedo-Ramírez, K. Cornish. Analysis of the first Taraxacum kok-saghyz transcriptome reveals potential rubber yield related SNPs.
Springer Science and Business Media LLC, 2017.
CrossrefGoogle Scholar
26
M. Kreuzberger, T. Hahn, S. Zibek, J. Schiemann, K. Thiele. Seasonal pattern of biomass and rubber and inulin of wild Russian dandelion (Taraxacum koksaghyz L. Rodin) under experimental field conditions.
Elsevier BV, 2016.
CrossrefGoogle Scholar
27
A. Shah, H. Keener, R. Fioritto, M. Klingman, D. Pote, and S. Wolfe. Taraxacum kok-saghyz Field Establishment.
Website
28
G. Bates, S. McNulty, N. Amstutz, V. Pool, K. Cornish. Planting Density and Growth Cycle Affect Actual and Potential Latex and Rubber Yields in Taraxacum kok-saghyz.
American Society for Horticultural Science, 2019.
CrossrefGoogle Scholar
29
DRIVE4EU. Dandelion Rubber and Inulin Valorization and Exploitation for Europe.
Website
30
M. Arias, M. Hernández, E. Ritter. How does water supply affect Taraxacum koksaghyz Rod. rubber, inulin and biomass production?.
Elsevier BV, 2016.
CrossrefGoogle Scholar
31
P. Rao, C. Saraswathyamma, M. Sethuraj. Studies on the relationship between yield and meteorological parameters of para rubber tree (Hevea brasiliensis)1The paper is based on the work and experience of the authors and in no way reflects the views of the Rubber Board or Department of Science and Technology, Government of India.1.
Elsevier BV, 2002.
CrossrefGoogle Scholar
32
A. Cahyo, M. Babel, A. Datta, K. Prasad, R. Clemente. EVALUATION OF LAND AND WATER MANAGEMENT OPTIONS TO ENHANCE PRODUCTIVITY OF RUBBER PLANTATION USING WaNuLCAS MODEL.
Agrivita, Journal of Agricultural Science (AJAS), 2016.
CrossrefGoogle Scholar
33
C. Roy, Z. Newby, J. Mathew, D. Guest. A climatic risk analysis of the threat posed by the South American leaf blight (SALB) pathogen Microcyclus ulei to major rubber producing countries.
Springer Science and Business Media LLC, 2016.
CrossrefGoogle Scholar
34
J. Fox, J. Castella. Expansion of rubber (Hevea brasiliensis) in Mainland Southeast Asia: what are the prospects for smallholders?.
Informa UK Limited, 2013.
CrossrefGoogle Scholar
35
M. Kenney-Lazar. Plantation rubber, land grabbing and social-property transformation in southern Laos.
Informa UK Limited, 2012.
CrossrefGoogle Scholar
36
M. Meinshausen, Z. Nicholls, J. Lewis, M. Gidden, E. Vogel, M. Freund, U. Beyerle, C. Gessner [...] R. Wang, M. Vollmer. The shared socio-economic pathway (SSP) greenhouse gas concentrations and their extensions to 2500.
Copernicus GmbH, 2020.
CrossrefGoogle Scholar
37
B. O'Neill, C. Tebaldi, D. van Vuuren, V. Eyring, P. Friedlingstein, G. Hurtt, R. Knutti, E. Kriegler [...] B. Sanderson, K. Riahi. The Scenario Model Intercomparison Project (ScenarioMIP) for CMIP6.
Copernicus GmbH, 2016.
CrossrefGoogle Scholar
38
D. Karger, D. Schmatz, G. Dettling, N. Zimmermann. High-resolution monthly precipitation and temperature time series from 2006 to 2100.
Springer Science and Business Media LLC, 2020.
CrossrefGoogle Scholar
39
R. Thompson, J. Beardall, J. Beringer, M. Grace, P. Sardina. Means and extremes: building variability into community‐level climate change experiments.
Wiley, 2013.
CrossrefGoogle Scholar
40
E. Stephens, T. Edwards, D. Demeritt. Communicating probabilistic information from climate model ensembles—lessons from numerical weather prediction.
Wiley, 2012.
CrossrefGoogle Scholar
41
N. Cuba. Research note: Sankey diagrams for visualizing land cover dynamics.
Elsevier BV, 2015.
CrossrefGoogle Scholar
42
International Rubber Study Group. IRSG Website.
Website
43
B. Hora Júnior, D. de Macedo, R. Barreto, H. Evans, C. Mattos, L. Maffia, E. Mizubuti. Erasing the Past: A New Identity for the Damoclean Pathogen Causing South American Leaf Blight of Rubber.
Public Library of Science (PLoS), 2014.
CrossrefGoogle Scholar
44
J. Guyot, V. Le Guen. A Review of a Century of Studies on South American Leaf Blight of the Rubber Tree.
Scientific Societies, 2017.
CrossrefGoogle Scholar
45
P. Priyadarshan. Genetic Diversity and Erosion in Hevea Rubber.
Springer International Publishing, 2015.
CrossrefGoogle Scholar
46
B. Barrès, J. Carlier, M. Seguin, C. Fenouillet, C. Cilas, V. Ravigné. Understanding the recent colonization history of a plant pathogenic fungus using population genetic tools and Approximate Bayesian Computation.
Springer Science and Business Media LLC, 2012.
CrossrefGoogle Scholar
47
E. Rezaei, H. Webber, S. Asseng, K. Boote, J. Durand, F. Ewert, P. Martre, D. MacCarthy. Climate change impacts on crop yields.
Springer Science and Business Media LLC, 2023.
CrossrefGoogle Scholar
48
P. Thanichanon, D. Schmidt-Vogt, M. Epprecht, A. Heinimann, U. Wiesmann. Balancing cash and food: The impacts of agrarian change on rural land use and wellbeing in Northern Laos.
Public Library of Science (PLoS), 2018.
CrossrefGoogle Scholar
Contents
Abstract
Introduction
Motivation
Data & Technical Background
Climatic Suitability Criteria
H. brasiliensis Cultivation Zones
Habitat Suitability Model for T. kok-saghyz
Natural Rubber in the Age of Climate Change
Modelling the Effects of Climate Change
Effects on Natural Rubber Production
Disease
Conclusion & Outlook
Materials and Methods
References
