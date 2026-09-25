## Stellar Kinematics Data Products (DR3StelKin)
https://docs.datacentral.org.au/sami/data-release-3/stellar-kinematics-data-products/<br>
For safe usage, we recommend only using data which meet the following criteria: 
- (SIG_ERR < SIG * 0.1 + 25)
- SN > 20 & SIG > 70 
- VEL_ERR < 30 km s−1

4.2.2 Velocity Dispersion values

We provide the stellar velocity dispersion derived from the aperture spectra as described in Section 3.7. Here, we have applied the additional selection criteria: S/N > 5 & SIG > 35 km s−1 & (SIG_ERR < SIG * 0.025 + 10). We do not provide additional safe usage criteria as it will depend on the specific science case.<br>
<br>
The catalogue parameters are:<br>
<br>
SIGMA_RE | Velocity dispersion from Sersic Re aperture spectra<br>
SIGMA_RE_ERR | 1-sigma error on sigma_re<br>
<br>
SIGMA_RE_MGE | Velocity dispersion from MGE Re aperture spectra<br>
SIGMA_RE_MGE_ERR | 1-sigma error on sigma_re<br>
<br>
SIGMA_3KPC | Velocity dispersion from 3kpc aperture spectra<br>
SIGMA_3KPC_ERR | 1-sigma error on sigma_3kpc<br>
SIGMA_1_4_ARCSEC | Velocity dispersion from 1.4 arcsec aperture spectra<br>
SIGMA_1_4_ARCSEC_ERR | 1-sigma error on sigma_1_4_arcsec<br>
SIGMA_2_ARCSEC | Velocity dispersion from 2 arcsec aperture spectra<br>
SIGMA_2_ARCSEC_ERR | 1-sigma error on sigma_2_arcsec<br>
SIGMA_3_ARCSEC | Velocity dispersion from 3 arcsec aperture spectra<br>
SIGMA_3_ARCSEC_ERR | 1-sigma error on sigma_3_arcsec<br>
SIGMA_4_ARCSEC | Velocity dispersion from 4 arcsec aperture spectra<br>
SIGMA_4_ARCSEC_ERR | 1-sigma error on sigma_4_arcsec<br>


## Input, photometric and observational catalogues (InputCatGAMADR3, DR3InputCatClusters, Dr3VisualMorphology)
https://docs.datacentral.org.au/sami/data-release-3/input-and-photometric-catalogues/<br>
A parameter ISBEST indicates in the case of repeats which data is considered the best, based on seeing and S/N. Other flags indicate missing data, or value added products, and other calibration of measurement problems or warnings.<br>
The BAD_CLASS parameter flags various problems with the input data, and the definition of these different classes are given in the table below and also in Bryant et al. (2015). Objects with BAD_CLASS = 0, 5 or 8 are potential targets to be observed.