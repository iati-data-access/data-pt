import shutil, os
import iatikit
from iatiflattener import FlattenIATIData
from iatiflattener.group_data import GroupFlatIATIData
from iatiflattener.data_quality import report as data_quality_report

if __name__ == "__main__":
    langs = ['pt']
    iatikit.download.data()
    os.makedirs('output/csv/', exist_ok=True)
    FlattenIATIData(refresh_rates=True,
        langs=langs)
    shutil.rmtree('__iatikitcache__')
    GroupFlatIATIData(langs=langs)
    data_quality_report(lang='pt')
    shutil.rmtree('output/csv/')
