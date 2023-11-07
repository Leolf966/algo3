def food_required(arr, l) -> int:
        n = 0
        for h in arr:
              n += h[0] + l*h[1]
        return n



def quick_sort(arr, l):
      if len(arr) <= 1:
            return arr
      
      pivot = arr[len(arr) // 2]
      left = [h for h in arr if h[0] + l*h[1] < pivot[0] + l*pivot[1]]
      middle = [h for h in arr if h[0] + l*h[1] == pivot[0] + l*pivot[1]]
      right = [h for h in arr if h[0] + l*h[1] > pivot[0] + l*pivot[1]]     
      return quick_sort(left, l) + middle + quick_sort(right, l)

def how_much_hamsters_can_you_handle_subtract(food, number_of_hams, hams) -> int:
        
        if number_of_hams != len(hams):
              print("Bye bye CHINAZZISSSSSSSSSSS")
              return None
      
        daily_food_required = 0
        while number_of_hams != 0:
                     
              hams = quick_sort(hams, number_of_hams -1)
              daily_food_required = food_required(hams, number_of_hams - 1)
              if daily_food_required <= food:
                    break
              hams.pop(number_of_hams - 1)
              number_of_hams -= 1

        return number_of_hams    

if __name__ == '__main__':
    result = how_much_hamsters_can_you_handle_subtract(15, 4, [[2, 0], [4, 3], [2, 4], [8, 1]])
    print(result)

