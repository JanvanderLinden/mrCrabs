target=~/.profile
echo "adding mrCrabs command to $target" 
echo "" >> $target
echo "alias mrCrabs='python3 $PWD/mrCrabs.py'" >> $target
echo "" >> $target
echo "done. Source $target to run 'mrCrabs', or just use 'mrCrabs.py'." 

