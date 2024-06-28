def count_versions(list_version):
    version_count = {}

    for id, version in list_version:
        key = (id, version)
        version_count[key] = version_count.get(key, 0) + 1

    result = [[key[0], key[1], value] for key, value in version_count.items()]

    return result
