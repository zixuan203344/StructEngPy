# -*- coding: utf-8 -*-
import numpy as np

class Pattern(object):
    def __init__(self,name:str):
        self.__name=name
        self.__nodal_load={}
        self.__nodal_disp={}
        self.__beam_distributed={}
        self.__beam_concentrated={}

    @property
    def name(self):
        return self.__name

    def set_nodal_load(self,name,f1,f2,f3,m1,m2,m3):
        self.__nodal_load[name]=np.array([f1,f2,f3,m1,m2,m3])

    def set_nodal_disp(self,name,u1,u2,u3,r1,r2,r3):
        self.__nodal_disp[name]=np.array([u1,u2,u3,r1,r2,r3])

    def set_beam_distribute(self,name,fi1,fi2,fi3,mi1,mi2,mi3,fj1,fj2,fj3,mj1,mj2,mj3):
        self.__beam_distribute[name]=np.array([fi1,fi2,fi3,mi1,mi2,mi3,fj1,fj2,fj3,mj1,mj2,mj3])

    def set_beam_concentrate(self,name,F1,F2,F3,M1,M2,M3,r):
        self.__beam_concentrate[name]=np.array([F1,F2,F3,M1,M2,M3,r]) 

    def get_nodal_load(self,name):
        if name in self.__nodal_load.keys():
            return self.__nodal_load[name]
        else:
            return None

    def get_nodal_load_dict(self):
        return self.__nodal_disp.copy()

    def get_nodal_disp(self,name):
        if name in self.__nodal_disp.keys():
            return self.__nodal_disp[name]
        else:
            return None

    def get_nodal_disp_dict(self):
        return self.__nodal_disp.copy()

    def get_beam_distributed(self,name):
        if name in self.__beam_distributed.keys():
            return self.__beam_distributed[name]
        return None

    def get_beam_concentrated(self,name):
        if name in self.__beam_distributed.keys():
            return self.__beam_distributed[name]
        return None

    # def set_node_force(self,node,force,append=False):
    #     """
    #     add node force to model.
    #     params:
    #         node: int, hid of node
    #         force: list of 6 of nodal force
    #         append: bool, if True, the input force will be additional on current force.
    #     return:
    #         bool, status of success
    #     """
    #     assert(len(force)==6)
    #     if append:
    #         self.__nodes[node].fn+=np.array(force).reshape((6,1))
    #     else:
    #         self.__nodes[node].fn=np.array(force).reshape((6,1))
    
    # def set_node_displacement(self,node,disp,append=False):
    #     """
    #     add node displacement to model
        
    #     params:
    #         node: int, hid of node
    #         disp: list of 6 of nodal displacement
    #         append: bool, if True, the input displacement will be additional on current displacement.
    #     return:
    #         bool, status of success
    #     """
    #     assert(len(disp)==6)
    #     if append:
    #         self.__nodes[node].dn+=np.array(disp).reshape((6,1))
    #     else:
    #         self.__nodes[node].dn=np.array(disp).reshape((6,1))
        