(defparameter *n* '(2 4 6 5 7))

(defun lis(l f) 
    (nth f l)
)
(princ "Which element of index do you want? : ")
(defvar a(read))
(format t "~a item from list is ~a ~%" a (lis *n* (- a 1)))


(defun factrec (n)
  (if (= n 0)
      1
      (* n (factrec (- n 1))) 
  ) 
)
	
(princ "Enter a number : ")
(defvar num1(read))
(format t "Factorial of ~a is ~a ~%" num1 (factrec num1))


(defun factnonrec (n)
	(defvar fact 1)
	(defvar x 1)
	(loop
		(setq fact (* fact x))
		(setq x (+ x 1))
		(when (> x n) (return fact))
	)
) 

(princ "Enter a number : ")
(defvar num2(read))
(format t "Factorial of ~a is ~a ~%" num2 (factnonrec num2))

