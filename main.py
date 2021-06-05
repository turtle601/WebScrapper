from indeed import get_indeed_jobs
from stackoverflow import get_so_jobs

merge_jobs = get_indeed_jobs() + get_so_jobs()

print(merge_jobs)