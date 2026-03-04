import pandas as pd


def load_data(data_path):
    student_info = pd.read_csv(f"{data_path}/studentInfo.csv")
    student_vle = pd.read_csv(f"{data_path}/studentVle.csv")
    student_assessment = pd.read_csv(f"{data_path}/studentAssessment.csv")
    assessments = pd.read_csv(f"{data_path}/assessments.csv")
    
    return student_info, student_vle, student_assessment, assessments


def engineer_features(student_info, student_vle, student_assessment, assessments):

    click_features = student_vle.groupby(
        ['code_module', 'code_presentation', 'id_student']
    ).agg(
        total_clicks=('sum_click', 'sum'),
        avg_clicks=('sum_click', 'mean'),
        click_std=('sum_click', 'std')
    ).reset_index()

    click_features['click_std'] = click_features['click_std'].fillna(0)

    assessment_merged = student_assessment.merge(
        assessments[['id_assessment', 'date']],
        on='id_assessment',
        how='left'
    )

    assessment_merged['date'] = pd.to_numeric(assessment_merged['date'], errors='coerce')

    assessment_merged['delay'] = (
        assessment_merged['date_submitted'] - assessment_merged['date']
    )

    delay_features = assessment_merged.groupby(
        ['code_module', 'code_presentation', 'id_student']
    )['delay'].mean().reset_index()

    delay_features.rename(columns={'delay': 'avg_delay'}, inplace=True)

    features = click_features.merge(
        delay_features,
        on=['code_module', 'code_presentation', 'id_student'],
        how='left'
    )

    features['avg_delay'] = features['avg_delay'].fillna(0)

    features = features.merge(
        student_info[['code_module', 'code_presentation', 'id_student', 'final_result']],
        on=['code_module', 'code_presentation', 'id_student'],
        how='left'
    )

    features['overload'] = features['final_result'].apply(
        lambda x: 1 if x in ['Fail', 'Withdrawn'] else 0
    )

    features.drop(columns=['final_result'], inplace=True)

    return features
