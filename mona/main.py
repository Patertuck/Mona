import os
import shutil
from typing import Final

from mona import runtime_factory
from mona.demo_programs.demo_runner import test_record_replay

# DEMO_SRC: Final[str] = """
# decl strlst(lst) {
#     if (lenof(lst) > 0) {
#         print(lst[0], "->");
#         strlst(lst[1:]);
#     }
# }
# strlst([1, 2, 9]);
# """
with open("mona/demo_programs/programs/queue.mona", "r", encoding="utf-8") as f:
#with open("mona/demo_programs/programs/singleThread.mona", "r", encoding="utf-8") as f:
#with open("mona/demo_programs/programs/sharedVariable.mona", "r", encoding="utf-8") as f:
    DEMO_SRC = f.read()


OUTPUT_DIR: Final[str] = os.path.join(os.getcwd(), "output_dir")
STEPS: Final[int] = 5
SNAPNR: Final[int] = 2


def main():
    # Initialise output directory.
    if os.path.isdir(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
    os.mkdir(OUTPUT_DIR)

    # Run program.
    # print(">>>>>> EVALUATING PROGRAM")
    # runtime_factory.run(src=DEMO_SRC, output_dir=OUTPUT_DIR)

    # print("\n>>>>>> COUNTING PROGRAM EXPRESSIONS")
    # runtime_factory.run_and_count_expressions(src=DEMO_SRC, output_dir=OUTPUT_DIR)

    print("\n>>>>>> RECORDING PROGRAM EXECUTION")
    runtime_factory.run_and_record(src=DEMO_SRC, output_dir=OUTPUT_DIR, steps=STEPS)

    # replay_snapshot_filepath = os.path.join(OUTPUT_DIR, f"{SNAPNR}_snap.pickle")
    # output_replay_snapshot_filepath = os.path.join(OUTPUT_DIR, f"{SNAPNR}_out_snap.pickle")
    # print(f"\n>>>>>> REPLAYING EXECUTION SNAPSHOT '{replay_snapshot_filepath}' into '{output_replay_snapshot_filepath}'")
    # runtime_factory.replay_snapshot(src=DEMO_SRC, snapshot_filename=replay_snapshot_filepath)

    replay_all_snapshots(src=DEMO_SRC, output_dir=OUTPUT_DIR)


# chatgpt generated
def replay_all_snapshots(src: str, output_dir: str) -> None:
    print("\n>>>>>> REPLAYING ALL SNAPSHOTS")
    files = sorted(
    (
        f for f in os.listdir(output_dir)
        if f.endswith("_snap.pickle") and f.split("_")[0].isdigit()
    ),
    key=lambda f: int(f.split("_")[0])

    )

    for snap_file in files:
        snap_num = snap_file.split("_")[0]
        snapshot_path = os.path.join(output_dir, snap_file)
        output_path = os.path.join(output_dir, f"{snap_num}_out_snap.pickle")

        print(f"\nReplaying: {snapshot_path}")
        try:
            runtime_factory.replay_snapshot(src=src, snapshot_filename=snapshot_path)
        except SystemExit:
            # Replay mode uses sys.exit() to stop early, so just continue
            print(f"Finished replay for snapshot {snap_num}")


if __name__ == "__main__":
    main()