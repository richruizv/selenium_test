import pandas as pd
import json


def file_to_json(filename):
    with open(filename+".json", encoding = 'utf-8') as f:
        #transform the file pointer to a json
        data = json.load(f)

        courses = []
        for step in data['steps']:
            for course in step['courses']:
                courses.append(course['course'])

        return pd.DataFrame(courses).convert_dtypes()
        

def common_courses():
    df_da = file_to_json("json/dataanalyst")
    df_ds = file_to_json("json/datascience")
    df_de = file_to_json("json/dataengineer")
    df_ml = file_to_json("json/machinelearning")

    df_join1 = df_da.merge(df_ds,on="title",how="inner")
    df_join2 = df_join1.merge(df_de,on="title",how="inner")
    df_join3 = df_join2.merge(df_ml,on="title",how="inner")

    print(df_join3)

if __name__ == "__main__":

    common_courses()
#   df_join = df_join[df_join['isApproved_y'] == False]
#     df_join[{'title','isApproved_y'}].to_csv('courses_common.csv')
#     print(f"""
# ===========================================================================

#     courses in common: {str(df_join.shape[0])} 

# ===========================================================================""")

    

#     df_pm = df_data.merge(df_ml,on="title",how="left")
#     df_pm = df_pm[df_pm['isApproved_y'].isnull()]
#     df_pm = df_pm[df_pm['isApproved_x'] == False]
#     df_pm[{'title','isApproved_x'}].to_csv('machine_learning_courses.csv')
#     print(f"""
# ===========================================================================

#     Machine learning pending courses: {str(df_pm.shape[0])} 

# ===========================================================================""")

#     print(df_pm)    

    

#     df_dm = df_data.merge(df_ml,on="title",how="right")
#     df_dm = df_dm[df_dm['isApproved_x'].isnull()]
#     df_dm = df_dm[df_dm['isApproved_y'] == False]
#     df_dm[{'title','isApproved_y'}].to_csv('data_engineer_courses.csv')
#     print(f"""
# ===========================================================================

#     Data engineer pending courses: {str(df_dm.shape[0])} 

# ===========================================================================""")

#     print(df_dm)
    
