import bin.helpers.utilities.dataLoader as loader
import bin.modules.preProcessing.transform as preProcessing

from bin.helpers.utilities.watcher import *
from bin.helpers.common.main import *

def main():
  ctx='Sequential Pattern Mining for Detection'
  start = watcherStart(ctx)

  # datasetName, stringDatasetName, selected = datasetMenu.getData()

  datasetName = ncc2
  stringDatasetName = 'ncc2'
  selected = 'scenario1'

  df = loader.binetflow(datasetName, selected, stringDatasetName)
  df = df.sort_values(by=['SrcAddr', 'StartTime'])
  df['Unix'] = df['StartTime'].apply(preProcessing.timeToUnix).fillna(0)
  df['Diff'] = df['Unix'] - df['Unix'][0]

  seq = [] #in one subDataset has one sequence
  subSeq = [] #subSequence is based on SrcAddr
  element = []
  totSeqPatternTime = 0
  existSrcAddr = ''
  netT = ()
  for index, row in df.iterrows():
    netT = (
      row['SrcAddr'],row['Sport'],row['DstAddr'],row['Dport'],
      row['State'],row['TotPkts'],row['TotBytes'],row['SrcBytes'],row['Diff']
    )
    if(existSrcAddr == '' or existSrcAddr == row['SrcAddr']):
      totSeqPatternTime += row['Diff']
      if(totSeqPatternTime < 3600):
        element.append(netT)
      else:
        subSeq.append(element)
        element = [netT]
        totSeqPatternTime = 0
    else:
      seq.append(subSeq)
      subSeq = []
      print(seq)
      break
    
    existSrcAddr = row['SrcAddr']

  watcherEnd(ctx, start)