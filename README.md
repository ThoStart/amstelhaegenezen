Amstelhaege Case
=============

Summary
------------
The amstelhaege case is a heuristic problem in which land sized 160 x 180 meter has to be filled with either 20, 40 or 60 houses. Each house has (depending on which house type it is) a certain amount of free space around it. The houses are to be placed in such a way that the land's value is the highest possible. Next to the houses 20% of the surface has to be water. 
If the amount of free space is higher than the standard free space, the value of a house will increase.

There are three different kinds of houses:
- Eengezinswoningen
- Bungalows
- Maisons

<table>
  <tr>
    <th>Type</th>
    <th>Standard Price</th>
    <th>Size</th>
    <th>Standard free space</th>
    <th>Factor increment</th>
    <th>Percentage of all houses</th>

  </tr>
  <tr>
    <td>Eengezinswoning</td>
    <td>$285.000</td>
    <td>8 x 8 meter </td>
    <td>2 meter</td>
    <td>0,03 </td>
    <td>60% </td>
  </tr>
    <tr>
    <td>Bungalow</td>
    <td>$399.000</td>
    <td>10 x 7.5 meter </td>
    <td>3 meter</td>
    <td>0,04 </td>
    <td>25% </td>
  </tr>
  <tr>
    <td>Maison</td>
    <td>$610.000</td>
    <td>11 x 10.5 meter </td>
    <td>6 meter</td>
    <td>0,06 </td>
    <td>15% </td>
  </tr>
</table>

Usage
------------
run main.py with python3
<pre><code> python3 main.py </code></pre>

A prompt will be opened which algorithm(s) you want to use to fill the numpy grid with houses.

Possible algorithms to use:
- random fill algorithm
- random fill algorithm in combination with hill climber algortihm
- greedy algorithm
- greedy algorithm in combination with hill climber algorithm

The prompt will also ask if you want to visualize the solution, visualations are done with tkinter.


Installation
------------
To use this program several applications need to be installed including Numpy, Tkinter and Matplotlib.

To install Numpy:
Please see: http://scipy.org/install.html for installing numpy on your system.

To install Tkinter use these commands in terminal:
<pre><code>sudo apt-get install python3-tk</code></pre>
To install Matplotlib use these commands in terminal: (matplotlib needs numpy to work)
<pre><code> 
brew install libpng freetype pkg-config
python -mpip install .
</code></pre>


Contributors
------------
Timo den Hartog - Programmer <br>
Alex Witkamp - Programmer <br>
Thomas Start - Programmer <br>

Quinten van der Post - Legend / Teaching Assistent
