#! /usr/bin/env python

import sys

import numpy as np
from matplotlib import pyplot as plt
import ogr
import gdal

import geolib
import extract_profile

#Input DEM
dem_fn = sys.argv[1]
dem_ds = gdal.Open(dem_fn)
dem_srs = geolib.get_srs(dem_ds)

#TLS location
tls_srs = geolib.wgs_srs
tls_coord = (0,0,0)
tls_height = 2.0
tls_vfov = (-30.0, 30.0)
tls_range = (5.0, 6000.0)

fig = plt.figure()
#Plot center point
plt.plot((0,tls_coord[2], color='b')  

dl = 100.0
geom_list = []
d_az = 90.0
az_range = (0.0, 360.0)
#az_list = (0.0, 90.0, 180.0, 270.0)
az_list = np.linspace(*az_range, d_az)
d_ele = 1.0
ele_list = np.linspace(*tls_vfov, d_ele)
for az in az_list:
    mx = (tls_coord[0], tls_range[1]*np.sin(np.deg2rad(az)))
    my = (tls_coord[1], tls_range[1]*np.cos(np.deg2rad(az)))
    line = ogr.Geometry(ogr.wkbLineString)
    geom_wkt = 'LINE(({0}))'.format(', '.join(['{0} {1}'.format(*a) for a in zip(mx,my)]))
    geom = ogr.CreateGeometryFromWkt(geom_wkt)
    if not tls_srs.IsSame(dem_srs):
        geolib.geom_transform(geom, dem_srs)
    geom.AssignSpatialReference(dem_srs)
 
    #Generate points in map coordinates for geom
    l, mX, mY = geolib.line2pts(geom,dl)
    z = extract_profile.getZ(dem, dem_ds.GetGeoTransform(), mX, mY) 
    plt.plot(l, z, color='k')
    d_min_idx = 1
    d_out = []
    z_out = []
    for ele in ele_list:
        for d,n in enumerate(l[d_min_idx:]):
            z_ele = d*np.tan(np.deg2rad(ele))
            z_d = z[idx+1]
            if z_d >= z_ele:
                d_min_idx = n
                d_out.append(d)
                z_out.append(z_d)
    plt.plot(d_out, z_out, color='r')
                
            
            
            
            
        
        
        
        
    
