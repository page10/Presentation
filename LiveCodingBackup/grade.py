# List of scores
SCORES = [45, 78, 32, 92, 58]


def append_pass_fail_status(scores):
    # List to store pass/fail results
    pass_fail_status = []
    for score in scores:
        if score >= 60:
            pass_fail_status.append("Pass")
        else:
            pass_fail_status.append("Fail")
    return pass_fail_status


def append_using_lambda(scores):
    # Define a lambda function to determine pass/fail
    def is_pass(score): return "Pass" if score >= 60 else "Fail"

    # List to store pass/fail results
    pass_fail_status = []
    for score in scores:
        pass_fail_status.append(is_pass(score))


def append_using_lambda_map(scores):
    pass_fail_status = list(
        map(lambda score: "Pass" if score >= 60 else "Fail", scores))
    return pass_fail_status


def main():
    print('Write in triditional style: ', append_pass_fail_status(SCORES))
    print('Write with lambda: ', append_using_lambda(SCORES))
    print('Write in lambda and map: ', append_using_lambda_map(SCORES))


if __name__ == '__main__':
    main()
