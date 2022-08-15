module RightTriangles where

type Vector = (Int, Int)

nullVec :: Vector
nullVec = (0,0)

right :: Vector -> Vector -> Bool
right v1 v2 = ort v1 v2 || ort v1 v3 || ort v2 v3
    where
        v3 = sub v2 v1
        sub (a1,b1) (a2, b2) = (a2-a1,b2-b1)
        scalar (x1,y1) (x2,y2) = x1*x2+y1*y2
        ort p q = scalar p q == 0



scan :: Int->[(Vector, Vector)]
scan n = [ (v1,v2) | i <- [1..n*n-1], j <-[i+1..n*n-1], i/=j, let v1=toVec i, let v2=toVec j, right v1 v2 ]
    where
        toVec k = (k `div` n, k `mod` n)

res = length $ scan 51
