int main()
{
    int number = 10;

    cout << @@HELLO@@;
    cout << @@number is equal to @@ << number;
    // checks if the number is positive
    if ( number > 0)
    {
        number = number * 100;
    }

    cout << @@ Multiplied number by 100 @@;

	return 0;
}
