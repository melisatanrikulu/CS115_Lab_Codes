# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 14:33:08 2019

@author: b
"""
from Patient import *
import datetime

class Outpatient(Patient):
    
    def __init__( self, name,  ins, aDate, aTime, clinic, dName, cPercent=0.0):
        self.setAppointmentDate(aDate)
        self.__appointmentTime = aTime
        self.__polyClinic = clinic
        self.__doctorName = dName
        if self.__polyClinic in ('Dentistry', 'Optometry'):
            cPercent /= 2
        Patient.__init__(self, name, ins, cPercent)
        
        
    def getAppointmentDate(self):
        return self.__appointmentDate
    
    def setAppointmentDate( self,aDate):
        self.__appointmentDate = datetime.datetime.strptime(aDate, '%Y%m%d').date()
        
    def getAppointmentTime(self):
        return self.__appointmentTime
    
    def setAppointmentTime( self, aTime):
        self.__appointmentTime = aTime 
        
    def getPolyClinic(self):
        return self.__polyClinic
    
    def setPolyClinic( self,clinic):
        self.__polyClinic = clinic
        
    def getDoctorName(self):
        return self.__doctorName
    
    def setDoctorName( self, dName):
        self.doctorName = dName 

    def __lt__(self,other):
        return (self.__appointmentDate,int(self.__appointmentTime[0:2]),int(self.__appointmentTime[3:])) < (other.__appointmentDate,int(other.__appointmentTime[0:2]),int(other.__appointmentTime[3:]))
    
    def __repr__(self):
            data ='\nAppointment Date: '+str(self.__appointmentDate)+' '+self.__appointmentTime
            data += Patient.__repr__(self)
            data += 'Poly Clinic: '+self.__polyClinic+' (Dr. '+self.__doctorName+')'
            data += '\nFee: '+str(self.calculateFee())+'\n'
            return data