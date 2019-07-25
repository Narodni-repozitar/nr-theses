from invenio_nusl_theses.marshmallow.data.fields_dict import FIELDS


def create_aliases():
    new_dict = dict()
    for k, v in FIELDS.items():
        if isinstance(v, list):
            for key in v:
                if not new_dict.get(key):
                    new_dict[key] = k
                else:
                    old_value = new_dict[key]
                    if isinstance(old_value, list):
                        new_value = old_value + [k]
                    else:
                        new_value = [old_value, k]
                    new_dict[key] = new_value
        else:
            if not new_dict.get(v):
                new_dict[v] = k
            else:
                old_value = new_dict[v]
                if isinstance(old_value, list):
                    new_value = old_value + [k]
                else:
                    new_value = [old_value, k]
                new_dict[v] = new_value

    return new_dict


if __name__ == "__main__":
    print(create_aliases())
