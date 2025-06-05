import os
import shutil
import sys
import sysconfig
import time
from typing import Final

from mona import runtime_factory

# DEMO_SRC: Final[str] = """
# decl strlst(lst) {
#     if (lenof(lst) > 0) {
#         print(lst[0], "->");
#         strlst(lst[1:]);
#     }
# }
# strlst([1, 2, 9]);
# """
with open("mona/demo_programs/programs/matrix_mul.mona", "r", encoding="utf-8") as f:
    DEMO_SRC_MULTI_THREAD = f.read()

with open("mona/demo_programs/programs/matrix_mul_single.mona", "r", encoding="utf-8") as f:
    DEMO_SRC_SINGLE_THREAD = f.read()

OUTPUT_DIR: Final[str] = os.path.join(os.getcwd(), "output_dir")
STEPS: Final[int] = 30
SNAPNR: Final[int] = 2


def main():
    # Initialise output directory.
    if os.path.isdir(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
    os.mkdir(OUTPUT_DIR)

    gilDisable()
   
    # Timing the multi-threaded execution
    print("\nRunning multi-threaded version...")
    start_time = time.time()
    runtime_factory.run(src=DEMO_SRC_MULTI_THREAD, output_dir=OUTPUT_DIR)
    multi_thread_time = time.time() - start_time
    print(f"Multi-threaded execution took {multi_thread_time:.4f} seconds")

    # Timing the single-threaded execution
    print("\nRunning single-threaded version...")
    start_time = time.time()
    runtime_factory.run(src=DEMO_SRC_SINGLE_THREAD, output_dir=OUTPUT_DIR)
    single_thread_time = time.time() - start_time
    print(f"Single-threaded execution took {single_thread_time:.4f} seconds")

    # Compare the times
    if multi_thread_time < single_thread_time:
        print("\nMulti-threaded version is faster!")
    elif multi_thread_time > single_thread_time:
        print("\nSingle-threaded version is faster!")
    else:
        print("\nBoth versions took the same time.")


def gilDisable():
    print(f"Python version: {sys.version}")

    status = sysconfig.get_config_var("Py_GIL_DISABLED")

    if status is None:
        print("GIL cannot be disabled")
    elif status == 0:
        print("GIL is active")
    elif status == 1:
        print("GIL is disabled")


if __name__ == "__main__":
    main()
