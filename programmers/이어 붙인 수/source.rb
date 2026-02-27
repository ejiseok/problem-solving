def solution(num_list)
  even_num_list = []
  odd_num_list = []

  num_list.each do |num|
    if num % 2 == 0
      even_num_list.push(num)
    else
      odd_num_list.push(num)
    end
  end

  sum_even_nums = even_num_list.join().to_i
  sum_odd_nums = odd_num_list.join().to_i

  sum_even_nums + sum_odd_nums
end