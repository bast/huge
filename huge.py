"""Find huge additions in Git history."""

__version__ = "0.1.0"


import subprocess
import itertools
from tqdm import tqdm
import click
from tabulate import tabulate


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


@click.command()
@click.option(
    "--branch", default="master", show_default=True, help="Which branch to scan."
)
@click.option(
    "--num-entries",
    default=20,
    type=int,
    show_default=True,
    help="How many top entries to show.",
)
@click.option(
    "--cutoff",
    default=1000000,
    type=int,
    show_default=True,
    help="Cutoff (bytes) below which to ignore entries.",
)
def main(branch, num_entries, cutoff):
    commits = get_all_commits_on_branch(branch)

    print("scanning the history ...")
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
        size_mb = float(k[0]) / 1000000.0
        additions.append((size_mb, k[1], v))

    additions = reversed(sorted(additions))

    print("\n")

    rows = list(itertools.islice(additions, num_entries))
    if len(rows) > 0:
        print(tabulate(rows, headers=["size (MB)", "path", "commit"],))
    else:
        print("no additions found")


if __name__ == "__main__":
    main()
