print('��������?') 
count = 0 
    
while True: 
  choice = input('������ ����� �����? y/n' ) 
  if choice == 'y': 
  current = koloda.pop() 
  print('��� �������� ����� ������������ %d' %current) 
  count += current 
  if count > 21: 
  print('��������, �� �� ���������') 
  break 
  elif count == 21: 
  print('����������, �� ������� 21!') 
  break 
  else: 
  print('� ��� %d �����.' %count) 
  elif choice == 'n': 
  print('� ��� %d ����� � �� ��������� ����.' %count) 
  break 
    
print('����!') 