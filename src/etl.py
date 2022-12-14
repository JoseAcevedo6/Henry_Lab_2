from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split


def transform(df, columns=[], target='', test_size=0, random_state=0, array=False, scalar=False):

    labelEncoder = LabelEncoder()

    for i in df.columns:
        if df[i].dtype == 'object':
            df[i] = labelEncoder.fit_transform(df[i].values)

    df_aux = df[columns].copy()

    if target != '':
        df[target] = df_aux[target] = df_aux[target].mask(df_aux[target] <= 8, 0)
        df[target] = df_aux[target] = df_aux[target].mask(df_aux[target] > 8, 1)
        df_aux.drop_duplicates(inplace=True)

        y = df_aux[[target]]
        x = df_aux.drop(target, axis=1)

        X_Train, X_Test, Y_Train, Y_Test = train_test_split(x, y, test_size=test_size, random_state=random_state)

        if array:
            X_Train = X_Train.to_numpy()
            X_Test = X_Test.to_numpy()
            Y_Train = Y_Train.values.ravel()
            Y_Test = Y_Test.values.ravel()

        if scalar:
            scalar = StandardScaler()
            X_Train = scalar.fit_transform(X_Train)
            X_Test = scalar.transform(X_Test)

        return X_Train, X_Test, Y_Train, Y_Test

    else:

        if array:
            df_aux = df_aux.to_numpy()

        if scalar:
            scalar = StandardScaler()
            df_aux = scalar.fit_transform(df_aux)

        return df_aux
