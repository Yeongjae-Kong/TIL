import heapq

def solution(jobs):
    jobs.sort()  # 요청 시간 기준으로 정렬
    heap = []  # 최소 힙 (소요 시간 기준 정렬)
    time, total_wait_time, count = 0, 0, 0
    job_index = 0
    
    while count < len(jobs):
        # 현재 시간 이하에서 실행 가능한 모든 작업을 힙에 추가
        while job_index < len(jobs) and jobs[job_index][0] <= time:
            heapq.heappush(heap, (jobs[job_index][1], jobs[job_index][0]))
            job_index += 1
        
        if heap:  # 실행 가능한 작업이 있다면
            duration, request_time = heapq.heappop(heap)
            time += duration
            total_wait_time += time - request_time
            count += 1
        else:  # 실행 가능한 작업이 없다면 시간을 다음 요청 작업 시점으로 이동
            time = jobs[job_index][0]
    
    return total_wait_time // len(jobs)
