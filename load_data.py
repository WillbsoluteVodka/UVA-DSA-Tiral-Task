import pandas as pd


def load_all_data(file_1,file_2):

    raven_df = pd.read_csv(file_1)
    trakstar_df = pd.read_csv(file_2)

    raven_df['Timestamp'] = pd.to_datetime(raven_df['Timestamp'])
    trakstar_df['Frame timestamp'] = pd.to_datetime(trakstar_df['Frame timestamp'])

    common_timestamps = pd.Index(raven_df['Timestamp']).intersection(pd.Index(trakstar_df['Frame timestamp']))

    selected_raven_df = raven_df[raven_df['Timestamp'].isin(common_timestamps)]
    selected_trakstar_df = trakstar_df[trakstar_df['Frame timestamp'].isin(common_timestamps)]

    raven_df_drop_dup = selected_raven_df.drop_duplicates(subset='Timestamp', keep='first')
    raven_df_drop_dup = raven_df_drop_dup.reset_index(drop=True)

    trakstar_df_drop_dup = selected_trakstar_df.drop_duplicates(subset='Frame timestamp', keep='first')
    trakstar_df_drop_dup = trakstar_df_drop_dup.reset_index(drop=True)

    print("Successfully Load Data")

    return raven_df_drop_dup, trakstar_df_drop_dup
