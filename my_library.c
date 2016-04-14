

void add_one(int *array,int array_lenght)
{
  int i;
  for (i=0; i < array_lenght ; ++ i )
      array[i]+= 1;

}

void multiply_by(int *array,int array_lenght,int factor)
{
  int i;
  for (i=0; i < array_lenght; ++i)
    array[i]*=factor;

}
