# init
Sets = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
TargetSol = [0, 0, 0, 1, 0, 1, 1, 0]
w = [1, 1, 1, 1, 1, 1, 1, 1]


def genInput(x):
    return [
        1,
        x[0],
        x[1],
        x[2],
        x[0] * x[1],
        x[1] * x[2],
        x[0] * x[2],
        x[0] * x[1] * x[2],
    ]


def activate(sum):
    if sum >= 0:
        return 1
    else:
        return 0


def perzeptronOut(x):
    inputPerzeptrion = 0
    for i in range(len(x)):
        inputPerzeptrion += x[i] * w[i]
    return inputPerzeptrion


def learnPerzeptron(x, output, target):
    error = target - output
    for i in range(0, len(w)):
        w[i] += error * x[i]


def testPerzeptrion():
    for i in range(len(Sets)):
        input = genInput(Sets[i])
        sum = perzeptronOut(input)
        if activate(sum) != TargetSol[i]:
            return False
    return True


if __name__ == '__main__':
    notWorking = True
    epoch = 0
    while notWorking and epoch < 10000:
        print("_______________________________________")
        epoch += 1
        print("Epoch: ", epoch)
        for i in range(len(TargetSol)):
            input = genInput(Sets[i])
            sum = perzeptronOut(input)
            output = activate(sum)
            if output != TargetSol[i]:
                learnPerzeptron(input, output, TargetSol[i])
        if testPerzeptrion():
            notWorking = False
        print("Weights: ", w)
    input_2 = [0, 0, 0]
    sum = perzeptronOut(genInput(input_2))
    print(activate(sum))
    input_2 = [0, 0, 1]
    sum = perzeptronOut(genInput(input_2))
    print(activate(sum))
    input_2 = [0, 1, 0]
    sum = perzeptronOut(genInput(input_2))
    print(activate(sum))
    input_2 = [0, 1, 1]
    sum = perzeptronOut(genInput(input_2))
    print(activate(sum))
    input_2 = [1, 0, 0]
    sum = perzeptronOut(genInput(input_2))
    print(activate(sum))
    input_2 = [1, 0, 1]
    sum = perzeptronOut(genInput(input_2))
    print(activate(sum))
    input_2 = [1, 1, 0]
    sum = perzeptronOut(genInput(input_2))
    print(activate(sum))
    input_2 = [1, 1, 1]
    sum = perzeptronOut(genInput(input_2))
    print(activate(sum))
