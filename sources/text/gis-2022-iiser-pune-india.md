# Model
## Our Goal in Modelling
Since commercialisation of our project is central to helping farmers tackle waterlogging, optimisation of our solution is of paramount importance. To make sure all the resources are being used efficiently and nothing is getting wasted, we tried to understand how our bacterium interacts with the environment, and what parameters most strongly influence these dynamics.
Various mathematical modelling techniques were implemented to work out the parameters that can be controlled to maximise the efficacy of our solution, and to understand the dynamics of how different subsystems in our solution fit together.
Diffusion modelling along with kinetic modelling were employed to understand the timescales involved in ACC import and degradation, and metabolic modelling was employed to get an order-of-magnitude estimate on how much of our culture would be required to help one plant, and by extension, how much product would be required for a field. Satellite data was analysed in climate modelling to develop a semi-predictive model on waterlogging hotspots in the country to better understand where our solution can have the most positive impact. When combined, all the modules came together to help us understand the best way our project can be optimized and implemented.
We used mathematical modelling to tackle the following questions about our system:
- What are the timescales involved in the system?
- What parameters of the project can we tune to achieve the desired effects?
- How much bacteria is needed per plant to achieve our goal?
- Can our bacteria use the products from the degradation reaction as its own source of nutrition?
- Which parameters is our system sensitive to, and which is it robust against?
- What regions in the country suffer from waterlogging regularly, and are in need of such kind of a solution?
← Parts
## What we wanted to do
As you may have read in the Description page, when a plant is under abiotic stress, it has a physiological response of producing ethylene. This response has two stages; the first is a small ethylene peak which is beneficial for the plant and helps it survive the stress, and the second stage is where the plant overproduces ethylene and ends up causing more harm than good for itself. Since our bacterial construct breaks down ACC—the precursor of ethylene—it essentially acts as an ethylene inhibitor for the plant.
However, we do not want to completely stop the production of ACC in the plant! Since the goal is to better equip plants to survive such abiotic stresses, it would be counterproductive to constitutively overexpress ACC deaminase and stop all ethylene production, because that would rob the plant of even the beneficial ethylene peak. To really help the plant, we need to make sure that our system can:
- Only activate when the plant needs it to
- Have a time lag such that the beneficial peak is not affected too much
To figure out whether the first peak would be affected, we needed to estimate the time scale our system would take to produce some amount of the enzyme. In an ideal situation, the enzyme rate would be negligibly low in the vicinity of the first peak, but significant in the vicinity of the second one. We used diffusion and kinetic modelling to make our estimates.
## How we did it
During waterlogging, the plant overproduces ACC in its roots. Some of it is released from the roots into the environment, but if the rate of its production is very high, it begins to accumulate near the roots, and then slowly makes its way to the shoots. Once in the shoots, ACC gets converted to ethylene, which causes a whole host of problems for the plant.
We know from the literature that the presence of a bacterium expressing the acdS gene near the plant roots helps the plant deal with abiotic stresses by reducing the amount of ethylene produced.[1][2] If we assume that the ACC deaminase enzyme is not leaving the bacteria, we could conclude that ACC is getting broken down inside the bacterium, essentially making it an ACC sink.
But why would an external sink of ACC reduce the amount of ethylene produced in the plant?
One straightforward answer could be that ACC is transported to and from the root via passive diffusion.
We proposed that only if the transport of ACC mimics the mechanics of diffusion closely, can the existence of a sink outside the plant affect its accumulation inside it . For the rest of the model, we assumed this hypothesis to be true and proceeded. To make a sink strong enough to utilise all the exuded ACC coming from the roots, we decided to first model the diffusion of ACC through the plant roots, and into the bacteria.
### Diffusion model
#### Overview
The rhizosphere is the influence-sphere of the roots consisting of the narrow region of soil or substrate directly influenced by root secretions like proteins and sugars exudates (substances emitted through the roots of plants composed mainly of sugars, amino acids, organic acids, vitamins, and high molecular weight polymers, and act as a rich source of nutrients for the rhizospheric microbes) and associated microorganisms in the soil known as the root microbiome.[18] The plant root exudations and secretion influence the rhizosphere around the roots to inhibit harmful microbes and promote the growth of self and kin plants as well as the beneficial microbes in the rhizosphere environment. The development of the rhizosphere determines how roots, and therefore plants, interact with each other and other organisms; the rhizosphere can have a profound impact at the ecosystem level. Since the rhizosphere is a complex system involving different molecules and parameters limiting experimental outputs, a mathematical model helps us to explain this system in better detail [19].
Through diffusion modelling, we aimed to model the different parameters which influence the diffusion of ACC (1-Aminocyclopropane-1-carboxylic acid) from the roots—which acts as the source of the product into the soil environment—and from the soil into the bacteria—the sink for the substance at a macroscopic level. We decided to design a model that predicted the concentration profile of exudate for multiple parameters.
The Newman and Watson’s model of microbial abundance in the rhizosphere describes the model to predict the abundance of microorganisms in the rhizosphere in relation to distance from the root surface and time since the root started exuding substrate [20]. Experiments show that the high population density will develop near the root surfaces and fall off steeply with increasing distance from the center of the root. On root surfaces, bacteria usually occur as microcolonies near the root surfaces, and the cells present on the root surfaces form colonisation sites which are the regions of greater exudation.[18]
#### Concentration Profile
##### Equation
To describe the extended rhizosphere, the concentration of microbial biomass in the rhizosphere is assumed to be proportional to the substrate concentration in the region:
[IMG]
- x = Microbial biomass/unit volume
- γ = Constant
- C = Substrate concentration
The model represents the rhizosphere as a cylinder with boundary conditions.[20][21] Under the steady state of microbial growth, the substrate can be assumed to be utilised only for maintenance purposes and described in terms of radial diffusion and chemical reaction in a uniform medium as:
[IMG]
- C = Concentration of diffusing substance
- t = Time
- r = Radial Distance
- D = Diffusion coefficient of the diffusing substance
- k = Reaction constant for immobilisation of the diffusing substance (kC = mx; for m = Maintenance Coefficient such that for x = γC, kC = γmC)
By calculating the steady state solution (dC/dt = 0)
[IMG]
- Where C(r) = Concentration at a radial distance r
- A and B are constants
- I0 is a modified Bessel function of the first kind of order 0
- K0 is a modified Bessel function of the second kind of order 0
Here, A and B can be determined from the boundary conditions
- C = Cl when r = a = root radius
- C = 0 when r = b = cylindrical radius of the rhizosphere
[IMG]
where
[IMG]
##### Assumptions
For the model, the following assumptions were made [18][21]:
- The root structure is considered to be a straight and solitary cylinder
- The concentration of microbial biomass is proportional to the concentration of the substrate
- The substrate movement by mass flow is neglected (this is done considering the substrate concentration to be less than 5 µg/cm3 )
- The endogenous soil microbial activity is equal to 0
- The metabolism of diffusant is not considered
- Expects to provide quantitative results with the method of ratios were plotted for
The variable parameter in the equations above is the diffusion coefficient (D) which is specific to the molecules according to their size and chemical nature, as well as the media it is diffusing through. Due to the limitation in the availability of proper equipment, it was not possible to experimentally determine the diffusion coefficient of ACC in water. Thus, we decided to determine it in-silico with the help of Molecular Dynamics Simulation. We are indebted to Ashish Kumar—a PhD student in Dr. Arnab Mukerjee’s lab, IISER Pune—for helping us in this regard.
##### Diffusion Coefficient for ACC
The diffusion coefficient was determined using the mean square displacement (MSD) calculation over the MD simulation. A brief methodology of how it was calculated is as follows:
Mean Square Displacement (MSD) was determined using the software GROMACS and VMD. MD simulation of ACC were performed with the AMBER99SB [22] forcefield (Assisted Model Building with Energy Refinement is a family of force fields for molecular dynamics of biomolecules developed by Peter Kollman's group at the University of California, San Francisco), and the force fields were determined using ACPYPE [23] (AnteChamber PYthon Parser interfacE is a wrapper script around the ANTECHAMBER software that simplifies the generation of small molecule topologies and parameters for MD programmes like GROMACS, CHARMM, and CNS.)
The initial structural coordinates of ACC (.cif file converted to .PDB) were solvated by 903 three-point transferable intermolecular potential (TIP4P water model) water molecules in a 3.0 x 3.0 x 3.0 nm3 box [24]. Simulations were performed at 300 K and 1 bar pressure. The molecular dynamics equation of motions was integrated using 2 fs time steps using the leap-frog algorithm and dumped trajectory every 0.01 ps. The system was minimised with 5000 steps of the steepest descent minimisation. We run an MD simulation for 800 ps keeping the temperature constant. Production runs have been executed at the NPT ensemble using the Berendsen thermostat. This was done to produce 5 .gro file outputs.
After energy minimizing and equilibrating, MD was again performed under the same conditions to produce the simulation, and they were visualised using VMD. Then we used the gmx msd command to compute the MSD of the molecule from the initial position as it removed the fluctuated data points observed in the beginning and in the end and did the linear fit. For the 5 simulations that were performed, we record 5 values of MSD, which are described by:
[IMG]
To calculate the diffusion coefficient from MSD, the following formula is used:
[IMG]
We have plotted the mean-square displacement (MSD) versus the time (t) plot. The diffusion constant is calculated by least squares fitting a straight line (D*t + c) where D is the diffusion constant, t is time, and c is constant through the MSD(t). The diffusion coefficient is determined by linear regression of the MSD. Using GROMACS software, we computed the diffusion constant (D) of ACC in water.
[IMG]
Figure 1: MSD with respect to time
ACC diffusion constant in water = 0.89 (±0.58) *(10-5 cm2/s)
#### Results
The above equations for several varying physical parameters were plotted for distance from the root vs the relative substrate concentration graph using MATLAB R2021b [24]. By varying the following parameters, the influence of each can be estimated in the whole system:
##### Varying Maintenance Coefficient
For a straight single root of radius = 0.2 cm, the effect of varying the maintenance coefficient (γ) from 1 to 100 when the diffusion coefficient (D) of ACC in water = 0.89 * 10-5 cm2/s (from MD calculations) and a maintenance coefficient of 5.6 * 10-6 s-1 over a cylindrical rhizosphere radial distance (b) of 6 cm. Here, the graph represents how a wide range of microbial distribution patterns can affect the relative concentrations from the roots:
[IMG]
Figure 2: The relative substrate concentration at a given distance from the root decreases with an increase in γ.
##### Varying Root Radius
The concentration of the substrate is assumed to be produced from the center of the roots hence the radius of the roots will also affect the concentration gradient. Hence, as expected, the profile is much steeper as the root radius decreases. Here the graph represents that for a smaller radius, the percentage change in area is the greatest.
[IMG]
Figure 3:The relative substrate concentration at a given distance from the root increases with an increase in root radius
##### Varying Diffusion Coefficient
Soil is a porous media, and hence diffusion coefficient (D) of the molecule will be slower as compared to the diffusion in a water medium. The effective diffusion coefficient is described, which takes into account the water content and porosity of the soil and the sorption of the chemical on the soil solids. Thus, we know that different soils will have different diffusion coefficients for the same molecule. This graph represents the relative concentration profile for different orders of diffusion coefficients of the substrate over the radial distance. This shows that the steepness decreases as the diffusion coefficient (D) increases.
[IMG]
Figure 4: The relative substrate concentration at a given distance from the root increases with an increase in the diffusion constant
#### Calculating Flux
The description of diffusion of molecules involves the mathematical equations derived by Adolf Fick called Fick’s Laws of Diffusion. According to Fick’s First Law, the movement of particles (diffusion flux) from high to low concentration is directly proportional to the particle’s concentration gradient:
- J = Diffusion flux, it measures the amount of substance that will flow through a unit area during a unit time interval
- D = Diffusion coefficient
- C(r) = Concentration of the substance
- r = Radial position
Where:
[IMG]
- C(r) = Concentration at a radial distance r
- A and B are constants
- I1 is a modified Bessel function of the first kind of order 1
- K1 is a modified Bessel function of the second kind of order 1
Flux here is the rate of exudation by the root and, in relative terms, can be expressed as:
[IMG]
Changing the constants A and B as given above, this equation becomes:
[IMG]
This graph represents the effect of varying root radius on relative flux at the root surface. The relative flux per unit root surface area declines with increasing the root radius.
[IMG]
Figure 5: Relative flux reduces as root radius increases
The microbes around the roots in the rhizosphere are more concentrated near the surface of the roots due to a rich source of nutrient availability, and the concentration of bacteria reduces with the increase in radial distance.
Considering the parameters as mentioned in the graph, the relative flux over the distance of 0.2 cm is:
= 4.3*10-6 µg/cm2/sec
The absolute value of the flux from the roots would then be the relative flux multiplied by the concentration of ACC at the surface of the root Cl. In a steady state system, this would be a constant. To find the value of Cl, we reached out to the UBC iGEM team, who had the resources to perform the experiment for us. We have detailed our interaction with the UBC team in the Partnership page.
Unfortunately due to time and resource constraints, we could not get the value of Cl. For the rest of the model, we assumed the flux of ACC into the bacteria is 0.01 µM s-1.
The value of the flux of the exudated ACC was essential for the Metabolic Modelling as the rate of substrate concentration per unit area and unit time tells us about how much of ACC is coming out of the root and reaching a bacteria present at a certain distance to understand the influx of ACC into the bacteria and understand the metabolic load of the intake.
#### Conclusion
The rhizosphere is a complex environment with many known and unknown variables that guide the chemical concentration profiles in the system. Hence, it is difficult to predict this in-silico, but for a specific application, reasonable inferences can be determined. Through this model, we tried to show how some external factors can affect the exudations of the roots, in this case, ACC, which are essential for the microbes present in the immediate surrounding of the rhizosphere for their growth.
The model helped us in predicting and showcasing the concentration profile of the substrate and how it changes by varying the microbial concentration pattern, the radius of the root it is being excluded from, and the diffusion coefficients (porosity of the soil medium). We also tried to determine the flux to show the concentration change per unit area per unit time of ACC from the roots. This was used to find the concentrations of ACC that reach the bacteria so that they can take up to carry out the enzymatic reactions as described in the Metabolic Modelling.
#### Future Work
Throughout our iGEM cycle we were in a constant exchange of work and resources with the UBC Vancouver team. Since this model assumed everything in-silico, it is important to test it out with experimental data for validation. The UBC team project aligned with our project because they were also dealing with the same molecule ACC. As they were working with the plants, the team helped us in creating an experimental plan with design and protocols with conditions and treatments. They inculcated a detailed plan for how ACC would be measured with the co-culture of our modified Azospirillum to observe the effect it will have on the levels of ACC in the roots. Due to laboratory constraints, they were unable to carry out the experiment successfully; but it is something we hope to do in the future to strengthen the model.
To read the experimental plan, click IISER PunexUBC Wetlab Partnership
### Kinetic model
With some clue about how much ACC is being produced by the plant for some root area, we can now begin to probe the time-dependence of the biochemical reactions that take place in our system using a set of Ordinary Differential Equations (ODEs). The first step to build a kinetic model, is to build this system of ODEs that can mathematically describe the processes that are occurr in the environment under consideration.
To do this, we made a box-model diagram for our system that included as many processes that we wanted to model. This diagram helped us keep track of how the processes are interlinked and guided us to form the ODEs.
[IMG]
Figure 6: box model
##### Deriving the ODEs
With the help of the box model, we could see the following flow in our system:
- The inducer will initiate the transcription of mRNA molecules for the ACC deaminase enzyme.
- The mRNA will bind the to the ribosomes, and transcribe the enzyme.
- The enzyme would accumulate in the cytosol and degrade with some half life.
- ACC would diffuse into the cytoplasm and come into contact with the enzyme.
- The substrate-enzyme reaction would produce two produce, ammonium and 2-oxobutanoate.
- We hypothesized that the bacteria would utilize the products for its own growth, thus increasing the biomass of the available cells.
We then created a detailed pathway of reactions and rates, which then made the ODEs stand out.
[IMG]
Figure 7: Chemical pathway with the promoter
Here, kd = koff/kon.
From this point on, we followed the steps discussed in the iGEM engineering webinars conducted by Dr. Alejandro Vignoni [3], and got our ODEs from very basic mass action law and conservation of mass.
The ACC degradation reaction for which we modelled the kinetics is the following:
[IMG]
The system of ordinary differential equations derived from our relations:
[IMG]
Where f = [Transcription factor], e = [ACC deaminase], s = [ACC substrate], c = [Enzyme-Substrate complex], p1 = [NH3] and p2 = [2-Oxobutanoate]
Deriving the ODEs left us with a lot of parameters, and for a realistic prediction of the time-scale of our system, it was crucial that we estimate the values of these parameters to the best representation of reality as possible.
Since our chassis was Azospirillum, very little data was available in the literature for such kinds of parameters, and so at times we had to take values from E. coli data, and at times do fermi calculations to get an order-of-magnitude estimate on some parameter values. However, as we will see in the optimisation section of the page, we only have to control a subset of these parameters to achieve the correct time lag and activity of the enzyme, since the time scale of the solution would depend only on some of these parameters.
The parameters and their sources are tabulated below.
[IMG]
### Results of Time Scale Estimation
Once the parameters and the ODEs were set, we shifted over to MATLAB, where the ODEs were coded for and solved.
We chose the ode15s() function to solve our system of ODEs to reduce the time it would take for the programme to solve the ODEs. This enabled us to perform numerous trials and plot multiple graphs within a short span of time.
The heavily commented MATLAB code used to solve the system is available in the appendix available in references tab of the models page.
The solutions for our system of ODEs was as follows:
[IMG]
Figure 8: Dynamics of metabolites in the system
It can be seen that the time scale of degradation of approximately 30 µM of ACC is about 30 seconds for a single bacteria, given the values of the parameters estimated. The value of kp we used was arbitrarily chosen because we did not find a suitable value in the existing literature, and so, this prediction acts as an outline to find a more realistic time scale given the value of kp.
Now, depending on the amount of ACC that is produced by the plant, we can scale the time factors by the relation:
[IMG]
where N is the number of bacteria in the vicinity of the plant.
The value of the amount of ACC produced and released by plant roots was not easily available in literature, since most of the experiments that measure ACC concentrations use crushed roots. Since we are only interested in the amount of ACC that is released by the roots via diffusion, the values in the literature would be overestimated.
The data from the experiments by the UBC team would help us estimate the released ACC by the roots of wheat plants. The procedure for the experiments is detailed in the Partnership page, and we aim to be able to finish these experiments in the near future.
The number of bacteria in the rhizosphere available to degrade the ACC can be found from our metabolic modelling section under the optimisation tab.
## What we wanted to do
From the beginning of the modelling exercise, the goal was to be able to optimise our solution such that it provides the most efficient and cost-effective biofertiliser to the farmers in need. We focussed on answering the following questions:
- How can we control the time scale of the system so that we can specifically target only the second ethylene peak?
- Approximately how much Azosprillum would we need per plant to be able to match the ACC release and degradation rates?
## How we did it
### Sensitivity Analysis - How can we control the time scale?
With the advancement of synthetic biology, scientists now have the ability to be able to tune specific parameters in their chassis to their needs, which then help them achieve specific target such as maximising enzyme production, or minimising the time taken for some reaction to occur. However, more often than not, there are a lot of parameters involved in the system. In such a situation, it is important to be able to find out which parameters the system is most sensitive to. This would then enable them to streamline their work to focus only on sensitive parameters.
In our model, we would like to control the total amount of enzyme produced, and also the time taken for the substrate to be broken down. By tuning both of these values, we will be able to make sure that the first ethylene peak is not affected, without giving up on the efficiency of the system with a very low enzyme concentration.
To find out which parameters the model is most sensitive to, we changed the values of the parameters—by 5% and then 10% (both up and down)—in a for loop and calculated the percentage change in the time-scale or total enzyme concentration’s representative value.
The ‘representative value’ for a certain dimension (ie time scale or total enzyme concentration) is a number that depends on that dimension linearly.
Once we change one parameter in our ODEs by some percentage and use the ode15s() function to numerically solve it, we get a list of numerical values which correspond to a certain value of time (see x1, t1 in the Kinetic Modelling MATLAB code). This list is then plotted against its corresponding time values to get the plots in figure 8.
You might notice, that this solution is not analytic, and so, something like a value for t{1/2} is not something we can extract from the equations of the curve. In such a situation, we need a number that can replace t{1/2} , and can be extracted from our solution set, and that would become the ‘representative number’ for the temporal dimension.
##### Representative number for the time scale:
In our solutions, we quickly realised that finding the value of time at which the substrate concentration is half its initial was not feasible. As a replacement then, we decided to take the time at which the concentration of the enzyme-substrate complex (c) reaches a maxima as our representative value for time.
The representative value tcm was calculated for each parameter after each change: ± 5% and ± 10% and the percentage change of this value was plotted against the percentage change in the parameter.
##### Representative number for total enzyme concentration:
In the case of the total enzyme concentration, we took the value of the ACC deaminase concentration (e) at tf where tf is the maximum time that our ODEs are solved till. Once again, the percentage change in this representative value was plotted against the percentage change in the parameter.
The flowchart details the algorithm used to find the sensitivity of a parameter in the case of increasing them by 10%. The same was repeated for increasing them by 5% and reducing them by 10% and 5%.
[IMG]
Figure 9
The results are illustrated in the following plot.
[IMG]
Figure 10.a Sensitivity of Time Scale to various parameters
[IMG]
Figure 10.b Sensitivity of Enzyme Concentration to various parameters
Figure 10.a: Sensitivity analysis for time scale. Here the height of the blue bars represent the percentage change (positive or negative) of the representative value for time for a 5% increase or decrease in the corresponding parameter. A taller blue bar means that there is a larger change in the representative value for a 5% change in the parameter. Similarly, the height of the dark green bar represents the percentage change in representative value for a 10% change in the parameter.
Figur 10.b: Sensitivity analysis for enzyme concentration. Here the height of the magenta bars represent the percentage change (positive or negative) of the representative value for time for a 5% increase or decrease in the corresponding parameter. A taller magenta bar means that there is a larger change in the representative value for a 5% change in the parameter. Similarly, the height of the purple bar represents the percentage change in representative value for a 10% change in the parameter.
The goal of this plot is to show, qualitatively, which parameters most affect (a) time, and (b) total enzyme concentration.
As can be seen from the plot, the time scale is sensitive to:
[IMG]
Similarly, we can see qualitatively that the total enzyme concentration is sensitive to:
[IMG]
To get a more quantitative measure of the sensitivity of a representative value to a parameter, we can divide the percentage change in the representative value by the percentage change in the parameter to get a sensitivity coefficient. Doing this for the values of the 10% changes, we get the following table.
Sensitivity coefficient for time scale for increase in parameter values by 10%:
[IMG]
Sensitivity coefficient for enzyme concentration for increase in parameter values by 10%:
[IMG]
From which we can see that kp has the highest sensitivity coefficient for time scale, and kd, k1 and k4 have the highest sensitivity coefficient for enzyme concentration. Making these the most important parameters to control to be able to steer the respective dimensions the way that would be most beneficial for farmers, and help reduce the operational cost of the process.
### Metabolic Flux Analysis—Amount of Azospirillum per Plant
To find out the amount of Azospirillum needed in the plant rhizosphere to match the degradation rate of ACC to its influx, we used metabolic modelling and Flux Balance Analysis.
Flux Balance Analysis (FBA) is a widely used technique to model cells at the metabolome level. It uses reactions that are available in the cell to predict the production and consumption rates of different metabolites in the cell along with the cell’s own biomass yield in a steady state. This is done by setting constraints on the rates of different metabolic reactions in the cell and using linear programming to find the distribution of fluxes through the reactions while maximising the flux through an objective reaction.
A short overview of FBA and the mathematical representation of metabolism can be found in “What is Flux Balance Analysis” Orth et al. 2010 [17]:
[IMG]
Figure 11
Here, the term ‘flux’ can be thought of as a measure of the amount of resources (for example, carbon content) flowing through a particular reaction. It is reported in units of (mmol/gDW)/Hr (millimoles per gram dry weight of bacteria, every hour). For example, a flux of 0.8 mmol /gDW/Hr through the isoleucine synthesis reaction is interpreted as: for every one gram of dry weight of the bacteria, 0.8 millimoles of isoleucine is being produced every hour.
Often in experiments, the yield of a certain metabolite is reported instead of the flux since it is easier to measure the yield of a certain metabolite. This is nothing but the flux through the reaction of interest divided by the rate determining input flux in the bacteria. For example, if the experiment measures the yield of isoleucine, (which, say, depends on how much glucose is being fed into the system) it would be the flux of Isoleucine divided by the input flux of Glucose.
To perform metabolic modelling, we needed a list of all the reactions that occur in the cell along with their constraints for our chassis Azospirillum brasilense. Such information is contained in the Genome Scale Model (GSM) of the bacterium. We searched extensively for an Azospirillum brasilense GSM in the literature, but could not find any. After taking some advice from Dr. Karthik Raman, we decided that if there are no GSMs available in the literature for Azospirillum, we would try to make one ourselves, and then later test it against an established GSM of a closely related bacterium to check the validity of our own predictions.
We faced a lot of issues with the reconstruction of the Azospirillum GSM. After numerous design, build, test and learn cycles (described in the Engineering page), we realized that it would not be possible for us to make a GSM from scratch given the amount of literature available for our chassis. Since most of the reaction constraints come from measurements and experiments, we would have had no real way to put realistic constraints into our models.
Given the constraints of time in the iGEM cycle, we were advised by our advisor Vijendra to switch to a GSM that is closely related to Azospirillum, but one that has been reconstructed completely, curated, and published in the literature. Based on the availability of GSMs, we chose the Pseudomonas putida GSM iJN1463 [27][28] to go ahead with the simulations. We chose this model because in literature, Dr. Glick [1] had worked on a similar problem as us and had used Pseudomonas putida as their chassis. Combined with the fact that Pseudomonas putida is a plant growth promoting bacterium that lives freely in the rhizosphere like Azospirillum, we believe that this model was the best choice as an order of magnitude approximation to the Azospirillum system.
Since Pseudomonas and Azospirillum are not even the same genus, the results that we get from the metabolic model are only approximations, and cannot be treated as accurate. Even so, we can gain important insight on the metabolic dependencies of a bacteria that breaks down ACC to its own growth rates and other metabolites, and so, it is still an indispensable exercise to perform FBA with the Pseudomonas GSM.
#### Method
The GSM was loaded onto MATLAB using the Cobra Toolbox [15], and written onto an spreadsheet which would made it easier to navigate within the model structure and search for reactions and metabolites.
##### Setting up the model
To make the model relevant to our system, we needed to add the ACC degradation reaction into the GSM and check to see if the reactions responsible for utilisation of the products are in the model already. Using the enzyme information on BRENDA [29] and reaction pathways from KEGG [30], we constructed a proposal pathway for the metabolite of interest ACC:
[IMG]
Figure 12: Proposed pathway of ACC metabolism
We then manually searched for similar reactions in the GSM to check whether this pathway is feasible in Pseudomonas or not, and it was found that the product 2-Oxobutanoate gets used up in the L-Isoleucine pathway. Hence, we hypothesised that the bacteria may be able to use ACC as a carbon source if it is able to degrade the ACC.
Since ACC was not a metabolite in the GSM, we added the extracellular, periplasmic, and cytosolic ACC metabolites into it, along with the relevant exchange reactions that would enable the model to “take up” ACC from the surrounding.
We then added constraints to our reactions. Since the exchange of ACC had to be into the model only, we set the constraints such that the exchange of ACC from the extracellular environment to the intracellular environment is irreversible. We also set a minimum threshold of -10 mmol per gDW per hour to the maximum of 100 mmol per gDW per hour, since in the literature, ACC deaminase activity was reported to be reversible.
##### Simulations
We ran multiple FBA simulations to see the distribution of fluxes in the system. Most of the time, the objective function that we wanted to maximise was the biomass reaction. The biomass reaction is a reaction involving various amino acids, ATP, ammonia, water, and other important metabolites, in different proportions, which when added together gives the mass distribution in mmol of 1 gram DW of biomass. The flux through this reaction is often treated as the ‘growth rate’ of the bacteria, since it gives the amount of biomass that 1 gram DW of bacteria can produce every hour.
We made sure that the model was self consistent by first setting all the carbon sources to 0, and checking if we get any flux through the biomass reaction. As expected, the output was 0. We also ran a sanity check by looking at the flux through the biomass reaction by allowing some flux to flow through the glucose import reaction. We got a positive growth rate, which meant that the system was consistent.
To test our hypothesis that ACC can be used as a carbon source, we ran FBA with all carbon source import fluxes set to 0 except that of the ACC import reaction. The output was:
Flux through biomass = 0.1659 mmol /gDW-Hr
This meant that we had some positive growth rates in the system with only ACC being a carbon source. This proved our initial hypothesis to be true, and meant that the plant and the bacterium could likely set up a stronger symbiotic relationship which would motivate the bacteria to stay near the roots.
We then tried to find what is the flux through the ACC degradation reaction, if we set the biomass reaction as the objective function
Flux through ACCdeg reaction = 57.2126 mmol /gDW-Hr if ACC is the only Carbon source
Flux through ACCdeg reaction = 64.2115 mmol /gDW-Hr with free Carbon uptake
In real life, the bacteria will never be in an environment where ACC is the only carbon source, since many carbon source metabolites are exuded from the roots of plants itself [16]. Hence, for our purposes, we can take the second value to be the more realistic number.
Here, we can see that the model predicts that about 64.2 mmol of ACC will be degraded every hour for every gram dry weight of bacteria present in the rhizosphere. If we assume that the amount of ACC being produce by a single plant is x, then the amount of bacteria that will be needed per plant would be at least
gDW bacteria per plant = x/62.2
The robustness of the flux through the biomass reaction can be seen if we plot the flux through the import reaction of ACC against the flux through the biomass reaction:
[IMG]
Figure 13: EX-acc-e-r is the name of the import reaction for ACC, and the objective is the biomass reaction.
Since it is the import flux, the values are negative. The graph shows that the biomass flux increases proportionally to the increased import of ACC into the system, but reaches a plateau at around 64 mmol/gDW/Hr. This is also what we have from the FBA simulation previously.
However, it must be noted that our bacteria would be under microaerobic conditions during waterlogging, which means that it would not have an unbounded supply of oxygen. This would affect the maximum flux through the biomass, and thus also the maximum flux that can flow through the ACC degradation reaction.
To understand how the biomass flux changes with availability of oxygen, we plotted the biomass flux against the import flux of oxygen:
[IMG]
Figure 14: EC-o2-e is the name of the import reaction and the biomass reaction is the objective
Since it is the import flux, the values are negative. The graph shows that the biomass flux increases proportionally to the increased import of oxygen into the system.
In order to represent the fluxes through ACC import, oxygen import, and biomass together, we prepared a phenotypic phase plane, which shows the three fluxes together:
[IMG]
Figure 15
Additionally, we also wanted to see the dependence of import flux of glucose and ACC on the biomass flux:
[IMG]
Figure 16
From these plots, we can see that we get a plane of possible solutions, and depending on the environment, the biomass flux would vary.
As an exercise, we calculated the maximum allowed flux through the ACC degradation reaction when the biomass is the objective in micro-aerobic conditions—low oxygen content as compared to the 22% in the atmosphere.
We ran FBA with the import flux of oxygen set to -5 mmol/gDW/Hr, since the physiological uptake rate of oxygen in the case of E. coli is about -20 mmol/gDW/Hr. With the objective still the biomass, the max flux through ACC degradation:
Flux through ACC degradation = 5.47 mmol/gDW/Hr
Thus making the optimal amount of bacteria per plant:
[IMG]
Where x is the amount of ACC produced by each plant in units of mmol per hour.
### Climate Modelling for Waterlogging hotspots in India:
When we started our project and were speaking to people to know about their views on waterlogging and its extent, we were extremely surprised to know that most people were either unaware of the term or had a misconception about waterlogging being the same as flooding. Not only that but we also realised that a majority of the population was unaware of that such a problem even existed.
When we started with our entrepreneurial journey with our company, Hydrazome (check the Entrepreneurship Page!), we decided it would be an interesting idea to first find the waterlogging hotspots in the country. This would help us prioritise and focus on the areas which would be greatly benefitted by our solution.
Our plan was to generate full India maps where the waterlogged areas have been highlighted. Initially, we did an image segmentation and pixel masking of a specific area [25]. However, the results were not good, and we shifted our approach to generating maps with Normalised Satellite Indexes [26].
[IMG]
Figure 17: Image Segmentation by k-means clustering
[IMG]
Figure 18: Pixel Masking
Normalised Satellite Indexes ratios between different bands. Bands are the light reflected in certain regions of the spectrum in the satellite.
We worked with 4 indexes -
- NDVI (Normalised Difference Vegetation Index): it is the measure of the greenness of an area.
- NDMI (Normalised Difference Moisture Index): it measures the vegetation water content.
- NDWI (Normalized Difference Water Index): it highlights the amount of water in water bodies.
- MNDWI (Modified Normalized Difference Water Index): it enhances the water bodies while suppressing the land noise in the NDWI.
Formula of the indexes:
[IMG]
Sentinal 2A and Landsat 8 band numbers:
[IMG]
Our first step was to find the thresholds for every index so that we knew the exact conditions above/below which soils are waterlogged. Then, with the help of SNAP, QGIS, and Google Earth Engine, we imported LANDSAT 8 and Sentinel 2A data for India and a specific area in Punjab, respectively.
Our next step was to work on the Sentinel 2A data on SNAP And QGIS. We generated the NDVI, NDMI, NDWI and MNDWI maps for the area in Punjab and overlay the NDVI map with NDMI, NDWI, and MNDWI to get 3 different maps, each with 2 layers. Then we used the thresholds to mask those areas which were below/ above the threshold to get just the waterlogged areas.
[IMG]
Figure 19: NDVI + MNDWI
[IMG]
Figure 20: NDVI + NDMI
[IMG]
Figure 21: NDVI + NDWI
The 3 figures above were generated on SNAP and QGIS softwares.
Our next step was to generate full-country maps with the same algorithm. We imported LANDSAT 8 Tier 1 raw 18 data on Google Earth Engine. Then we used Java Script to import and filter the bounds of the image.
Generating 3 maps:
1. NDVI+NDMI map:
After importing and filtering our data, we coded for the NDVI, NDMI, and composite layers. Then we generated NDVI and NDMI masked layers using the thresholds.
[IMG]
Figure 22: NDVI + NDMI Map
The thresholds are:
NDMI - >0.4
NDVI - <0.20
The aquamarine-coloured parts show the NDMI map.
The dark blue parts are the NDMI-masked areas which include both the water bodies as well as waterlogged soils.
The dark green parts are the NDVI masking layer where anything below 0.20 NDVI has been masked. Basically, this masking was done to exclude the water bodies from the NDMI-masked areas.
Conclusion The dark blue areas cover Punjab, Arunachal Pradesh, Assam, West Bengal and parts of Kerela and the Malabar Coast; these areas are waterlogging hotspots according to the map.
2. NDVI+NDWI map:
Following a similar algorithm as the NDVI+NDMI map, we generated the following map:
[IMG]
Figure 23: NDVI + NDWI map
The thresholds are: NDVI - <0.65
NDWI - <0.50
The dark blue areas on the map are the waterlogging hotspots.
The green layer on the map is the NDVI-masked layer which excludes the water bodies and the non-waterlogged areas.
According to the map, parts of Punjab, Himachal Pradesh, Uttarakhand, Arunachal Pradesh, Assam, Tripura, Mizoram, Manipur, Kerala, West Bengal and Andhra Pradesh are waterlogged.
3. NDVI+MNDWI map:
The last map that we generated using the same algorithm as before is the NDVI+MNDWI map.
[IMG]
Figure 24: NDVI + MNDWI Map
The thresholds are:
NDVI - <0.65
MNDWI - <0.45
The white areas are the waterlogged hotspots, according to this map. The green areas are the NDVI-masked layer which excludes the waterbodies and the non-waterlogged areas from the MNDWI-masked layer.
### Results of Optimisation
From our modelling modules, we have developed a mathematical structure to give us the ideal time-scale for the reactions, along with the ideal amount of bacteria in a field, which will help greatly in the implementation of our product for farmers, by giving them a rough estimate on how much of the fertilizer would be needed in their fields.
We have found that the time scale has the highest sensitivity to kp, and the total enzyme concentration has the highest sensitivity to kd, k1 and k4. Controlling these values would give the best result since we would be able to target only the second ethylene peak.
We also showed the bacteria has a metabolic advantage to break down ACC and consume the products for its own growth, and thus strengthening the point that the plant and the bacteria have a symbiotic relationship.
From climate modelling, we found the places in the country where our biofertiliser could be useful. This information would not only help warn farmers in regions of high chance of waterlogging, but also help us set up a distribution network to make sure that the biofertiliser reaches the regions in the country it is most required in.
And with that, we attempted to answer all the questions that we had set out to answer in the introduction of the modelling page!
### Appendix
In the appendix, we include heavily commented MATLAB code that we used for our computations. We tried to make the comments comprehensive so that anyone who reads through the pdf files can get a basic grasp on the algorithms we used. It may be helpful for future iGEM teams to use this code to save time for their computations.
#### Oridinary Differential Equation Function code
#### Diffusion Modelling code
#### Kinetic Modelling code
#### Sensitivity Analysis code
#### Metabolic Modelling code
#### Climate Modelling code
### References
[1] Glick, Bernard & Penrose, Donna & Li, Jiping. (1998). A Model For the Lowering of Plant Ethylene Concentrations by Plant Growth-promoting Bacteria. Journal of theoretical biology. 190. 63-8. 10.1006/jtbi.1997.0532
[2] Holguin G, Glick BR. Transformation of Azospirillum brasilense Cd with an ACC deaminase gene from enterobacter cloacae UW4 fused to the Tet r gene promoter improves its fitness and plant growth promoting ability. Microb Ecol. 2003 Jul;46(1):122-33. doi: 10.1007/s00248-002-1036-x.
[3] Alejandro Vignoni (2021). Webinar 2, Webinar 5. https://2021.igem.org/Engineering/Webinars
[4] http://book.bionumbers.org/what-are-the-copy-numbers-of-transcription-factors/
[5] Kd for binding of Elongation Factor-G-GTP to vacant ribosome, Bionumbers BNID103826
[6] Transcription and translation rates in E.coli, Bionumbers BNID108487
[7] Average translation rate, Bionumbers BNID111689
[8] Nascimento, F.; Rossi, M.; Soares, C.; McConkey, B.; Glick, B. New insights into 1-aminocyclopropane-1-carboxylate (ACC) deaminase phylogeny, evolution and ecological significance (2014), PLoS ONE, 9, e99168.
[9] Hyone-Myong Eun, in Enzymology Primer for Recombinant DNA Technology, 1996 textbook
[10] Anecdotal from PhD mentor
[11] Taniguchi Y, Choi PJ, Li GW, Chen H, Babu M, Hearn J, Emili A, Xie XS. Quantifying E. coli proteome and transcriptome with single-molecule sensitivity in single cells. Science. 2010
[12] Average protein half life, Bionumbers BNID111930
[13] Walsh, C.T.; Pascal, R.A.; Johnston, M.; Raines, R.; Dikshit, D.; Krantz, A.; Honma, M. Mechanistic studies on the pyridoxal phosphate enzyme 1-aminocyclopropane-1-carboxylate deaminase from Pseudomonas sp. (1981), Biochemistry, 20, 7509-7519.
[14] MATLAB_R2022a, Mathworks. Inc
[15] Laurent Heirendt, Sylvain Arreckx, Thomas Pfau, Sebastian N. Mendoza, Anne Richelle, Almut Heinken, Hulda S. Haraldsdottir, Jacek Wachowiak, Sarah M. Keating, Vanja Vlasov, Stefania Magnusdottir, Chiam Yu Ng, German Preciat, Alise Zagare, Siu H.J. Chan, Maike K. Aurich, Catherine M. Clancy, Jennifer Modamio, John T. Sauls, Alberto Noronha, Aarash Bordbar, Benjamin Cousins, Diana C. El Assal, Luis V. Valcarcel, Inigo Apaolaza, Susan Ghaderi, Masoud Ahookhosh, Marouen Ben Guebila, Andrejs Kostromins, Nicolas Sompairac, Hoai M. Le, Ding Ma, Yuekai Sun, Lin Wang, James T. Yurkovich, Miguel A.P. Oliveira, Phan T. Vuong, Lemmer P. El Assal, Inna Kuperstein, Andrei Zinovyev, H. Scott Hinton, William A. Bryant, Francisco J. Aragon Artacho, Francisco J. Planes, Egils Stalidzans, Alejandro Maass, Santosh Vempala, Michael Hucka, Michael A. Saunders, Costas D. Maranas, Nathan E. Lewis, Thomas Sauter, Bernhard Ø. Palsson, Ines Thiele, Ronan M.T. Fleming, Creation and analysis of biochemical constraint-based models: the COBRA Toolbox v3.0, Nature Protocols, volume 14, pages 639–702, 2019 doi.org/10.1038/s41596-018-0098-2.
[16] Pétriacq P, Williams A, Cotton A, McFarlane AE, Rolfe SA, Ton J. Metabolite profiling of non-sterile rhizosphere soil. Plant J. 2017 Oct;92(1):147-162. doi: 10.1111/tpj.13639. Epub 2017 Aug 31. PMID: 28742258; PMCID: PMC5639361.
[17] Orth, J., Thiele, I. & Palsson, B. What is flux balance analysis?. Nat Biotechnol 28, 245–248 (2010). https://doi.org/10.1038/nbt.1614
[18] Microbial Health of the Rhizosphere,https://web.archive.org/web/20070312061312/http://uwstudentweb.uwyo.edu/T/Twhite/
[19]Kuppe, C.W., Schnepf, A., von Lieres, E. et al. Rhizosphere models: their concepts and application to plant-soil ecosystems. Plant Soil 474, 17–55 (2022). https://doi.org/10.1007/s11104-021-05201-7
[20]Newman, E.I., Watson, A. Microbial abundance in the rhizosphere: A computer model. Plant Soil 48, 17–56 (1977). https://doi.org/10.1007/BF00015157
[21]Xavier Raynaud, Soil properties are key determinants for the development of exudate gradients in a rhizosphere simulation model, Soil Biology and Biochemistry, Volume 42, Issue 2, 2010, Pages 210-219, ISSN 0038-0717, https://doi.org/10.1016/j.soilbio.2009.10.019.
[22]AMBER: Assisted Model Building with Energy Refinement (AMBER) https://en.wikipedia.org/wiki/AMBER
[23]Sousa da Silva, A.W., Vranken, W.F. ACPYPE - AnteChamber PYthon Parser interfacE. BMC Res Notes 5, 367 (2012). https://doi.org/10.1186/1756-0500-5-367
[24]AMBER: Collins MD, Hummer G, Quillin ML, Matthews BW, Gruner SM. Cooperative water filling of a nonpolar protein cavity observed by high-pressure crystallography and simulation. Proc Natl Acad Sci U S A. 2005 Nov 15;102(46):16668-71. doi: 10.1073/pnas.0508224102
[25]Kaushik, S., Dhote, P.R., Thakur, P.K. et al. An integrated approach for identification of waterlogged areas using RS and GIS technique and groundwater modelling. Sustain. Water Resour. Manag. 5, 1887–1901 (2019). https://doi.org/10.1007/s40899-019-00342-1
[26]Arnous, Mohamed O., and David R. Green. “Monitoring and Assessing Waterlogged and Salt-Affected Areas in the Eastern Nile Delta Region, Egypt, Using Remotely Sensed Multi-Temporal Data and GIS.” Journal of Coastal Conservation 19, no. 3 (2015): 369–91. http://www.jstor.org/stable/24760826
[27]Lewis, Leah & Perisin, Matthew & Tobias, Alex. (2020). Metabolic modeling of Pseudomonas putida to understand and improve the breakdown of plastic waste. 10.13140/RG.2.2.25853.28643.
[28]Model iJN1463, bigg models database http://bigg.ucsd.edu/models/iJN1463
[29]BRENDA database https://www.brenda-enzymes.org
[30]KEGG database https://www.kegg.jp
[31] NDVI and NDMI vegetation indices: instructions for use
[32] Sentinel 2 Bands and Combinations
[33] https://www.lifeingis.com/computation-of-mndwi-in-google-earth-engine-using-sentinel-2/
Human Practices →
[IMG]
Access Wiki Tools View Source Code
[IMG]
