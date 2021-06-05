from indeed import get_indeed_jobs
from stackoverflow import get_so_jobs
from make_csv_file import make_csv

merge_jobs = get_indeed_jobs() + get_so_jobs()
make_csv(merge_jobs)
