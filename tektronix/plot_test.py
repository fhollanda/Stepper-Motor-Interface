import tds2024Cusb
import numpy
import matplotlib.pyplot as plot
import time

scope = tds2024Cusb.tek2024('/dev/usbtmc0') #osciloscopio virtual

channel1 = tds2024Cusb.channel(scope,1) #canal virtual

# DEFAULT_FREQUENCY = 1000000
# DEFAULT_CYCLES = 2
# DEFAULT_AVERAGING = 64
# DEFAULT_V_SCALE = 0.01
# DEFAULT_T_SCALE = 0.000001
# DEFAULT_SAVE_DATA = True

# scope.set_hScale(frequency=DEFAULT_FREQUENCY, cycles=DEFAULT_CYCLES)    	# Set the time scale to the mimimum that contains 1 waveforms
# scope.set_averaging(DEFAULT_AVERAGING)                        		# Set the scope to do 0X averaging
# channel1.set_vScale(DEFAULT_V_SCALE)                      		# Set the voltage scale to 200mV
# channel1.set_tScale(DEFAULT_T_SCALE)
channel1.set_waveformParams('RPBinary')
# aquisicao do sinal
data_adc_d_p = channel1.get_waveform()#_autoRange()                         # Download the waveform from channel 1

bigger = 0.0

array1 = data_adc_d_p[0]
array2 = data_adc_d_p[1]

for i in range(0, len(array1)):	
	if(array1[i] > bigger):
		bigger = array1[i]
		indice = i

print(bigger)

print ("Maior tempo: %s | maior voltagem: %s" % (array1[indice], array2[indice]) )

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