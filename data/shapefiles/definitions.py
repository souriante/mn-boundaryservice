from datetime import date
from boundaryservice import utils
import processing

SHAPEFILES = {
    # This key should be the plural name of the boundaries in this set
    'State House districts (2002)': {
        # Path to a shapefile, relative to /data/shapefiles
        'file': 'state-house-districts/2002-census/tl_2010_27_sldl10/tl_2010_27_sldl10.shp',
        # Generic singular name for an boundary of from this set
        'singular': 'State House district (2002)',
        # Should the singular name come first when creating canonical identifiers for this set?
        'kind_first': False,
        # Function which each feature wall be passed to in order to extract its "external_id" property
        # The utils module contains several generic functions for doing this
        'ider': utils.simple_namer(['geoid10']),
        # Function which each feature will be passed to in order to extract its "name" property
        #
        # This ends up being the slug: 63a-state-house-district-2002
        'namer': utils.simple_namer(['sldlst10'], normalizer=lambda x: x.lstrip('0')),
        # Authority that is responsible for the accuracy of this data
        'authority': 'U.S. Census Bureau TIGER lines',
        # Geographic extents which the boundary set encompasses
        'domain': 'Minnesota',
        # Last time the source was checked for new data
        'last_updated': date(2012, 5, 3),
        # A url to the source of the data
        'href': 'http://www.census.gov/cgi-bin/geo/shapefiles2010/main',
        # Notes identifying any pecularities about the data, such as columns that were deleted or files which were merged
        'notes': 'These districts were defined in 2002.',
        # Encoding of the text fields in the shapefile, i.e. 'utf-8'. If this is left empty 'ascii' is assumed
        'encoding': '',
        # SRID of the geometry data in the shapefile if it can not be inferred from an accompanying .prj file
        # This is normally not necessary and can be left undefined or set to an empty string to maintain the default behavior
        'srid': ''
    },
    'State House districts (2012)': {
        'file': 'state-house-districts/2012-mn_leg_gis/L2012/L2012.shp',
        'singular': 'State House district (2012)',
        'kind_first': False,
        'ider': utils.simple_namer(['id']),
        'namer': utils.simple_namer(['district'], normalizer=lambda x: x.lstrip('0')),
        'authority': 'Minnesota Legislative Coordinating Commission - GIS Office',
        'domain': 'Minnesota',
        'last_updated': date(2012, 5, 3),
        'href': 'http://www.gis.leg.mn/redist2010/plans.html',
        'notes': 'These districts were defined in 2012.',
        'encoding': '',
        'srid': ''
    },

    # State Senate
    'State Senate districts (2002)': {
        'file': 'state-senate-districts/2002-census/tl_2010_27_sldu10/tl_2010_27_sldu10.shp',
        'singular': 'State Senate district (2002)',
        'kind_first': False,
        'ider': utils.simple_namer(['geoid10']),
        'namer': utils.simple_namer(['sldust10'], normalizer=lambda x: x.lstrip('0')),
        'authority': 'U.S. Census Bureau TIGER lines',
        'domain': 'Minnesota',
        'last_updated': date(2012, 5, 3),
        'href': 'http://www.census.gov/cgi-bin/geo/shapefiles2010/main',
        'notes': 'These districts were defined in 2002.',
        'encoding': '',
        'srid': ''
    },
    'State Senate districts (2012)': {
        'file': 'state-senate-districts/2012-mn_leg_gis/S2012/S2012.shp',
        'singular': 'State Senate district (2012)',
        'kind_first': False,
        'ider': utils.simple_namer(['id']),
        'namer': utils.simple_namer(['district'], normalizer=lambda x: x.lstrip('0')),
        'authority': 'Minnesota Legislative Coordinating Commission - GIS Office',
        'domain': 'Minnesota',
        'last_updated': date(2012, 5, 3),
        'href': 'http://www.gis.leg.mn/redist2010/plans.html',
        'notes': 'These districts were defined in 2012.',
        'encoding': '',
        'srid': ''
    },

    # Congress
    'Congressional districts (2002)': {
        'file': 'congressional-districts/2002-census/tl_2010_27_cd111/tl_2010_27_cd111.shp',
        'singular': 'Congressional district (2002)',
        'kind_first': False,
        'ider': utils.simple_namer(['geoid10']),
        'namer': utils.simple_namer(['cd111fp'], normalizer=lambda x: x.lstrip('0')),
        'authority': 'U.S. Census Bureau TIGER lines',
        'domain': 'Minnesota',
        'last_updated': date(2012, 5, 3),
        'href': 'http://www.census.gov/cgi-bin/geo/shapefiles2010/main',
        'notes': 'These districts were defined in 2002.',
        'encoding': '',
        'srid': ''
    },
    'Congressional districts (2012)': {
        'file': 'congressional-districts/2012-mn_leg_gis/C2012/C2012.shp',
        'singular': 'Congressional district (2012)',
        'kind_first': False,
        'ider': utils.simple_namer(['id']),
        'namer': utils.simple_namer(['district'], normalizer=lambda x: x.lstrip('0')),
        'authority': 'Minnesota Legislative Coordinating Commission - GIS Office',
        'domain': 'Minnesota',
        'last_updated': date(2012, 5, 3),
        'href': 'http://www.gis.leg.mn/redist2010/plans.html',
        'notes': 'These districts were defined in 2012.',
        'encoding': '',
        'srid': ''
    },

    # School districts
    'School districts (2010)': {
        'file': 'school-districts/2010-census/tl_2010_27_unsd10.shp',
        'singular': 'School district (2010)',
        'kind_first': False,
        'ider': utils.simple_namer(['geoid10']),
        'namer': utils.simple_namer(['geoid10'], normalizer=lambda x: x.lstrip('0')),
        'authority': 'U.S. Census Bureau TIGER lines',
        'domain': 'Minnesota',
        'last_updated': date(2012, 5, 3),
        'href': 'http://www.census.gov/cgi-bin/geo/shapefiles2010/main',
        'notes': '',
        'encoding': '',
        'srid': ''
    },
    'School districts (2012)': {
        'file': 'school-districts/2012-mngeo/sd12.shp',
        'singular': 'School district (2012)',
        'kind_first': False,
        'ider': processing.simple_index_namer(['sdnum'], normalizer=lambda x: '0' if x is '0' else x.lstrip('0')),
        'namer': processing.simple_index_namer(['sdnum'], normalizer=lambda x: '0' if x is '0' else x.lstrip('0')),
        'authority': 'MN Geo and Minnesota Department of Education',
        'domain': 'Minnesota',
        'last_updated': date(2012, 7, 18),
        'href': 'http://www.mngeo.state.mn.us/chouse/metadata/sd12.html',
        'notes': 'Aitkin and Minneapolis share the same ID, so Minneapolis is 1-1.',
        'encoding': '',
        'srid': ''
    },
    'School districts (2013)': {
        'file': 'school-districts/2013-mn-leg/sd13.shp',
        'singular': 'School district (2013)',
        'kind_first': False,
        'ider': processing.simple_index_namer(['sdnum'], normalizer=lambda x: '0' if x is '0' else x.lstrip('0')),
        'namer': processing.simple_index_namer(['sdnum'], normalizer=lambda x: '0' if x is '0' else x.lstrip('0')),
        'authority': 'MN State Legislature and Minnesota Department of Education',
        'domain': 'Minnesota',
        'last_updated': date(2013, 10, 10),
        'href': 'http://www.gis.leg.mn/html/download.html',
        'notes': 'Aitkin and Minneapolis share the same ID, so Minneapolis is 1-1.',
        'encoding': '',
        'srid': ''
    },

    # Cenus tracts
    'Census tracts (2011)': {
        'file': 'census-tracts/2011-census/tl_2011_27_tract.shp',
        'singular': 'Census tract (2011)',
        'kind_first': False,
        'ider': utils.simple_namer(['geoid']),
        'namer': utils.simple_namer(['name'], normalizer=lambda x: x.lstrip('0')),
        'authority': 'U.S. Census Bureau TIGER lines',
        'domain': 'Minnesota',
        'last_updated': date(2012, 6, 22),
        'href': 'http://www.census.gov/cgi-bin/geo/shapefiles2011/main',
        'notes': '',
        'encoding': '',
        'srid': ''
    },

    # Counties
    'Counties (2010)': {
        'file': 'counties/2010-mn-gis-leg/county2010.shp',
        'singular': 'County (2010)',
        'kind_first': False,
        'ider': utils.simple_namer(['data'], normalizer=lambda x: x.lstrip('0')),
        'namer': utils.simple_namer(['data'], normalizer=lambda x: x.lstrip('0')),
        'authority': 'Minnesota Legislative Coordinating Commission - GIS Office',
        'domain': 'Minnesota',
        'last_updated': date(2012, 11, 12),
        'href': 'http://www.gis.leg.mn/metadata/county2010.htm',
        'notes': 'The County ID used is the Minnesota count code, as opposed to the Census code.',
        'encoding': '',
        'srid': ''
    },

    # State forests
    'State forests (2009)': {
        'file': 'state-forests/2009-mn-dnr/bdry_stforpy3.shp',
        'singular': 'State forest (2009)',
        'kind_first': False,
        'ider': utils.index_namer(['sft']),
        'namer': utils.simple_namer(['sft']),
        'authority': 'Minnesota Department of Natural Resources (DNR)',
        'domain': 'Minnesota',
        'last_updated': date(2012, 6, 22),
        'href': 'http://deli.dnr.state.mn.us/metadata.html?id=L220000170201',
        'notes': '',
        'encoding': '',
        'srid': ''
    },

    # State parks
    'State parks (2002)': {
        'file': 'state-parks/2002-mn-dnr/bdry_stprkpy3.shp',
        'singular': 'State park (2002)',
        'kind_first': False,
        'ider': utils.index_namer('pgm_prj'),
        'namer': utils.simple_namer(['pgm_prj']),
        'authority': 'Minnesota Department of Natural Resources (DNR)',
        'domain': 'Minnesota',
        'last_updated': date(2012, 6, 22),
        'href': 'http://deli.dnr.state.mn.us/metadata.html?id=L220000190201',
        'notes': '',
        'encoding': '',
        'srid': ''
    },

    # National parks
    'National forests (2008)': {
        'file': 'national-forests/2008-mn-dnr/bdry_ntforpy3.shp',
        'singular': 'National forest (2008)',
        'kind_first': False,
        'ider': processing.simple_index_namer(['region', 'forest_num'], normalizer=lambda x: x.lstrip('0')),
        'namer': processing.simple_index_namer(['region', 'forest_num'], normalizer=lambda x: x.lstrip('0')),
        'authority': 'Minnesota Department of Natural Resources (DNR)',
        'domain': 'Minnesota',
        'last_updated': date(2012, 6, 22),
        'href': 'http://deli.dnr.state.mn.us/metadata.html?id=L220000110201',
        'notes': '',
        'encoding': '',
        'srid': ''
    },

    # Reservation land
    'Reservation lands (2010)': {
        'file': 'reservations/2010-mn_leg_gis/amerind2010.shp',
        'singular': 'Reservation land (2010)',
        'kind_first': False,
        'ider': utils.simple_namer(['id']),
        'namer': utils.simple_namer(['id'], normalizer=lambda x: x.lstrip('0')),
        'authority': 'Minnesota Legislative Coordinating Commission - GIS Office',
        'domain': 'Minnesota',
        'last_updated': date(2012, 6, 22),
        'href': 'http://www.gis.leg.mn/metadata/amerind2010.htm',
        'notes': '',
        'encoding': '',
        'srid': ''
    },

    # Voting precincts (will take awhile)
    'Voting precincts (2010)': {
        'file': 'voting-precincts/2010-mn_leg_gis/vtd_20101029.shp',
        'singular': 'Voting precinct (2010)',
        'kind_first': False,
        'ider': utils.simple_namer(['district'], normalizer=lambda x: x.lstrip('0')),
        'namer': utils.simple_namer(['district'], normalizer=lambda x: x.lstrip('0')),
        'authority': 'Minnesota Legislative Coordinating Commission - GIS Office and Minnesota Secretary of State',
        'domain': 'Minnesota',
        'last_updated': date(2012, 6, 22),
        'href': 'http://www.gis.leg.mn/metadata/vtd2010.htm',
        'notes': '',
        'encoding': '',
        'srid': ''
    },
    'Voting precincts (2012)': {
        'file': 'voting-precincts/2012-mn_sos/vtd2012general.shp',
        'singular': 'Voting precinct (2012)',
        'kind_first': False,
        'ider': utils.simple_namer(['vtd'], normalizer=lambda x: x.lstrip('0')),
        'namer': utils.simple_namer(['vtd'], normalizer=lambda x: x.lstrip('0')),
        'authority': 'Minnesota Secretary of State',
        'domain': 'Minnesota',
        'last_updated': date(2012, 7, 24),
        'href': 'http://www.gis.leg.mn/metadata/vtd2012.htm',
        'notes': 'A couple precincts in Makota did not have a proper ID so it was manually added assuming a specific identification scheme.',
        'encoding': '',
        'srid': ''
    },

    # Minor civic divisons (cities and towns) (will take awhile)
    'Minor civil divisions (2010)': {
        'file': 'minor-civil-divisions/2010-mn_leg_gis/mcd2010.shp',
        'singular': 'Minor civil division (2010)',
        'kind_first': False,
        'ider': utils.simple_namer(['mcd'], normalizer=lambda x: x.lstrip('0')),
        'namer': utils.simple_namer(['mcd'], normalizer=lambda x: x.lstrip('0')),
        'authority': 'Minnesota Legislative Coordinating Commission - GIS Office',
        'domain': 'Minnesota',
        'last_updated': date(2012, 6, 22),
        'href': 'http://www.gis.leg.mn/metadata/mcd2010.htm',
        'notes': 'Minor civil divisions are also considered cities and townships.',
        'encoding': '',
        'srid': ''
    },

    # District courts
    'District courts (2008)': {
        'file': 'district-courts/2008-mn_gis_leg/US_Judicial_Districts-edited.shp',
        'singular': 'District court (2008)',
        'kind_first': False,
        'ider': utils.simple_namer(['judicial'], normalizer=lambda x: x.lstrip('0')),
        'namer': utils.simple_namer(['judicial'], normalizer=lambda x: x.lstrip('0')),
        'authority': 'Minnesota Legislative Coordinating Commission - GIS Office',
        'domain': 'Minnesota',
        'last_updated': date(2012, 7, 13),
        'href': 'http://gis.leg.mn/',
        'notes': 'Emailed directly from the MN Leg GIS dept.  Edited to add more descriptive name.',
        'encoding': '',
        'srid': ''
    },
    'District courts (2012)': {
        'file': 'district-courts/2012-mn_sos/vtd2012_judicial_district.shp',
        'singular': 'District court (2012)',
        'kind_first': False,
        'ider': utils.simple_namer(['juddist'], normalizer=lambda x: x.lstrip('0')),
        'namer': utils.simple_namer(['juddist'], normalizer=lambda x: x.lstrip('0')),
        'authority': 'Minnesota Secretary of State',
        'domain': 'Minnesota',
        'last_updated': date(2012, 7, 24),
        'href': 'http://www.gis.leg.mn/metadata/vtd2012.htm',
        'notes': 'This dataset was derived from the 2012 voting precincts dataset.',
        'encoding': '',
        'srid': ''
    },

    # Zip codes
    'ZIP codes (2010)': {
        'file': 'zipcodes/2010-census/tl_2010_27_zcta510.shp',
        'singular': 'Zip code (2010)',
        'kind_first': False,
        'ider': utils.simple_namer(['ZCTA5CE10']),
        'namer': utils.simple_namer(['ZCTA5CE10']),
        'authority': 'U.S. Census Bureau TIGER lines',
        'domain': 'Minnesota',
        'last_updated': date(2012, 7, 18),
        'href': 'ftp://ftp2.census.gov/geo/tiger/TIGER2010/ZCTA5/2010/',
        'notes': '',
        'encoding': '',
        'srid': ''
    },

    # County Commissioner districts
    'County Commissioner districts (2012)': {
        'file': 'county-commissioner/2012-mn_sos/vtd2012_county_commissioner.shp',
        'singular': 'County Commissioner district (2012)',
        'kind_first': False,
        'ider': utils.simple_namer(['ccd_id'], normalizer=lambda x: x.lstrip('0')),
        'namer': utils.simple_namer(['ccd_id'], normalizer=lambda x: x.lstrip('0')),
        'authority': 'Minnesota Secretary of State',
        'domain': 'Minnesota',
        'last_updated': date(2012, 7, 24),
        'href': 'http://www.gis.leg.mn/metadata/vtd2012.htm',
        'notes': 'This dataset was derived from the 2012 voting precincts dataset.',
        'encoding': '',
        'srid': ''
    },

    # Hospital districts
    'Hospital districts (2012)': {
        'file': 'hospitals/2012-mn_sos/vtd2012_hospital_districts.shp',
        'singular': 'Hospital district (2012)',
        'kind_first': False,
        'ider': utils.simple_namer(['hospdist'], normalizer=lambda x: x.lstrip('0')),
        'namer': utils.simple_namer(['hospdist'], normalizer=lambda x: x.lstrip('0')),
        'authority': 'Minnesota Secretary of State',
        'domain': 'Minnesota',
        'last_updated': date(2012, 7, 24),
        'href': 'http://www.gis.leg.mn/metadata/vtd2012.htm',
        'notes': 'This dataset was derived from the 2012 voting precincts dataset.',
        'encoding': '',
        'srid': ''
    },

    # Soil and water districts
    'Soil and Water districts (2012)': {
        'file': 'soil-water/2012-mn_sos/vtd2012_soil_water.shp',
        'singular': 'Soil and Water district (2012)',
        'kind_first': False,
        'ider': utils.simple_namer(['soilwdist'], normalizer=lambda x: x.lstrip('0')),
        'namer': utils.simple_namer(['soilwdist'], normalizer=lambda x: x.lstrip('0')),
        'authority': 'Minnesota Secretary of State',
        'domain': 'Minnesota',
        'last_updated': date(2012, 7, 24),
        'href': 'http://www.gis.leg.mn/metadata/vtd2012.htm',
        'notes': 'This dataset was derived from the 2012 voting precincts dataset.',
        'encoding': '',
        'srid': ''
    },

    # Wards
    # In theory the id for this should be the MCD code with the Ward code, but
    # since the MCD code is not with the data, then we use the MCD name
    'Wards (2012)': {
        'file': 'wards/2012-mn_sos/vtd2012_wards.shp',
        'singular': 'Ward (2012)',
        'kind_first': False,
        'ider': utils.simple_namer(['ward_id'], normalizer=lambda x: x.lstrip('0')),
        'namer': utils.simple_namer(['ward_id'], normalizer=lambda x: x.lstrip('0')),
        'authority': 'Minnesota Secretary of State',
        'domain': 'Minnesota',
        'last_updated': date(2012, 7, 24),
        'href': 'http://www.gis.leg.mn/metadata/vtd2012.htm',
        'notes': 'This dataset was derived from the 2012 voting precincts dataset.',
        'encoding': '',
        'srid': ''
    },

    # Minneapolis neighborhoods
    'Minneapolis Neighborhoods (2013)': {
        'file': 'neighborhoods/2013-minneapolis-neighborhoods/minneapolis-neighborhoods-2013.shp',
        'singular': 'Minneapolis Neighborhood (2013)',
        'kind_first': False,
        'ider': utils.simple_namer(['neighbor_1']),
        'namer': utils.simple_namer(['neighbor_1']),
        'authority': 'City of Minneapolis',
        'domain': 'Minnesota',
        'last_updated': date(2013, 6, 4),
        'href': 'http://www.minneapolismn.gov/maps/about_maps_public-maps-links',
        'notes': 'This dataset was was altered to create unique descriptive IDs for each neighborhood for better referencing.',
        'encoding': '',
        'srid': ''
    },

    # St. Paul district councils (neighborhoods)
    'St. Paul District Councils (2012)': {
        'file': 'neighborhoods/2012-st-paul-district-councils/District_Councils.shp',
        'singular': 'St. Paul District Council (2012)',
        'kind_first': False,
        'ider': utils.simple_namer(['DISTRICT']),
        'namer': utils.simple_namer(['DISTRICT']),
        'authority': 'City of St. Paul',
        'domain': 'Minnesota',
        'last_updated': date(2013, 6, 4),
        'href': 'http://stpaul.gov/index.aspx?nid=4836',
        'notes': 'This data was requested via email.',
        'encoding': '',
        'srid': ''
    },
    'St. Paul District Councils (2014)': {
        'file': 'neighborhoods/2014-st-paul-district-councils/District_CouncilsNew2014.shp',
        'singular': 'St. Paul District Council (2014)',
        'kind_first': False,
        'ider': utils.simple_namer(['DISTRICT']),
        'namer': utils.simple_namer(['DISTRICT']),
        'authority': 'City of St. Paul',
        'domain': 'Minnesota',
        'last_updated': date(2013, 6, 4),
        'href': 'http://stpaul.gov/index.aspx?nid=4836',
        'notes': 'This data was requested via email.',
        'encoding': '',
        'srid': ''
    },

    # MetCouncil districts
    'Metropolitan Council districts (2013)': {
        'file': 'metropolitan-council-districts/2013-mn-leg/mc2013-1A.shp',
        'singular': 'Metropolitan Council district (2013)',
        'kind_first': False,
        'ider': processing.simple_index_namer(['id'], normalizer=lambda x: '0' if x is '' else x.lstrip('0')),
        'namer': processing.simple_index_namer(['district'], normalizer=lambda x: '0' if x is '' else x.lstrip('0')),
        'authority': 'MN State Legislature',
        'domain': 'Minnesota',
        'last_updated': date(2013, 10, 10),
        'href': 'http://www.gis.leg.mn/html/download.html',
        'notes': '',
        'encoding': '',
        'srid': ''
    },

    # Minneapolis Parks and Recreation districts
    'Minneapolis Parks and Recreation districts (2012)': {
        'file': 'parks-recreation-districts/2012-minneapolis-parks-recreation/2012_CommDist_Redistricting_ALL.shp',
        'singular': 'Minneapolis Parks and Recreation district (2012)',
        'kind_first': False,
        'ider': processing.simple_index_namer(['mplspark']),
        'namer': processing.simple_index_namer(['mplspark']),
        'authority': 'Minneapolis Parks and Recreation Board',
        'domain': 'Minnesota',
        'last_updated': date(2013, 10, 17),
        'href': 'http://www.minneapolisparks.org/default.asp?PageID=1005',
        'notes': 'Recieved via email from the Minneapolis Parks and Recreation Board.',
        'encoding': '',
        'srid': ''
    },
    'Minneapolis Parks and Recreation districts (2014)': {
        'file': 'parks-recreation-districts/2014-minneapolis-parks-recreation/2014-minneapolis-parks-recreation.shp',
        'singular': 'Minneapolis Parks and Recreation district (2014)',
        'kind_first': False,
        'ider': processing.simple_index_namer(['id']),
        'namer': processing.simple_index_namer(['id']),
        'authority': 'Minneapolis Parks and Recreation Board',
        'domain': 'Minnesota',
        'last_updated': date(2013, 10, 17),
        'href': 'http://www.minneapolisparks.org/default.asp?PageID=1005',
        'notes': 'Compiled manually from multiple shapefiles recieved via email from the Minneapolis Parks and Recreation Board.',
        'encoding': '',
        'srid': ''
    },

    # Census places
    #'Census places (2011)': {
    #    'file': 'census-places/2011-census/tl_2011_27_place.shp',
    #    'singular': 'Census place (2011)',
    #    'kind_first': False,
    #    'ider': utils.simple_namer(['geoid']),
    #    'namer': utils.simple_namer(['geoid'], normalizer=lambda x: x.lstrip('0')),
    #    'authority': 'U.S. Census Bureau TIGER lines',
    #    'domain': 'Minnesota',
    #    'last_updated': date(2012, 6, 22),
    #    'href': 'http://www.census.gov/cgi-bin/geo/shapefiles2011/main',
    #    'notes': 'From Wikipedia: "A census-designated place (CDP) is a concentration of population identified by the United States Census Bureau for statistical purposes. CDPs are delineated for each decennial census as the statistical counterparts of incorporated places such as cities, towns and villages. CDPs are populated areas that lack separate municipal government, but which otherwise physically resemble incorporated places."',
    #    'encoding': '',
    #    'srid': ''
    #},

    # States
    #'States (2011)': {
    #    'file': 'states/2011-census/tl_2011_us_state.shp',
    #    'singular': 'State (2011)',
    #    'kind_first': False,
    #    'ider': utils.simple_namer(['stusps'], normalizer=lambda x: x.lstrip('0')),
    #    'namer': utils.simple_namer(['name'], normalizer=lambda x: x.lstrip('0')),
    #    'authority': 'U.S. Census Bureau TIGER lines',
    #    'domain': 'United States of America',
    #    'last_updated': date(2012, 7, 13),
    #    'href': 'ftp://ftp2.census.gov/geo/tiger/TIGER2011/STATE/',
    #    'notes': '',
    #    'encoding': '',
    #    'srid': ''
    #},

    # Countries
    #'Countries (2012)': {
    #    'file': 'countries/2012-natural_earth_1.4.0/10m-admin-0-countries-edited.shp',
    #    'singular': 'Country (2012)',
    #    'kind_first': False,
    #    'ider': utils.simple_namer(['ne_10m_adm'], normalizer=lambda x: x.lstrip('0')),
    #    'namer': utils.simple_namer(['admin'], normalizer=lambda x: x.lstrip('0')),
    #    'authority': 'Natural Earth',
    #    'domain': 'World',
    #    'last_updated': date(2012, 7, 13),
    #    'href': 'http://www.naturalearthdata.com/downloads/10m-cultural-vectors/',
    #    'notes': 'Edited to remove columns to reduce file size, and to remove any non-ASCII characters.',
    #    'encoding': '',
    #    'srid': ''
    #},

    # Timezones
    #'Timezones (2012)': {
    #    'file': 'timezones/2012-natural_earth_beta_3/ne_10m_time_zones_beta_3-edited.shp',
    #    'singular': 'Timezone (2012)',
    #    'kind_first': False,
    #    'ider': utils.simple_namer(['gid'], normalizer=lambda x: x.lstrip('0')),
    #    'namer': utils.simple_namer(['time_zone']),
    #    'authority': 'Natural Earth',
    #    'domain': 'World',
    #    'last_updated': date(2012, 7, 13),
    #    'href': 'http://www.naturalearthdata.com/',
    #    'notes': 'Edited to add identifier.',
    #    'encoding': '',
    #    'srid': ''
    #},
}