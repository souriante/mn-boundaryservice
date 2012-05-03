from datetime import date

from boundaryservice import utils

SHAPEFILES = {
    # This key should be the plural name of the boundaries in this set
    'Minnesota 2002 State House districts': {
        # Path to a shapefile, relative to /data/shapefiles
        'file': 'state-house-districts/2010/tl_2010_27_sldl10/tl_2010_27_sldl10.shp',
        # Generic singular name for an boundary of from this set
        'singular': 'State House district (2002)',
        # Should the singular name come first when creating canonical identifiers for this set?
        'kind_first': False,
        # Function which each feature wall be passed to in order to extract its "external_id" property
        # The utils module contains several generic functions for doing this
        'ider': utils.simple_namer(['geoid10']),
        # Function which each feature will be passed to in order to extract its "name" property
        'namer': utils.simple_namer(['sldlst10'], normalizer=lambda x: x.lstrip('0')),
        # Authority that is responsible for the accuracy of this data
        'authority': 'U.S. Census Bureau Tiger lines',
        # Geographic extents which the boundary set encompasses
        'domain': 'Minnesota',
        # Last time the source was checked for new data
        'last_updated': date(2012, 5, 3),
        # A url to the source of the data
        'href': 'http://www.census.gov/cgi-bin/geo/shapefiles2010/main',
        # Notes identifying any pecularities about the data, such as columns that were deleted or files which were merged
        'notes': '',
        # Encoding of the text fields in the shapefile, i.e. 'utf-8'. If this is left empty 'ascii' is assumed
        'encoding': '',
        # SRID of the geometry data in the shapefile if it can not be inferred from an accompanying .prj file
        # This is normally not necessary and can be left undefined or set to an empty string to maintain the default behavior
        'srid': ''
    },
    'Minnesota 2002 State Senate districts': {
        'file': 'state-senate-districts/2010/tl_2010_27_sldu10/tl_2010_27_sldu10.shp',
        'singular': 'State Senate district (2002)',
        'kind_first': False,
        'ider': utils.simple_namer(['geoid10']),
        'namer': utils.simple_namer(['sldust10'], normalizer=lambda x: x.lstrip('0')),
        'authority': 'U.S. Census Bureau Tiger lines',
        'domain': 'Minnesota',
        'last_updated': date(2012, 5, 3),
        'href': 'http://www.census.gov/cgi-bin/geo/shapefiles2010/main',
        'notes': '',
        'encoding': '',
        'srid': ''
    },
    'Minnesota 2012 State House districts': {
        'file': 'state-house-districts/2012/L2012/L2012.shp',
        'singular': 'State House district',
        'kind_first': False,
        'ider': utils.simple_namer(['id']),
        'namer': utils.simple_namer(['district'], normalizer=lambda x: x.lstrip('0')),
        'authority': 'Minnesota GIS',
        'domain': 'Minnesota',
        'last_updated': date(2012, 5, 3),
        'href': 'http://www.gis.leg.mn/redist2010/plans.html',
        'notes': '',
        'encoding': '',
        'srid': ''
    },
    'Minnesota 2012 State Senate districts': {
        'file': 'state-senate-districts/2012/S2012/S2012.shp',
        'singular': 'State Senate district',
        'kind_first': False,
        'ider': utils.simple_namer(['id']),
        'namer': utils.simple_namer(['district'], normalizer=lambda x: x.lstrip('0')),
        'authority': 'Minnesota GIS',
        'domain': 'Minnesota',
        'last_updated': date(2012, 5, 3),
        'href': 'http://www.gis.leg.mn/redist2010/plans.html',
        'notes': '',
        'encoding': '',
        'srid': ''
    },
    '2012 Congressional districts': {
        'file': 'congressional-districts/2012/C2012/C2012.shp',
        'singular': 'Congressional district',
        'kind_first': False,
        'ider': utils.simple_namer(['id']),
        'namer': utils.simple_namer(['district']),
        'authority': 'Minnesota GIS',
        'domain': 'Minnesota',
        'last_updated': date(2012, 5, 3),
        'href': 'http://www.gis.leg.mn/redist2010/plans.html',
        'notes': '',
        'encoding': '',
        'srid': ''
    },
    '2002 Congressional districts': {
        'file': 'congressional-districts/2010/tl_2010_27_cd111/tl_2010_27_cd111.shp',
        'singular': 'Congressional district (2002)',
        'kind_first': False,
        'ider': utils.simple_namer(['geoid10']),
        'namer': utils.simple_namer(['cd111fp'], normalizer=lambda x: x.lstrip('0')),
        'authority': 'U.S. Census Bureau Tiger lines',
        'domain': 'Minnesota',
        'last_updated': date(2012, 5, 3),
        'href': 'http://www.census.gov/cgi-bin/geo/shapefiles2010/main',
        'notes': '',
        'encoding': '',
        'srid': ''
    },
    'School districts': {
        'file': 'school-districts/tl_2010_27_unsd10/tl_2010_27_unsd10.shp',
        'singular': 'School district',
        'kind_first': False,
        'ider': utils.simple_namer(['geoid10']),
        'namer': utils.simple_namer(['name10']),
        'authority': 'U.S. Census Bureau Tiger lines',
        'domain': 'Minnesota',
        'last_updated': date(2012, 5, 3),
        'href': 'http://www.census.gov/cgi-bin/geo/shapefiles2010/main',
        'notes': '',
        'encoding': '',
        'srid': ''
    }
}