import re


def parse_gtf_record(record):
    """
    Parse a single record from a gtf file and return a dictionary with specific keys.
    """
    parts = record.strip().split("\t")  # Split the record into columns
    if len(parts) < 9:
        raise ValueError("record does not contain enough fields")

    # Extract fields from the record
    seqname, source, feature, start, end, score, strand, frame, attributes = parts

    # Regular expression to match key="value"
    attribute_pattern = re.compile(r'(\w+) "([^"]+)"')

    # Use regular expression to find all key-value pairs in the attributes
    attributes_dict = {
        match.group(1): match.group(2)
        for match in attribute_pattern.finditer(attributes)
    }

    # Create and return the dictionary
    return {
        "seqname": seqname,
        "source": source,
        "feature": feature,
        "start": int(start),
        "end": int(end),
        "score": float(score) if score != "." else None,
        "strand": strand,
        "frame": frame,
        "attribute": attributes_dict,
    }
