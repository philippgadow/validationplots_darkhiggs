# Validation plots for MadGraph job options for dark Higgs signal

Link to job options: https://github.com/philippgadow/jobOptions_darkHiggsbb


## Run validation plots

### Produce histograms

In a new shell, execute

```
source setup_release.sh
bash run_histograms.sh
```


### Produce validation plots from histograms

In a new shell (with no analysis release set up), execute

```
source setup_venv.sh
source run_plots.sh
```

Use an anaconda Python3 version for a nice experience. 

## Samples

Samples with ME reweighting weights:

Weights:
```
weights for reweigthing in gx:
0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0,
1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0,
2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0
```

| ------ | ------------- | ---------------------- | ---------------------- | ------------ |
| DSID   | Z' mass [GeV] | dark Higgs mass [GeV]  | dark matter mass [GeV] | coupling gx  |
| ------ | ------------- | ---------------------- | ---------------------- | ------------ |
| 110000 |           500 |                     50 |                    100 |          1.0 |
| 110001 |           500 |                     50 |                    100 |          1.5 |
| 110002 |           500 |                     50 |                    100 |          2.0 |
| 110003 |           500 |                     50 |                    100 |          2.5 |
| 110004 |           500 |                     50 |                    100 |          3.0 |
| 110010 |           500 |                     90 |                    100 |          1.0 |
| 110011 |           500 |                     90 |                    100 |          1.5 |
| 110012 |           500 |                     90 |                    100 |          2.0 |
| 110013 |           500 |                     90 |                    100 |          2.5 |
| 110014 |           500 |                     90 |                    100 |          3.0 |
| ------ | ------------- | ---------------------- | ---------------------- | ------------ |

Samples for closure checks without weights:

| ------ | ------------- | ---------------------- | ---------------------- | ------------ |
| DSID   | Z' mass [GeV] | dark Higgs mass [GeV]  | dark matter mass [GeV] | coupling gx  |
| ------ | ------------- | ---------------------- | ---------------------- | ------------ |
| 111000 |           500 |                     50 |                    100 |          0.1 |
| 111001 |           500 |                     50 |                    100 |          0.3 |
| 111002 |           500 |                     50 |                    100 |          0.5 |
| 111003 |           500 |                     50 |                    100 |          0.7 |
| 111004 |           500 |                     50 |                    100 |          1.0 |
| 111005 |           500 |                     50 |                    100 |          1.3 |
| 111006 |           500 |                     50 |                    100 |          1.7 |
| 111007 |           500 |                     50 |                    100 |          2.0 |
| 111008 |           500 |                     50 |                    100 |          2.3 |
| 111009 |           500 |                     50 |                    100 |          2.7 |
| 111010 |           500 |                     90 |                    100 |          0.1 |
| 111011 |           500 |                     90 |                    100 |          0.3 |
| 111012 |           500 |                     90 |                    100 |          0.5 |
| 111013 |           500 |                     90 |                    100 |          0.7 |
| 111014 |           500 |                     90 |                    100 |          1.0 |
| 111015 |           500 |                     90 |                    100 |          1.3 |
| 111016 |           500 |                     90 |                    100 |          1.7 |
| 111017 |           500 |                     90 |                    100 |          2.0 |
| 111018 |           500 |                     90 |                    100 |          2.3 |
| 111019 |           500 |                     90 |                    100 |          2.7 |
| ------ | ------------- | ---------------------- | ---------------------- | ------------ |
