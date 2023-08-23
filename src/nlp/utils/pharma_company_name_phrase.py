import re

removable_strings = [
    ', inc.'
]

removable_regexps = [
    ' \(.*\)',
]


def parse_names_to_phrases(phrases):
    results = []
    for phrase in phrases:
        lowercase_phrase = phrase.lower()
        results.append(lowercase_phrase)
        for part in removable_strings:
            sliced_phrase = lowercase_phrase.replace(part, '')
            if sliced_phrase is not lowercase_phrase:
                results.append(sliced_phrase)
        for regexp in removable_regexps:
            sliced_phrase = re.sub(regexp, '', lowercase_phrase)
            if sliced_phrase is not lowercase_phrase:
                results.append(sliced_phrase)

    return list(dict.fromkeys(results))

