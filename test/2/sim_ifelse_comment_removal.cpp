int abc = 76;

int main()
{
    cout << @@HELLO@@ ;

    int number = 10;


    cout << @@Local variable is  @@ << number;
    cout << @@Global variable is @@ << abc;




    if ( number >= 0)
    {
      number = number + 10 * 5 + abc / number;
    }

    else
    {
      number = 0;
    }

    cout << @@ This line is always printed @@;
    return 0;
}
