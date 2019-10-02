# CMU Pushing dataset
Tool for downloading and using the pushing dataset. In this dataset, there are ~7500 push attempts on 8 simple block objects.

![Alt text](output.gif "Title")

## Getting started with the data

```bash
cd ~
git https://github.com/Dhiraj100892/pushing_dataset.git
cd pushing_dataset
wget https://www.dropbox.com/s/ftostshszsbpehm/data.tar.gz
tar -xvzf data.tar.gz
rm data.tar.gz
```

## Visualize the data
```buildoutcfg
python vis_data.py
```

