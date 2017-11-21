import time

import disneylandClient.disneyland_pb2
from disneylandClient.disneyland_pb2 import ListJobsRequest, Job, RequestWithId, ListOfJobs

print("\tUser able to:")

user_client = disneylandClient.new_client()

print("\tCreate Job blank")
blank_job = user_client.CreateJob(Job())
print("success\n{0}".format(blank_job))

print("\tModify Job")
blank_job.status = Job.PENDING
blank_job.metadata = "meta_test"
blank_job.kind = "docker"
updated_job = user_client.ModifyJob(blank_job)
print("success\n{0}".format(updated_job))

print("\tCreate Job with params")
job = Job(metadata="vs", input="python-client-input", output="python-client-output", kind="test")
created_job = user_client.CreateJob(job)
print("success\n{0}".format(created_job))

print("\tGet Job")
read_job = user_client.GetJob(RequestWithId(id=blank_job.id))
disneylandClient.check_jobs_equal(blank_job, read_job)
print("success\n{0}".format(read_job))

print("\tList Jobs with params")
all_jobs = user_client.ListJobs(ListJobsRequest(how_many=1))
if len(all_jobs.jobs) > 0:
    print("success\n{0}".format(all_jobs))

print("\tPull Jobs with proper project")
pulled_jobs = user_client.PullPendingJobs(ListJobsRequest(how_many=2))
if len(pulled_jobs.jobs) > 0:
    print("success\n{0}".format(pulled_jobs))

print("\tCreate Job with params")
created_job = user_client.CreateJob(Job(kind="docker"))
print("success\n{0}".format(created_job))

print("\tDelete Job")
deleted_job = user_client.DeleteJob(RequestWithId(id=blank_job.id))
print("success\n{0}".format(deleted_job))

print("\tCreate Multiple blank Jobs")
lst = [Job(metadata="mul1-python"), Job(metadata="mul2-python")]
result = user_client.CreateMultipeJobs(ListOfJobs(jobs=lst))
if len(result.jobs) == len(lst):
    print("success\n{0}".format(result))
