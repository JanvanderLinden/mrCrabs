# mrCrabs
utility wrapper for crab queries

## usage

```
python3 mrCrabs.py [crabDirectories]
```
Also supports automatically resubmitting failed jobs (`--resubmit`) and appending crab options to the resubmit command (`-a`).

Make sure to have the CMSSW env activated, a valid voms proxy and the usual crab env sourced.

Add the alias `mrCrabs` to your `.profile` with the setup script, to easily use the script anywhere.


## recovery

If a job doesnt terminate start a recovery job by following these steps:
1. kill the job via `crab kill`
2. make a report of the job you just killed via `crab report`
3. use the `recovery.py` script to generate a new crab config with the filtered lumi list (can also be done by hand, so this is just for convenience)
```
python3 recovery.py -p CRAB/DIRECTORY -c ORIGINAL/CRABCONFIG.py
```
4. submit the newly created recovery config
