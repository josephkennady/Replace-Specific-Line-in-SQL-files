<!DOCTYPE html>
<html>
<body>
    <h1>Replace Specific Line in SQL files</h1>
    <p>This script uses the glob, os, and fileinput modules in Python to replace a specific line in multiple SQL files in a folder.</p>
    <h2>Usage</h2>
    <ol>
        <li>Set the directory path where your SQL files are located in the directory variable.</li>
        <li>Set the line that you want to replace in old_line variable and the replacement line in new_line variable.</li>
        <li>Run the script with Python</li>
    </ol>
    <h2>Notes</h2>
    <ul>
        <li>This script will replace the line in place, meaning the original files will be modified.</li>
        <li>Please make sure to make a backup of your files before making any changes.</li>
        <li>This script only works with SQL files, it will not replace the line in any other type of file.</li>
        <li>The script uses glob library to get the list of files and then uses fileinput module to do the inplace replacement of the line.</li>
    </ul>
</body>
</html>
