import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
import tqdm
import re
from sklearn import preprocessing
import librosa


def load(fileRange: list):
    def loadFileHelper():
        df = None

        def loadFile(frame: pd.DataFrame) -> pd.DataFrame:
            nonlocal df
            if df is None:
                df = frame.copy()
                return df
            df = pd.concat([df, frame], axis=1)
            return df

        def final() -> pd.DataFrame:
            return df

        return loadFile, final

    attachList = []
    for dirI in fileRange:
        for root, _, files in os.walk(f'../3rd天府杯A提/附件{dirI}'):
            sorted_files = sorted(files, key=lambda x: int(os.path.splitext(x)[0]))
            attachList += [f'{os.path.join(root, i)}' for i in sorted_files]

    helper, getFinalDf = loadFileHelper()

    tqdmList = tqdm.tqdm(attachList)
    for i in tqdmList:
        res = re.search(r'附件(\d+)\\(\d+)', i)
        header = '-'.join(res.groups())
        tqdmList.set_description(i, header)
        df = pd.read_table(i, sep=r'\n', header=None, engine='python')
        df.columns = [header]
        helper(df)

    df = getFinalDf()
    return df, attachList
