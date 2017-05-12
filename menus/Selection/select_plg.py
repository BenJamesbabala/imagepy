# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 22:31:12 2016

@author: yxl
"""
from imagepy.core.manager import RoiManager
from imagepy.core.engine import Simple
from imagepy.core.roi.rectangleroi import RectangleRoi
from imagepy import IPy

class SelectAll(Simple):
    """SelectAll: derived from imagepy.core.engine.Simple """
    title = 'Select All'
    note = ['all']

    def run(self, ips, imgs, para = None):
        ips.roi = RectangleRoi(0,0,ips.size[1],ips.size[0])

class SelectNone(Simple):
    """SelectNone: derived from imagepy.core.engine.Simple """
    title = 'Select None'
    note = ['all']

    def run(self, ips, imgs, para = None):
        ips.roi = None
        
class Add2Manager(Simple):
    """Add2Manager: derived from imagepy.core.engine.Simple """
    title = 'Add To Manager'
    note = ['all', 'req_roi']
    para = {'name':''}
    view = [(str, 'Name', 'name', '')]

    def run(self, ips, imgs, para = None):
        RoiManager.add(para['name'], ips.roi)
        
class LoadRoi(Simple):
    """LoadRoi: derived from imagepy.core.engine.Simple """
    title = 'Load Roi'
    note = ['all']
    para = {'name':''}
    
    def load(self, ips):
        titles = list(RoiManager.rois.keys())
        if len(titles)==0: 
            IPy.alert('No roi in manager!')
            return False
        self.para['name'] = titles[0]
        LoadRoi.view = [(list, titles, str, 'Name', 'name', '')]
        return True

    def run(self, ips, imgs, para = None):
        ips.roi = RoiManager.get(para['name'])
        
class Inflate(Simple):
    """Inflate: derived from imagepy.core.engine.Simple """
    title = 'Inflate'
    note = ['all', 'req_roi']
    para = {'r':5}
    view = [(int, (1,100),0, 'radius', 'r','pix')]

    def run(self, ips, imgs, para = None):
        ips.roi = ips.roi.buffer(para['r'])
        
class Shrink(Simple):
    """Shrink: derived from imagepy.core.engine.Simple """
    title = 'Shrink'
    note = ['all', 'req_roi']
    para = {'r':5}
    view = [(int, (1,100),0, 'radius', 'r','pix')]

    def run(self, ips, imgs, para = None):
        ips.roi = ips.roi.buffer(-para['r'])
        
class Convex(Simple):
    """Convex: derived from imagepy.core.engine.Simple """
    title = 'Convex Hull'
    note = ['all', 'req_roi']
    
    def run(self, ips, imgs, para = None):
        ips.roi = ips.roi.convex()
        
class Box(Simple):
    """Box: derived from imagepy.core.engine.Simple """
    title = 'Bound Box'
    note = ['all', 'req_roi']
    
    def run(self, ips, imgs, para = None):
        ips.roi = ips.roi.bounds()
        
class Clip(Simple):
    """Clip: derived from imagepy.core.engine.Simple """
    title = 'Clip Roi'
    note = ['all', 'req_roi']
    
    def run(self, ips, imgs, para = None):
        rect = RectangleRoi(0,0,ips.size[1],ips.size[0])
        ips.roi = ips.roi.clip(rect)
        
class Invert(Simple):
    """Invert: derived from imagepy.core.engine.Simple """
    title = 'Invert Roi'
    note = ['all', 'req_roi']
    
    def run(self, ips, imgs, para = None):
        rect = RectangleRoi(0,0,ips.size[1],ips.size[0])
        ips.roi = ips.roi.invert(rect)
        
plgs = [SelectAll, SelectNone, 
        '-', Inflate, Shrink, Convex, Box, Clip, Invert, 
        '-', Add2Manager, LoadRoi]