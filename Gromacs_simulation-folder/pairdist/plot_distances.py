

import numpy as np
import matplotlib.pyplot as plt
import time




def get_distances_forAllFrame(cl_file,threshold):
	"""function that return distances for all frames as a matrix"""

	all_frame_distances = []
	dist = [] 
	final_dist = []

	with open(cl_file, "r") as file :
		for line in file:
			#skipping lines which contain @ and "#"
			if "@" not in line and "#" not in line:
				line = line.split("\t")
				line[-1] = line[-1].replace("\n","")
				lines = line[0][11::]
				lines = lines.split()
				n_lines = [float(i) for i in lines]
				#print(line[0][0:11])
				all_frame_distances.append(n_lines)
			
			

	dict_frames_chlore_ID= {}
	for l in range(0,len(all_frame_distances)):
		for c in range(0,len(all_frame_distances[119])):
			if float(all_frame_distances[l][c])<= threshold:
				if c not in dict_frames_chlore_ID:
					dict_frames_chlore_ID[l] = c
					

				else:
					pass


				
	return np.array(all_frame_distances), dict_frames_chlore_ID


def print_Cl_ID_AND_distance_Per_Site(threshold):
	"""function that print chlore ID for each frame"""
	file_list =   [ "pairdist1.xvg", "pairdist3.xvg"]
	for file in file_list:
		dist, chlore_ID = get_distances_forAllFrame(file, threshold)
		print("site "+file[8]+" with threshlod =",threshold,":",chlore_ID)
		#print("distance CL-site"+file[8],":\n",dist)
		print("************************************\n")



def main():



	f1 = "pairdist1.xvg"
	f2 = "pairdist2.xvg"
	f3 = "pairdist3.xvg"
	f4 = "pairdist4.xvg"
	f5 = "pairdist5.xvg"



	threshold = 0.1
	dist1, chlore_ID1 = get_distances_forAllFrame(f1,threshold)
	dist2 , chlore_ID2 = get_distances_forAllFrame(f2,threshold)
	dist3 , chlore_ID3 = get_distances_forAllFrame(f3,threshold)
	dist4 , chlore_ID4 = get_distances_forAllFrame(f4,threshold)
	dist5 , chlore_ID5 = get_distances_forAllFrame(f5,threshold)


		
	"""**************************************************Printing chlore ID and corresponding frames ************************************************************ 

	site 1 with threshlod = 0.36 : {110: 27}

	site 1 with threshlod = 0.38 : {106: 27, 109: 27, 110: 27}

	site 2 with threshlod = 0.1 : {11714: 97, 11722: 97, 11766: 97, 17719: 102, 17720: 102}

	site 3 with threshlod = 0.2 : {280: 11, 281: 11, 2125: 6, 2135: 6, 11589: 61, 13550: 78, 13551: 78, 13552: 78, 13554: 78, 13555: 78, 13558: 78, 13559: 78, 13570: 78, 13571: 78, 14317: 38, 15637: 80}
	dmin = d(Cl78, s3)

	site 4 with threshlod = 0.1 : {12767: 46, 15888: 24, 16031: 29}
	dmin = d(Cl46, s4)


	site 5 with threshlod = 0.1 : {12632: 26, 19456: 25}
	dmin = d(Cl26,s5)
	***********************************************************************************************************"""




#******************Ploting distances********************************************************************************
	font = {'family' : 'normal','weight' : 'bold','size' : 14}
	plt.rc('font', **font)
	#plt.plot(dist1[:,27],label = "chlore 27")
	#plt.plot(dist2[:,97], label = "chlore 97")
	#plt.plot(dist2[:,102], label = "chlore 102")
	#plt.plot(dist3[:,11], "-m", label = "chlore 11")
	#plt.plot(dist3[:,6], "-c", label = "chlore 6")
	#plt.plot(dist3[:,78], "-y", label = "chlore 78")
	#plt.plot(dist4[:,46], "-m", label = "chlore 46")
	#plt.plot(dist4[:,24], "-r", label = "chlore 24")
	#plt.plot(dist4[:,29], "-g", label = "chlore 29")
	#plt.plot(dist4[:,26], "-r", label = "chlore 26")
	#plt.plot(dist4[:,25], "-c", label = "chlore 25")
	plt.title("Evolution des distances entre les ions chlore 97 et 102 et le site 2")
	plt.xlabel("numéro de frames")
	plt.ylabel("distances en nm")
	plt.legend(loc = "upper left")
	plt.show()
	plt.savefig("figure1")







main()
exit(0)
