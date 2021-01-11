import pandas as pd

from variable import input_file, output_file

df = pd.read_csv(input_file)
parsed = df.loc[(df['업종명'] == '스포츠레져용품') &
                (df['성별'] == '여') &
                (df['연령대별'] == '20대'),
                ['제주중분류', '업종명', '성별', '연령대별', '카드이용금액']]
parsed.to_csv(output_file, index=False)
