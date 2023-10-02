def progress():

    num = int(input())
    index_num = num // 10
    loading_bar = []
    loading_progress = (10 - index_num) * '.'

    loading_bar.append(index_num * '%')
    loading_bar.append(loading_progress)
    result = '[' + ' '.join([loading_bar[0] + loading_bar[1]]) + ']'

    if num < 100:
        return (f"{num}% {result} \nStill loading...")
    if num == 100:
        return (f"{num}% Complete! \n{result}")

print(progress())
