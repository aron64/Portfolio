module Rainbow where

next :: [Double] -> Double
next p xxs@(x:xs)
    | sum xxs == 50 = fromIntegral . length $ filter (/=10) xxs
    |
     where 
        s = sum xxs

next :: [Double] -> Double
next xxs@(x:xs)
    | sum xxs == 67 = fromIntegral . (*7).  length $ filter (/=10) xxs
    | otherwise = sum . map (\(p, ls) -> p*next ls). filter (\(p,ls) -> p>0 && possible ls) . map (\i -> ((xxs!!i/(sum xxs)), (take i xxs) ++ [xxs!!i-1] ++ (drop (i+1) xxs)) ) $ [0..6]
    where
        possible [y] = True
        possible (x:y:xs) = x<=y && possible (y:xs)
        -- go (x:xs)
            -- | x==0 = go xs
            -- | otherwise = ( x/(sum xxs) ) * next (x-1:xs)


arr = [0,1, 2, 3, 4, 7, 10, 11, 12, 13, 16, 17, 18, 19, 20, 23, 24, 25, 26, 29, 30, 31, 34, 35, 36, 37, 40, 41, 42, 45, 48, 49, 50, 51, 54, 57, 58, 59, 62, 65, 66, 67, 68, 69, 72, 73, 74, 75, 78, 79, 80, 83, 84, 85, 88, 89, 90, 91, 94, 95, 96, 97, 100, 103, 104, 105, 106, 107, 110, 111, 112, 115, 116, 117, 118, 119, 122, 125, 126, 127, 128, 129, 132, 135, 136, 137, 138, 141, 142, 145, 146, 149, 152, 155, 156, 157, 158, 159, 162, 163, 164, 165, 166, 169, 170, 171, 172]
:{
memo_ways :: Int -> Integer
memo_ways = (!!) (map ways [0..]) 
    where
        ways 0 = 1
        ways n = let val=array!!n in sum [memo_ways (n-k) | k<-[1,2,3], n-k>=0, array!!(n-k) >= (val-3) ]

:}