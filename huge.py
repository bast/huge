import subprocess
import itertools
from tqdm import tqdm


def get_all_commits_on_branch(branch):
    return (
        subprocess.check_output(f"git rev-list {branch}", shell=True)
        .decode("utf8")
        .splitlines()
    )


def get_file_entries(commit):
    return (
        subprocess.check_output(f"git ls-tree -lr {commit}", shell=True)
        .decode("utf8")
        .splitlines()
    )


if __name__ == "__main__":
    cutoff = 1000000
    how_many = 20

    commits = get_all_commits_on_branch("master")

    additions_dict = {}
    for commit in tqdm(commits):
        entries = get_file_entries(commit)
        for line in entries:
            _, _, _, size, path = line.split()
            if not "-" in size:
                if int(size) > cutoff:
                    if not (size, path) in additions_dict:
                        additions_dict[(size, path)] = commit

    additions = []
    for k, v in additions_dict.items():
        additions.append((int(k[0]), k[1], v))

    additions = reversed(sorted(additions))
    for addition in itertools.islice(additions, how_many):
        print(addition)
