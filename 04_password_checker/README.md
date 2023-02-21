# password_checker
This tool uses the pwnedpasswords API which uses the k-Anonymity model allowing for the search of a password via a partial SHA-1 hash-key (first 5 hashes).
***
It is a commandline tool to safely check if your passwords have been pawned.

**To use:** run with python through terminal and input any number of passwords to check.

e.g. `python .\checkmypass.py password1 password2` and so on.
***
**_Notes:_**
_The input password will not be sent over to any servers and remains local on machine._
Clear the readline text of your terminal once done to delete terminal input history.

In PowerShell I ran the following:
```powershell
Get-PSReadlineOption | select -expand historysavepath
```
then copied the path it returns and pasted instead of the "pathGoesHere" section.
```powershell
Clear-Content pathGoesHere -Force
```
This will clear your entire input history in Windows powershell.