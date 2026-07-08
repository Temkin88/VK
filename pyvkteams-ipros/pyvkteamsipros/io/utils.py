def parse_scheme(istr, scheme):
    if not istr.inAvail():
        return None

    assert isinstance(scheme, dict)
    ret = {}
    while istr.inAvail():
        t, v = istr.getTlv()

        if t not in scheme:
            continue

        subscheme = scheme[t]

        if isinstance(subscheme, dict):
            ret[t] = parse_scheme(v, subscheme)

        elif isinstance(subscheme, list):
            assert len(subscheme) == 1
            subscheme = subscheme[0]

            if isinstance(subscheme, dict):
                ret.setdefault(t, []).append(parse_scheme(v, subscheme))
            else:
                ret.setdefault(t, []).append(v)
        else:
            ret[t] = v

    return ret
