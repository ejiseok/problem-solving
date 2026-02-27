def solution(num_list)
  last = num_list[-1]
  prevLast = num_list[-2]
  return [*num_list, last - prevLast] if last > prevLast
  [*num_list, last * 2]
end
