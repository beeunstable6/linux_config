import Data.Char

-- exercise 1
average :: [Float] -> Float
average x = ave x / fromIntegral(length(x))

ave(x:[]) = (x + 0.0)
ave (x:xs) = x + ave xs

average1 :: [Float] -> Float
average1 x = sum x / fromIntegral(length(x))

-- exercise 2
-- divides1 :: Integer -> [Integer]

divides2 :: Integer -> [Integer]
divides2 x = [n | n <- [1..x], x `mod` n == 0]

isPrime :: Integer -> Bool
isPrime x
 | length(divides2 x) == 2 = True
 | otherwise = False

-- exercise 3
prefix :: String -> String -> Bool
prefix s1 s2
 | take (length(s1)) s2 == s1 = True
 | otherwise = False

substring :: String -> String -> Bool
substring s1 (x:xs)


-- exercise 4

-- exercise 5
numbers = "0123456789"
delims = " ,.:;[]{}()"

capitalise :: String -> String
capitalise s = map toUpper(leaveLetters(s))

leaveLetters s = [x | x <- s, not(x `elem` numbers || x `elem` delims)]

-- exercise 6