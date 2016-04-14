

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

void matrice_add_a(int *mat_a,int mat_a_length,int *mat_b,int repeat)
{
  int i;
  int y;
  for (y = 0; y < repeat; ++y)
    for (i = 0 ; i < mat_a_length ; ++i)
      mat_a[i] += mat_b[i];


}
