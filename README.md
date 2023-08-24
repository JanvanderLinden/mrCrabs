# mrCrabs
utility wrapper for crab queries

## usage

```
python3 mrCrabs.py [crabDirectories]
```
Also supports automatically resubmitting failed jobs (`--resubmit`) and appending crab options to the resubmit command (`-a`).

Make sure to have the CMSSW env activated, a valid voms proxy and the usual crab env sourced.

Add the alias `mrCrabs` to your `.profile` with the setup script, to easily use the script anywhere.
