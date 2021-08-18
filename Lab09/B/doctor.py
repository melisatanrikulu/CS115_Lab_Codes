# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 11:45:35 2019

@author: b
"""

class Doctor:
    
    def __init__(self, dId, dName, dSpec, hosp):
        self.__doctorId = dId
        self.__doctorName = dName
        self.__specialty = dSpec
        self.__hospital = hosp
    

    def getDoctorId(self):
        return self.__doctorId
    

    def getDoctorId(self, dId):
        self.__doctorId = dId
    

    def getDoctorName(self):
        return self.__doctorName
    
    def setDoctorName(self, dName):
        self.__doctorName = dName
    
 
    def getSpecialty(self):
        return self.__specialty
    
    def setSpecialty(self, dSpec):
        self.__specialty = dSpec
    

    def getHospital(self):
        return self.__hospital

    def setHospital(self, hosp):
        self.__hospital= hosp
    
    def __repr__(self):
        return self.__doctorId+' '+self.__doctorName+' '+self.__specialty+' '+self.__hospital
    
    def __eq__(self,other):
        return self.__doctorId == other.__doctorId
    
    
        
            