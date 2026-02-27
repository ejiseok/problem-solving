def solution(n, control)
  control.each_char do |ch|
    if ch == "w"
      n += 1
    elsif ch == "s"
      n -= 1
    elsif ch == "d"
      n += 10
    elsif ch == "a"
      n -= 10
    end
  end
  
  n
end