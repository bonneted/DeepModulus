#
noise = 0 # noise level, 10%. 
num_epochs = 400000 # number of training epochs.
num_speckle = 200 # number of speckles.
num_test = 1 # number of tests.
mu_start = 4.0
lam_load_start = 7.0
#
#
import os
# Read File
with open("Template/Run_Deepxde.py", "r", encoding="utf-8") as f:
    text = f.read()
#
file_name = "Run_Deepxde.py"
#
file_pre = f"{num_speckle}-{mu_start}-{lam_load_start}-" #str(num_speckle) + "-" + str(noise) + "-" 
#
file_count = 0
num_test_count = 0
#
while True:
    #
    file_count = file_count + 1
    #
    if file_count > 100:
        break
    #
    if num_test_count >= num_test:
        break
    #
    folder_name = file_pre + str(file_count)
    if os.path.exists(folder_name):
        continue
    #
    #
    os.mkdir(folder_name)    
    #
    os.chdir(folder_name)
    #
    with open(file_name, "w", encoding="utf-8") as f:
        f.write("noise = " + str(float(noise)*0.01) + "\n")
        f.write("num_epochs = " + str(num_epochs) + "\n")
        f.write("num_speckle= " + str(num_speckle)+ "\n")
        f.write("mu_start= " + str(mu_start)+ "\n")
        f.write("lam_load_start= " + str(lam_load_start)+ "\n")
        f.writelines(text)
        
    #
    os.system("python " + file_name )
    os.chdir("..")
    #
    num_test_count = num_test_count + 1
    #
