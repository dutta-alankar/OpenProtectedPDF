# OpenProtectedPDF
This shell script will open certain types of password protected PDF files which are very popular in India.
Files are:
(1) Bank account statement
(2) Few certificates
where the first four letters are first four letters of your name along with your date and month of birthdate.

- This code uses MPI to perform coordinated parallel guesses using multiple processors.
- This is ideal for guessing long passwords with brute force using supercomputers.

Use Python (tested with version `3.10`) to run this
- [Optional] Create and use virtual environment: `python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt`
- Run the code: `time mpiexec -n <num_procs> python guess_pdfPass-parallel.py`

> Note: Dependency: qpdf (https://github.com/qpdf/qpdf), tested with version 11.9.1. Make sure `qpdf` and its libraries are added to `PATH` and `LD_LIBRARY_PATH` respectively.
