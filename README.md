# CDSA-Tools
Tools to make living CDSA easier and faster. This is a work in progress!<br>
Feel free to use them as you see fit. If you found these tools useful, I would be greatful if you could acknowledge this GitHub Repo! =)

----
TO INSTALL:
----
<ol>
  <li>Download the latest version of python 3 from <a href="https://www.python.org/downloads/">here</a> (these codes were written for python 3.10 or higher):</li>
  <li>Install python. Make sure to select the 'Add python.exe to PATH' in the installer if it is an option.</li>
  <li>Install the python modules we need:
    <ol>
      <li>For windows:</li>
        <ol>
          <li>Press the windows key + x and then select 'windows powershell (Admin)</li>
          <li>Then, type the following (without quotation marks):</li>
            <ol>
              <li>"pip3 install numpy"</li>
              <li>"pip3 install matplotlib"</li>
              <li>"pip3 install pandas"</li>
              <li>"pip3 install seaborn"</li>
              <li>"pip3 install scipy"</li>
              <li>"pip3 install xlsxwriter"</li>
              <li>"pip3 install hplc-py"</li>
            </ol>
          <li>wait for each package to install before starting the next. You can use the same "pip3 install X" command to install any package named X.</li>
          <li>you can check your python installation works by typing "py -3 --version" in the command prompt / powershell, it should tell you your python version.</li>
        </ol>
      <li>For OSX (mac users):</li>
        <ol>
          <li>Open a new terminal window (type terminal into the search bar)</li>
          <li>In the terminal, type the following commands (without quotation marks):
            <ol>
              <li>"python -m pip install numpy"</li>
              <li>"python -m pip install matplotlib"</li>
              <li>"python -m pip install pandas"</li>
              <li>"python -m pip install seaborn"</li>
              <li>"python -m pip install scipy"</li>
              <li>"python -m pip install xlsxwriter"</li>
              <li>"python -m pip install hplc-py"</li>
            </ol>
          <li>you can use the same "python -m pip install X" command to install any package named X.</li>
          <li>you can check python works by typing "python -V" in a terminal window to see your python version.</li>
        </ol>
      <li>Linux users should know what to do!!</li>
    </ol>
  <li>now you can use the scripts! The scripts are designed to go in the same folder as the data you wish to analyze. More details on this coming soon.</li> 
</ol>
<br>
----
Modules needed:
----

You will need the following installed on your system to utilize these codes:
<ol>
  <li>Python 3.10 or higher</li>
  <li>Numpy</li>
  <li>Matplotlib</li>
  <li>Pandas</li>
  <li>Seaborn</li>
  <li>SciPy</li>
  <li>xlsxwriter</li>
  <li>hplc-py</li>
</ol>
<br>
Note, not all scripts need all packages.
<br>
----
Current tools:
----

So far, we have:<br>
<ol>
  <li>General chemistry tools:
    <ol>
      <li>Molecular Weight Calculator</li>
      <li>GPC processing and data plotting (supports multiple samples, uses Mw and WF/dLogM data).
        <br>To use this scrpt, just place it in the same folder as your GPC data. Currently this supports Malvern Omnisec instruments and Wyatt/Agilent insturments.
        <br>Examples of the data input format needed can be found in the 'GPC processing' folder.</li>
      <li>HPLC processing and data plotting.
        <br>Supports Shimadzu insturments.</li>
      <li>UV-Vis processing and data plotting.
        <br>Supports Agilent insturments.</li>
      <li>CD processing and data plotting.
        <br>This is a work in progress.</li>
      <li>Magritek Benchtop NMR Folder Cleanup.
        <br>This script deletes the shim and standby datasets from a backup folder to save space.</li>
    </ol>
  </li>
<br>
  <li>Self-assembly tools:
    <ol>
      <li>living CDSA calculator (for seeded growth experiments)</li>
      <li>Micelle Counting Statistics and Histogram Script (automates the analysis of measured nanoparticle sizes/lengths from Fiji/ImageJ).
          <br>To use this script, just place it in the folder with your measurment data from Fiji and ensure the measurments file is called "Results.csv".<br>
          Then run the batch script!</li>
      <li>Continuous-Flow Self-Assembly Experiment Planner.
        <br>This script allows you to quickly and easily plan self-assembly experiemnts in flow. More features and updates are planned.</li>
    </ol>
  </li>
</ol>
<br>
More ideas coming when I have time! Any feedback is welcome =)
