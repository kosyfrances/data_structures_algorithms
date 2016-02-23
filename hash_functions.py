def HASH_FUNCTION(s):
    """Simple but not ideal hash function."""
    return sum(ord(c) for c in s)

# Using remainder method to get bucket position
bucket_count = 50
bucket_number_for_brazil = HASH_FUNCTION("Brazil") % bucket_count
