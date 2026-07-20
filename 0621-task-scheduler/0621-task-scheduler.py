class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = Counter(tasks)

        heap = []

        for task,frequency in count.items():
            heapq.heappush(heap,(-frequency,task))

        cooldown = deque()

        time = 0

        while heap or cooldown:

            time +=1

            if cooldown and cooldown[0][0] == time:
                
                _,avail_task,rem_count = cooldown.popleft()
                heapq.heappush(heap,(-rem_count,avail_task))
                

            if heap:
                freq,task = heapq.heappop(heap)

                rem_count = -freq
                rem_count -=1

                if rem_count > 0:
                    cooldown.append((time+n+1,task,rem_count))


        return time
