def main():
    calc = lambda pricing, discount: pricing * (100 - discount) / 100

    try:
        price = int(input('Enter the product price $: '))
        per = int(input('What is your discount? %: '))

        print(f'Total price to pay: ${calc(price, per)}')
    except ValueError:
        print('Only can introduce numbers \n')
        main()

if __name__ == '__main__':
    main()