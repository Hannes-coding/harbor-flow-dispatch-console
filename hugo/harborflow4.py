#scanned labels: gb-104, GB-220, gb-104, se-011, GB-220
#Unique load list:
#1. GB-104
#2. GB-220
#3. SE-011
#Total unique parcels: 3

def consolidate_parcel_labels(label):
    scanned_labels = label
    unique_labels = []
    for word in label.upper().split():
        clean_word = word.strip(",")
        if clean_word not in unique_labels:
            unique_labels.append(clean_word)
    print(f"scanned labels: {scanned_labels}")
    print("Unique load list:")
    i = 0
    while len(unique_labels) > i:
        print(f"{i+1}: {unique_labels[i]}")
        i +=1
    print(f"Total unique parcels: {len(unique_labels)}")
    


consolidate_parcel_labels("gb-104, GB-220, gb-104, se-011, GB-220") #=> [GB-104,GB-220,SE-011]