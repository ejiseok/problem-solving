def solution(a, b)
  num1 = (a.to_s + b.to_s).to_i
  num2 = (b.to_s + a.to_s).to_i
  num1 >= num2 ? num1 : num2
end
