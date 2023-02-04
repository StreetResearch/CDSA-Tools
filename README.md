# CDSA-Tools
Tools to make living CDSA easier and faster. This is a work in progress!

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
</ol>
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
        <br>To use this scrpt, just place it in the same folder as your GPC data. Currently this only supports Malvern Omnisec instruments.
        <br>An example of the data input format needed can be found in the 'GPC processing' folder.</li>
    </ol>
  </li>
<br>
  <li>Self-assembly tools:
    <ol>
      <li>living CDSA calculator (for seeded growth experiments)</li>
      <li>Micelle Counting Statistics and Histogram Script (automates the analysis of measured nanoparticle sizes/lengths from Fiji/ImageJ).
          <br>To use this script, just place it in the folder with your measurment data from Fiji and ensure the measurments file is called "Results.csv".<br>
          Then run the batch script!</li>
    </ol>
  </li>
</ol>
<br>
More ideas coming when I have time! Any feedback is welcome =)
