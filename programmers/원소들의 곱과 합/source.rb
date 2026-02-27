def solution(num_list)
  num_list.reduce(:*) < num_list.sum ** 2 ? 1 : 0
end