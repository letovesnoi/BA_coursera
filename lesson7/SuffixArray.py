from collections import defaultdict

def sort_bucket(str, bucket, order):
    d = defaultdict(list)
    for i in bucket:
        key = str[i:i + order]
        d[key].append(i)
    result = []
    for k, v in sorted(d.iteritems()):
        if len(v) > 1:
            result += sort_bucket(str, v, order * 2)
        else:
            result.append(v[0])
    return result

def main():
    with open('inputSAC.txt', 'r') as fin:
        Text = fin.readline()
    y = sort_bucket(Text, (i for i in range(len(Text))), 1)
    with open('outputSAC.txt', 'w') as fout:
        ans = str(y).strip('[]')
        fout.write(ans)

#main()
