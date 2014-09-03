"""
.. module:: initialize_institute.py
   :platform: Unix
   :synopsis: Initializes collection of supported institutes.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
# -*- coding: iso-8859-15 -*-

# Module imports.
from .. import (
    models, 
    session
    )



def execute():
    """Initializes collection of supported institutes.

    """
    # BADC.
    i = models.Institute()
    i.Name = "--"
    i.LongName = "Placeholder for scenario when an institute is undefined"
    i.CountryCode = "--"
    session.insert(i)

    # BADC.
    i = models.Institute()
    i.Name = "BADC"
    i.LongName = "British Atmospheric Data Centre"
    i.CountryCode = "UK"
    i.URL = "http://badc.nerc.ac.uk/home/index.html"
    session.insert(i)

    # COLA-CFS.
    i = models.Institute()
    i.Name = "COLA-CFS"
    i.LongName = "Center for Ocean-Land-Atmosphere Studies"
    i.CountryCode = "US"
    i.URL = "http://grads.iges.org/colablurb.html"
    session.insert(i)

    # CSIRO-BOM.
    i = models.Institute()
    i.Name = "CSIRO-BOM"
    i.LongName = "Commonwealth Scientific and Industrial Research Organization (CSIRO) and Bureau of Meteorology (BOM), Australia"
    i.CountryCode = "AU"
    i.URL = "http://www.csiro.au/"
    session.insert(i)

    # BCC.
    i = models.Institute()
    i.Name = "BCC"
    i.LongName = "Beijing Climate Center, China Meteorological Administration"
    i.CountryCode = "CN"
    i.URL = "http://bcc.cma.gov.cn/en/"
    session.insert(i)

    # GCESS.
    i = models.Institute()
    i.Name = "GCESS"
    i.LongName = "College of Global Change and Earth System Science, Beijing Normal University"
    i.CountryCode = "CN"
    i.URL = "http://www.bnu.edu.cn/gces/"
    session.insert(i)

    # CCCMA.
    i = models.Institute()
    i.Name = "CCCMA"
    i.LongName = "Canadian Centre for Climate Modelling and Analysis"
    i.CountryCode = "CA"
    i.URL = "http://www.ec.gc.ca/ccmac-cccma/"
    session.insert(i)

    # RSMAS.
    i = models.Institute()
    i.Name = "RSMAS"
    i.LongName = "University of Miami - RSMAS"
    i.CountryCode = "US"
    i.URL = "http://www.rsmas.miami.edu/"
    session.insert(i)

    # NCAR.
    i = models.Institute()
    i.Name = "NCAR"
    i.LongName = "National Center for Atmospheric Research"
    i.CountryCode = "US"
    i.URL = "http://ncar.ucar.edu/"
    session.insert(i)

    # NSF-DOE-NCAR.
    i = models.Institute()
    i.Name = "NSF-DOE-NCAR"
    i.LongName = "Community Earth System Model Contributors"
    i.CountryCode = "US"
    i.URL = "http://www.cesm.ucar.edu/"
    session.insert(i)

    # NCEP.
    i = models.Institute()
    i.Name = "NCEP"
    i.LongName = "National Centers for Environmental Prediction"
    i.CountryCode = "US"
    i.URL = "http://www.ncep.noaa.gov/"
    session.insert(i)

    # CMCC.
    i = models.Institute()
    i.Name = "CMCC"
    i.LongName = "Centro Euro-Mediterraneo per I Cambiamenti Climatici"
    i.CountryCode = "IT"
    i.URL = "http://www.cmcc.it/"
    session.insert(i)

    # CNRM-CERFACS.
    i = models.Institute()
    i.Name = "CNRM-CERFACS"
    i.LongName = "Centre National de Recherches Meteorologiques / Centre Europeen de Recherche et de Formation Avancee en Calcul Scientifique"
    i.CountryCode = "FR"
    i.URL = "http://www.cerfacs.fr/"
    session.insert(i)

    # CSIRO-QCCCE.
    i = models.Institute()
    i.Name = "CSIRO-QCCCE"
    i.LongName = "Commonwealth Scientific and Industrial Research Organisation / Queensland Climate Change Centre of Excellence"
    i.CountryCode = "AU"
    i.URL = "http://www.csiro.au/"
    session.insert(i)

    # EC-EARTH.
    i = models.Institute()
    i.Name = "EC-EARTH"
    i.LongName = "EC-EARTH"
    i.CountryCode = "NL"
    i.URL = "http://ecearth.knmi.nl/"
    session.insert(i)

    # LASG-CESS.
    i = models.Institute()
    i.Name = "LASG-CESS"
    i.LongName = "LASG, Institute of Atmospheric Physics, Chinese Academy of Sciences and CESS,Tsinghua University"
    i.CountryCode = "CN"
    i.URL = "http://www.iap.ac.cn/ http://www.tsinghua.edu.cn/publish/cessen/"
    session.insert(i)

    # LASG-IAP.
    i = models.Institute()
    i.Name = "LASG-IAP"
    i.LongName = "LASG, Institute of Atmospheric Physics, Chinese Academy of Sciences"
    i.CountryCode = "CN"
    i.URL = "http://www.iap.ac.cn/"
    session.insert(i)

    # FIO.
    i = models.Institute()
    i.Name = "FIO"
    i.LongName = "The First Institute of Oceanography, SOA, China"
    i.CountryCode = "CN"
    i.URL = "http://www.fio.org.cn/"
    session.insert(i)

    # INPE.
    i = models.Institute()
    i.Name = "INPE"
    i.LongName = "Instituto Nacional de Pesquisas Espaciais"
    i.CountryCode = "BR"
    i.URL = "http://www.inpe.br/"
    session.insert(i)

    # NASA GMAO.
    i = models.Institute()
    i.Name = "NASA-GMAO"
    i.LongName = "NASA Global Modeling and Assimilation Office"
    i.CountryCode = "US"
    i.URL = "https://gmao.gsfc.nasa.gov/"
    session.insert(i)

    # NOAA-GFDL.
    i = models.Institute()
    i.Name = "NOAA-GFDL"
    i.LongName = "NOAA Geophysical Fluid Dynamics Laboratory"
    i.CountryCode = "US"
    i.URL = "http://www.gfdl.noaa.gov/"
    session.insert(i)

    # NASA GISS.
    i = models.Institute()
    i.Name = "NASA-GISS"
    i.LongName = "NASA Goddard Institute for Space Studies"
    i.CountryCode = "US"
    i.URL = "http://www.giss.nasa.gov/"
    session.insert(i)

    # NIMR-KMA.
    i = models.Institute()
    i.Name = "NIMR-KMA"
    i.LongName = "National Institute of Meteorological Research/Korea Meteorological Administration"
    i.CountryCode = "KR"
    i.URL = "http://www.nimr.go.kr/MA/main.jsp"
    session.insert(i)

    # MOHC.
    i = models.Institute()
    i.Name = "MOHC"
    i.LongName = "Met Office Hadley Centre"
    i.CountryCode = "UK"
    i.URL = "http://www.metoffice.gov.uk/climatechange/science/hadleycentre/"
    session.insert(i)

    # INM.
    i = models.Institute()
    i.Name = "INM"
    i.LongName = "Institute of Numerical Mathematics"
    i.CountryCode = "RU"
    i.URL = "http://www.inm.ras.ru/"
    session.insert(i)

    # IPSL.
    i = models.Institute()
    i.Name = "IPSL"
    i.LongName = "Institut Pierre Simon Laplace"
    i.CountryCode = "FR"
    i.URL = "http://www.ipsl.fr/"
    session.insert(i)

    # MIROC.
    i = models.Institute()
    i.Name = "MIROC"
    i.LongName = "Japan Agency for Marine-Earth Science and Technology, Atmosphere and Ocean Research Institute (The University of Tokyo), and National Institute for Environmental Studies"
    i.CountryCode = "JP"
    i.URL = "http://www.ccsr.u-tokyo.ac.jp/"
    session.insert(i)

    # MPI-M.
    i = models.Institute()
    i.Name = "MPI-M"
    i.LongName = "Max Planck Institute for Meteorology"
    i.CountryCode = "DE"
    i.URL = "http://www.mpimet.mpg.de/"
    session.insert(i)

    # MRI.
    i = models.Institute()
    i.Name = "MRI"
    i.LongName = "Meteorological Research Institute"
    i.CountryCode = "JP"
    i.URL = "http://www.mri-jma.go.jp/"
    session.insert(i)

    # NICAM.
    i = models.Institute()
    i.Name = "NICAM"
    i.LongName = "Nonhydrostatic Icosahedral Atmospheric Model Group"
    i.CountryCode = "JP"
    i.URL = "http://www.ccsr.u-tokyo.ac.jp/~satoh/nicam/index.html"
    session.insert(i)

    # NCC.
    i = models.Institute()
    i.Name = "NCC"
    i.LongName = "Norwegian Climate Centre"
    i.CountryCode = "NO"
    i.URL = "http://www.cicero.uio.no/"
    session.insert(i)

