def find_differences(Json_old, Json_new, diff_list):
    result = {}
    old_data = Json_old.get('data', {})
    new_data = Json_new.get('data', {})

    for key in diff_list:
        if key in old_data and key in new_data:
            if old_data[key] != new_data[key]:
                result[key] = new_data[key]

    return result


