end_code = int(input())
interactor = int(input())
checker = int(input())

verdict = int()

if interactor == 0 and end_code != 0:
    verdict = 3
elif interactor == 0 and end_code == 0:
    verdict = checker
elif interactor == 4 and end_code != 0:
    verdict = 3
elif interactor == 4 and end_code == 0:
    verdict = 4
elif interactor == 1:
    verdict = checker
elif interactor == 6:
    verdict = 0
elif interactor == 7:
    verdict = 1
else:
    verdict = interactor

print(verdict)
