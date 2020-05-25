# Assignment 2 : Readme

In this file you can find:

1. Description of project
2. Instructions on how to execute the code
3. Explanation on the code flow.

## Team members

- Alena Tesařová (*up201911219*)

- Stylianos Tsagkarakis (*up2019112311*)

## Libraries and tools used

- Essentia standard 

- Google colab
- Overleaf
- Visual Studio Code

## Project’s file structure

The project can be found on Google Drive [here](https://drive.google.com/drive/folders/1MCN_aZQ9LZJGSZAURgtvO5M77seHKGY5?usp=sharing). Access to the link gives view privileges. 

.										  // Main folder + notebook + helper .py files
├── Original					// Here are the sound files
├── plots						 // Here you can find plots about instant descriptors and waveforms
└── statistics				  // All statistics extracted
    ├── plots					 // 2D plots for task3
        ├── instrument	  // classification on instruments
        ├── name group    // classification on type of instruments
        ├── percussion      // classification on percussion
        ├── pitch		         // classification on pitch
        └── sustained		 // classification on sustainability

​    ├── statistics				// json files of statistics

​    └── csv						  // csv files of statistics



## Report

Tou can find the file **SMUL_REPORT.pdf** in the main folder.

To write the report we used Overleaf as our main tool.

## How to execute code

The python notebook can run on any computer with below prerequisites: 

- python3.5 

- essentia library

  > pip3 install essentia

- a folder with soundfiles



### Editing paths

First thing you should do is fix your paths on one fuction *get_paths()*. Use your desired paths

```python
def get_paths():
    # fix path to match with the location of sound files
    sound_path = "/content/drive/My Drive/FEUP - Multimedia/Original/"

    # fix path to match with the location you want to save the plots
    plots_path = "/content/drive/My Drive/FEUP - Multimedia/plots/"
    
    # fix extension to match with the type of sound file
    file_type_extension = '.wav'
    
    # fix statistics to match with the type of sound file
    statistics = "/content/drive/My Drive/FEUP - Multimedia/statistics/"
    
    return (sound_path, plots_path, statistics, file_type_extension)
```

After inserting your paths, code until Task 2 should run properly, with no errors.

### Generating plots

In the cell under **Assignment 2 / Task 2 / Generate Plots**  you find the code below:

```python
# COMMENT LINE BELOW ONLY IF YOU DONT WANT TO REGENERATE PLOT FILES
create_and_save_plots(final_list, save = True)
```

As the comment states, if you **don't**  want to (re)generate the files comment this line.

**Be careful since around 600 plots are generated and this might create issues with RAM. ** 

### Statistics handling (Task 3)

At one point we generate a *.json* file with the desired extracted statistics. With the help of PHP we convert this file to *.csv*. You can find in the the **SMUL.php** inside the *.zip*.  

For the sake of faster handling and avoiding errors, **excelfile.csv** which is the converted *.json* comes also in the *.zip*. This *.csv* file should be placed in the same folder as the *.ipynb*.

### Predictions (Task 5)

Results for predictions are calculated in the last 3 cells of the *.ipynb*. Same functions are used, but different lines and data. 

