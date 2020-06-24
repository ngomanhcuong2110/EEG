import os
from fusi_sdk import *
import time
import matplotlib.pyplot as plt
import random
from itertools import count
import pandas as pd

from matplotlib.animation import FuncAnimation
import numpy as np

start_time = time.time()

class MyListener(FusiHeadbandListener):
    def on_connection_change(self, connection_state):
        print("Connection state changed:%s" % connection_state.name)
        if connection_state == ConnectionState.connected:
            headband.set_forehead_led_color((255, 0, 0))
            print("Headband connected")
        elif connection_state == ConnectionState.interrupted:
            print("Headband connection interrupted")
        elif connection_state == ConnectionState.disconnected:
            print("Headband disconnected")
            
    def on_attention(self,attention):
        self.attention = attention
        #print("Attention: %.3f" % attention)
       # print("lendeadband",len(headbands))
        attention_history.append( attention)
        
        
        
    def on_meditation(self, meditation):
        #self.mediation = meditation
        meditation_history.append(meditation)
    # raw data
    def on_eeg_data(self, eeg_data):
        self.eeg_data = eeg_data
        (sample_rate,pga,data) = eeg_data.getValue()
        sample_rate_history.append(sample_rate)
        pga_history.append(pga)
        data_history.extend(data)
        

    #Brainwave database
    def on_brain_wave(self, brain_wave):
        self.brain_wave = brain_wave
       
        (delta, theta, alpha, low_beta, high_beta, gamma) = brain_wave.getValue()
        delta_history.append(delta)
        theta_history.append(theta)
        alpha_history.append(alpha)
        low_beta_history.append(low_beta)
        high_beta_history.append(high_beta)
        gamma_history.append(gamma)

    def on_blink(self):
        print("User's eye blinked!!")

class Get_Diagram(FusiHeadbandListener):
    def valuable(self,attention,meditation,eeg_data,brain_wave):
        self.mediation = meditation
        self.attention = attention
        self. eeg_data = eeg_data
        self.brain_wave = brain_wave


def on_found_devices(devices):
    global headband
    #Check information of each device
    for device in devices:
        #if device.get_mac() == _TARGET_MAC:
        #    headband = device
       
        headband = device
        headbands.append(headband)
    if headbands is None:
        print("No device found")
    else:
      #  for headband in devices:
         #   print ("Name of device:",device.get_name())
          #  print("headband: ",headband)
            
           # headband.set_listener(MyListener())
            
            #headband.connect()
         for i in range(0,len(headbands)):
             
            print ("Name of device:",device.get_name())
            
            
            device.set_listener(MyListener())
            print("headband thu: ", i )
            print(attention_history)
            device.connect();
           
def on_search_error(error):
    print("Pls check your system again")
    print(error)

def animate(i):
    
    
            y1 = attention_history
            
            plt.cla()
            plt.plot(pga_history, label='data_wave')
            #plt.plot(theta_history, label='theta_wave')
            #plt.plot(alpha_history, label='alpha')
            #plt.plot(low_beta_history, label='low_beta')
            #plt.plot(high_beta_history, label='high_beta')
            #plt.plot(gamma_history, label='gamma')
            #plt.plot( attention_history, label='attention')
           
           
            #plt.plot
            plt.legend(loc='upper left')
            plt.tight_layout()
if __name__ == "__main__":
    try:
        _TOTAL_RUN_TIME =1*10 
        headband = None
        meditation_history = []
        attention_history = []
        delta_history = []
        theta_history = []
        alpha_history = []
        low_beta_history = []
        high_beta_history = []
        gamma_history = []
        headbands= []
        sample_rate_history = []
        pga_history = []
        data_history = []
        
        FusiSDK.search_devices(on_found_devices, on_search_error)
        
        ani = FuncAnimation(plt.gcf(), animate, interval=1000)
        
        plt.tight_layout()
        plt.show()
        time.sleep(_TOTAL_RUN_TIME)
        
        print("Timeout, disposing")
       

        
    except KeyboardInterrupt:
        print("Early termination from keyboard")

       



'''

'''
