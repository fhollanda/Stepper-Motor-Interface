import tds2024Cusb
import numpy
import matplotlib.pyplot as plot
import time

# elementos usados para criacao virtual de um osciloscopio, canal e configuracao do mesmo 
scope = tds2024Cusb.tek2024('/dev/usbtmc0') #osciloscopio virtual

channel1 = tds2024Cusb.channel(scope,1) #canal virtual

#scope.set_autoRange('both')

scope.set_hScale(frequency=250000, cycles=10)    	# Set the time scale to the mimimum that contains 1 waveforms
scope.set_averaging(64)                        		# Set the scope to do 0X averaging
channel1.set_vScale(50)                      		# Set the voltage scale to 200mV

# aquisicao do sinal
data_adc_d_p = channel1.get_measurement()#_autoRange()                         # Download the waveform from channel 1


# elementos necessarios apenas para apresentacao ----------------
fig = plot.figure(figsize=(15,15))
plot.title("Oscilloscope Result")
plot.ylabel("Voltage (V)\n")
plot.xlabel("Time (Sec)")
ax1 = fig.add_subplot(411,axisbg =(0.85, 0.85, 0.85))
ax1.plot(data_adc_d_p[0], data_adc_d_p[1], color='red')
ax1.grid(True)


# criacao de arquvio --------------------------------------------
ts = time.time()
f = open( 'data_'+ str(ts).replace(".","") +'.py', 'w' )
f.write( 'data = ' + repr(data_adc_d_p) + '\n' )
f.close()

plot.show()