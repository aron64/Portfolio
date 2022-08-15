
works :: Integer -> Bool
works c = right_side == left_side
    where
        left_side = c*c-c
        k=left_side `div` 2
        right_side = let a = fromIntegral . ceiling . sqrt . fromIntegral $ k in 2*(a*a-a)
        -- k=a*a-a
        -- right_side = 2*k
        -- left_side = let b = fromIntegral . ceiling . sqrt . right_side $ a in b*b-b

       -- 1000000000000

works' :: Integer -> Integer
works' c = right_side
    where
        b = fromIntegral c
        left_side = b*b-b
        k=left_side / 2
        right_side = let a = fromIntegral . ceiling . sqrt $ k in a