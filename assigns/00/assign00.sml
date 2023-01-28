(* ****** ****** *)
(*
Assign00: Warmup!
*)
(* ****** ****** *)


fun fact(x: int): int =
  if x > 0 then x * fact(x-1) else 1


(*
Assign00-01: 10 points
Please find the first integer N such that the
evaluation of fact(N) in SML/NJ yields an Overflow
exception.
*)


(*
Assign00-02: 10 points
Please implement a function that tests whether a
given natural number is a prime:
*)

fun isPrime(n0: int): bool = 
  let fun find_divisor(x: int) =
    if x * x >= n0 then 
      true
    else if n0 mod x = 0 then 
      false
	  else find_divisor(x + 1)
  in
    find_divisor(2)

(*
Assign00-03: 10 points
Please implement a function that converts a given
integer to a string that represents the integer:
*)

fun int2str(i0: int): string =
  if i0 > 0 then 
    i0 = i0 div 10
    i0 = Char.i0 
    i0 = Char.i
    
  else modUse(x+1)
  in 
    find_divisor()

    
  
  (* How to iterate the int then concat *)


(*
Assign00-04: 10 points
Please implement a function that converts a given
string to an integer:
In particular, it is expected that str2int(int2str(x)) = x
*)


(* fun str2int(cs: string): int =  *)
  




(*
Assign00-05: 10 points
Please implement a function that returns the reverse of
a given string:
*)

fun stringrev(cs: string): string = 
  let fun new_str =

  return cs




(* end of [CS320-2023-Spring-assign00.sml] *)
