
"""
    Another Brick in the Wall
    john
    jack

    harry: 11 bricks
                total
    john: 1     1
    jack: 2     3
    john: 2     5
    jack: 4     9
    
  > john: 3     12 <
    
    john: 2     11

    Goal: Find who placed the last brick. john or jack ?
          and how many bricks in the end ?
          
          Ans
          john: 2     11

"""
bricks_by_customer=int(input("Enter no of bricks:"))

print("Wall must be constructed with ",bricks_by_customer,"bricks")

total=0

for bricks in range(1,bricks_by_customer+1):   

    john=bricks
    total += john

    if total > bricks_by_customer:
        extra_bricks =  total-bricks_by_customer
        last_brick= john-extra_bricks
        print('John placed the last brick:',last_brick)
        break

    jack_bricks = john*2
    total += jack_bricks

    if total > bricks_by_customer:
       extra_bricks =  total-bricks_by_customer
       last_brick= jack_bricks-extra_bricks
       print('John placed the last brick:', last_brick)
       break


